"""
Latency recording module for LLM4FaaS pipeline.

Writes per-sample wall-clock timing records to a CSV file under
data/evaluation/{experiment}/{task}_latency.csv.

CSV columns:
    filename        - generated source filename (primary identifier)
    user_index      - numeric user index extracted from filename
    provider        - LLM provider name (openai, ollama, gemini)
    model           - model name
    task            - task name (remote_control, auto_adapt, plan, ...)
    generate_s      - wall-clock seconds spent on LLM generation
                      (includes judge/refinement loop when validation is enabled)
    prepare_s       - wall-clock seconds spent preparing the function directory
    upload_s        - wall-clock seconds spent uploading to tinyFaaS
    execute_s       - wall-clock seconds spent waiting for tinyFaaS HTTP response
"""
import csv
import os
import re
from typing import List, Dict, Optional


# Canonical column order used in every output CSV.
LATENCY_COLUMNS = [
    'filename',
    'user_index',
    'provider',
    'model',
    'task',
    'generate_s',
    'prepare_s',
    'upload_s',
    'execute_s',
]


def _extract_user_index(filename: str, task: str) -> str:
    """
    Extract the numeric user index from a generated filename.

    Examples
    --------
    openai_gpt-4o_remote_control_5_1234.py        -> '5'
    openai_gpt-4o_remote_control_5_validated_...  -> '5'
    """
    # Match the task name followed by underscore and digits
    pattern = rf'{re.escape(task)}_(\d+)'
    match = re.search(pattern, filename)
    return match.group(1) if match else 'unknown'


class LatencyRecord:
    """Holds timing measurements for a single pipeline sample."""

    def __init__(
        self,
        filename: str,
        task: str,
        provider: str,
        model: str,
        generate_s: Optional[float] = None,
        prepare_s: Optional[float] = None,
        upload_s: Optional[float] = None,
        execute_s: Optional[float] = None,
    ):
        self.filename = filename
        self.user_index = _extract_user_index(filename, task)
        self.task = task
        self.provider = provider
        self.model = model
        self.generate_s = generate_s
        self.prepare_s = prepare_s
        self.upload_s = upload_s
        self.execute_s = execute_s

    def to_dict(self) -> Dict:
        return {
            'filename': self.filename,
            'user_index': self.user_index,
            'provider': self.provider,
            'model': self.model,
            'task': self.task,
            'generate_s': f'{self.generate_s:.4f}' if self.generate_s is not None else '',
            'prepare_s': f'{self.prepare_s:.4f}' if self.prepare_s is not None else '',
            'upload_s': f'{self.upload_s:.4f}' if self.upload_s is not None else '',
            'execute_s': f'{self.execute_s:.4f}' if self.execute_s is not None else '',
        }


class LatencyWriter:
    """Collects LatencyRecord instances and writes them to a CSV file."""

    def __init__(self):
        self._records: List[LatencyRecord] = []

    def add(self, record: LatencyRecord) -> None:
        """Append a record."""
        self._records.append(record)

    def merge_generate_timings(self, generate_timings: List[Dict]) -> None:
        """
        Upsert generation timing dicts (from LLMGenerator.generate_batch).

        Each dict must contain:
            filename    - output filename (basename)
            task        - task name
            provider    - provider name
            model       - model name
            generate_s  - elapsed seconds
        """
        for t in generate_timings:
            # Try to find an existing record for this filename
            existing = next(
                (r for r in self._records if r.filename == t['filename']),
                None
            )
            if existing:
                existing.generate_s = t['generate_s']
            else:
                self._records.append(LatencyRecord(
                    filename=t['filename'],
                    task=t['task'],
                    provider=t['provider'],
                    model=t['model'],
                    generate_s=t['generate_s'],
                ))

    def merge_prepare_timings(self, prepare_timings: List[Dict]) -> None:
        """
        Upsert preparation timing dicts (from FunctionPreparer.prepare_batch).

        Each dict must contain:
            source_filename - original .py/.js filename (basename)
            prepare_s       - elapsed seconds
        """
        for t in prepare_timings:
            src = t['source_filename']
            existing = next(
                (r for r in self._records if r.filename == src),
                None
            )
            if existing:
                existing.prepare_s = t['prepare_s']
            # If no matching generate record, skip (prepare without generate would be unusual)

    def merge_deploy_timings(self, deploy_timings: List[Dict]) -> None:
        """
        Upsert deployment timing dicts (from TinyFaaSManager.deploy_batch).

        Each dict must contain:
            source_filename - original .py filename that produced this deployment
            upload_s        - time for upload_function
            execute_s       - time for trigger_function (None if not executed)
        """
        for t in deploy_timings:
            src = t['source_filename']
            existing = next(
                (r for r in self._records if r.filename == src),
                None
            )
            if existing:
                existing.upload_s = t.get('upload_s')
                existing.execute_s = t.get('execute_s')

    def write_csv(self, output_path: str) -> None:
        """Write all collected records to a CSV file."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=LATENCY_COLUMNS)
            writer.writeheader()
            for record in sorted(self._records, key=lambda r: r.user_index):
                writer.writerow(record.to_dict())
        print(f'✓ Latency data saved to: {output_path}')
