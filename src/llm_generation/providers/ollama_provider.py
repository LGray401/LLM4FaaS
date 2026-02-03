"""
Ollama provider implementation.
"""
import json
import requests
from openai import OpenAI
from .base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):
    """Ollama local LLM provider."""
    
    def __init__(self, model: str = 'deepseek-r1:7b', 
                 temperature: float = 0.7, max_tokens: int = 1500,
                 url: str = 'http://localhost:11434/api/generate'):
        """
        Initialize Ollama provider.
        
        Args:
            model: Ollama model name
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            url: Ollama API URL
        """
        super().__init__(model, temperature, max_tokens)
        self.url = url
    
    def generate(self, prompt: str, system_prompt: str = None) -> str:
        """Generate text using Ollama API."""
        # Use OpenAI-compatible API
        client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama'  # Required but unused
        )
        
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        
        return response.choices[0].message.content.strip()
    
    def generate_streaming(self, prompt: str, system_prompt: str = None) -> str:
        """Generate text using Ollama streaming API (alternative method)."""
        payload = {
            'model': self.model,
            'prompt': prompt,
            'options': {
                'temperature': self.temperature,
            }
        }
        
        if system_prompt:
            payload['system'] = system_prompt
        
        r = requests.post(self.url, json=payload, stream=True)
        r.raise_for_status()
        
        response_parts = []
        for line in r.iter_lines():
            body = json.loads(line)
            response_part = body.get('response', '')
            
            if 'error' in body:
                raise Exception(body['error'])
            
            response_parts.append(response_part)
            
            if body.get('done', False):
                break
        
        return ''.join(response_parts).strip()
