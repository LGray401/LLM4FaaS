"""
OpenAI provider implementation.
"""
import openai
from .base import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):
    """OpenAI API provider."""
    
    def __init__(self, api_key: str, model: str = 'gpt-4o', 
                 temperature: float = 0.7, max_tokens: int = 1500):
        """
        Initialize OpenAI provider.
        
        Args:
            api_key: OpenAI API key
            model: Model name (gpt-4o, gpt-4o-mini, etc.)
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
        """
        super().__init__(model, temperature, max_tokens)
        openai.api_key = api_key
        if not getattr(openai, "api_type", None):
            openai.api_type = "openai"
    
    def generate(self, prompt: str, system_prompt: str = None) -> str:
        """Generate text using OpenAI API."""
        if system_prompt is None:
            system_prompt = "You are a helpful assistant."
        
        response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        
        return response.choices[0].message.content.strip()
