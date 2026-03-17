"""
OpenAI provider implementation.
"""
import openai
from .base import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):
    """OpenAI API provider."""

    _THINKING_MODEL_PREFIXES = (
        "o1",
        "o3",
        "o4",
        "gpt-5",
        "gpt-5.2",
        "gpt-5.3",
        "gpt-5.4",
    )
    
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

        request_kwargs = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": self.temperature,
            # Newer OpenAI models (for example gpt-5.x) require this field.
            "max_completion_tokens": self.max_tokens,
        }

        # Disable chain-of-thought style reasoning by default on thinking models
        # to reduce latency and token usage.
        if self._is_thinking_model(self.model):
            request_kwargs["reasoning_effort"] = "none"

        try:
            response = openai.chat.completions.create(**request_kwargs)
        except openai.BadRequestError as exc:
            # Keep backward compatibility with models that still expect max_tokens.
            error_text = str(exc)
            has_fallback = False

            if "Unsupported parameter: 'max_completion_tokens'" in error_text:
                request_kwargs.pop("max_completion_tokens", None)
                request_kwargs["max_tokens"] = self.max_tokens
                has_fallback = True

            if "Unsupported parameter: 'reasoning_effort'" in error_text:
                request_kwargs.pop("reasoning_effort", None)
                has_fallback = True

            if not has_fallback:
                raise

            response = openai.chat.completions.create(**request_kwargs)
        
        return response.choices[0].message.content.strip()

    def _is_thinking_model(self, model_name: str) -> bool:
        """Return True for OpenAI models that support thinking/reasoning controls."""
        lowered = model_name.lower()
        return lowered.startswith(self._THINKING_MODEL_PREFIXES)
