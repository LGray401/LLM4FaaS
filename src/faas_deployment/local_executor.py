"""
Local execution module for prepared Python functions.
Executes tinyFaaS-prepared function folders without deploying to tinyFaaS.
"""
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List


class LocalExecutor:
    """Executes prepared Python function folders locally."""

    def __init__(self, timeout: int = 30):
        """
        Initialize the local executor.

        Args:
            timeout: Per-function execution timeout in seconds
        """
        self.timeout = timeout

    def execute_function_dir(self, function_dir: str) -> Dict:
        """
        Execute a single prepared function directory by importing fn.py and calling fn().

        Args:
            function_dir: Path to a prepared function directory containing fn.py

        Returns:
            Dict with function_name, success, stdout, stderr, and timing
        """
        func_name = Path(function_dir).name
        start = time.time()

        # Call fn.fn(None, None) to mirror tinyFaaS invocation semantics.
        invoke_code = (
            "import fn\n"
            "result = fn.fn(None, None)\n"
            "if isinstance(result, str):\n"
            "    print(result, end='')\n"
        )

        process = None
        try:
            process = subprocess.Popen(
                [sys.executable, "-c", invoke_code],
                cwd=function_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            stdout, stderr = process.communicate(timeout=self.timeout)
            return_code = process.returncode
            success = return_code == 0

            return {
                "function_name": func_name,
                "success": success,
                "stdout": stdout,
                "stderr": stderr,
                "timing": {
                    "upload_s": None,
                    "execute_s": time.time() - start,
                },
            }
        except subprocess.TimeoutExpired:
            if process is not None:
                process.kill()
                stdout, stderr = process.communicate()
            else:
                stdout, stderr = "", ""
            timeout_msg = f"Timeout after {self.timeout} seconds"
            stderr = f"{stderr}\n{timeout_msg}".strip()
            return {
                "function_name": func_name,
                "success": False,
                "stdout": stdout,
                "stderr": stderr,
                "timing": {
                    "upload_s": None,
                    "execute_s": time.time() - start,
                },
            }
        except Exception as exc:
            return {
                "function_name": func_name,
                "success": False,
                "stdout": "",
                "stderr": str(exc),
                "timing": {
                    "upload_s": None,
                    "execute_s": time.time() - start,
                },
            }

    def execute_batch(self, function_dirs: List[str]) -> List[Dict]:
        """
        Execute multiple prepared function directories.

        Args:
            function_dirs: List of prepared function directory paths

        Returns:
            List of result dicts from execute_function_dir
        """
        results: List[Dict] = []
        for function_dir in function_dirs:
            results.append(self.execute_function_dir(function_dir))
        return results
