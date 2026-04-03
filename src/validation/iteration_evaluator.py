"""
Per-iteration runtime evaluation against standard logs.
"""
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, Optional

from ..evaluation.test_results import FunctionEvaluator
from ..faas_deployment.local_executor import LocalExecutor
from ..faas_deployment.prepare_functions import FunctionPreparer


class IterationRuntimeEvaluator:
    """Execute and evaluate refinement iterations against standard logs."""

    def __init__(self, standard_logs_dir: str, local_timeout: int = 30):
        self.standard_logs_dir = Path(standard_logs_dir)
        self.local_timeout = local_timeout
        self.function_evaluator = FunctionEvaluator(str(self.standard_logs_dir))

        base_dir = Path(__file__).resolve().parents[2]
        smart_home_dir = base_dir / 'templates' / 'smart_home'
        self.preparer = FunctionPreparer(str(smart_home_dir))
        self.executor = LocalExecutor(timeout=local_timeout)

    def evaluate_iteration(
        self,
        code: str,
        task_name: Optional[str],
        sample_index: Optional[str],
        iteration: int,
    ) -> Dict[str, Any]:
        """Evaluate one refinement iteration and return structured result data."""
        started = time.time()

        if not task_name or not sample_index:
            return {
                'iteration': iteration,
                'task': task_name,
                'sample_index': sample_index,
                'status': 'Standard log not found',
                'match_percentage': None,
                'unmatched_lines': None,
                'standard_log_path': None,
                'timing_s': time.time() - started,
                'error': 'Could not infer task/sample index from prompt filename.',
            }

        standard_log_path = self.standard_logs_dir / task_name / f'{task_name}_{sample_index}.log'
        if not standard_log_path.exists():
            return {
                'iteration': iteration,
                'task': task_name,
                'sample_index': sample_index,
                'status': 'Standard log not found',
                'match_percentage': None,
                'unmatched_lines': None,
                'standard_log_path': str(standard_log_path),
                'timing_s': time.time() - started,
                'error': 'Standard log file is missing for this sample.',
            }

        try:
            with tempfile.TemporaryDirectory(prefix='llm4faas_iter_eval_') as tmp_dir:
                tmp_path = Path(tmp_dir)
                source_dir = tmp_path / 'source'
                prepared_dir = tmp_path / 'prepared'
                source_dir.mkdir(parents=True, exist_ok=True)
                prepared_dir.mkdir(parents=True, exist_ok=True)

                source_file = source_dir / 'candidate.py'
                source_file.write_text(code, encoding='utf-8')

                function_dir = self.preparer.prepare_python_function(
                    str(source_file),
                    str(prepared_dir),
                    function_name='candidate',
                )
                execution_result = self.executor.execute_function_dir(function_dir)

                return_code = self._resolve_return_code(execution_result)
                actual_log = tmp_path / 'actual.log'
                self._write_log_file(
                    actual_log,
                    stdout=execution_result.get('stdout', ''),
                    stderr=execution_result.get('stderr', ''),
                    return_code=return_code,
                )

                result = self.function_evaluator.evaluate_log(
                    str(actual_log),
                    str(standard_log_path),
                )

                return {
                    'iteration': iteration,
                    'task': task_name,
                    'sample_index': sample_index,
                    'status': result.get('status'),
                    'match_percentage': result.get('match_percentage'),
                    'unmatched_lines': result.get('unmatched_lines'),
                    'standard_log_path': str(standard_log_path),
                    'execution_success': execution_result.get('success', False),
                    'execution_stdout': execution_result.get('stdout', ''),
                    'execution_stderr': execution_result.get('stderr', ''),
                    'execution_return_code': return_code,
                    'timing_s': time.time() - started,
                }
        except Exception as exc:
            return {
                'iteration': iteration,
                'task': task_name,
                'sample_index': sample_index,
                'status': 'Evaluation Error',
                'match_percentage': None,
                'unmatched_lines': None,
                'standard_log_path': str(standard_log_path),
                'timing_s': time.time() - started,
                'error': str(exc),
            }

    def _resolve_return_code(self, execution_result: Dict[str, Any]) -> Optional[int]:
        if execution_result.get('success', False):
            return 0

        stderr = execution_result.get('stderr', '') or ''
        if 'Timeout after' in stderr:
            return None

        return 1

    def _write_log_file(self, path: Path, stdout: str, stderr: str, return_code: Optional[int]) -> None:
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