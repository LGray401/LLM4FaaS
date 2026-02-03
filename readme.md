# LLM4FaaS: No-Code Application Development using LLMs and FaaS

LLM4FaaS is a No-Code application development framework that combines Large Language Models (LLMs) with Function-as-a-Service (FaaS) platforms, enabling non-technical users to build and run customized applications using only natural language.

By leveraging FaaS, LLM4FaaS abstracts infrastructure and deployment complexity while constraining LLM generation to core business logic, avoids boilerplate generation and improves reliability.

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/your-repo/LLM4FaaS.git
cd LLM4FaaS

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys
```

### Basic Usage

LLM4FaaS provides a unified CLI for the complete pipeline:

```bash
# Extract prompts from Excel data
python main.py extract --task remote_control --excel data/input/data.xlsx --column 6

# Generate code using OpenAI
python main.py generate --task remote_control --provider openai --model gpt-4o

# Deploy to tinyFaaS
python main.py deploy --task remote_control --provider openai --tinyfaas-dir /path/to/tinyFaaS

# Evaluate results
python main.py evaluate --task remote_control --provider openai

# Or run the full pipeline
python main.py full --task remote_control --provider openai --excel data/input/data.xlsx --column 6
```

## Project Structure

```
LLM4FaaS/
├── main.py                 # Unified CLI entry point
├── src/                    # Source code
│   ├── prompt_extraction/  # Extract prompts from Excel
│   ├── llm_generation/     # Provider-agnostic LLM generation
│   ├── faas_deployment/    # Function preparation and deployment
│   ├── evaluation/         # Testing and code quality analysis
│   └── utils/             # Utility functions
├── templates/              # Prompt templates and runtime code
│   ├── python/            # Python prompt templates
│   ├── javascript/        # JavaScript prompt templates
│   ├── baseline/          # Baseline templates
│   └── smart_home/        # Smart home runtime code
├── data/                   # All data files
│   ├── input/             # Excel data and standard logs
│   ├── prompts/           # Generated prompts
│   ├── functions/         # Generated function code
│   ├── logs/              # Execution logs
│   └── evaluation/        # Evaluation results
├── archive/                # Legacy experiment directories
└── test/                  # Test utilities

```

## Introduction

LLM4FaaS uses [tinyFaaS](https://github.com/OpenFogStack/tinyFaas) as the FaaS backend and supports multiple LLM providers including OpenAI (GPT-4o), Ollama (local models), and Google Gemini.


## Research
We introduced the LLM4FaaS concept and use it as a base platform to explore the factors influencing LLM suitability for no-code development in the following publications.

To use LLM4FaaS or our follow-up studies, please cite them as:

### Text
Wang, M., Pfandzelter, T., Schirmer, T., & Bermbach, D. (2025). LLM4FaaS: No-Code Application Development using LLMs and FaaS. arXiv preprint arXiv:2502.14450.

Wang, M., Kapp, A., Schirmer, T., Pfandzelter, T., & Bermbach, D. (2026). Exploring Influence Factors on LLM Suitability for No‐Code Development of End User Applications. Software: Practice and Experience, 56(1), 96-118.


### BibTex

```bibtex
@article{wang2025llm4faas,
  title={LLM4FaaS: No-Code Application Development using LLMs and FaaS},
  author={Wang, Minghe and Pfandzelter, Tobias and Schirmer, Trever and Bermbach, David},
  journal={arXiv preprint arXiv:2502.14450},
  year={2025}
}
```

```bibtex
@article{wang2026exploring,
  title={Exploring Influence Factors on LLM Suitability for No-Code Development of End User Applications},
  author={Wang, Minghe and Kapp, Alexandra and Schirmer, Trever and Pfandzelter, Tobias and Bermbach, David},
  journal={Software: Practice and Experience},
  volume={56},
  number={1},
  pages={96--118},
  year={2026},
  publisher={Wiley Online Library}
}
```
For a full list of publications from our research group, please see [our website](https://www.tu.berlin/en/3s/research/publications).


