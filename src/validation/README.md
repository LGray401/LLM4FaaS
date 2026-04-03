# LLM-as-a-Judge Validation

This module implements self-validation for generated FaaS functions using an LLM judge to detect semantic errors before deployment.

## Overview

The validation system adds an optional quality gate between code generation and deployment:

1. **Generate** code with primary LLM
2. **Validate** with judge LLM (checks correctness, API usage, logic)
3. **Refine** if invalid (up to max iterations)
4. **Deploy** best validated version

## Quick Start

### Basic Usage

```bash
# Enable validation with default settings (same provider/model as generator)
python main.py generate --task remote_control --provider openai \
    --validate-judge

# Use different judge model for cost efficiency
python main.py generate --task remote_control --provider openai --model gpt-4o \
    --validate-judge --judge-model gpt-4o-mini

# Full pipeline with validation
python main.py full --task remote_control --provider openai \
    --excel data/input/data.xlsx --column 6 \
    --validate-judge --max-iterations 3 \
    --tinyfaas-dir /path/to/tinyFaaS --execute --evaluate
```

### CLI Flags

- `--validate-judge`: Enable LLM-as-a-Judge validation
- `--judge-provider`: Provider for judge (openai, ollama, gemini)
- `--judge-model`: Model name for judge
- `--max-iterations`: Maximum refinement attempts (default: 3)

## Configuration

Add to `.env`:

```bash
# Judge Configuration (optional - defaults to generation settings)
JUDGE_PROVIDER=openai
JUDGE_MODEL=gpt-4o-mini
JUDGE_TEMPERATURE=0.3
JUDGE_MAX_TOKENS=2000

# Validation Behavior
VALIDATION_MAX_ITERATIONS=3
VALIDATION_TIMEOUT=60
VALIDATION_USE_JSON=true
```

## How It Works

### 1. Initial Generation

Standard LLM generates code from user requirement:

```python
generator = LLMGenerator('openai', 'gpt-4o')
code = generator.generate_from_file('prompt.md')
```

### 2. Validation

Judge evaluates code against requirement:

```python
judge = LLMJudge('openai', 'gpt-4o-mini')
result = judge.validate(requirement, code)

# result.is_valid: bool
# result.issues: List[str]
# result.suggestions: List[str]
# result.confidence: float
```

### 3. Refinement (if needed)

If validation fails, regenerate with feedback:

```python
refinement_loop = RefinementLoop(judge, generator, max_iterations=3)
best_code, final_result, history = refinement_loop.refine_until_valid(
    requirement, code
)
```

### 4. Best Candidate Selection

If max iterations exhausted without validation:
- Return any valid version if found
- Otherwise, select version with highest confidence
- Fall back to version with fewest issues

## Output Files

### Generated Code

Filenames include validation metadata:

```
openai_gpt-4o_sample001_validated_iter2_1707667200000.py
openai_gpt-4o_sample002_unvalidated_iter3_1707667210000.py
```

### Validation Logs

Stored in `data/validation/{experiment}/{task}/`:

```json
{
  "max_iterations": 3,
  "total_iterations": 2,
  "final_valid": true,
  "iterations": [
    {
      "iteration": 1,
      "code": "...",
      "validation_result": {
        "is_valid": false,
        "issues": ["Sensor not turned on before reading"],
        "suggestions": ["Add sensor.turn_on() before get_reading()"],
        "confidence": 0.9
      }
    },
    {
      "iteration": 2,
      "code": "...",
      "validation_result": {
        "is_valid": true,
        "issues": [],
        "suggestions": []
      }
    }
  ]
}
```

## Architecture

### Module Structure

```
src/validation/
├── __init__.py
├── config.py                 # Configuration settings
├── validation_result.py      # ValidationResult dataclass
├── llm_judge.py             # LLMJudge implementation
└── refinement_loop.py       # Iterative refinement logic

templates/validation/
├── judge_system_prompt.md           # Judge instructions
└── refinement_prompt_template.md   # Refinement template

data/validation/
└── {experiment}/
    └── {task}/
        └── sample001_validation_*.json
```

### Validation Criteria

The judge evaluates code based on:

1. **Correctness**: Implements all requirements
2. **API Usage**: Proper sensor/actuator initialization and methods
3. **Logic**: Sound control flow and conditions
4. **Completeness**: Production-ready (function signature, error handling)

