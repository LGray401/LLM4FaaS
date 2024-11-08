import os
import time

import qianfan

from eva.scripts.model_setting import QIANFAN_MODEL

os.environ["QIANFAN_AK"] = "jRwwUizkxVFlDaxahX0tElE0"
os.environ["QIANFAN_SK"] = "v9VheASwZGaFwlk5yaHcQ9D3ia1AaJim"

#【推荐】建议您在生产环境使用IAM认证鉴权，文档地址 https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
# os.environ["QIANFAN_ACCESS_KEY"] = "your_iam_ak"
# os.environ["QIANFAN_SECRET_KEY"] = "your_iam_sk"

MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/auto_adapt/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/energy/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/remote_control/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/plans/'

OUTPUT_DIR = '../../baidu_functions/'

# model = "Qianfan-Chinese-Llama-2-70B"
# free models
# model = "ERNIE-Lite-8K-0922"
# model = "ERNIE-Speed-128K"
# model = "ERNIE-Tiny-8K"
# model = "ERNIE Speed-AppBuilder"

# best models for now
# model ="ernie-4.0-turbo-8k"
model = QIANFAN_MODEL

# external invocation
# model = "ERNIE Functions"

def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # print(content)
    return content


def baidu_generate_python_code(prompt):

    resp = qianfan.ChatCompletion().do(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
        ],
        system = "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。",
        temperature=0.7,
        max_output_tokens=1500, # default 4096
    )

    response_content = resp["body"]['result']
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
            python_code = baidu_generate_python_code(prompt)

            base_name = os.path.basename(md_file_path).replace('.md', '')
            output_file_name = os.path.join(output_dir, f'zhipu_{model}_{base_name}_{time.time_ns()}.py')

            # save the generated python code to a file
            save_python_code(python_code, output_file_name)
            print(f"Saved Python file to {output_file_name}")
            time.sleep(1)

if __name__ == '__main__':
    generate_files_from_directory(MD_FILES_DIR, OUTPUT_DIR)

    # markdown_content = read_markdown(MD_FILES_DIR)
    # prompt = f"{markdown_content}"
    # baidu_generate_python_code(prompt)