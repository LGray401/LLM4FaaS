"""
LLM Judge for validating generated code against requirements.
"""
import json
import re
import logging
from pathlib import Path
from typing import Optional, Tuple

from .validation_result import ValidationResult
from .config import JUDGE_TEMPERATURE, JUDGE_MAX_TOKENS, VALIDATION_USE_JSON, VALIDATION_TIMEOUT
from ..llm_generation.providers import OpenAIProvider, OllamaProvider
from ..llm_generation.config import (
    OPENAI_API_KEY, OPENAI_MODEL,
    OLLAMA_MODEL, OLLAMA_URL,
    GEMINI_API_KEY, GEMINI_MODEL
)

logger = logging.getLogger(__name__)


class LLMJudge:
    """LLM-based judge for code validation."""
    
    SUPPORTED_PROVIDERS = ['openai', 'ollama', 'gemini']
    
    def __init__(self, provider: str, model: str = None, 
                 temperature: float = None, max_tokens: int = None,
                 api_key: str = None):
        """
        Initialize the judge with specified provider.
        
        Args:
            provider: Provider name (openai, ollama, gemini)
            model: Model name (uses default from config if None)
            temperature: Sampling temperature (uses default if None)
            max_tokens: Maximum tokens (uses default if None)
            api_key: API key (uses environment variable if None)
        """
        if provider not in self.SUPPORTED_PROVIDERS:
            raise ValueError(f"Judge provider must be one of {self.SUPPORTED_PROVIDERS}")
        
        self.provider_name = provider
        self.temperature = temperature if temperature is not None else JUDGE_TEMPERATURE
        self.max_tokens = max_tokens or JUDGE_MAX_TOKENS
        
        # Initialize provider
        if provider == 'openai':
            model = model or OPENAI_MODEL
            api_key = api_key or OPENAI_API_KEY
            self.provider = OpenAIProvider(api_key, model, self.temperature, self.max_tokens)
            self.model_name = model
        elif provider == 'ollama':
            model = model or OLLAMA_MODEL
            self.provider = OllamaProvider(model, self.temperature, self.max_tokens, OLLAMA_URL)
            self.model_name = model
        elif provider == 'gemini':
            from ..llm_generation.providers.gemini_provider import GeminiProvider
            model = model or GEMINI_MODEL
            api_key = api_key or GEMINI_API_KEY
            self.provider = GeminiProvider(api_key, model, self.temperature, self.max_tokens)
            self.model_name = model
        
        # Load validation prompt templates
        self._load_templates()
    
    def _load_templates(self):
        """Load judge and refinement prompt templates."""
        templates_dir = Path(__file__).parent.parent.parent / 'templates' / 'validation'
        
