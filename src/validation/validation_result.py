"""
ValidationResult dataclass for structured validation feedback.
"""
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any
from datetime import datetime


@dataclass
class ValidationResult:
    """Structured validation feedback from LLM judge."""
    
    # Core validation decision
    is_valid: bool
    
    # Identified issues (empty list if valid)
    issues: List[str] = field(default_factory=list)
    
    # Specific improvement suggestions
    suggestions: List[str] = field(default_factory=list)
    
    # Judge's raw response for debugging
    raw_response: str = ""
    
    # Confidence score (0-1) if provided by judge
    confidence: Optional[float] = None
    
    # Judge metadata
    judge_provider: str = ""
    judge_model: str = ""
    
    # Timestamp
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)
    
    def has_critical_issues(self) -> bool:
        """Check if validation result contains critical issues."""
        if not self.issues:
            return False
        
        # Check for keywords indicating critical problems
        critical_keywords = ['missing', 'incorrect', 'wrong', 'error', 'fails', 'does not']
        return any(
            any(keyword in issue.lower() for keyword in critical_keywords)
            for issue in self.issues
        )
    
    def get_summary(self) -> str:
        """Get a human-readable summary of validation result."""
        if self.is_valid:
            return "✓ Code is valid and meets requirements"
        
        summary = f"✗ Code has {len(self.issues)} issue(s):\n"
        for i, issue in enumerate(self.issues, 1):
            summary += f"  {i}. {issue}\n"
        
        if self.suggestions:
            summary += f"\nSuggestions ({len(self.suggestions)}):\n"
            for i, suggestion in enumerate(self.suggestions, 1):
                summary += f"  {i}. {suggestion}\n"
        
        return summary
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ValidationResult':
        """Create ValidationResult from dictionary."""
        return cls(**data)
