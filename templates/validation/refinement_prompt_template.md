# Code Refinement Request

The previously generated code has validation issues and needs to be revised. Please generate an improved version that addresses the feedback below.

---

## Original User Requirement

{requirement}

---

## Previous Generated Code

```python
{previous_code}
```

---

## Validation Feedback

### Issues Identified:
{issues}

### Improvement Suggestions:
{suggestions}

---

## Instructions

Please generate a **revised and improved version** of the code that:

1. **Addresses all identified issues** from the validation feedback
2. **Implements the suggestions** provided above
3. **Maintains the original requirement** - don't change what the user asked for
4. **Uses the smart home API correctly** - proper imports, sensor activation, actuator control
5. **Is complete and production-ready** - proper function signature, error handling, logging

Return only the complete, corrected Python code. Make sure to:
- Import all necessary modules (sensor, actuator, config, home_plan, logger_config)
- Turn on sensors before reading values
- Use correct sensor/actuator types for the rooms mentioned
- Implement the logic exactly as required
- Include the proper `def fn(data, headers):` function signature for FaaS deployment

Focus on fixing the semantic issues while keeping the code structure clean and maintainable.
