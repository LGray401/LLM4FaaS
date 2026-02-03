"""
Base provider interface for LLM generation.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseLLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    def __init__(self, model: str, temperature: float = 0.7, max_tokens: int = 1500):
        """
        Initialize the provider.
        
        Args:
            model: Model identifier
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
        """
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
    
    @abstractmethod
    def generate(self, prompt: str, system_prompt: str = None) -> str:
        """
        Generate text from a prompt.
        
        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            
        Returns:
            Generated text
        """
        pass
    
    def extract_code(self, response: str) -> str:
        """
        Extract Python code from LLM response.
        
        Args:
            response: Raw LLM response
            
        Returns:
            Extracted Python code with comments
        """
        start_index = response.find('```python')
        end_index = response.find('```', start_index + len('```python')) if start_index != -1 else -1
        
        if start_index != -1 and end_index != -1:
            # Extract context before code block as comments
            context = response[:start_index].strip()
            code = response[start_index + len('```python'):end_index].strip()
            
            if context:
                context_as_comment = '\n'.join(f"# {line}" for line in context.split('\n'))
                full_code = f"{context_as_comment}\n\n{code}"
            else:
                full_code = code
        else:
            # No code block found, comment everything
            full_code = '\n'.join(f"# {line}" for line in response.split('\n'))
        
        return full_code
