"""
Configuration settings for LLM generation.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Default system prompt for FaaS function generation
DEFAULT_SYSTEM_PROMPT = (
    "You are a helpful assistant. "
    "I want you to provide me a 'function.py' file for my current smart home project "
    "based on my given functional description. "
    "Four code files in my project, i.e., sensor.py, actuator.py, home_plan.py and config.py, "
    "are in the 'home' folder. "
    "The required 'function.py' should locate in the 'functions' folder, "
    "function.py should contain main function. "
    "I will first give you the functional description, then give you the 4 python source code."
)

# Generation parameters
TEMPERATURE = float(os.getenv('LLM_TEMPERATURE', '0.7'))
MAX_TOKENS = int(os.getenv('LLM_MAX_TOKENS', '1500'))
DELAY_SECONDS = int(os.getenv('LLM_DELAY_SECONDS', '10'))

# Provider-specific model names
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'deepseek-r1:7b')
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'models/gemini-1.5-flash')
ZHIPU_MODEL = os.getenv('ZHIPU_MODEL', 'glm-4-flash')
QIANFAN_MODEL = os.getenv('QIANFAN_MODEL', 'ernie-4.0-turbo-8k')
ALI_TONGYI_MODEL = os.getenv('ALI_TONGYI_MODEL', 'qwen-max-0919')
DOUBAO_MODEL = os.getenv('DOUBAO_MODEL', 'doubao-pro')

# Provider-specific URLs
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434/api/generate')
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT', '')

# API Keys (loaded from environment)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
ZHIPU_API_KEY = os.getenv('ZHIPU_API_KEY', '')
QIANFAN_API_KEY = os.getenv('QIANFAN_API_KEY', '')
QIANFAN_SECRET_KEY = os.getenv('QIANFAN_SECRET_KEY', '')
ALI_TONGYI_API_KEY = os.getenv('ALI_TONGYI_API_KEY', '')
DOUBAO_API_KEY = os.getenv('DOUBAO_API_KEY', '')
AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY', '')