### Response Format

Judge returns structured JSON:

```json
{
  "is_valid": true/false,
  "issues": ["specific problem 1", "specific problem 2"],
  "suggestions": ["fix 1", "fix 2"],
  "confidence": 0.9
}
```

Fallback text parsing handles non-JSON responses.

## Cost Optimization

### Use Cheaper Judge Models

```bash
# GPT-4o generates, GPT-4o-mini validates (50% cost reduction on validation)
python main.py generate --provider openai --model gpt-4o \
    --validate-judge --judge-model gpt-4o-mini
```

### Limit Iterations

```bash
# Only 1 refinement attempt
python main.py generate --provider openai --validate-judge --max-iterations 1
```

### Selective Validation

Validate subset for budget testing:

```bash
# Validate first 10 samples manually
python main.py generate --provider openai --prompt-dir data/prompts/test/ \
    --validate-judge
```

## Error Handling

### Graceful Degradation

If judge API fails:
- Logs error
- Returns unvalidated code
- Pipeline continues (validation is optional)

### Timeout Protection

Validation times out after 60s (configurable):

```bash
VALIDATION_TIMEOUT=60  # seconds
```

### Malformed Responses

Parser handles both JSON and free-text judge responses with fallback heuristics.

## Integration with Existing Pipeline

Validation is **opt-in** and backward compatible:

- Without `--validate-judge`: Works exactly as before
- With `--validate-judge`: Adds validation layer

No changes to:
- Prompt extraction
- FaaS deployment
- Evaluation metrics

## Example Workflow

### Cost-Efficient Validation

```bash
# 1. Generate with validation
python main.py generate \
    --task remote_control \
    --provider openai --model gpt-4o \
    --validate-judge --judge-provider openai --judge-model gpt-4o-mini \
    --max-iterations 3 \
    --experiment validation_test

# 2. Deploy validated functions
python main.py deploy \
    --task remote_control \
    --provider openai \
    --experiment validation_test \
    --tinyfaas-dir ~/tinyFaaS \
    --execute

# 3. Evaluate results
python main.py evaluate \
    --task remote_control \
    --provider openai \
    --experiment validation_test \
    --code-quality
```

### Local Generation + Commercial Validation

```bash
# Use free Ollama for generation, paid OpenAI for validation
python main.py generate \
    --task remote_control \
    --provider ollama --model deepseek-r1:7b \
    --validate-judge --judge-provider openai --judge-model gpt-4o-mini
```

## Evaluation Metrics

Compare validation effectiveness:

### A/B Testing

```bash
# Control (no validation)
python main.py full --task remote_control --provider openai --experiment control

# Treatment (with validation)
python main.py full --task remote_control --provider openai --experiment treatment \
    --validate-judge --max-iterations 3
```

### Validation Logs Analysis

Parse `data/validation/{experiment}/` logs to compute:

- **Precision**: % of judge rejections that were actually wrong
- **Recall**: % of wrong code caught by judge
- **Refinement success rate**: % improved after refinement
- **Iteration distribution**: Average iterations to validation

## Troubleshooting

### Judge Always Rejects Valid Code (False Positives)

- Lower judge temperature: `JUDGE_TEMPERATURE=0.2`
- Try different judge model
- Review judge system prompt for bias

### Judge Never Rejects Invalid Code (False Negatives)

- Use stronger judge model (e.g., GPT-4o instead of GPT-4o-mini)
- Increase confidence threshold in prompt
- Add more specific validation criteria

### Refinement Doesn't Improve Code

- Check refinement prompt clarity
- Ensure generator understands feedback format
- Try different generator model
- Limit iterations to avoid degradation

### High API Costs

- Use cheaper judge model
- Reduce max iterations
- Validate only samples, not full dataset
- Cache validation results (manual implementation needed)

## Future Enhancements

Potential improvements not in MVP:

- **Caching**: Avoid re-validating identical code
- **Parallel validation**: Batch multiple validations
- **Multi-judge consensus**: Use multiple judges, take majority vote
- **Confidence thresholding**: Auto-accept high-confidence validations
- **Custom validation rules**: Task-specific validation criteria
- **Validation metrics dashboard**: Real-time validation statistics

## References

- Requirements: `notes/requirements_llm_as_judge.md`
- Templates: `templates/validation/`
- Module: `src/validation/`
- Main CLI: `main.py`
