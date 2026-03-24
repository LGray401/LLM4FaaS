"""
Aggregate evaluation results for paper reporting.

Mirrors the logic from the original archive scripts:
- archive/eva_code_quality/get_pylint_report.py   (Pylint score extraction)
- archive/eva_code_quality/radon_result_processing.py  (Radon metric parsing)

The pass-rate computation follows the paper definitions:
- Syntactic pass: Status in {"No Error & Warning", "Warning Exists"}
- Semantic pass:  Success Rate == 1.0  (syntactic pass is a prerequisite)
"""
import csv
import os
import re
from pathlib import Path
from typing import Dict, List, Optional


_CC_PATTERN = re.compile(r"Average complexity: \w+ \(([\d.]+)\)")
_MI_PATTERN = re.compile(r"- \w+ \(([\d.]+)\)")
_HALS_PATTERN = re.compile(r"effort:\s*([\d.]+)")

# Pylint score — identical to archive/eva_code_quality/get_pylint_report.py
_PYLINT_SCORE_PATTERN = re.compile(r"Your code has been rated at ([\d\.]+)/10")

# Status values that count as syntactic pass (from paper §4.3)
_SYNTACTIC_PASS_STATUSES = {"No Error & Warning", "Warning Exists"}

# Rows with these statuses are excluded from pass-rate totals.
# ``Invalid Prompt`` entries are bookkeeping artifacts (known invalid task/index
# pairs) and should not affect denominator-based metrics.
_EXCLUDED_FROM_TOTAL_STATUSES = {"invalid prompt"}


