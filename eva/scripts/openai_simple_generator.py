import os
import time

import openai

from model_setting import MAX_TOKENS, TEMPERATURE, OPENAI_MODEL, DELAY_SECONDS, SYSTEM_PROMPT
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]

openai.api_key = api_key
model = OPENAI_MODEL


# test dir
# md_file = '/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/remote_control/remote_control_1.md'

# default experiment -- Chinese prompts
# MD_FILES_DIR = '/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/remote_control/'
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/plans/"
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/auto_adapt/"
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/energy/"

# default experiment -- English prompts
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_English/remote_control/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_English/plans/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_English/auto_adapt/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_English/energy/'
MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_English/temp/'

# system-prompt experiment -- Chinese prompts
# MD_FILES_DIR = '/Users/minghe/llm4faas/system_prompts_experiments/user_prompt_zh_short/remote_control/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/system_prompts_experiments/user_prompt_zh_short/plans/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/system_prompts_experiments/user_prompt_zh_short/auto_adapt/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/system_prompts_experiments/user_prompt_zh_short/energy/'

# system-prompt experiment -- English prompts
# MD_FILES_DIR = '/Users/minghe/llm4faas/system_prompts_experiments/user_prompt_en_short/auto_adapt/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/system_prompts_experiments/user_prompt_en_short/remote_control/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/system_prompts_experiments/user_prompt_en_short/energy/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/system_prompts_experiments/user_prompt_en_short/plans/'

# output dir -- default experiment
# OUTPUT_DIR = '../../default_experiments/functions_en/gpt-4o_en_functions/energy/'
# OUTPUT_DIR = '../../generated_functions/'

OUTPUT_DIR = '.'


# output dir -- system-prompt experiment
# OUTPUT_DIR = '../../system_prompts_experiments/zh_functions/gpt4o-mini/'
# OUTPUT_DIR = '../../system_prompts_experiments/en_functions/gpt4o-mini/'

def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # print(content)
    return content


def generate_python_code(prompt):
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            # {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE
    )
    response_content = response.choices[0].message.content.strip()
    # return response_content
    start_index = response_content.find('```python')
    end_index = response_content.find('```', start_index + len('```python'))

    if start_index != -1 and end_index != -1:
        context = response_content[:start_index].strip()
        code = response_content[start_index + len('```python'):end_index].strip()
        context_as_comment = '\n'.join(f"# {line}" for line in context.split('\n'))
        full_code = f"{context_as_comment}\n\n{code}"
    else:
        full_code = '\n'.join(f"# {line}" for line in response_content.split('\n'))

    return full_code


def save_python_code(code, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(code)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(MD_FILES_DIR):
        if filename.endswith('.md'):
            md_file_path = os.path.join(MD_FILES_DIR, filename)
            markdown_content = read_markdown(md_file_path)
            prompt = f"{markdown_content}"
            python_code = generate_python_code(prompt)

            base_name = os.path.basename(md_file_path).replace('.md', '')
            output_file_name = os.path.join(OUTPUT_DIR, f'openai_{model}_{base_name}.py')

            # save the generated python code to a file
            save_python_code(python_code, output_file_name)
            print(f"Saved Python file to {output_file_name}")
            time.sleep(DELAY_SECONDS)


    # markdown_content = read_markdown(md_file)
    # prompt = f"{markdown_content}"
    # python_code = generate_python_code(prompt)
    #
    # base_name = os.path.basename(md_file).replace('.md', '')
    # output_file_name = f'../../functions/test{model}_{base_name}.py'
    #
    # # Save the Python code to the constructed file name
    # save_python_code(python_code, output_file_name)
    # print(f"Saved Python file to {output_file_name}")


if __name__ == "__main__":
    main()
