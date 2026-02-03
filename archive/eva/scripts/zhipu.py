import os
import time

from zhipuai import ZhipuAI
from eva.scripts.model_setting import ZHIPU_MODEL, TEMPERATURE, MAX_TOKENS, DELAY_SECONDS

client = ZhipuAI(api_key="1b50c844b2c87b83e3a92355eb365976.cPhvlK4VT2pUccRJ")
model=ZHIPU_MODEL,

# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/auto_adapt/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/energy/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/remote_control/'
MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/plans/'

OUTPUT_DIR = '../../zhipu_functions/'


def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # print(content)
    return content


def zhipu_generate_python_code(prompt):
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[
            {"role": "system", "content": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。"},
            {"role": "user", "content": prompt}
        ],
        temperature= 0.7,
        max_tokens= 1500,
    )
    # print(response.choices[0].message)
    response_content = response.choices[0].message.content.strip()
    # print(response_content)

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


def generate_files_from_directory(prompt_dir, output_dir):
    # def main():
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(prompt_dir):
        if filename.endswith('.md'):
            md_file_path = os.path.join(prompt_dir, filename)
            markdown_content = read_markdown(md_file_path)
            prompt = f"{markdown_content}"
            python_code = zhipu_generate_python_code(prompt)

            base_name = os.path.basename(md_file_path).replace('.md', '')
            output_file_name = os.path.join(output_dir, f'zhipu_{model}_{base_name}_{time.time_ns()}.py')

            # save the generated python code to a file
            save_python_code(python_code, output_file_name)
            print(f"Saved Python file to {output_file_name}")
            time.sleep(10)

# def repeatable_experiments(md_dir, output_dir, repeat_times):
#     for i in range(repeat_times):
#         print(f"Start {i+1} Iteration")
#         generate_files_from_directory(md_dir, output_dir)
#         print(f"Finished {i + 1} round iteration.\n")
#

if __name__ == '__main__':
    generate_files_from_directory(MD_FILES_DIR, OUTPUT_DIR)