class ResultsAggregator:
    """Produces aggregate CSVs from per-file report directories and results CSVs."""

    # ------------------------------------------------------------------
    # Pylint
    # ------------------------------------------------------------------

    def parse_pylint_reports(self, reports_dir: str, output_csv: str) -> str:
        """
        Parse pylint report files (*_pylint.txt) and write a per-file score CSV.

        Mirrors archive/eva_code_quality/get_pylint_report.py::run_pylint() —
        specifically the score extraction and CSV writing steps.

        CSV columns: Absolute Path, Score

        Args:
            reports_dir: Directory containing ``*_pylint.txt`` report files
                         (produced by CodeQualityAnalyzer.run_pylint).
            output_csv:  Path for the output CSV file.

        Returns:
            Path to the written CSV.
        """
        scores: List[tuple] = []

        for filename in os.listdir(reports_dir):
            if not filename.endswith('_pylint.txt'):
                continue

            file_path = os.path.join(reports_dir, filename)
            absolute_path = os.path.abspath(file_path)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            score_match = _PYLINT_SCORE_PATTERN.search(content)
            score = float(score_match.group(1)) if score_match else None

            scores.append((absolute_path, score))
            print(f"Pylint score for {filename}: {score}")

        os.makedirs(os.path.dirname(output_csv) or '.', exist_ok=True)
        with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Absolute Path', 'Score'])
            writer.writerows(scores)

        print(f'✓ Pylint scores saved to: {output_csv}')
        return output_csv

    # ------------------------------------------------------------------
    # Radon
    # ------------------------------------------------------------------

    def parse_radon_reports(self, reports_dir: str, output_csv: str) -> str:
        """
        Parse combined Radon report files (*_radon.txt) and write a per-file CSV.

        Mirrors archive/eva_code_quality/radon_result_processing.py exactly:
        - reads every ``.txt`` file in ``reports_dir``
        - extracts CC average, MI value, and total Halstead effort using the
          same regex patterns from the archive
        - writes CSV with columns: absolute_path, cc_average, mi_value, hals_effort

        The combined ``.txt`` reports are produced by
        CodeQualityAnalyzer.run_radon_combined().

        Args:
            reports_dir: Directory containing ``*_radon.txt`` combined report files.
            output_csv:  Path for the output CSV file.

        Returns:
            Path to the written CSV.
        """
        results: List[Dict] = []

        if not os.path.exists(reports_dir):
            print(f'!!!Folder {reports_dir} Does Not Exist!!! Pass')
            return output_csv

        for filename in os.listdir(reports_dir):
            if not filename.endswith('.txt'):
                continue

            file_path = os.path.join(reports_dir, filename)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            cc_average = None
            mi_value = None
            total_hals_effort = 0.0

            match = _CC_PATTERN.search(content)
            if match:
                cc_average = match.group(1)

            match = _MI_PATTERN.search(content)
            if match:
                mi_value = match.group(1)

            efforts = _HALS_PATTERN.findall(content)
            if efforts:
                total_hals_effort = sum(map(float, efforts))

            results.append({
                'absolute_path': file_path,
                'cc_average': cc_average,
                'mi_value': mi_value,
                'hals_effort': total_hals_effort,
            })

        os.makedirs(os.path.dirname(output_csv) or '.', exist_ok=True)
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['absolute_path', 'cc_average', 'mi_value', 'hals_effort']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

        print(f'✓ Radon aggregates saved to: {output_csv}')
        return output_csv

    # ------------------------------------------------------------------
    # Pass rates
    # ------------------------------------------------------------------

    def compute_pass_rates(self, results_csv_path: str) -> Dict:
        """
        Compute syntactic and semantic pass rates from a ``*_results.csv`` file
        produced by FunctionEvaluator.write_results_to_csv().

        Definitions (from §4.2 of the paper):
        - Syntactic pass: Status in {"No Error & Warning", "Warning Exists"}
        - Semantic pass:  Success Rate == 1.0
          (syntactic pass is a prerequisite, so only syntactically passing
           entries can also be semantically passing)

        Args:
            results_csv_path: Path to ``{task}_results.csv``.

        Returns:
            Dictionary with keys:
                total           – number of evaluated rows after exclusions
                syntactic_pass  – count of syntactically passing rows
                semantic_pass   – count of semantically passing rows
                syntactic_rate  – syntactic_pass / total  (0.0–1.0)
                semantic_rate   – semantic_pass / total   (0.0–1.0)
                rows            – list of included row dicts for further processing
        """
        rows: List[Dict] = []

        with open(results_csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                status = row.get('Status', '')
                if status.strip().lower() in _EXCLUDED_FROM_TOTAL_STATUSES:
                    continue
                rows.append(row)

        total = len(rows)
        syntactic_pass = 0
        semantic_pass = 0

        for row in rows:
            status = row.get('Status', '')
            success_rate_str = row.get('Success Rate', '0')

            if status in _SYNTACTIC_PASS_STATUSES:
                syntactic_pass += 1

                try:
                    if float(success_rate_str) == 1.0:
                        semantic_pass += 1
                except (ValueError, TypeError):
                    pass

        syntactic_rate = syntactic_pass / total if total > 0 else 0.0
        semantic_rate = semantic_pass / total if total > 0 else 0.0

        return {
            'total': total,
            'syntactic_pass': syntactic_pass,
            'semantic_pass': semantic_pass,
            'syntactic_rate': syntactic_rate,
            'semantic_rate': semantic_rate,
            'rows': rows,
        }

    def write_pass_rates_csv(
        self,
        results_csv_paths: List[str],
        output_csv: str,
    ) -> str:
        """
        Compute pass rates for one or more ``*_results.csv`` files and write a
        summary CSV.

        Each input file produces one row in the output, identified by the
        task name extracted from the filename.

        CSV columns:
            task, total, syntactic_pass, semantic_pass,
            syntactic_rate, semantic_rate

        Args:
            results_csv_paths: List of paths to ``*_results.csv`` files.
            output_csv:        Path for the output CSV file.

        Returns:
            Path to the written CSV.
        """
        summary_rows: List[Dict] = []

        for csv_path in results_csv_paths:
            task_name = Path(csv_path).stem.replace('_results', '')
            stats = self.compute_pass_rates(csv_path)
            summary_rows.append({
                'task': task_name,
                'total': stats['total'],
                'syntactic_pass': stats['syntactic_pass'],
                'semantic_pass': stats['semantic_pass'],
                'syntactic_rate': f"{stats['syntactic_rate']:.4f}",
                'semantic_rate': f"{stats['semantic_rate']:.4f}",
            })
            print(
                f"  {task_name}: syntactic={stats['syntactic_rate']*100:.2f}%  "
                f"semantic={stats['semantic_rate']*100:.2f}%  "
                f"(n={stats['total']})"
            )

        os.makedirs(os.path.dirname(output_csv) or '.', exist_ok=True)
        fieldnames = [
            'task', 'total',
            'syntactic_pass', 'semantic_pass',
            'syntactic_rate', 'semantic_rate',
        ]
        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(summary_rows)

        print(f'✓ Pass rates saved to: {output_csv}')
        return output_csv


def main():
    """CLI for aggregate evaluation."""
    import argparse

    parser = argparse.ArgumentParser(description='Aggregate evaluation results for paper reporting')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # pylint scores
    p_pylint = subparsers.add_parser('pylint', help='Parse pylint report files → scores CSV')
    p_pylint.add_argument('--reports-dir', required=True,
                          help='Directory with *_pylint.txt report files')
    p_pylint.add_argument('--output', required=True, help='Output CSV path')

    # radon aggregates
    p_radon = subparsers.add_parser('radon', help='Parse combined radon report files → metrics CSV')
    p_radon.add_argument('--reports-dir', required=True,
                         help='Directory with *_radon.txt combined report files')
    p_radon.add_argument('--output', required=True, help='Output CSV path')

    # pass rates
    p_pass = subparsers.add_parser('pass-rates', help='Compute syntactic/semantic pass rates')
    p_pass.add_argument('--results-csv', nargs='+', required=True,
                        help='One or more *_results.csv files')
    p_pass.add_argument('--output', required=True, help='Output summary CSV path')

    args = parser.parse_args()
    agg = ResultsAggregator()

    if args.command == 'pylint':
        agg.parse_pylint_reports(args.reports_dir, args.output)
    elif args.command == 'radon':
        agg.parse_radon_reports(args.reports_dir, args.output)
    elif args.command == 'pass-rates':
        agg.write_pass_rates_csv(args.results_csv, args.output)


if __name__ == '__main__':
    main()
