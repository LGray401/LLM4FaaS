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
                      system_prompt: str = None, delay: float = None) -> None:
        """
        Generate Python code from multiple prompt files.
        
        Args:
            prompt_dir: Directory containing prompt markdown files
            output_dir: Directory to save generated Python files
            system_prompt: Optional system prompt
            delay: Delay between API calls in seconds (uses default if None)
        """
        delay = delay or DELAY_SECONDS
        os.makedirs(output_dir, exist_ok=True)
        
        prompt_files = sorted([f for f in os.listdir(prompt_dir) if f.endswith('.md')])
        
        for filename in prompt_files:
            prompt_path = os.path.join(prompt_dir, filename)
            print(f"Processing: {prompt_path}")
            
            try:
                code = self.generate_from_file(prompt_path, system_prompt)
                
                # Create output filename
                base_name = filename.replace('.md', '')
                timestamp = int(time.time() * 1000)
                output_filename = f"{self.provider_name}_{self.provider.model.replace('/', '_')}_{base_name}_{timestamp}.py"
                output_path = os.path.join(output_dir, output_filename)
                
                # Save generated code
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(code)
                
                print(f"✓ Saved: {output_path}")
                
                # Rate limiting
                if delay > 0:
                    time.sleep(delay)
                    
            except Exception as e:
                print(f"✗ Error processing {filename}: {e}")
                continue


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
