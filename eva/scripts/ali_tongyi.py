import time

from openai import OpenAI
import os

# <<<<<<< HEAD
from eva.scripts.model_setting import ALI_TONGYI_MODEL, TEMPERATURE, MAX_TOKENS

#
# # model= "qwen-max-0919"
model = ALI_TONGYI_MODEL
# tongyi_api_key = "sk-aa6301b2bf33440481749c81ab21c12b" #chinese account
tongyi_api_key = 'sk-5792cb8b87ac4e6bbc28a66746852d73' # international account

MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/auto_adapt/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/plan/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/energy_control/'
# MD_FILES_DIR = '/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_Chinese/remote_control/'

OUTPUT_DIR = '../../ali_tongyi_functions/'

# access key C7mNgqjgRIvobsIC%1W&7NnQvQeM7A?|
def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # print(content)
    return content


def get_response(prompt):
    client = OpenAI(
        api_key='sk-5792cb8b87ac4e6bbc28a66746852d73',
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
    )
    start_time = time.time()
    response = client.chat.completions.create(
        # model='qwen-max',
        model='qwen1.5-7b-chat',  # 'qwen1.5-1.8b-8k-instruct-20240229' or 'qwen1.5-1.8b-8k-instruct',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
    end_time = time.time()
    response_content = response.choices[0].message.content.strip()
    print(response_content)
    latency = end_time - start_time
    print(f"Response latency: {latency:.2f} seconds")

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
    # generate_files_from_directory(MD_FILES_DIR, OUTPUT_DIR)
    # get_response('how are you?')
    get_response("""Q: What is the capital of France?
# A. Berlin
# B. Madrid
# C. Paris
# D. Rome
# Answer:""")