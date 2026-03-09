"""
Main generator module with provider-agnostic interface.
"""
import os
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
                      validation_log_dir: str = None) -> list:
        """
        Generate Python code from multiple prompt files.

        Args:
            prompt_dir: Directory containing prompt markdown files
            output_dir: Directory to save generated Python files
            system_prompt: Optional system prompt
            delay: Delay between API calls in seconds (uses default if None)
            validate_judge: Enable LLM-as-a-Judge validation
            judge_provider: Provider for judge (defaults to generation provider)
            judge_model: Model for judge (defaults to generation model)
            max_iterations: Maximum refinement iterations (uses config default if None)
            validation_log_dir: Directory to save validation logs (optional)

        Returns:
            List of timing dicts, one per successfully processed file.
            Each dict contains: filename, task, provider, model, generate_s.
        """
        delay = delay or DELAY_SECONDS
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize validation components if enabled
        judge = None
        refinement_loop = None
        if validate_judge:
            from ..validation import LLMJudge, RefinementLoop
            
            judge_provider = judge_provider or self.provider_name
            judge_model = judge_model or self.provider.model
            
            print(f"Validation enabled: {judge_provider}/{judge_model}")
            judge = LLMJudge(judge_provider, judge_model)
            refinement_loop = RefinementLoop(judge, self, max_iterations)
            
            if validation_log_dir:
                os.makedirs(validation_log_dir, exist_ok=True)
        
        prompt_files = sorted([f for f in os.listdir(prompt_dir) if f.endswith('.md')])
        timing_records = []

        for filename in prompt_files:
            prompt_path = os.path.join(prompt_dir, filename)
            print(f"Processing: {prompt_path}")

            try:
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

                if validate_judge and judge and refinement_loop:
                    print(f"  Validating with judge...")
                    code, validation_result, refinement_history = refinement_loop.refine_until_valid(
                        requirement, code, system_prompt
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
                base_name = filename.replace('.md', '')
                timestamp = int(time.time() * 1000)

                if validate_judge and validation_result:
                    status = "validated" if validation_result.is_valid else "unvalidated"
                    output_filename = (f"{self.provider_name}_{self.provider.model.replace('/', '_')}_"
                                     f"{base_name}_{status}_iter{iteration_count}_{timestamp}.py")
                else:
                    output_filename = f"{self.provider_name}_{self.provider.model.replace('/', '_')}_{base_name}_{timestamp}.py"

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
                if validate_judge and validation_log_dir and refinement_history:
                    log_filename = f"{base_name}_validation_{timestamp}.json"
                    log_path = os.path.join(validation_log_dir, log_filename)
                    refinement_loop.save_history(Path(log_path))
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
