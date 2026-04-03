"""
Configuration settings for LLM-as-a-Judge validation.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Judge provider configuration (defaults to generation provider if not set)
JUDGE_PROVIDER = os.getenv('JUDGE_PROVIDER', '')
JUDGE_MODEL = os.getenv('JUDGE_MODEL', '')
JUDGE_TEMPERATURE = float(os.getenv('JUDGE_TEMPERATURE', '0.3'))
JUDGE_MAX_TOKENS = int(os.getenv('JUDGE_MAX_TOKENS', '2000'))

# Validation behavior
VALIDATION_MAX_ITERATIONS = int(os.getenv('VALIDATION_MAX_ITERATIONS', '3'))
VALIDATION_TIMEOUT = int(os.getenv('VALIDATION_TIMEOUT', '60'))

# Response format preference
VALIDATION_USE_JSON = os.getenv('VALIDATION_USE_JSON', 'true').lower() == 'true'
