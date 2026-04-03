"""
Refinement loop for iterative code improvement with validation.
"""
import logging
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime

from .validation_result import ValidationResult
from .llm_judge import LLMJudge
from .config import VALIDATION_MAX_ITERATIONS

logger = logging.getLogger(__name__)


class RefinementIteration:
    """Track details of a single refinement iteration."""
    
    def __init__(
        self,
        iteration: int,
        code: str,
        validation_result: ValidationResult,
        iteration_evaluation: Optional[Dict[str, Any]] = None,
    ):
        self.iteration = iteration
        self.code = code
        self.validation_result = validation_result
        self.iteration_evaluation = iteration_evaluation
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            'iteration': self.iteration,
            'code': self.code,
            'validation_result': self.validation_result.to_dict(),
            'iteration_evaluation': self.iteration_evaluation,
            'timestamp': self.timestamp
        }


class RefinementLoop:
    """Manage iterative refinement of generated code with validation."""
    
    def __init__(self, judge: LLMJudge, generator, max_iterations: int = None):
        """
        Initialize refinement loop.
        
        Args:
            judge: LLMJudge instance for validation
            generator: LLMGenerator instance for code generation
            max_iterations: Maximum refinement attempts (uses config default if None)
        """
        self.judge = judge
        self.generator = generator
        self.max_iterations = max_iterations or VALIDATION_MAX_ITERATIONS
        self.history: List[RefinementIteration] = []
    
    def refine_until_valid(self, requirement: str, initial_code: str,
                          system_prompt: str = None,
                          smart_home_docs: str = "",
                          iteration_evaluator: Any = None,
                          evaluation_context: Optional[Dict[str, Any]] = None) -> Tuple[str, ValidationResult, List[RefinementIteration]]:
        """
        Iteratively refine code until validation passes or max iterations reached.
        
        Args:
            requirement: Original user requirement
            initial_code: Initially generated code
            system_prompt: System prompt for generator (for refinement)
            smart_home_docs: Smart home API documentation
            
        Returns:
            Tuple of (best_code, final_validation_result, iteration_history)
        """
        self.history = []
        current_code = initial_code
        
        logger.info(f"Starting refinement loop (max {self.max_iterations} iterations)")
        
        evaluation_context = evaluation_context or {}

        for iteration in range(1, self.max_iterations + 1):
            logger.info(f"Iteration {iteration}/{self.max_iterations}")
            
            # Validate current code
            validation_result = self.judge.validate(requirement, current_code, smart_home_docs)

            # Execute/evaluate current iteration against standard log if enabled
            iteration_evaluation = None
            if iteration_evaluator is not None:
                try:
                    iteration_evaluation = iteration_evaluator.evaluate_iteration(
                        code=current_code,
                        task_name=evaluation_context.get('task_name'),
                        sample_index=evaluation_context.get('sample_index'),
                        iteration=iteration,
                    )
                except Exception as exc:
                    iteration_evaluation = {
                        'iteration': iteration,
                        'task': evaluation_context.get('task_name'),
                        'sample_index': evaluation_context.get('sample_index'),
                        'status': 'Evaluation Error',
                        'match_percentage': None,
                        'unmatched_lines': None,
                        'error': str(exc),
                    }
            
            # Store iteration
            self.history.append(
                RefinementIteration(
                    iteration,
                    current_code,
                    validation_result,
                    iteration_evaluation=iteration_evaluation,
                )
            )
            
            logger.info(f"Validation result: valid={validation_result.is_valid}, "
                       f"issues={len(validation_result.issues)}")
            
            # Check if valid
            if validation_result.is_valid:
                logger.info(f"Code validated successfully at iteration {iteration}")
                return current_code, validation_result, self.history
            
            # Check if final iteration
            if iteration >= self.max_iterations:
                logger.warning(f"Max iterations ({self.max_iterations}) reached without validation success")
                break
            
            # Generate refinement prompt
            refinement_prompt = self.judge.create_refinement_prompt(
                requirement, current_code, validation_result
            )
            
            # Regenerate code
            logger.info(f"Regenerating code with validation feedback...")
            try:
                # Use generator to produce improved code
                refined_code = self.generator.generate_from_prompt(refinement_prompt, system_prompt)
                
                if not refined_code or refined_code.strip() == "":
                    logger.error(f"Regeneration produced empty code at iteration {iteration}")
                    break
                
                current_code = refined_code
                
            except Exception as e:
                logger.error(f"Regeneration failed at iteration {iteration}: {e}")
                break
        
        # Max iterations exhausted - select best candidate
        best_code, best_result = self._select_best_candidate()
        
        return best_code, best_result, self.history
    
    def _select_best_candidate(self) -> Tuple[str, ValidationResult]:
        """
        Select the best code version when max iterations exhausted.
        
        Selection criteria:
        1. Prefer any valid code
        2. Otherwise, select highest confidence score
        3. Fall back to first generation if no clear winner
        
        Returns:
            Tuple of (best_code, best_validation_result)
        """
        if not self.history:
            raise ValueError("Cannot select best candidate from empty history")
        
        # Check for any valid results
        valid_iterations = [it for it in self.history if it.validation_result.is_valid]
        if valid_iterations:
            # Return last valid iteration
            best = valid_iterations[-1]
            logger.info(f"Selected valid code from iteration {best.iteration}")
            return best.code, best.validation_result
        
        # No valid results - select by confidence score
        iterations_with_confidence = [
            it for it in self.history 
            if it.validation_result.confidence is not None
        ]
        
        if iterations_with_confidence:
            best = max(iterations_with_confidence, 
                      key=lambda it: it.validation_result.confidence)
            logger.info(f"Selected code from iteration {best.iteration} "
                       f"(highest confidence: {best.validation_result.confidence})")
            return best.code, best.validation_result
        
        # Check for fewest issues
        best = min(self.history, key=lambda it: len(it.validation_result.issues))
        logger.info(f"Selected code from iteration {best.iteration} "
                   f"(fewest issues: {len(best.validation_result.issues)})")
        return best.code, best.validation_result
    
    def get_history_summary(self) -> str:
        """Get human-readable summary of refinement history."""
        if not self.history:
            return "No refinement iterations performed"
        
        summary = f"Refinement History ({len(self.history)} iterations):\n"
        for it in self.history:
            status = "✓ VALID" if it.validation_result.is_valid else "✗ INVALID"
            summary += f"  Iteration {it.iteration}: {status}"
            if not it.validation_result.is_valid:
                summary += f" ({len(it.validation_result.issues)} issues)"
            summary += "\n"
        
        return summary
    
    def save_history(self, output_path: Path) -> None:
        """
        Save refinement history to JSON file.
        
        Args:
            output_path: Path to save JSON file
        """
        history_data = {
            'max_iterations': self.max_iterations,
            'total_iterations': len(self.history),
            'final_valid': self.history[-1].validation_result.is_valid if self.history else False,
            'iterations': [it.to_dict() for it in self.history]
        }
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(history_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved refinement history to {output_path}")
    
    @staticmethod
    def load_history(input_path: Path) -> Dict[str, Any]:
        """
        Load refinement history from JSON file.
        
        Args:
            input_path: Path to JSON file
            
        Returns:
            Dictionary containing history data
        """
        with open(input_path, 'r', encoding='utf-8') as f:
            return json.load(f)
