# Ground Truth Code Refinement Request

The previous generated code did not match ground-truth runtime expectations. Please revise it using the mismatch details below.

---

## Original User Requirement

{requirement}

---

## Previous Generated Code

```python
{previous_code}
```

---

## Ground Truth Comparison

### Expected Output (XML)
{expected}

### Actual Output (XML)
{actual}

### Mismatch Summary
- {summary}

---

## Instructions

Generate a corrected Python implementation that:

1. Satisfies the original requirement.
2. Produces runtime behavior that matches the expected output.
3. Preserves valid existing behavior and only fixes mismatches.
4. Returns complete code suitable for FaaS deployment.

Return only the corrected Python code.
