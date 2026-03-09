"""
TinyFaaS deployment and execution module.
"""
import os
import re
import subprocess
import time
import requests
from typing import Tuple, Optional


class TinyFaaSManager:
    """Manages deployment and execution of functions on tinyFaaS."""
    
    def __init__(self, tinyfaas_dir: str, 
                 management_port: int = 8080, http_port: int = 8000):
        """
        Initialize the tinyFaaS manager.
        
        Args:
            tinyfaas_dir: Path to tinyFaaS installation directory
            management_port: Management API port
            http_port: HTTP function invocation port
        """
        self.tinyfaas_dir = tinyfaas_dir
        self.management_port = management_port
        self.http_port = http_port
        self.upload_script = os.path.join(tinyfaas_dir, 'scripts', 'upload.sh')
        self.management_url = f"http://localhost:{management_port}/"
    
    def _is_running(self) -> bool:
        """Return True if the management service is reachable on the expected URL."""
        try:
            # Any HTTP response means something is listening on the management port.
            requests.get(self.management_url, timeout=2)
            return True
        except requests.RequestException:
            return False
    
    def _ensure_running(self) -> bool:
        """Start tinyFaaS using `make start` if the management service is not reachable.

        Returns True when the service is confirmed running, False otherwise.
        """
        if self._is_running():
            return True
        print("tinyFaaS not running, attempting to start via `make start`...")
        try:
            process = subprocess.Popen(
                ["make", "start"],
                cwd=self.tinyfaas_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                start_new_session=True,
            )

            # Wait up to 15 seconds for management service to become reachable
            for _ in range(15):
                if self._is_running():
                    print("✓ tinyFaaS started successfully.")
                    return True
                if process.poll() is not None:
                    stdout, stderr = process.communicate()
                    error_output = (stderr or stdout or "").strip()
                    if error_output:
                        print(f"✗ tinyFaaS start failed: {error_output}")
                    else:
                        print("✗ tinyFaaS start process exited before service became reachable.")
                    return False
                time.sleep(1)

            print("✗ tinyFaaS did not respond after startup.")
            return False
        except OSError as e:
            print(f"✗ Failed to start tinyFaaS: {e}")
            return False
    
    def upload_function(self, function_dir: str, function_name: str, 
                       runtime: str = 'python3') -> bool:
        """
        Upload a function to tinyFaaS.
        
        This method will ensure the tinyFaaS management service is running
        before attempting an upload.
        
        Args:
            function_dir: Path to function directory
            function_name: Name to register the function as
            runtime: Runtime environment ('python3' or 'nodejs')
            
        Returns:
            True if upload successful, False otherwise
        """
        # make sure tinyFaaS is up and listening
        if not self._ensure_running():
            print("✗ Cannot upload because tinyFaaS failed to start or is unreachable.")
            return False

        # Sanitize function name (alphanumeric only)
        alphanumeric_name = re.sub(r'[^a-zA-Z0-9]', '', function_name)
        
        print(f"Uploading {function_dir} as {alphanumeric_name}...")
        
        try:
            result = subprocess.run(
                [self.upload_script, function_dir, alphanumeric_name, runtime, "1"],
                check=True,
                cwd=self.tinyfaas_dir,
                capture_output=True,
                text=True
            )

            print(f"✓ Uploaded: {alphanumeric_name}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to upload {alphanumeric_name}: {e.stderr}")
            return False
    
    def trigger_function(self, function_name: str, 
                        data: Optional[dict] = None,
                        timeout: int = 30) -> Tuple[bool, str]:
        """
        Trigger a function and get its response.
        
        Args:
            function_name: Name of the function to trigger
            data: Optional data payload
            timeout: Request timeout in seconds
            
        Returns:
            Tuple of (success, response_text or error_message)
        """
        # make sure tinyFaaS management endpoint is available
        if not self._ensure_running():
            return False, "tinyFaaS is not running; cannot trigger function"

        # Sanitize function name
        alphanumeric_name = re.sub(r'[^a-zA-Z0-9]', '', function_name)
        url = f"http://localhost:{self.http_port}/{alphanumeric_name}"
        
        print(f"Triggering: {alphanumeric_name}")
        
        try:
            response = requests.post(url, json=data, timeout=timeout)
            
            if response.status_code == 200:
                print(f"✓ Triggered successfully: {alphanumeric_name}")
                return True, response.text
            else:
                error_msg = f"Status {response.status_code}: {response.text}"
                print(f"✗ Trigger failed: {error_msg}")
                return False, error_msg
                
        except requests.Timeout:
            error_msg = f"Timeout after {timeout} seconds"
            print(f"✗ {error_msg}")
            return False, error_msg
            
        except requests.RequestException as e:
            error_msg = f"Request error: {e}"
            print(f"✗ {error_msg}")
            return False, error_msg
    
    def deploy_and_execute(self, function_dir: str, function_name: str,
                          runtime: str = 'python3',
                          trigger_data: Optional[dict] = None) -> Tuple[bool, str, dict]:
        """
        Upload a function and immediately trigger it.

        Args:
            function_dir: Path to function directory
            function_name: Name for the function
            runtime: Runtime environment
            trigger_data: Optional data to send when triggering

        Returns:
            Tuple of (success, response_text or error_message, timing_dict).
            timing_dict keys: upload_s, execute_s (None when not reached).
        """
        # Upload
        t_upload = time.time()
        upload_success = self.upload_function(function_dir, function_name, runtime)
        upload_s = time.time() - t_upload

        if not upload_success:
            return False, "Upload failed", {'upload_s': upload_s, 'execute_s': None}

        # Small delay to ensure function is ready
        time.sleep(1)

        # Trigger
        t_exec = time.time()
        success, response = self.trigger_function(function_name, trigger_data)
        execute_s = time.time() - t_exec

        return success, response, {'upload_s': upload_s, 'execute_s': execute_s}
    
    def deploy_batch(self, function_dirs: list, runtime: str = 'python3',
                    execute: bool = False) -> list:
        """
        Deploy multiple functions.

        Args:
            function_dirs: List of function directory paths
            runtime: Runtime environment
            execute: Whether to also trigger each function

        Returns:
            List of tuples (function_name, success, response, timing_dict).
            timing_dict keys: upload_s, execute_s (execute_s is None when execute=False).
        """
        results = []

        for func_dir in function_dirs:
            func_name = os.path.basename(func_dir)

            if execute:
                success, response, timing = self.deploy_and_execute(func_dir, func_name, runtime)
            else:
                t_upload = time.time()
                success = self.upload_function(func_dir, func_name, runtime)
                upload_s = time.time() - t_upload
                response = "Not executed"
                timing = {'upload_s': upload_s, 'execute_s': None}

            results.append((func_name, success, response, timing))

            # Rate limiting
            time.sleep(2)

        return results


