import os
import json
import time

import requests

from eva.scripts.model_setting import SYSTEM_PROMPT, TEMPERATURE, OLLAMA_URL, OLLAMA_MODEL

# directory
# MD_FILES_DIR = '/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/remote_control/'
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/plans/"
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/auto_adapt/"
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/energy/"

# MD_FILES_DIR = '/Users/minghe/llm4faas/logs_questionnaire_in_English/remote_control/'
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_English/plans/"
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_English/auto_adapt/"
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_English/energy/"

MD_FILES_DIR = "/Users/minghe/llm4faas/experiments_default/logs_questionnaire_in_Chinese/plans/"
OUTPUT_DIR = '/Users/minghe/llm4faas/experiments_default/functions_zh/deepseek-r1-functions'


# OUTPUT_DIR = '/Users/minghe/llm4faas/experiments_default/functions_zh/llama31_functions'


def generate(prompt_file, context, output_file):
    with open(prompt_file, 'r') as f:
        prompt = f.read()

    r = requests.post(OLLAMA_URL,
                      json={
                          'model': OLLAMA_MODEL,
                          'prompt': prompt,
                          'context': context,
                          # 'system': SYSTEM_PROMPT, # comment this line when running the default experiment
                          'options': {
                              'temperature': TEMPERATURE,
                          },
                      },
                      stream=True)
    r.raise_for_status()

    response_parts = []
    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')

        if 'error' in body:
            raise Exception(body['error'])

        response_parts.append(response_part)

        if body.get('done', False):
            break

    response_content = ''.join(response_parts).strip()

    # comment out non-code parts
    result_lines = []
    in_code_block = False

    for line in response_content.splitlines():
        if '```python' in line or '```' in line:
            result_lines.append(f'# {line}')  # Commenting out the start and end markers of a code block
            in_code_block = not in_code_block
        elif in_code_block:
            result_lines.append(line)  # Adding content within a code block
        else:
            result_lines.append(f'# {line}')  # Commenting out non-block content

    # write the processed content to a file
    with open(output_file, 'w') as f:
        f.write('\n'.join(result_lines))


def process_directory(directory):
    context = []  # Storing dialogue history for better contextual understanding by the model
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            prompt_file = os.path.join(directory, filename)
            base_name = filename.replace('.md', '')
            output_file_name = f"{OLLAMA_MODEL}_{base_name}_{time.time_ns()}.py"
            output_file = os.path.join(OUTPUT_DIR, output_file_name)
            context = generate(prompt_file, context, output_file)
            print(f"Saved Python file to {output_file_name}")
            time.sleep(5)


def main():
    process_directory(MD_FILES_DIR)

if __name__ == "__main__":
    main()