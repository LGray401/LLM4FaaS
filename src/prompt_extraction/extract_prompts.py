"""
Prompt extraction module for LLM4FaaS.
Extracts user requirements from Excel files and generates prompt files from templates.
"""
import pandas as pd
import os
from pathlib import Path


class PromptExtractor:
    """Handles extraction of prompts from Excel data using templates."""
    
    def __init__(self, excel_file: str, sheet_name: str = 'Sheet1'):
        """
        Initialize the prompt extractor.
        
        Args:
            excel_file: Path to the Excel file containing user requirements
            sheet_name: Name of the sheet to read from
        """
        self.excel_file = excel_file
        self.sheet_name = sheet_name
        self.df = self._read_excel_with_fallback(excel_file, sheet_name)

    @staticmethod
    def _read_excel_with_fallback(excel_file: str, sheet_name: str):
        """Read Excel sheet with a fallback to the first sheet if name is missing."""
        try:
            return pd.read_excel(excel_file, sheet_name=sheet_name)
        except ValueError as exc:
            with pd.ExcelFile(excel_file) as xls:
                available_sheets = list(xls.sheet_names)
            if available_sheets and sheet_name not in available_sheets:
                fallback_sheet = available_sheets[0]
                print(
                    f"⚠️  Sheet '{sheet_name}' not found. "
                    f"Using first sheet '{fallback_sheet}'."
                )
                return pd.read_excel(excel_file, sheet_name=fallback_sheet)
            raise exc
    
    def extract_remote_control(self, template_path: str, output_dir: str, 
                               column_index: int, prefix: str = 'remote_control'):
        """
        Extract remote control prompts.
        
        Args:
            template_path: Path to the template markdown file
            output_dir: Directory to save generated prompts
            column_index: Excel column index containing the requirements
            prefix: Prefix for output filenames
        """
        if column_index is None:
            column_index = self._infer_column_index(prefix)
        texts = self.df.iloc[:, column_index].dropna().tolist()
        os.makedirs(output_dir, exist_ok=True)
        
        for i, text in enumerate(texts):
            with open(template_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            content = content.replace('<!-- INSERT HERE -->', str(text))
            output_file = os.path.join(output_dir, f'{prefix}_{i+1}.md')
            
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f'Generated: {output_file}')

    def _infer_column_index(self, task_prefix: str) -> int:
        """Infer column index based on task prefix and column names."""
        normalized_columns = [str(col).lower() for col in self.df.columns]

        if task_prefix == 'remote_control':
            keywords = ['remote control', 'functional scenario 1']
        elif task_prefix == 'energy_control':
            keywords = ['energy saving mode', 'functional scenario 4', 'energy']
        else:
            keywords = []

        for keyword in keywords:
            for idx, col in enumerate(normalized_columns):
                if keyword in col:
                    return idx

        available = ", ".join([str(col) for col in self.df.columns])
        raise ValueError(
            "Column index not provided and no matching column found for "
            f"task '{task_prefix}'. Available columns: {available}"
        )
    
    def extract_energy_control(self, template_path: str, output_dir: str,
                               column_index: int, prefix: str = 'energy_control'):
        """
        Extract energy control prompts (same format as remote control).
        
        Args:
            template_path: Path to the template markdown file
            output_dir: Directory to save generated prompts
            column_index: Excel column index containing the requirements
            prefix: Prefix for output filenames
        """
        self.extract_remote_control(template_path, output_dir, column_index, prefix)
    
    def extract_auto_adapt(self, template_path: str, output_dir: str,
                          temp_col: int, humidity_col: int, light_col: int,
                          prefix: str = 'auto_adapt'):
        """
        Extract auto-adapt prompts with three sensor thresholds.
        
        Args:
            template_path: Path to the template markdown file
            output_dir: Directory to save generated prompts
            temp_col: Column index for temperature threshold
            humidity_col: Column index for humidity threshold
            light_col: Column index for light threshold
            prefix: Prefix for output filenames
        """
        temperatures = self.df.iloc[:, temp_col].dropna().astype(str).tolist()
        humidities = self.df.iloc[:, humidity_col].dropna().astype(str).tolist()
        lights = self.df.iloc[:, light_col].dropna().astype(str).tolist()
        
        os.makedirs(output_dir, exist_ok=True)
        
        min_length = min(len(temperatures), len(humidities), len(lights))
        
        for i in range(min_length):
            with open(template_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            content = content.replace('<!-- INSERT TEMPERATURE HERE -->', temperatures[i])
            content = content.replace('<!-- INSERT HUMIDITY HERE -->', humidities[i])
            content = content.replace('<!-- INSERT LIGHT HERE -->', lights[i])
            
            output_file = os.path.join(output_dir, f'{prefix}_{i+1}.md')
            
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f'Generated: {output_file}')
    
    def extract_plan(self, template_path: str, output_dir: str,
                    morning_col: int, leave_home_col: int, movie_col: int,
                    prefix: str = 'plan'):
        """
        Extract plan prompts with three scenarios (morning, leave_home, movie).
        
        Args:
            template_path: Path to the template markdown file
            output_dir: Directory to save generated prompts
            morning_col: Column index for morning plan
            leave_home_col: Column index for leave home plan
            movie_col: Column index for movie plan
            prefix: Prefix for output filenames
        """
        morning_plans = self.df.iloc[:, morning_col].dropna().astype(str).tolist()
        leave_home_plans = self.df.iloc[:, leave_home_col].dropna().astype(str).tolist()
        movie_plans = self.df.iloc[:, movie_col].dropna().astype(str).tolist()
        
        os.makedirs(output_dir, exist_ok=True)
        
        min_length = min(len(morning_plans), len(leave_home_plans), len(movie_plans))
        
        for i in range(min_length):
            with open(template_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            content = content.replace('<!-- INSERT MORNING HERE -->', morning_plans[i])
            content = content.replace('<!-- INSERT LEAVE_HOME HERE -->', leave_home_plans[i])
            content = content.replace('<!-- INSERT MOVIE HERE -->', movie_plans[i])
            
            output_file = os.path.join(output_dir, f'{prefix}_{i+1}.md')
            
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f'Generated: {output_file}')


