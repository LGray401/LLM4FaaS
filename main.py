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
from src.faas_deployment import FunctionPreparer, TinyFaaSManager, LocalExecutor
from src.evaluation import FunctionEvaluator, CodeQualityAnalyzer, LatencyWriter, ResultsAggregator


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
        
        # Setup validation log directory if validation enabled
        validation_log_dir = None
        if getattr(args, 'validate_judge', False):
            validation_log_dir = self.data_dir / 'validation' / args.experiment / args.task
            validation_log_dir.mkdir(parents=True, exist_ok=True)
        
        generator = LLMGenerator(
            provider=args.provider,
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens
        )
        
        timing_records = generator.generate_batch(
            prompt_dir=prompt_dir,
            output_dir=str(output_dir),
            delay=args.delay,
            validate_judge=getattr(args, 'validate_judge', False),
            judge_provider=getattr(args, 'judge_provider', None),
            judge_model=getattr(args, 'judge_model', None),
            max_iterations=getattr(args, 'max_iterations', None),
            validation_log_dir=str(validation_log_dir) if validation_log_dir else None
        )

        print(f"✓ Code saved to: {output_dir}")
        return str(output_dir), timing_records

    def deploy_functions(self, args):
        """Prepare functions, optionally deploy to tinyFaaS, and/or execute locally."""
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
        function_dirs, prepare_timings = preparer.prepare_batch(source_dir, str(prepared_dir), args.language)

        print(f"✓ Prepared {len(function_dirs)} functions")

        deploy_timings = []

        # Deploy to tinyFaaS (upload always; execution controlled by --execute)
        if args.tinyfaas_dir:
            print("\n→ Deploying to tinyFaaS...")
            manager = TinyFaaSManager(args.tinyfaas_dir)
            runtime = 'python3' if args.language == 'python' else 'nodejs'
            results = manager.deploy_batch(function_dirs, runtime, args.execute)

            successful = sum(1 for _, success, _, _ in results if success)
            print(f"✓ Deployed {successful}/{len(results)} functions")

            if args.execute:
                logs_dir = self.data_dir / 'logs' / args.experiment / args.task
                logs_dir.mkdir(parents=True, exist_ok=True)
                for func_name, success, response, timing in results:
                    # If local execution is also enabled, keep tinyFaaS logs out of
                    # the default evaluation directory to avoid duplicate samples.
                    if not getattr(args, 'local_execution', False):
                        log_path = logs_dir / f"{func_name}.log"
                        stdout = response if success else ""
                        stderr = "" if success else str(response)
                        return_code = 0 if success else 1
                        with open(log_path, 'w', encoding='utf-8') as log_file:
                            log_file.write("Standard Output:\n")
                            if stdout:
                                log_file.write(f"{stdout}\n")
                            log_file.write("Standard Error:\n")
                            if stderr:
                                log_file.write(f"{stderr}\n")
                            log_file.write(f"Return code: {return_code}\n")

                    deploy_timings.append({
                        'source_filename': f"{func_name}.py",
                        'upload_s': timing.get('upload_s'),
                        'execute_s': timing.get('execute_s'),
                    })
            else:
                for func_name, success, response, timing in results:
                    deploy_timings.append({
                        'source_filename': f"{func_name}.py",
                        'upload_s': timing.get('upload_s'),
                        'execute_s': timing.get('execute_s'),
                    })

        # Local execution for semantic evaluation without tinyFaaS response constraints.
        if getattr(args, 'local_execution', False):
            if args.language != 'python':
                raise ValueError("Local execution currently supports only --language python")

            print("\n→ Executing functions locally...")
            logs_dir = self.data_dir / 'logs' / args.experiment / args.task
            logs_dir.mkdir(parents=True, exist_ok=True)

            executor = LocalExecutor(timeout=getattr(args, 'local_timeout', 30))
            local_results = executor.execute_batch(function_dirs)

            successful_local = sum(1 for item in local_results if item['success'])
            print(f"✓ Locally executed {successful_local}/{len(local_results)} functions")

            for item in local_results:
                func_name = item['function_name']
                stdout = item['stdout'] or ""
                stderr = item['stderr'] or ""
                return_code = 0 if item['success'] else 1

                log_path = logs_dir / f"{func_name}.log"
                with open(log_path, 'w', encoding='utf-8') as log_file:
                    log_file.write("Standard Output:\n")
                    if stdout:
                        log_file.write(stdout)
                        if not stdout.endswith("\n"):
                            log_file.write("\n")
                    log_file.write("Standard Error:\n")
                    if stderr:
                        log_file.write(stderr)
                        if not stderr.endswith("\n"):
                            log_file.write("\n")
                    log_file.write(f"Return code: {return_code}\n")

                timing = item['timing']
                deploy_timings.append({
                    'source_filename': f"{func_name}.py",
                    'upload_s': timing.get('upload_s'),
                    'execute_s': timing.get('execute_s'),
                })

        return str(prepared_dir), prepare_timings, deploy_timings
    
    def evaluate_results(self, args):
        """Evaluate function outputs."""
        print("=" * 60)
        print("STEP 4: Evaluating Results")
        print("=" * 60)
        
        logs_dir = getattr(args, 'logs_dir', None) or str(self.data_dir / 'logs' / args.experiment / args.task)
        standard_logs_dir = getattr(args, 'standard_logs_dir', None) or str(self.base_dir / 'test' / 'standard_log')
        output_csv = self.data_dir / 'evaluation' / args.experiment / f'{args.task}_results.csv'
        output_csv.parent.mkdir(parents=True, exist_ok=True)
        
        evaluator = FunctionEvaluator(standard_logs_dir)
        results = evaluator.evaluate_batch(logs_dir, args.task)
        evaluator.write_results_to_csv(results, str(output_csv), args.task)
        
        print(f"✓ Evaluation saved to: {output_csv}")
        
        # Code quality analysis if requested
        if args.code_quality:
            print("\n→ Running code quality analysis...")
            source_dir = getattr(args, 'source_dir', None) or str(self.data_dir / 'functions' / args.experiment / f'{args.provider}_{args.task}')
            quality_output_dir = self.data_dir / 'evaluation' / args.experiment / 'code_quality' / args.task
            quality_output_dir.mkdir(parents=True, exist_ok=True)
            
            analyzer = CodeQualityAnalyzer()
            analyzer.analyze_directory(source_dir, str(quality_output_dir))
            
            print(f"✓ Code quality reports saved to: {quality_output_dir}")

        # Step 5 (integrated into Step 4): Aggregate results after every evaluation run.
        self._aggregate_results(args)

    def _aggregate_results(self, args):
        """Aggregate pass rates (and quality metrics when available) for the experiment."""
        print("\n→ Running aggregation...")

        evaluation_dir = self.data_dir / 'evaluation' / args.experiment
        aggregator = ResultsAggregator()

        # Aggregate pass rates across all evaluated task result files in this experiment.
        result_csv_paths = sorted(str(path) for path in evaluation_dir.glob('*_results.csv'))
        if result_csv_paths:
            pass_rates_output = evaluation_dir / 'pass_rates_summary.csv'
            aggregator.write_pass_rates_csv(result_csv_paths, str(pass_rates_output))
        else:
            print("! No *_results.csv files found for pass-rate aggregation")

        # Aggregate code-quality reports if the task report directory exists.
        quality_reports_dir = evaluation_dir / 'code_quality' / args.task
        if quality_reports_dir.exists():
            pylint_output = quality_reports_dir / 'pylint_scores.csv'
            radon_output = quality_reports_dir / 'radon_aggregates.csv'
            aggregator.parse_pylint_reports(str(quality_reports_dir), str(pylint_output))
            aggregator.parse_radon_reports(str(quality_reports_dir), str(radon_output))

        print("✓ Aggregation complete")
    
    def run_full_pipeline(self, args):
        """Run the complete pipeline from extraction to evaluation."""
        print("=" * 60)
        print("FULL PIPELINE: Extract → Generate → Deploy → Evaluate")
        print("=" * 60)

        # Step 1: Extract prompts
        prompt_dir = self.extract_prompts(args)
        args.prompt_dir = prompt_dir

        # Step 2: Generate code (captures per-sample timing)
        code_dir, generate_timings = self.generate_code(args)
        args.source_dir = code_dir

        # Step 3: Deploy (captures prepare + deploy timing)
        prepare_timings = []
        deploy_timings = []
        if args.tinyfaas_dir or getattr(args, 'local_execution', False):
            _, prepare_timings, deploy_timings = self.deploy_functions(args)

        # Write latency CSV when at least one timed stage ran
        if generate_timings or prepare_timings or deploy_timings:
            latency_writer = LatencyWriter()
            latency_writer.merge_generate_timings(generate_timings)
            latency_writer.merge_prepare_timings(prepare_timings)
            latency_writer.merge_deploy_timings(deploy_timings)

            latency_csv = self.data_dir / 'evaluation' / args.experiment / f'{args.task}_latency.csv'
            latency_csv.parent.mkdir(parents=True, exist_ok=True)
            latency_writer.write_csv(str(latency_csv))

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
    # Validation flags
    gen_parser.add_argument('--validate-judge', action='store_true',
                           help='Enable LLM-as-a-Judge validation')
    gen_parser.add_argument('--judge-provider',
                           choices=['openai', 'ollama', 'gemini'],
                           help='Judge provider (defaults to generation provider)')
    gen_parser.add_argument('--judge-model', help='Judge model (defaults to generation model)')
    gen_parser.add_argument('--max-iterations', type=int,
                           help='Maximum refinement iterations (default: 3)')
    
    # Deploy subcommand
    deploy_parser = subparsers.add_parser('deploy', parents=[common],
                                         help='Deploy functions to tinyFaaS')
    deploy_parser.add_argument('--source-dir', help='Directory with generated code')
    deploy_parser.add_argument('--tinyfaas-dir', help='TinyFaaS installation directory')
    deploy_parser.add_argument('--provider', help='Provider name (for path resolution)')
    deploy_parser.add_argument('--execute', action='store_true', help='Also execute functions')
    deploy_parser.add_argument('--local-execution', action='store_true',
                              help='Also execute prepared Python functions locally')
    deploy_parser.add_argument('--local-timeout', type=int, default=30,
                              help='Local execution timeout per function in seconds')
    
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
    # Validation flags for full pipeline
    full_parser.add_argument('--validate-judge', action='store_true',
                            help='Enable LLM-as-a-Judge validation')
    full_parser.add_argument('--judge-provider',
                            choices=['openai', 'ollama', 'gemini'],
                            help='Judge provider (defaults to generation provider)')
    full_parser.add_argument('--judge-model', help='Judge model (defaults to generation model)')
    full_parser.add_argument('--max-iterations', type=int,
                            help='Maximum refinement iterations (default: 3)')
    full_parser.add_argument('--provider', required=True, help='LLM provider')
    full_parser.add_argument('--model', help='Model name')
    full_parser.add_argument('--temperature', type=float, help='Sampling temperature')
    full_parser.add_argument('--max-tokens', type=int, help='Maximum tokens')
    full_parser.add_argument('--delay', type=float, help='Delay between API calls')
    full_parser.add_argument('--tinyfaas-dir', help='TinyFaaS directory')
    full_parser.add_argument('--execute', action='store_true', help='Execute functions')
    full_parser.add_argument('--local-execution', action='store_true',
                            help='Also execute prepared Python functions locally')
    full_parser.add_argument('--local-timeout', type=int, default=30,
                            help='Local execution timeout per function in seconds')
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
