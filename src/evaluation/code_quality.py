"""
Code quality evaluation module using Pylint and Radon.
"""
import os
import subprocess
from pathlib import Path
from typing import List, Dict


class CodeQualityAnalyzer:
    """Analyzes code quality using static analysis tools."""
    
    def __init__(self):
        """Initialize the analyzer."""
        pass
    
    def run_pylint(self, file_path: str, output_dir: str) -> str:
        """
        Run Pylint on a Python file.
        
        Args:
            file_path: Path to Python file
            output_dir: Directory to save report
            
        Returns:
            Path to the generated report
        """
        os.makedirs(output_dir, exist_ok=True)
        
        filename = Path(file_path).stem
        report_path = os.path.join(output_dir, f'{filename}_pylint.txt')
        
        try:
            result = subprocess.run(
                ['pylint', file_path],
                capture_output=True,
                text=True
            )
            
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(result.stdout)
                if result.stderr:
                    f.write(f"\n\nErrors:\n{result.stderr}")
            
            print(f"✓ Pylint report: {report_path}")
            return report_path
            
        except FileNotFoundError:
            print("✗ Pylint not installed. Install with: pip install pylint")
            return None
        except Exception as e:
            print(f"✗ Pylint error: {e}")
            return None
    
    def run_radon_cc(self, file_path: str, output_dir: str) -> str:
        """
        Run Radon cyclomatic complexity analysis.
        
        Args:
            file_path: Path to Python file
            output_dir: Directory to save report
            
        Returns:
            Path to the generated report
        """
        os.makedirs(output_dir, exist_ok=True)
        
        filename = Path(file_path).stem
        report_path = os.path.join(output_dir, f'{filename}_radon_cc.txt')
        
        try:
            result = subprocess.run(
                ['radon', 'cc', file_path, '-a'],
                capture_output=True,
                text=True
            )
            
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(result.stdout)
                if result.stderr:
                    f.write(f"\n\nErrors:\n{result.stderr}")
            
            print(f"✓ Radon CC report: {report_path}")
            return report_path
            
        except FileNotFoundError:
            print("✗ Radon not installed. Install with: pip install radon")
            return None
        except Exception as e:
            print(f"✗ Radon error: {e}")
            return None
    
    def run_radon_mi(self, file_path: str, output_dir: str) -> str:
        """
        Run Radon maintainability index analysis.
        
        Args:
            file_path: Path to Python file
            output_dir: Directory to save report
            
        Returns:
            Path to the generated report
        """
        os.makedirs(output_dir, exist_ok=True)
        
        filename = Path(file_path).stem
        report_path = os.path.join(output_dir, f'{filename}_radon_mi.txt')
        
        try:
            result = subprocess.run(
                ['radon', 'mi', file_path],
                capture_output=True,
                text=True
            )
            
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(result.stdout)
                if result.stderr:
                    f.write(f"\n\nErrors:\n{result.stderr}")
            
            print(f"✓ Radon MI report: {report_path}")
            return report_path
            
        except FileNotFoundError:
            print("✗ Radon not installed. Install with: pip install radon")
            return None
        except Exception as e:
            print(f"✗ Radon error: {e}")
            return None
    
    def analyze_file(self, file_path: str, output_dir: str, 
                     tools: List[str] = None) -> Dict[str, str]:
        """
        Run all specified analysis tools on a file.
        
        Args:
            file_path: Path to Python file
            output_dir: Directory to save reports
            tools: List of tools to run (['pylint', 'radon_cc', 'radon_mi'])
                  If None, runs all tools
            
        Returns:
            Dictionary mapping tool names to report paths
        """
        if tools is None:
            tools = ['pylint', 'radon_cc', 'radon_mi']
        
        results = {}
        
        if 'pylint' in tools:
            report_path = self.run_pylint(file_path, output_dir)
            if report_path:
                results['pylint'] = report_path
        
        if 'radon_cc' in tools:
            report_path = self.run_radon_cc(file_path, output_dir)
            if report_path:
                results['radon_cc'] = report_path
        
        if 'radon_mi' in tools:
            report_path = self.run_radon_mi(file_path, output_dir)
            if report_path:
                results['radon_mi'] = report_path
        
        return results
    
    def analyze_directory(self, source_dir: str, output_dir: str,
                         tools: List[str] = None) -> Dict[str, Dict[str, str]]:
        """
        Analyze all Python files in a directory.
        
        Args:
            source_dir: Directory containing Python files
            output_dir: Directory to save reports
            tools: List of tools to run
            
        Returns:
            Dictionary mapping filenames to their analysis results
        """
        results = {}
        
        for filename in os.listdir(source_dir):
            if filename.endswith('.py'):
                file_path = os.path.join(source_dir, filename)
                print(f"Analyzing: {filename}")
                
                file_results = self.analyze_file(file_path, output_dir, tools)
                results[filename] = file_results
        
        return results


def main():
    """CLI for code quality analysis."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze code quality')
    parser.add_argument('--source-dir', required=True, help='Directory with Python files')
    parser.add_argument('--output-dir', required=True, help='Output directory for reports')
    parser.add_argument('--tools', nargs='+', 
                       choices=['pylint', 'radon_cc', 'radon_mi'],
                       help='Tools to run (default: all)')
    
    args = parser.parse_args()
    
    analyzer = CodeQualityAnalyzer()
    results = analyzer.analyze_directory(args.source_dir, args.output_dir, args.tools)
    
    print(f"\n✓ Analyzed {len(results)} files")
    print(f"Reports saved to: {args.output_dir}")


if __name__ == '__main__':
    main()
