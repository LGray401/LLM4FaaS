import time

from openai import OpenAI
import os

from eva.scripts.model_setting import ALI_TONGYI_MODEL

# model= "qwen-max-0919"
model = ALI_TONGYI_MODEL
tongyi_api_key = "sk-aa6301b2bf33440481749c81ab21c12b"


MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/auto_adapt/'
OUTPUT_DIR = '../../ali_tongyi_functions/'


def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # print(content)
    return content


def get_response(prompt):
    client = OpenAI(
        api_key=tongyi_api_key, # 如果你没有配置环境变量，使用"your-api-key"替换
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", # 这里使用的是阿里云的大模型，如果需要使用其他平台，请参考对应的开发文档后对应修改
    )
    response = client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}],
        temperature=0.7,
        max_tokens=1500,
    )

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
            python_code = get_response(prompt)

            base_name = os.path.basename(md_file_path).replace('.md', '')
            output_file_name = os.path.join(output_dir, f'ali_{model}_{base_name}_{time.time_ns()}.py')

            # save the generated python code to a file
            save_python_code(python_code, output_file_name)
            print(f"Saved Python file to {output_file_name}")
            time.sleep(10)

if __name__ == '__main__':
    generate_files_from_directory(MD_FILES_DIR, OUTPUT_DIR)
