"""
Evaluation module for testing function outputs against standard logs.
"""
import os
import re
import csv
import logging
from typing import List, Tuple, Optional
from pathlib import Path


class FunctionEvaluator:
    """Evaluates function outputs against expected results."""
    
    def __init__(self, standard_logs_dir: str, log_level: int = logging.INFO):
        """
        Initialize the evaluator.
        
        Args:
            standard_logs_dir: Directory containing standard log files
            log_level: Logging level
        """
        self.standard_logs_dir = standard_logs_dir
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(log_level)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def parse_log_file(self, log_file_path: str) -> Tuple[str, str, Optional[int]]:
        """
        Parse a log file into stdout, stderr, and return code.
        
        Args:
            log_file_path: Path to log file
            
        Returns:
            Tuple of (stdout, stderr, return_code)
        """
        stdout, stderr, return_code = [], [], None
        current_section = None
        
        with open(log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line == 'Standard Output:':
                    current_section = 'stdout'
                elif line == 'Standard Error:':
                    current_section = 'stderr'
                elif line.startswith('Return code:'):
                    try:
                        return_code = int(line.split('Return code:')[1].strip())
                    except ValueError:
                        return_code = None
                elif current_section == 'stdout':
                    stdout.append(line)
                elif current_section == 'stderr':
                    stderr.append(line)
        
        return '\n'.join(stdout), '\n'.join(stderr), return_code
    
    def multi_condition_match(self, standard_line: str, actual_lines: List[str]) -> bool:
        """
        Check if any condition in standard_line matches actual output.
        Conditions in standard_line are separated by '||'.
        
        Args:
            standard_line: Expected output line (may contain || for OR conditions)
            actual_lines: List of actual output lines
            
        Returns:
            True if any condition matches
        """
        conditions = [cond.strip() for cond in standard_line.split('||')]
        return any(any(cond in actual_line for actual_line in actual_lines) for cond in conditions)
    
    def evaluate_log(self, actual_log_path: str, standard_log_path: str) -> dict:
        """
        Evaluate an actual log against a standard log.
        
        Args:
            actual_log_path: Path to actual log file
            standard_log_path: Path to standard log file
            
        Returns:
            Dictionary with evaluation results
        """
        actual_stdout, actual_stderr, actual_return_code = self.parse_log_file(actual_log_path)
        standard_stdout, _, _ = self.parse_log_file(standard_log_path)
        
        status = ''
        unmatched_lines = None
        match_percentage = 0
        
        # Check for errors first
        if actual_return_code == 1:
            status = "Error"
            self.logger.error(f"{actual_log_path}: Error detected with return code 1")
        elif actual_stderr:
            status = "Warning Exists"
        elif actual_return_code == 0:
            status = "No Error & Warning"
        elif actual_return_code is None:
            status = "Timeout"
        else:
            status = f"Unexpected return code {actual_return_code}"
            self.logger.warning(f"{actual_log_path}: {status}")
        
        # Compare outputs if no critical errors
        if status in {"No Error & Warning", "Warning Exists", "Timeout"}:
            actual_output_lines = actual_stdout.strip().splitlines()
            standard_output_lines = standard_stdout.strip().splitlines()
            
            matched_lines = [
                line for line in standard_output_lines 
                if self.multi_condition_match(line, actual_output_lines)
            ]
            unmatched_lines = [
                line for line in standard_output_lines 
                if not self.multi_condition_match(line, actual_output_lines)
            ]
            
            matched_count = len(matched_lines)
            total_standard_lines = len(standard_output_lines)
            match_percentage = matched_count / total_standard_lines if total_standard_lines > 0 else 0
            
            # Check for special markers in unmatched lines
            if unmatched_lines:
                if any("Manual Check Required" in line for line in unmatched_lines):
                    status = "Manual Check Required"
                    unmatched_lines = None
                    self.logger.info(f"{actual_log_path}: Manual Check Required")
                elif any("Invalid prompt" in line for line in unmatched_lines):
                    status = "Invalid Prompt"
                    unmatched_lines = None
                    self.logger.info(f"{actual_log_path}: Invalid Prompt")
                else:
                    if status == "No Error & Warning":
                        self.logger.info(
                            f"{actual_log_path}: Matched {matched_count}/{total_standard_lines} "
                            f"({match_percentage * 100:.2f}% match)"
                        )
            else:
                self.logger.info(
                    f"{actual_log_path}: All lines matched! "
                    f"{matched_count}/{total_standard_lines} ({match_percentage * 100:.2f}% match)"
                )
        
        return {
            'log_file': actual_log_path,
            'match_percentage': match_percentage,
            'status': status,
            'unmatched_lines': unmatched_lines
        }
    
    def evaluate_batch(self, logs_dir: str, task_name: str) -> List[dict]:
        """
        Evaluate all logs for a specific task.
        
        Args:
            logs_dir: Directory containing actual log files
            task_name: Task name (e.g., 'remote_control', 'auto_adapt')
            
        Returns:
            List of evaluation result dictionaries
        """
        results = []
        
        for filename in os.listdir(logs_dir):
            if task_name in filename and filename.endswith('.log'):
                actual_log_path = os.path.join(logs_dir, filename)
                
                # Extract user answer index
                match = re.search(rf'{task_name}_(\d+)', filename)
                if not match:
                    self.logger.warning(f"Could not parse index from {filename}")
                    continue
                
                user_index = match.group(1)
                standard_log_filename = f'{task_name}_{user_index}.log'
                standard_log_path = os.path.join(self.standard_logs_dir, task_name, standard_log_filename)
                
                if os.path.exists(standard_log_path):
                    result = self.evaluate_log(actual_log_path, standard_log_path)
                    results.append(result)
                else:
                    self.logger.debug(f"{actual_log_path}: Standard log not found")
                    results.append({
                        'log_file': actual_log_path,
                        'match_percentage': None,
                        'status': 'Standard log not found',
                        'unmatched_lines': None
                    })
        
        return results
    
    def write_results_to_csv(self, results: List[dict], output_path: str, task_name: str) -> None:
        """
        Write evaluation results to CSV.
        
        Args:
            results: List of evaluation result dictionaries
            output_path: Path to output CSV file
            task_name: Task name
        """
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'Filename', 'Task Name', 'User Index', 
                'Success Rate', 'Status', 'Unmatched Lines'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for result in results:
                filename = os.path.basename(result['log_file'])
                
                # Extract user index
                match = re.search(rf'{task_name}_(\d+)', filename)
                user_index = match.group(1) if match else 'Unknown'
                
                success_rate = f"{result['match_percentage']:.4f}" if result['match_percentage'] is not None else "N/A"
                
                writer.writerow({
                    'Filename': filename,
                    'Task Name': task_name,
                    'User Index': user_index,
                    'Success Rate': success_rate,
                    'Status': result['status'],
                    'Unmatched Lines': result['unmatched_lines']
                })


def main():
    """CLI for evaluation."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Evaluate function outputs')
    parser.add_argument('--logs-dir', required=True, help='Directory with actual logs')
    parser.add_argument('--standard-logs-dir', required=True, help='Directory with standard logs')
    parser.add_argument('--task', required=True, 
                       choices=['remote_control', 'energy_control', 'auto_adapt', 'plan'],
                       help='Task name')
    parser.add_argument('--output', required=True, help='Output CSV file')
    
    args = parser.parse_args()
    
    evaluator = FunctionEvaluator(args.standard_logs_dir)
    results = evaluator.evaluate_batch(args.logs_dir, args.task)
    evaluator.write_results_to_csv(results, args.output, args.task)
    
    print(f"✓ Evaluated {len(results)} logs, saved to {args.output}")


if __name__ == '__main__':
    main()
