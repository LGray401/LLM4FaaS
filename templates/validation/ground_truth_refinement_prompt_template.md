# Ground Truth Refinement Task

You are refining previously generated Python code after a failed ground-truth runtime comparison.

## Goal
Produce a corrected implementation that satisfies the original requirement and aligns runtime behavior with the expected output.

## Inputs

### Original User Prompt
{requirement}

### Previous Code
```python
{previous_code}
```

### Expected Runtime Output (XML)
{expected}

### Actual Runtime Output (XML)
{actual}

### Mismatch Summary
{summary}

## How To Interpret Expected Output
Expected runtime output may look different from literal full actual lines. Treat the expected stdout as canonical matching targets, not always full verbatim lines.

Important interpretation rules:
1. A line containing `||` means valid alternatives. Matching any one alternative is acceptable for that step.
2. Many expected lines are intentionally partial canonical prefixes (for example IDs or stable action prefixes) to reduce brittleness.
3. Expected lines are checked by substring containment against corresponding actual lines, so actual lines can be longer.


## Required Repair Procedure
1. Preserve the original intent of the requirement.
2. Compare expected vs actual in this order:
	1. return_code
	2. stderr
	3. stdout
3. Identify the smallest code changes that remove the mismatch.
4. Keep all behavior that is already correct.

## Implementation Constraints
1. Output must be valid Python code only.
2. Return complete, runnable code (not a patch, not snippets).
3. Do not include markdown, explanations, comments to user, or code fences.
4. Keep changes minimal and targeted to mismatch causes.
5. Avoid introducing new dependencies unless absolutely required.
6. Preserve FaaS suitability:
	1. Keep a callable entrypoint compatible with the existing flow.
	2. Use deterministic logic for outputs that are evaluated by exact matching.
	3. Avoid unnecessary non-determinism (timestamps, random output, unordered prints).

## Success Criteria
The revised code should produce runtime output that matches expected output as closely as possible under the evaluator's matching logic.

Return only the corrected Python code.