def main():
    """Example usage of the PromptExtractor."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Extract prompts from Excel data')
    parser.add_argument('--excel', required=True, help='Path to Excel file')
    parser.add_argument('--sheet', default='Sheet1', help='Sheet name')
    parser.add_argument('--task', required=True, 
                       choices=['remote_control', 'energy_control', 'auto_adapt', 'plan'],
                       help='Task type')
    parser.add_argument('--template', required=True, help='Path to template file')
    parser.add_argument('--output', required=True, help='Output directory')
    parser.add_argument('--column', type=int, help='Column index (for remote/energy)')
    parser.add_argument('--temp-col', type=int, help='Temperature column (for auto_adapt)')
    parser.add_argument('--humidity-col', type=int, help='Humidity column (for auto_adapt)')
    parser.add_argument('--light-col', type=int, help='Light column (for auto_adapt)')
    parser.add_argument('--morning-col', type=int, help='Morning column (for plan)')
    parser.add_argument('--leave-col', type=int, help='Leave home column (for plan)')
    parser.add_argument('--movie-col', type=int, help='Movie column (for plan)')
    
    args = parser.parse_args()
    
    extractor = PromptExtractor(args.excel, args.sheet)
    
    if args.task == 'remote_control':
        extractor.extract_remote_control(args.template, args.output, args.column)
    elif args.task == 'energy_control':
        extractor.extract_energy_control(args.template, args.output, args.column)
    elif args.task == 'auto_adapt':
        extractor.extract_auto_adapt(args.template, args.output, 
                                    args.temp_col, args.humidity_col, args.light_col)
    elif args.task == 'plan':
        extractor.extract_plan(args.template, args.output,
                              args.morning_col, args.leave_col, args.movie_col)
    
    print('All files generated successfully.')


if __name__ == '__main__':
    main()
