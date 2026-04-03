"""
Main generator module with provider-agnostic interface.
"""
import json
import os
import re
import time
from pathlib import Path
from typing import Optional

from .config import (
    TEMPERATURE, MAX_TOKENS, DELAY_SECONDS, DEFAULT_SYSTEM_PROMPT,
    OPENAI_API_KEY, OPENAI_MODEL, 
    OLLAMA_MODEL, OLLAMA_URL,
    GEMINI_API_KEY, GEMINI_MODEL
)
from .providers import OpenAIProvider, OllamaProvider


class LLMGenerator:
    """Provider-agnostic LLM generator for function code."""
    
    SUPPORTED_PROVIDERS = ['openai', 'ollama', 'gemini']

    @staticmethod
    def _extract_task_and_index(prompt_base_name: str) -> tuple[Optional[str], Optional[str]]:
        """Extract task name and sample index from prompt base name."""
        match = re.match(r'^(.*)_(\d+)$', prompt_base_name)
        if not match:
            return None, None
        return match.group(1), match.group(2)

    @staticmethod
    def _extract_ground_truth_payload(raw_response: str) -> dict:
        """Extract expected/actual/comparison payload from ground-truth raw response."""
        if not raw_response:
            return {}

        try:
            payload = json.loads(raw_response)
        except (TypeError, json.JSONDecodeError):
            return {}

        expected = payload.get('expected')
        actual = payload.get('actual')
        comparison = payload.get('comparison')

        if not isinstance(expected, dict) or not isinstance(actual, dict):
            return {}

        return {
            'expected_output': expected,
            'produced_output': actual,
            'comparison': comparison if isinstance(comparison, dict) else {},
        }

    def _save_validation_history(self,
                                 log_path: Path,
                                 refinement_loop,
                                 refinement_history: list,
                                 validation_mode: str) -> None:
        """Persist validation history and enrich ground-truth logs with runtime payloads."""
        refinement_loop.save_history(log_path)

        if validation_mode != 'ground-truth':
            return

        try:
            with open(log_path, 'r', encoding='utf-8') as f:
                log_data = json.load(f)

            iterations = log_data.get('iterations', [])
            for index, item in enumerate(iterations):
                if index >= len(refinement_history):
                    break
                raw_response = refinement_history[index].validation_result.raw_response
                payload = self._extract_ground_truth_payload(raw_response)
                if payload:
                    item['ground_truth_runtime'] = payload

            with open(log_path, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)
        except Exception:
            # Keep pipeline resilient if log enrichment fails.
            pass
    
    def __init__(self, provider: str, model: str = None, 
                 temperature: float = None, max_tokens: int = None,
                 api_key: str = None):
        """
        Initialize the generator with specified provider.
        
        Args:
            provider: Provider name (openai, ollama, gemini)
            model: Model name (uses default from config if None)
            temperature: Sampling temperature (uses default if None)
            max_tokens: Maximum tokens (uses default if None)
            api_key: API key (uses environment variable if None)
        """
        if provider not in self.SUPPORTED_PROVIDERS:
            raise ValueError(f"Provider must be one of {self.SUPPORTED_PROVIDERS}")
        
        self.provider_name = provider
        self.temperature = temperature or TEMPERATURE
        self.max_tokens = max_tokens or MAX_TOKENS
        
        # Initialize provider
        if provider == 'openai':
            model = model or OPENAI_MODEL
            api_key = api_key or OPENAI_API_KEY
            self.provider = OpenAIProvider(api_key, model, self.temperature, self.max_tokens)
        elif provider == 'ollama':
            model = model or OLLAMA_MODEL
            self.provider = OllamaProvider(model, self.temperature, self.max_tokens, OLLAMA_URL)
        elif provider == 'gemini':
            from .providers.gemini_provider import GeminiProvider
            model = model or GEMINI_MODEL
            api_key = api_key or GEMINI_API_KEY
            self.provider = GeminiProvider(api_key, model, self.temperature, self.max_tokens)
    
    def generate_from_prompt(self, prompt: str, system_prompt: str = None) -> str:
        """
        Generate Python code from a text prompt.
        
        Args:
            prompt: User prompt describing the function
            system_prompt: Optional system prompt (uses default if None)
            
        Returns:
            Generated Python code
        """
        if system_prompt is None:
            system_prompt = DEFAULT_SYSTEM_PROMPT
        
        response = self.provider.generate(prompt, system_prompt)
        return self.provider.extract_code(response)
    
    def generate_from_file(self, prompt_file: str, system_prompt: str = None) -> str:
        """
        Generate Python code from a prompt file.
        
        Args:
            prompt_file: Path to markdown file containing prompt
            system_prompt: Optional system prompt
            
        Returns:
            Generated Python code
        """
        with open(prompt_file, 'r', encoding='utf-8') as f:
            prompt = f.read()
        
        return self.generate_from_prompt(prompt, system_prompt)
    
    def generate_batch(self, prompt_dir: str, output_dir: str,
                      system_prompt: str = None, delay: float = None,
                      validate_judge: bool = False, judge_provider: str = None,
                      judge_model: str = None, max_iterations: int = None,
                      validation_log_dir: str = None,
                      validation_mode: str = 'none',
                      local_execution: bool = False,
                      local_timeout: int = 30) -> list:
        """
        Generate Python code from multiple prompt files.

        Args:
            prompt_dir: Directory containing prompt markdown files
            output_dir: Directory to save generated Python files
            system_prompt: Optional system prompt
            delay: Delay between API calls in seconds (uses default if None)
            validate_judge: Enable LLM-as-a-Judge validation (legacy alias)
            judge_provider: Provider for judge (defaults to generation provider)
            judge_model: Model for judge (defaults to generation model)
            max_iterations: Maximum refinement iterations (uses config default if None)
            validation_log_dir: Directory to save validation logs (optional)
            validation_mode: Validation mode ('none', 'judge', 'ground-truth')
            local_execution: Whether local execution is enabled for runtime validation
            local_timeout: Local execution timeout in seconds

        Returns:
            List of timing dicts, one per successfully processed file.
            Each dict contains: filename, task, provider, model, generate_s.
        """
        delay = delay or DELAY_SECONDS
        os.makedirs(output_dir, exist_ok=True)
        
        # Validate mode and support the legacy --validate-judge switch.
        if validate_judge and validation_mode == 'none':
            validation_mode = 'judge'

        if validation_mode not in {'none', 'judge', 'ground-truth'}:
            raise ValueError("validation_mode must be one of: none, judge, ground-truth")

        # Initialize validation components if enabled
        validator = None
        refinement_loop = None
        iteration_evaluator = None
        if validation_mode != 'none' and not local_execution:
            raise ValueError(
                "validation with per-iteration runtime evaluation requires --local/--local-execution"
            )

        if validation_mode != 'none':
            from ..validation.iteration_evaluator import IterationRuntimeEvaluator

            default_standard_logs_dir = Path(__file__).resolve().parents[2] / 'test' / 'standard_log'
            iteration_evaluator = IterationRuntimeEvaluator(
                standard_logs_dir=str(default_standard_logs_dir),
                local_timeout=local_timeout,
            )

        if validation_mode == 'judge':
            from ..validation import LLMJudge, RefinementLoop
            
            judge_provider = judge_provider or self.provider_name
            judge_model = judge_model or self.provider.model
            
            print(f"Validation enabled (judge): {judge_provider}/{judge_model}")
            validator = LLMJudge(judge_provider, judge_model)
            refinement_loop = RefinementLoop(validator, self, max_iterations)

            if validation_log_dir:
                os.makedirs(validation_log_dir, exist_ok=True)

        if validation_mode == 'ground-truth':
            from ..validation import GroundTruthValidator, RefinementLoop

            if not local_execution:
                raise ValueError("ground-truth validation currently requires --local/--local-execution")

            gt_provider = judge_provider or self.provider_name
            gt_model = judge_model or self.provider.model

            print(f"Validation enabled (ground-truth): {gt_provider}/{gt_model}")
            validator = GroundTruthValidator(
                provider=gt_provider,
                model=gt_model,
                local_execution=local_execution,
                local_timeout=local_timeout,
            )
            refinement_loop = RefinementLoop(validator, self, max_iterations)
            
            if validation_log_dir:
                os.makedirs(validation_log_dir, exist_ok=True)
        
        prompt_files = sorted([f for f in os.listdir(prompt_dir) if f.endswith('.md')])
        timing_records = []

        for filename in prompt_files:
            prompt_path = os.path.join(prompt_dir, filename)
            print(f"Processing: {prompt_path}")

            try:
                base_name = filename.replace('.md', '')
                task_name, sample_index = self._extract_task_and_index(base_name)

                # Read requirement for validation
                with open(prompt_path, 'r', encoding='utf-8') as f:
                    requirement = f.read()

                # --- start generation timer (includes validation/refinement) ---
                t_gen_start = time.time()

                # Generate initial code
                code = self.generate_from_file(prompt_path, system_prompt)

                # Validate and refine if enabled
                validation_result = None
                iteration_count = 1
                refinement_history = []

                if validation_mode != 'none' and validator and refinement_loop:
                    print(f"  Validating with {validation_mode}...")
                    code, validation_result, refinement_history = refinement_loop.refine_until_valid(
                        requirement,
                        code,
                        system_prompt,
                        iteration_evaluator=iteration_evaluator,
                        evaluation_context={
                            'task_name': task_name,
                            'sample_index': sample_index,
                        },
                    )
                    iteration_count = len(refinement_history)

                    if validation_result.is_valid:
                        print(f"  ✓ Validated (iteration {iteration_count})")
                    else:
                        print(f"  ⚠ Not validated after {iteration_count} iterations")
                        print(f"    Issues: {len(validation_result.issues)}")

                generate_s = time.time() - t_gen_start
                # ----------------------------------------------------------------

                # Create output filename with validation metadata
                if validation_mode != 'none' and validation_result:
                    status = "validated" if validation_result.is_valid else "unvalidated"
                    output_filename = (f"{self.provider_name}_{self.provider.model.replace('/', '_')}_"
                                     f"{base_name}_{status}_iter{iteration_count}.py")
                else:
                    output_filename = f"{self.provider_name}_{self.provider.model.replace('/', '_')}_{base_name}.py"

                output_path = os.path.join(output_dir, output_filename)

                # Save generated code
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(code)

                print(f"✓ Saved: {output_path}")

                # Record timing
                # Infer task from the base_name prefix (e.g. "remote_control_5" -> "remote_control")
                task_guess = '_'.join(base_name.split('_')[:-1]) if '_' in base_name else base_name
                timing_records.append({
                    'filename': output_filename,
                    'task': task_guess,
                    'provider': self.provider_name,
                    'model': self.provider.model,
                    'generate_s': generate_s,
                })

                # Save validation logs if enabled
                if validation_mode != 'none' and validation_log_dir and refinement_history:
                    log_filename = f"{base_name}_validation.json"
                    log_path = os.path.join(validation_log_dir, log_filename)
                    self._save_validation_history(
                        log_path=Path(log_path),
                        refinement_loop=refinement_loop,
                        refinement_history=refinement_history,
                        validation_mode=validation_mode,
                    )
                    print(f"  Validation log: {log_path}")

                # Rate limiting
                if delay > 0:
                    time.sleep(delay)

            except Exception as e:
                print(f"✗ Error processing {filename}: {e}")
                import traceback
                traceback.print_exc()
                continue

        return timing_records


def main():
    """CLI for the generator."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate function code using LLMs')
    parser.add_argument('--provider', required=True, 
                       choices=['openai', 'ollama', 'gemini'],
                       help='LLM provider')
    parser.add_argument('--model', help='Model name (optional, uses default)')
    parser.add_argument('--prompt-dir', required=True, help='Directory with prompt files')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    parser.add_argument('--temperature', type=float, help='Sampling temperature')
    parser.add_argument('--max-tokens', type=int, help='Maximum tokens')
    parser.add_argument('--delay', type=float, help='Delay between calls (seconds)')
    parser.add_argument('--api-key', help='API key (optional, uses env var)')
    
    args = parser.parse_args()
    
    generator = LLMGenerator(
        provider=args.provider,
        model=args.model,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        api_key=args.api_key
    )
    
    generator.generate_batch(
        prompt_dir=args.prompt_dir,
        output_dir=args.output_dir,
        delay=args.delay
    )
    
    print("✓ Batch generation complete")


if __name__ == '__main__':
    main()
