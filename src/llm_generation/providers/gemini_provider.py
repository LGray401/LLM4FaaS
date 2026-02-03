"""
Google Gemini provider implementation.
"""
import google.generativeai as genai
from .base import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):
    """Google Gemini API provider."""
    
    def __init__(self, api_key: str, model: str = 'models/gemini-1.5-flash',
                 temperature: float = 0.7, max_tokens: int = 1500):
        """
        Initialize Gemini provider.
        
        Args:
            api_key: Google API key
            model: Gemini model name
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
        """
        super().__init__(model, temperature, max_tokens)
        genai.configure(api_key=api_key)
        self.client = genai.GenerativeModel(model)
    
    def generate(self, prompt: str, system_prompt: str = None) -> str:
        """Generate text using Gemini API."""
        # Gemini doesn't have separate system prompt, prepend to user prompt
        full_prompt = prompt
        if system_prompt:
            full_prompt = f"{system_prompt}\n\n{prompt}"
        
        response = self.client.generate_content(
            full_prompt,
            generation_config=genai.GenerationConfig(
                temperature=self.temperature,
                max_output_tokens=self.max_tokens
            )
        )
        
        return response.text.strip()
