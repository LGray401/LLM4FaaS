# system prompt experiment settings
SYSTEM_PROMPT = "You are a helpful assistant." \
                "I want you to provide me a 'function.py' file for my current smart home project based on my given functional description." \
                "Four code files in my project, i.e., sensor.py, actuator.py, home_plan.py and config.py, are in the 'home' folder." \
                "The required 'function.py' should locate in the 'functions' folder, function.py should contain main function." \
                "I will first give you the functional description, then give you the 4 python source code."

# default experiment setting
# SYSTEM_PROMPT = "You are a helpful assistant."
# todo: comment 'system' line in ollama simple generator

DELAY_SECONDS = 10

TEMPERATURE = 0.7
MAX_TOKENS = 1500

# OPENAI_MODEL = 'o1-mini'
OPENAI_MODEL = 'gpt-4o-mini'
# OPENAI_MODEL = 'gpt-4o'
# OPENAI_MODEL = "gpt-3.5-turbo"


# OLLAMA_MODEL = 'llama3.1'
OLLAMA_MODEL = 'deepseek-r1:7b'


OLLAMA_URL = 'http://localhost:11434/api/generate'
ZHIPU_MODEL = "glm-4-flash"

# free model
# QIANFAN_MODEL = "ERNIE-Speed-128K"
QIANFAN_MODEL ='ernie-4.0-turbo-8k'
# enhanced llama2 model, which can generate function code
# QIANFAN_URL = 'Qianfan-Chinese-Llama-2-70B'

ALI_TONGYI_MODEL = "qwen-max-0919"