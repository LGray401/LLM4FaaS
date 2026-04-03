# Evaluation

Three independent analyses: functional correctness (test results), code quality (Pylint + Radon), and latency. Each can be run in isolation or together via the `evaluate` CLI command.

## Prerequisites

- **Python ≥ 3.10**
- **Dependencies**: `pip install -r requirements.txt`
- **Pylint and Radon** (required for `--code-quality`):
  ```bash
  pip install pylint radon
  ```
- **Execution logs** for functional evaluation: produced by `python main.py deploy --execute`  
  Default location: `data/logs/{experiment}/{task}/`
- **Standard logs** for comparison: `test/standard_log/{task}/{task}_{n}.log`  
  Already included in the repository.

## Usage

Run functional evaluation only:
```bash
python main.py evaluate \
  --task remote_control \
  --experiment default \
  --provider openai
```

Add code quality analysis (Pylint + Radon CC/MI/HAL on all generated `.py` files):
```bash
python main.py evaluate \
  --task remote_control \
  --experiment default \
  --provider openai \
  --code-quality
```

Override default input/output paths:
```bash
python main.py evaluate \
  --task remote_control \
  --experiment default \
  --provider openai \
  --logs-dir path/to/logs \            # actual execution logs
  --standard-logs-dir path/to/stdlib \ # expected outputs
  --source-dir path/to/functions \     # generated .py files (for --code-quality)
  --code-quality
```

Evaluation also runs automatically at the end of a full pipeline run when `--evaluate` is passed:
```bash
python main.py full --task remote_control --provider openai \
  --excel data/input/data.xlsx --column 6 \
  --tinyfaas-dir /path/to/tinyFaaS --execute --evaluate
```

### Flag reference

| Flag | Default | Description |
|---|---|---|
| `--task` | *(required)* | `remote_control`, `auto_adapt`, `plan`, `energy_control` |
| `--experiment` | `default` | Namespace for all output paths |
| `--provider` | — | Provider name used to resolve default function directory |
| `--logs-dir` | `data/logs/{experiment}/{task}/` | Directory with `.log` files from execution |
| `--standard-logs-dir` | `test/standard_log/` | Directory with expected output logs |
| `--source-dir` | `data/functions/{experiment}/{provider}_{task}/` | Generated `.py` files for code quality |
| `--code-quality` | off | Also run Pylint + Radon on source files |

## Output

### Functional results — `data/evaluation/{experiment}/{task}_results.csv`

One row per execution log. Columns:

| Column | Description |
|---|---|
| `Filename` | Log filename |
| `Task Name` | Task (e.g. `remote_control`) |
| `User Index` | Numeric index extracted from filename |
| `Success Rate` | Fraction of expected output lines matched (0.0–1.0) |
| `Status` | `No Error & Warning`, `Error`, `Warning Exists`, `Timeout`, `Invalid Prompt`, `Manual Check Required`, or `Standard log not found` |
| `Unmatched Lines` | Expected lines not found in actual output (empty when all matched or status is non-comparable) |

Standard log format expected by the evaluator:
```
Standard Output:
<line1>
<line2>
Standard Error:
<error lines>
Return code: 0
```

Lines in standard logs may contain `||` as an OR separator — any matching alternative counts as a match.

### Code quality reports — `data/evaluation/{experiment}/code_quality/{task}/`

Four files written per source `.py` file:

| File suffix | Tool | Content |
|---|---|---|
| `_pylint.txt` | Pylint | Score, convention/warning/error counts, per-issue messages |
| `_radon_cc.txt` | `radon cc -a` | Per-function cyclomatic complexity + average |
| `_radon_mi.txt` | `radon mi` | Maintainability index grade per file |
| `_radon_hal.txt` | `radon hal` | Halstead metrics including effort, volume, and difficulty |

### Latency data — `data/evaluation/{experiment}/{task}_latency.csv`

Written automatically at the end of a `full` pipeline run (not by `evaluate` alone). One row per generated function. Columns:

| Column | Description |
|---|---|
| `filename` | Generated source filename |
| `user_index` | Numeric user index |
| `provider` | LLM provider |
| `model` | Model name |
| `task` | Task name |
| `generate_s` | Wall-clock seconds for LLM generation (includes validation/refinement loop) |
| `prepare_s` | Wall-clock seconds for function directory preparation |
| `upload_s` | Wall-clock seconds for tinyFaaS upload |
| `execute_s` | Wall-clock seconds for tinyFaaS HTTP execution |

All latency values are wall-clock and include any internal waits (rate-limit delays, deployment readiness sleep). Empty cells indicate a stage was not reached (e.g. `upload_s`/`execute_s` are empty when tinyFaaS was not used).
