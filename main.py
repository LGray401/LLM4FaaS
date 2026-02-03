#!/usr/bin/env python3
"""
LLM4FaaS - No-Code FaaS Development using Large Language Models
Main entry point for the unified CLI.
"""
import os
import sys
import argparse
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.prompt_extraction import PromptExtractor
from src.llm_generation import LLMGenerator
from src.faas_deployment import FunctionPreparer, TinyFaaSManager
from src.evaluation import FunctionEvaluator, CodeQualityAnalyzer


class LLM4FaaS:
    """Main orchestrator for the LLM4FaaS pipeline."""
    
    def __init__(self, config: dict):
        """
        Initialize the orchestrator.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.base_dir = Path(__file__).parent
        self.data_dir = self.base_dir / 'data'
        self.templates_dir = self.base_dir / 'templates'
        
        # Ensure data directories exist
        (self.data_dir / 'input').mkdir(parents=True, exist_ok=True)
        (self.data_dir / 'prompts').mkdir(parents=True, exist_ok=True)
        (self.data_dir / 'functions').mkdir(parents=True, exist_ok=True)
        (self.data_dir / 'logs').mkdir(parents=True, exist_ok=True)
        (self.data_dir / 'evaluation').mkdir(parents=True, exist_ok=True)
    
    def extract_prompts(self, args):
        """Extract prompts from Excel data."""
        print("=" * 60)
        print("STEP 1: Extracting Prompts")
        print("=" * 60)
        
        excel_path = args.excel or str(self.data_dir / 'input' / 'data.xlsx')
        if not os.path.exists(excel_path):
            raise FileNotFoundError(
                f"Excel file not found: {excel_path}. "
                "Provide --excel or place data.xlsx under data/input/."
            )
        template_path = self._get_template_path(args.language, args.template_type, args.task)
        output_dir = self.data_dir / 'prompts' / args.experiment / args.task
        
        extractor = PromptExtractor(excel_path, args.sheet)
        
        if args.task in ['remote_control', 'energy_control']:
            extractor.extract_remote_control(
                template_path, str(output_dir), args.column, args.task
            )
        elif args.task == 'auto_adapt':
            extractor.extract_auto_adapt(
                template_path, str(output_dir),
                args.temp_col, args.humidity_col, args.light_col
            )
        elif args.task == 'plan':
            extractor.extract_plan(
                template_path, str(output_dir),
                args.morning_col, args.leave_col, args.movie_col
            )
        
        print(f"✓ Prompts saved to: {output_dir}")
        return str(output_dir)
    
    def generate_code(self, args):
        """Generate function code using LLM."""
        print("=" * 60)
        print("STEP 2: Generating Code")
        print("=" * 60)
        
        prompt_dir = args.prompt_dir or str(self.data_dir / 'prompts' / args.experiment / args.task)
        output_dir = self.data_dir / 'functions' / args.experiment / f'{args.provider}_{args.task}'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        generator = LLMGenerator(
            provider=args.provider,
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens
        )
        
        generator.generate_batch(
            prompt_dir=prompt_dir,
            output_dir=str(output_dir),
            delay=args.delay
        )
        
        print(f"✓ Code saved to: {output_dir}")
        return str(output_dir)
    
    def deploy_functions(self, args):
        """Prepare and deploy functions to tinyFaaS."""
        print("=" * 60)
        print("STEP 3: Deploying to tinyFaaS")
        print("=" * 60)
        
        source_dir = args.source_dir or str(self.data_dir / 'functions' / args.experiment / f'{args.provider}_{args.task}')
        prepared_dir = self.data_dir / 'functions' / args.experiment / f'{args.provider}_{args.task}_prepared'
        prepared_dir.mkdir(parents=True, exist_ok=True)
        
        smart_home_dir = self.templates_dir / 'smart_home'
        
        # Prepare functions
        print("\n→ Preparing functions...")
        preparer = FunctionPreparer(str(smart_home_dir))
        function_dirs = preparer.prepare_batch(source_dir, str(prepared_dir), args.language)
        
        print(f"✓ Prepared {len(function_dirs)} functions")
        
        # Deploy to tinyFaaS
        if args.tinyfaas_dir:
            print("\n→ Deploying to tinyFaaS...")
            manager = TinyFaaSManager(args.tinyfaas_dir)
            runtime = 'python3' if args.language == 'python' else 'nodejs'
            results = manager.deploy_batch(function_dirs, runtime, args.execute)
            
            successful = sum(1 for _, success, _ in results if success)
            print(f"✓ Deployed {successful}/{len(results)} functions")
            
            if args.execute:
                logs_dir = self.data_dir / 'logs' / args.experiment / args.task
                logs_dir.mkdir(parents=True, exist_ok=True)
                # Save execution results to logs
                # (Implementation depends on how tinyFaaS returns logs)
        
        return str(prepared_dir)
    
    def evaluate_results(self, args):
        """Evaluate function outputs."""
        print("=" * 60)
        print("STEP 4: Evaluating Results")
        print("=" * 60)
        
        logs_dir = args.logs_dir or str(self.data_dir / 'logs' / args.experiment / args.task)
        standard_logs_dir = args.standard_logs_dir or str(self.data_dir / 'input' / 'standard_logs')
        output_csv = self.data_dir / 'evaluation' / args.experiment / f'{args.task}_results.csv'
        output_csv.parent.mkdir(parents=True, exist_ok=True)
        
        evaluator = FunctionEvaluator(standard_logs_dir)
        results = evaluator.evaluate_batch(logs_dir, args.task)
        evaluator.write_results_to_csv(results, str(output_csv), args.task)
        
        print(f"✓ Evaluation saved to: {output_csv}")
        
        # Code quality analysis if requested
        if args.code_quality:
            print("\n→ Running code quality analysis...")
            source_dir = args.source_dir or str(self.data_dir / 'functions' / args.experiment / f'{args.provider}_{args.task}')
            quality_output_dir = self.data_dir / 'evaluation' / args.experiment / 'code_quality' / args.task
            quality_output_dir.mkdir(parents=True, exist_ok=True)
            
            analyzer = CodeQualityAnalyzer()
            analyzer.analyze_directory(source_dir, str(quality_output_dir))
            
            print(f"✓ Code quality reports saved to: {quality_output_dir}")
    
    def run_full_pipeline(self, args):
        """Run the complete pipeline from extraction to evaluation."""
        print("=" * 60)
        print("FULL PIPELINE: Extract → Generate → Deploy → Evaluate")
        print("=" * 60)
        
        # Step 1: Extract prompts
        prompt_dir = self.extract_prompts(args)
        args.prompt_dir = prompt_dir
        
        # Step 2: Generate code
        code_dir = self.generate_code(args)
        args.source_dir = code_dir
        
        # Step 3: Deploy (if tinyFaaS dir provided)
        if args.tinyfaas_dir:
            self.deploy_functions(args)
        
        # Step 4: Evaluate (if logs available)
        if args.evaluate:
            self.evaluate_results(args)
        
        print("\n" + "=" * 60)
        print("✓ Full pipeline complete!")
        print("=" * 60)
    
    def _get_template_path(self, language: str, template_type: str, task: str) -> str:
        """Get the appropriate template path."""
        if template_type == 'baseline':
            template_dir = self.templates_dir / 'baseline'
            if task == 'plan':
                return str(template_dir / 'baseline_v2_plans_template.md')
            else:
                return str(template_dir / 'baseline_v2_remote-control_template.md')
        
        elif language == 'javascript':
            template_dir = self.templates_dir / 'javascript'
            if 'baseline' in template_type:
                if task == 'plan':
                    return str(template_dir / 'js_baseline_plans_template.md')
                elif task == 'auto_adapt':
                    return str(template_dir / 'js_baseline_auto_adapt_template.md')
                else:
                    return str(template_dir / 'js_baseline_remote_control_template.md')
            else:
                if task in ['auto_adapt', 'plan']:
                    return str(template_dir / 'js_keyword-prompt_template.md')
                else:
                    return str(template_dir / 'js_remote-control-prompt_template.md')
        
        else:  # Python
            template_dir = self.templates_dir / 'python'
            if task in ['auto_adapt', 'plan']:
                return str(template_dir / 'keyword-prompt_template.md')
            else:
                return str(template_dir / 'remote-control-prompt_template.md')


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='LLM4FaaS - Generate FaaS functions using LLMs',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Common arguments
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--experiment', default='default', help='Experiment name')
    common.add_argument('--task', required=True,
                       choices=['remote_control', 'energy_control', 'auto_adapt', 'plan'],
                       help='Task type')
    common.add_argument('--language', choices=['python', 'javascript'], default='python',
                       help='Programming language')
    
    # Extract subcommand
    extract_parser = subparsers.add_parser('extract', parents=[common],
                                           help='Extract prompts from Excel')
    extract_parser.add_argument('--excel', help='Path to Excel file')
    extract_parser.add_argument('--sheet', default='Sheet1', help='Sheet name')
    extract_parser.add_argument('--template-type', default='default',
                               choices=['default', 'baseline', 'baseline_auto', 'baseline_plans'],
                               help='Template type')
    extract_parser.add_argument('--column', type=int, help='Column index (remote/energy)')
    extract_parser.add_argument('--temp-col', type=int, help='Temperature column (auto_adapt)')
    extract_parser.add_argument('--humidity-col', type=int, help='Humidity column (auto_adapt)')
    extract_parser.add_argument('--light-col', type=int, help='Light column (auto_adapt)')
    extract_parser.add_argument('--morning-col', type=int, help='Morning column (plan)')
    extract_parser.add_argument('--leave-col', type=int, help='Leave home column (plan)')
    extract_parser.add_argument('--movie-col', type=int, help='Movie column (plan)')
    
    # Generate subcommand
    gen_parser = subparsers.add_parser('generate', parents=[common],
                                       help='Generate code using LLM')
    gen_parser.add_argument('--provider', required=True,
                           choices=['openai', 'ollama', 'gemini'],
                           help='LLM provider')
    gen_parser.add_argument('--model', help='Model name (uses default if not specified)')
    gen_parser.add_argument('--prompt-dir', help='Directory with prompts')
    gen_parser.add_argument('--temperature', type=float, help='Sampling temperature')
    gen_parser.add_argument('--max-tokens', type=int, help='Maximum tokens')
    gen_parser.add_argument('--delay', type=float, help='Delay between API calls (seconds)')
    
    # Deploy subcommand
    deploy_parser = subparsers.add_parser('deploy', parents=[common],
                                         help='Deploy functions to tinyFaaS')
    deploy_parser.add_argument('--source-dir', help='Directory with generated code')
    deploy_parser.add_argument('--tinyfaas-dir', help='TinyFaaS installation directory')
    deploy_parser.add_argument('--provider', help='Provider name (for path resolution)')
    deploy_parser.add_argument('--execute', action='store_true', help='Also execute functions')
    
    # Evaluate subcommand
    eval_parser = subparsers.add_parser('evaluate', parents=[common],
                                       help='Evaluate function outputs')
    eval_parser.add_argument('--logs-dir', help='Directory with execution logs')
    eval_parser.add_argument('--standard-logs-dir', help='Directory with standard logs')
    eval_parser.add_argument('--source-dir', help='Source directory for code quality')
    eval_parser.add_argument('--code-quality', action='store_true',
                            help='Run code quality analysis')
    eval_parser.add_argument('--provider', help='Provider name (for path resolution)')
    
    # Full pipeline subcommand
    full_parser = subparsers.add_parser('full', parents=[common],
                                       help='Run complete pipeline')
    full_parser.add_argument('--excel', help='Path to Excel file')
    full_parser.add_argument('--sheet', default='Sheet1', help='Sheet name')
    full_parser.add_argument('--template-type', default='default', help='Template type')
    full_parser.add_argument('--column', type=int, help='Column index')
    full_parser.add_argument('--temp-col', type=int, help='Temperature column')
    full_parser.add_argument('--humidity-col', type=int, help='Humidity column')
    full_parser.add_argument('--light-col', type=int, help='Light column')
    full_parser.add_argument('--morning-col', type=int, help='Morning column')
    full_parser.add_argument('--leave-col', type=int, help='Leave home column')
    full_parser.add_argument('--movie-col', type=int, help='Movie column')
    full_parser.add_argument('--provider', required=True, help='LLM provider')
    full_parser.add_argument('--model', help='Model name')
    full_parser.add_argument('--temperature', type=float, help='Sampling temperature')
    full_parser.add_argument('--max-tokens', type=int, help='Maximum tokens')
    full_parser.add_argument('--delay', type=float, help='Delay between API calls')
    full_parser.add_argument('--tinyfaas-dir', help='TinyFaaS directory')
    full_parser.add_argument('--execute', action='store_true', help='Execute functions')
    full_parser.add_argument('--evaluate', action='store_true', help='Run evaluation')
    full_parser.add_argument('--code-quality', action='store_true', help='Run code quality analysis')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Initialize orchestrator
    llm4faas = LLM4FaaS({})
    
    # Route to appropriate handler
    if args.command == 'extract':
        llm4faas.extract_prompts(args)
    elif args.command == 'generate':
        llm4faas.generate_code(args)
    elif args.command == 'deploy':
        llm4faas.deploy_functions(args)
    elif args.command == 'evaluate':
        llm4faas.evaluate_results(args)
    elif args.command == 'full':
        llm4faas.run_full_pipeline(args)


if __name__ == '__main__':
    main()
