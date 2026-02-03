"""
FaaS function preparation module.
Prepares generated Python/JavaScript code for tinyFaaS deployment.
"""
import os
import re
import shutil
from pathlib import Path
from typing import Optional


class FunctionPreparer:
    """Prepares functions for tinyFaaS deployment."""
    
    def __init__(self, smart_home_dir: str):
        """
        Initialize the preparer.
        
        Args:
            smart_home_dir: Path to the smart home code directory
        """
        self.smart_home_dir = smart_home_dir
    
    def prepare_python_function(self, source_file: str, output_dir: str,
                               function_name: Optional[str] = None) -> str:
        """
        Prepare a Python function for tinyFaaS.
        
        Args:
            source_file: Path to generated Python file
            output_dir: Root directory for function folders
            function_name: Optional name for the function (auto-generated if None)
            
        Returns:
            Path to the created function directory
        """
        # Generate function name from source file
        if function_name is None:
            function_name = Path(source_file).stem
        
        # Create function directory structure
        func_dir = os.path.join(output_dir, function_name)
        os.makedirs(func_dir, exist_ok=True)
        
        # Copy smart home code (flatten into function root for tinyFaaS python runtime)
        for entry in os.listdir(self.smart_home_dir):
            src_path = os.path.join(self.smart_home_dir, entry)
            dest_path = os.path.join(func_dir, entry)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dest_path)
            elif os.path.isdir(src_path):
                # Copy directories too (e.g., 'home' subdirectory)
                if os.path.exists(dest_path):
                    shutil.rmtree(dest_path)
                shutil.copytree(src_path, dest_path)
        
        # Copy and transform function code
        fn_path = os.path.join(func_dir, 'fn.py')
        self._transform_python_function(source_file, fn_path)
        
        # Create requirements.txt
        requirements_path = os.path.join(func_dir, 'requirements.txt')
        with open(requirements_path, 'w', encoding='utf-8') as f:
            pass  # Empty for now
        
        print(f"✓ Prepared Python function: {func_dir}")
        return func_dir
    
    def _transform_python_function(self, source: str, dest: str) -> None:
        """
        Transform Python code to FaaS format.
        Comments out 'if __name__ == "__main__":' and adds 'def fn(data, headers):'.
        
        Args:
            source: Source Python file
            dest: Destination fn.py file
        """
        with open(source, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        inserted_fn = False
        
        for line in lines:
            if 'from home.' in line:
                line = line.replace('from home.', 'from ')
            if 'import home.' in line:
                line = line.replace('import home.', 'import ')
            stripped = line.strip()
            if stripped == 'if __name__ == "__main__":':
                # Comment out the main guard
                new_lines.append("# " + line)
                if not inserted_fn:
                    new_lines.append("def fn(data, headers):\n")
                    inserted_fn = True
            else:
                new_lines.append(line)
        
        # If no main guard found, insert fn wrapper at the top
        if not inserted_fn:
            new_lines.insert(0, "def fn(data, headers):\n\n")
        
        with open(dest, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    
    def prepare_javascript_function(self, source_file: str, output_dir: str,
                                    function_name: Optional[str] = None) -> str:
        """
        Prepare a JavaScript function for tinyFaaS.
        
        Args:
            source_file: Path to generated JavaScript file
            output_dir: Root directory for function folders
            function_name: Optional name for the function
            
        Returns:
            Path to the created function directory
        """
        if function_name is None:
            function_name = Path(source_file).stem
        
        # Create function directory structure
        func_dir = os.path.join(output_dir, function_name)
        os.makedirs(func_dir, exist_ok=True)
        
        # Copy smart home code (NodeJS version)
        home_dest = os.path.join(func_dir, 'home')
        if os.path.exists(home_dest):
            shutil.rmtree(home_dest)
        shutil.copytree(self.smart_home_dir, home_dest)
        
        # Copy and transform function code
        index_path = os.path.join(func_dir, 'functions', 'index.js')
        os.makedirs(os.path.dirname(index_path), exist_ok=True)
        self._transform_javascript_function(source_file, index_path)
        
        # Create package.json
        package_json_path = os.path.join(func_dir, 'package.json')
        self._create_package_json(package_json_path, function_name)
        
        print(f"✓ Prepared JavaScript function: {func_dir}")
        return func_dir
    
    def _transform_javascript_function(self, source: str, dest: str) -> None:
        """
        Transform JavaScript code to FaaS format (module.exports = (req, res) => {...}).
        
        Args:
            source: Source JavaScript file
            dest: Destination index.js file
        """
        with open(source, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Wrap in module.exports if not already wrapped
        if 'module.exports' not in code:
            wrapped_code = f"module.exports = (req, res) => {{\n{code}\n}};\n"
        else:
            wrapped_code = code
        
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(wrapped_code)
    
    def _create_package_json(self, path: str, function_name: str) -> None:
        """Create a basic package.json for JavaScript functions."""
        package_json = {
            "name": function_name,
            "version": "1.0.0",
            "description": "LLM-generated smart home function",
            "main": "functions/index.js",
            "dependencies": {}
        }
        
        import json
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(package_json, f, indent=2)
    
    def prepare_batch(self, source_dir: str, output_dir: str, 
                     language: str = 'python') -> list:
        """
        Prepare multiple functions from a directory.
        
        Args:
            source_dir: Directory containing generated code files
            output_dir: Root directory for function folders
            language: Programming language ('python' or 'javascript')
            
        Returns:
            List of created function directory paths
        """
        extension = '.py' if language == 'python' else '.js'
        source_files = [f for f in os.listdir(source_dir) if f.endswith(extension)]
        
        prepared_dirs = []
        for filename in source_files:
            source_path = os.path.join(source_dir, filename)
            
            try:
                if language == 'python':
                    func_dir = self.prepare_python_function(source_path, output_dir)
                else:
                    func_dir = self.prepare_javascript_function(source_path, output_dir)
                
                prepared_dirs.append(func_dir)
            except Exception as e:
                print(f"✗ Error preparing {filename}: {e}")
                continue
        
        return prepared_dirs


def main():
    """CLI for function preparation."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Prepare functions for tinyFaaS')
    parser.add_argument('--source-dir', required=True, help='Directory with generated code')
    parser.add_argument('--output-dir', required=True, help='Output directory for functions')
    parser.add_argument('--smart-home-dir', required=True, help='Smart home code directory')
    parser.add_argument('--language', choices=['python', 'javascript'], default='python',
                       help='Programming language')
    
    args = parser.parse_args()
    
    preparer = FunctionPreparer(args.smart_home_dir)
    prepared = preparer.prepare_batch(args.source_dir, args.output_dir, args.language)
    
    print(f"✓ Prepared {len(prepared)} functions")


if __name__ == '__main__':
    main()
