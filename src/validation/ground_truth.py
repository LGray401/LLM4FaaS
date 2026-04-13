"""
Ground-truth validation based on expected-vs-actual runtime output.
"""
import json
import logging
import re
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict

from .validation_result import ValidationResult
from ..faas_deployment.local_executor import LocalExecutor
from ..faas_deployment.prepare_functions import FunctionPreparer
from ..evaluation.test_results import FunctionEvaluator
from ..llm_generation.providers import OpenAIProvider, OllamaProvider
from ..llm_generation.config import (
    OPENAI_API_KEY, OPENAI_MODEL,
    OLLAMA_MODEL, OLLAMA_URL,
    GEMINI_API_KEY, GEMINI_MODEL,
)

logger = logging.getLogger(__name__)


class GroundTruthValidator:
    """Runtime validation using LLM-generated expected console output."""

    SUPPORTED_PROVIDERS = ['openai', 'ollama', 'gemini']

    def __init__(
        self,
        provider: str,
        model: str = None,
        temperature: float = 1,
        max_tokens: int = 1200,
        api_key: str = None,
        local_execution: bool = False,
        local_timeout: int = 30,
    ):
        if provider not in self.SUPPORTED_PROVIDERS:
            raise ValueError(f"Provider must be one of {self.SUPPORTED_PROVIDERS}")

        self.provider_name = provider
        self.local_execution = local_execution
        self.local_timeout = local_timeout

        if provider == 'openai':
            model = model or OPENAI_MODEL
            api_key = api_key or OPENAI_API_KEY
            self.provider = OpenAIProvider(api_key, model, temperature, max_tokens)
            self.model_name = model
        elif provider == 'ollama':
            model = model or OLLAMA_MODEL
            self.provider = OllamaProvider(model, temperature, max_tokens, OLLAMA_URL)
            self.model_name = model
        else:
            from ..llm_generation.providers.gemini_provider import GeminiProvider
            model = model or GEMINI_MODEL
            api_key = api_key or GEMINI_API_KEY
            self.provider = GeminiProvider(api_key, model, temperature, max_tokens)
            self.model_name = model

        self._load_templates()

    def _load_templates(self) -> None:
        """Load all ground-truth prompts from markdown templates."""
        templates_dir = Path(__file__).parent.parent.parent / 'templates' / 'validation'

        system_prompt_path = templates_dir / 'ground_truth_system_prompt.md'
        user_prompt_path = templates_dir / 'ground_truth_prompt_template.md'
        refinement_prompt_path = templates_dir / 'ground_truth_refinement_prompt_template.md'

        required_files = [system_prompt_path, user_prompt_path, refinement_prompt_path]
        missing_files = [str(path) for path in required_files if not path.exists()]
        if missing_files:
            raise FileNotFoundError(
                "Missing ground-truth prompt template file(s): " + ", ".join(missing_files)
            )

        self.ground_truth_system_prompt = system_prompt_path.read_text(encoding='utf-8')
        self.ground_truth_prompt_template = user_prompt_path.read_text(encoding='utf-8')
        self.ground_truth_refinement_template = refinement_prompt_path.read_text(encoding='utf-8')

    def validate(self, requirement: str, generated_code: str, smart_home_docs: str = "") -> ValidationResult:
        """Validate code by comparing expected and actual runtime outputs."""
        if not self.local_execution:
            return ValidationResult(
                is_valid=False,
                issues=["Ground-truth validation currently requires --local/--local-execution."],
                suggestions=["Re-run with --local and ground-truth validation mode enabled."],
                judge_provider=self.provider_name,
                judge_model=self.model_name,
            )

        try:
            expected = self._generate_expected_output(requirement)
            actual = self._execute_locally(generated_code)
            comparison = self._compare_outputs(expected, actual)

            issues = []
            suggestions = []
            if not comparison['is_valid']:
                issues.append(comparison['summary'])
                suggestions.append(
                    "Align the function behavior with the expected stdout/stderr/return code."
                )

            raw_payload = {
                'expected': expected,
                'actual': actual,
                'comparison': comparison,
            }
            confidence = 1.0 if comparison['is_valid'] else 0.0

            return ValidationResult(
                is_valid=comparison['is_valid'],
                issues=issues,
                suggestions=suggestions,
                raw_response=json.dumps(raw_payload, ensure_ascii=False, indent=2),
                confidence=confidence,
                judge_provider=self.provider_name,
                judge_model=self.model_name,
            )
        except Exception as exc:
            logger.exception("Ground-truth validation failed")
            return ValidationResult(
                is_valid=False,
                issues=[f"Ground-truth validation failed: {exc}"],
                suggestions=["Inspect generated code and local execution environment."],
                judge_provider=self.provider_name,
                judge_model=self.model_name,
            )

    def create_refinement_prompt(self, requirement: str, previous_code: str, validation_result: ValidationResult) -> str:
        """Create refinement prompt from expected-vs-actual diff payload."""
        expected = {}
        actual = {}
        summary = "Validation mismatch detected."

        try:
            payload = json.loads(validation_result.raw_response or "{}")
            expected = payload.get('expected', {})
            actual = payload.get('actual', {})
            summary = payload.get('comparison', {}).get('summary', summary)
        except json.JSONDecodeError:
            pass

        return self.ground_truth_refinement_template.format(
            requirement=requirement,
            previous_code=previous_code,
            expected=self._serialize_output_as_xml(expected),
            actual=self._serialize_output_as_xml(actual),
            summary=summary,
        )

    def _generate_expected_output(self, requirement: str) -> Dict[str, Any]:
        prompt = self.ground_truth_prompt_template.format(requirement=requirement)

        response = self.provider.generate(prompt, self.ground_truth_system_prompt)
        data = self._extract_xml_object(response)

        return_code_value = data.get('return_code', '0')
        try:
            return_code = int(str(return_code_value).strip())
        except (TypeError, ValueError):
            return_code = 0

        return {
            'stdout': str(data.get('stdout', '')),
            'stderr': str(data.get('stderr', '')),
            'return_code': return_code,
        }

    def _execute_locally(self, generated_code: str) -> Dict[str, Any]:
        base_dir = Path(__file__).resolve().parents[2]
        smart_home_dir = base_dir / 'templates' / 'smart_home'

        with tempfile.TemporaryDirectory(prefix='llm4faas_gt_') as tmp:
            tmp_path = Path(tmp)
            source_dir = tmp_path / 'source'
            prepared_dir = tmp_path / 'prepared'
            source_dir.mkdir(parents=True, exist_ok=True)
            prepared_dir.mkdir(parents=True, exist_ok=True)

            source_file = source_dir / 'candidate.py'
            source_file.write_text(generated_code, encoding='utf-8')

            preparer = FunctionPreparer(str(smart_home_dir))
            func_dir = preparer.prepare_python_function(
                str(source_file),
                str(prepared_dir),
                function_name='candidate',
            )

            executor = LocalExecutor(timeout=self.local_timeout)
            result = executor.execute_function_dir(func_dir)

            return {
                'stdout': result.get('stdout', ''),
                'stderr': result.get('stderr', ''),
                'return_code': 0 if result.get('success', False) else 1,
            }

    def _compare_outputs(self, expected: Dict[str, Any], actual: Dict[str, Any]) -> Dict[str, Any]:
        expected_payload = {
            'stdout': self._normalize_text(expected.get('stdout', '')),
            'stderr': self._normalize_text(expected.get('stderr', '')),
            'return_code': self._safe_int(expected.get('return_code', 0), fallback=0),
        }
        actual_payload = {
            'stdout': self._normalize_text(actual.get('stdout', '')),
            'stderr': self._normalize_text(actual.get('stderr', '')),
            'return_code': self._safe_int(actual.get('return_code', 0), fallback=1),
        }

        evaluator_result = self._evaluate_with_function_evaluator(expected_payload, actual_payload)

        status = evaluator_result.get('status', 'Evaluation Error')
        match_percentage = evaluator_result.get('match_percentage')
        unmatched_lines = evaluator_result.get('unmatched_lines')

        syntactic_ok = status in {'No Error & Warning', 'Warning Exists'}
        semantic_ok = syntactic_ok and (match_percentage == 1.0)

        if semantic_ok:
            summary = 'Output fully matches LLM-generated ground truth using evaluation pipeline matching logic.'
        else:
            rate_str = f"{(match_percentage or 0) * 100:.2f}%"
            summary = f"Evaluation mismatch: status={status}, success_rate={rate_str}"

        return {
            'is_valid': semantic_ok,
            'summary': summary,
            'status': status,
            'match_percentage': match_percentage,
            'unmatched_lines': unmatched_lines,
            'expected': expected_payload,
            'actual': actual_payload,
        }

    def _evaluate_with_function_evaluator(self, expected: Dict[str, Any], actual: Dict[str, Any]) -> Dict[str, Any]:
        with tempfile.TemporaryDirectory(prefix='llm4faas_gt_eval_') as tmp:
            tmp_path = Path(tmp)
            expected_log = tmp_path / 'expected.log'
            actual_log = tmp_path / 'actual.log'

            self._write_log_file(expected_log, expected['stdout'], expected['stderr'], expected['return_code'])
            self._write_log_file(actual_log, actual['stdout'], actual['stderr'], actual['return_code'])

            evaluator = FunctionEvaluator(str(tmp_path), log_level=logging.WARNING)
            return evaluator.evaluate_log(str(actual_log), str(expected_log))

    def _write_log_file(self, path: Path, stdout: str, stderr: str, return_code: Any) -> None:
        with open(path, 'w', encoding='utf-8') as log_file:
            log_file.write('Standard Output:\n')
            if stdout:
                log_file.write(stdout)
                if not stdout.endswith('\n'):
                    log_file.write('\n')

            log_file.write('Standard Error:\n')
            if stderr:
                log_file.write(stderr)
                if not stderr.endswith('\n'):
                    log_file.write('\n')

            if return_code is None:
                log_file.write('Return code: \n')
            else:
                log_file.write(f'Return code: {return_code}\n')

    def _safe_int(self, value: Any, fallback: int) -> int:
        try:
            return int(str(value).strip())
        except (TypeError, ValueError):
            return fallback

    def _extract_xml_object(self, text: str) -> Dict[str, Any]:
        match = re.search(r'<ground_truth_output>[\s\S]*?</ground_truth_output>', text)
        if not match:
            return {}

        try:
            root = ET.fromstring(match.group(0))
        except ET.ParseError:
            return {}

        def _read(tag: str) -> str:
            node = root.find(tag)
            if node is None:
                return ''
            return ''.join(node.itertext())

        return {
            'stdout': _read('stdout'),
            'stderr': _read('stderr'),
            'return_code': _read('return_code'),
        }

    def _serialize_output_as_xml(self, payload: Dict[str, Any]) -> str:
        stdout = str(payload.get('stdout', ''))
        stderr = str(payload.get('stderr', ''))
        return_code = str(payload.get('return_code', 0))

        # Use CDATA for stdout/stderr to preserve line breaks and special chars.
        return (
            "<ground_truth_output>\n"
            f"  <stdout><![CDATA[{stdout}]]></stdout>\n"
            f"  <stderr><![CDATA[{stderr}]]></stderr>\n"
            f"  <return_code>{return_code}</return_code>\n"
            "</ground_truth_output>"
        )

    def _normalize_text(self, value: str) -> str:
        text = str(value).replace('\r\n', '\n').strip()
        return text
