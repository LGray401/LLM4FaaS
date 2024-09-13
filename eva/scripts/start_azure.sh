#!/bin/bash
python3 -m venv myenv
source myenv/bin/activate || { echo "Activating virtual environment failed"; exit 1; }
# python3 azure_openai_simple_generator.py || { echo "Running azure openai failed"; exit 1; }
python3 openai_simple_generator.py || { echo "Running azure openai failed"; exit 1; }