def main():
    """CLI for deployment."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Deploy functions to tinyFaaS')
    parser.add_argument('--tinyfaas-dir', required=True, help='TinyFaaS directory')
    parser.add_argument('--function-dir', help='Single function directory')
    parser.add_argument('--function-name', help='Function name')
    parser.add_argument('--functions-root', help='Root directory containing multiple functions')
    parser.add_argument('--runtime', choices=['python3', 'nodejs'], default='python3',
                       help='Runtime environment')
    parser.add_argument('--execute', action='store_true', help='Also trigger functions')
    
    args = parser.parse_args()
    
    manager = TinyFaaSManager(args.tinyfaas_dir)
    
    if args.function_dir and args.function_name:
        # Single function
        if args.execute:
            success, response = manager.deploy_and_execute(
                args.function_dir, args.function_name, args.runtime
            )
            print(f"Response: {response}")
        else:
            success = manager.upload_function(
                args.function_dir, args.function_name, args.runtime
            )
    
    elif args.functions_root:
        # Batch deployment
        function_dirs = [
            os.path.join(args.functions_root, d) 
            for d in os.listdir(args.functions_root)
            if os.path.isdir(os.path.join(args.functions_root, d))
        ]
        
        results = manager.deploy_batch(function_dirs, args.runtime, args.execute)
        
        successful = sum(1 for _, success, _ in results if success)
        print(f"✓ Deployed {successful}/{len(results)} functions")
    
    else:
        parser.error("Specify either --function-dir/--function-name or --functions-root")


if __name__ == '__main__':
    main()
