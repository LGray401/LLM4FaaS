"""
Base provider interface for LLM generation.
"""
import re
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
        Extract code from LLM response flexibly.
        
        Args:
            response: Raw LLM response
            
        Returns:
            Extracted code with conversational text as comments
        """
        if response is None:
            return ""

        # Look for fenced code blocks (```python, ```js, or just ```)
        fence_pattern = re.compile(
            r"```[ \t]*([a-zA-Z0-9_+-]+)?[ \t]*\r?\n(.*?)(?:\r?\n)?```",
            re.DOTALL,
        )
        matches = list(fence_pattern.finditer(response))

        if matches:
            def score(match: re.Match) -> tuple[int, int]:
                lang = (match.group(1) or "").strip().lower()
                code = (match.group(2) or "").strip()
                lang_bonus = 1000 if lang in {"python", "py"} else 0
                return (lang_bonus, len(code))

            best = max(matches, key=score)
            code = (best.group(2) or "").strip()
            context = response[:best.start()].strip()

            if context:
                context_as_comment = "\n".join(f"# {line}" for line in context.split("\n"))
                return f"{context_as_comment}\n\n{code}"
            return code

        # If a fence was started but never closed, grab what's after it.
        fence_start = response.find("```")
        if fence_start != -1:
            remainder = response[fence_start + 3 :]
            remainder_lines = remainder.splitlines()
            if remainder_lines:
                first_line = remainder_lines[0].strip()
                if re.fullmatch(r"[a-zA-Z0-9_+-]+", first_line):
                    remainder_lines = remainder_lines[1:]
            remainder_text = "\n".join(remainder_lines).strip()
            if remainder_text:
                return remainder_text

        # Fallback: if it looks like code, return as-is.
        code_patterns = [
            r"^\s*(def|class|import|from|async\s+def|if\s+__name__)\b",
            r"^\s*(const|let|function|class)\b",
        ]
        if any(re.search(pattern, response, re.MULTILINE) for pattern in code_patterns):
            return response.strip()

        # If it doesn't look like code at all, comment everything
        return "\n".join(f"# {line}" for line in response.split("\n"))