#        judge_prompt_path = templates_dir / 'judge_system_prompt.md'
        judge_prompt_path = templates_dir / 'judge_system_prompt.md'

        refinement_prompt_path = templates_dir / 'refinement_prompt_template.md'
        
        if judge_prompt_path.exists():
            with open(judge_prompt_path, 'r', encoding='utf-8') as f:
                self.judge_system_prompt = f.read()
        else:
            logger.warning(f"Judge system prompt not found at {judge_prompt_path}, using default")
            self.judge_system_prompt = self._get_default_judge_prompt()
        
        if refinement_prompt_path.exists():
            with open(refinement_prompt_path, 'r', encoding='utf-8') as f:
                self.refinement_template = f.read()
        else:
            logger.warning(f"Refinement template not found at {refinement_prompt_path}, using default")
            self.refinement_template = self._get_default_refinement_template()
    
    def _get_default_judge_prompt(self) -> str:
        """Get default judge system prompt if template not found."""
        return """You are a code validation expert. Your task is to evaluate whether generated Python code correctly implements the given requirements for a smart home FaaS function.

Evaluate the code based on:
1. Correctness: Does it implement all required functionality?
2. API Usage: Does it use the smart home API correctly?
3. Logic: Is the logic sound and will it work as intended?
4. Completeness: Are all requirements addressed?

Respond in JSON format:
{
    "is_valid": true/false,
    "issues": ["list of specific problems if invalid"],
    "suggestions": ["specific improvement recommendations"],
    "confidence": 0.0-1.0
}

Be conservative: only mark as valid if you're confident it will work correctly."""
    
    def _get_default_refinement_template(self) -> str:
        """Get default refinement template if not found."""
        return """The previous generated code has validation issues. Please revise it based on the feedback below.

ORIGINAL REQUIREMENT:
{requirement}

PREVIOUS CODE:
```python
{previous_code}
```

VALIDATION FEEDBACK:
Issues identified:
{issues}

Suggestions:
{suggestions}

Please generate an improved version that addresses these issues."""
    
    def validate(self, requirement: str, generated_code: str, 
                 smart_home_docs: str = "") -> ValidationResult:
        """
        Validate generated code against requirements.
        
        Args:
            requirement: Original user requirement
            generated_code: Generated Python code to validate
            smart_home_docs: Optional smart home API documentation
            
        Returns:
            ValidationResult with structured feedback
        """
        # Build validation prompt
        validation_prompt = self._build_validation_prompt(
            requirement, generated_code, smart_home_docs
        )
        
        try:
            # Get judge response
            response = self.provider.generate(validation_prompt, self.judge_system_prompt)
            
            # Parse validation result
            result = self._parse_validation_response(response)
            result.judge_provider = self.provider_name
            result.judge_model = self.model_name
            result.raw_response = response
            
            return result
        
        except Exception as e:
            logger.error(f"Validation failed: {e}")
            # Return default invalid result on error
            return ValidationResult(
                is_valid=False,
                issues=[f"Validation error: {str(e)}"],
                suggestions=["Manual review recommended"],
                raw_response=str(e),
                judge_provider=self.provider_name,
                judge_model=self.model_name
            )
    
    def _build_validation_prompt(self, requirement: str, code: str, 
                                  docs: str = "") -> str:
        """Build the validation prompt for the judge."""
        prompt = f"""Please validate the following generated code against the user requirement.

USER REQUIREMENT:
{requirement}

GENERATED CODE:
```python
{code}
```
"""
        
        if docs:
            prompt += f"""
SMART HOME API DOCUMENTATION:
{docs}
"""
        
        if VALIDATION_USE_JSON:
            prompt += """
Please respond with a JSON object containing:
- is_valid (boolean): whether the code meets requirements
- issues (array): list of specific problems if invalid
- suggestions (array): specific improvement recommendations
- confidence (number 0-1): your confidence in this assessment
"""
        else:
            prompt += """
Please provide your assessment in this format:
Valid: YES/NO
Issues:
- [list each issue on a new line]
Suggestions:
- [list each suggestion on a new line]
Confidence: [0.0-1.0]
"""
        
        return prompt
    
    def _parse_validation_response(self, response: str) -> ValidationResult:
        """Parse judge response into ValidationResult."""
        # Try JSON parsing first
        json_match = re.search(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', response, re.DOTALL)
        if json_match:
            try:
                data = json.loads(json_match.group(0))
                return ValidationResult(
                    is_valid=data.get('is_valid', False),
                    issues=data.get('issues', []),
                    suggestions=data.get('suggestions', []),
                    confidence=data.get('confidence')
                )
            except json.JSONDecodeError:
                pass
        
        # Fallback to text parsing
        return self._parse_text_response(response)
    
    def _parse_text_response(self, response: str) -> ValidationResult:
        """Parse free-text validation response."""
        response_lower = response.lower()
        
        # Determine validity
        is_valid = False
        if 'valid: yes' in response_lower or 'is_valid: true' in response_lower:
            is_valid = True
        elif 'valid: no' in response_lower or 'is_valid: false' in response_lower:
            is_valid = False
        else:
            # Heuristic: if response mentions problems/issues/errors, likely invalid
            problem_keywords = ['issue', 'problem', 'error', 'incorrect', 'missing', 'wrong']
            is_valid = not any(keyword in response_lower for keyword in problem_keywords)
        
        # Extract issues
        issues = []
        issues_section = re.search(r'issues?:\s*(.*?)(?:suggestions?:|confidence:|$)', 
                                   response, re.IGNORECASE | re.DOTALL)
        if issues_section:
            issues_text = issues_section.group(1).strip()
            issues = [line.strip('- ').strip() for line in issues_text.split('\n') 
                     if line.strip() and line.strip() not in ['none', 'n/a', '[]']]
        
        # Extract suggestions
        suggestions = []
        suggestions_section = re.search(r'suggestions?:\s*(.*?)(?:confidence:|$)', 
                                       response, re.IGNORECASE | re.DOTALL)
        if suggestions_section:
            suggestions_text = suggestions_section.group(1).strip()
            suggestions = [line.strip('- ').strip() for line in suggestions_text.split('\n') 
                          if line.strip() and line.strip() not in ['none', 'n/a', '[]']]
        
        # Extract confidence
        confidence = None
        confidence_match = re.search(r'confidence:\s*([0-9.]+)', response, re.IGNORECASE)
        if confidence_match:
            try:
                confidence = float(confidence_match.group(1))
            except ValueError:
                pass
        
        return ValidationResult(
            is_valid=is_valid,
            issues=issues,
            suggestions=suggestions,
            confidence=confidence
        )
    
    def create_refinement_prompt(self, requirement: str, previous_code: str, 
                                 validation_result: ValidationResult) -> str:
        """
        Create a refinement prompt for regeneration based on validation feedback.
        
        Args:
            requirement: Original user requirement
            previous_code: Previously generated code that failed validation
            validation_result: Validation feedback from judge
            
        Returns:
            Refinement prompt for regeneration
        """
        issues_text = "\n".join(f"- {issue}" for issue in validation_result.issues)
        suggestions_text = "\n".join(f"- {suggestion}" for suggestion in validation_result.suggestions)
        
        return self.refinement_template.format(
            requirement=requirement,
            previous_code=previous_code,
            issues=issues_text or "No specific issues identified",
            suggestions=suggestions_text or "No specific suggestions provided"
        )
