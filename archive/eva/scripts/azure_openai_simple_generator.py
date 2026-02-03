import os
import time
import openai
from openai import AzureOpenAI

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
endpoint = os.environ["AZURE_ENDPOINT"]
api_key = os.environ["AZURE_API_KEY"]

AZURE_ENDPOINT = endpoint
AZURE_API_KEY = api_key
API_VERSION = "2024-02-01"

# AZURE_MODEL = "gpt-4o-new"
# AZURE_MODEL = "gpt-4o-mini"
AZURE_MODEL = "gpt-35-turbo-16k"

DELAY_SECONDS = 10

temperature = 0.7
max_tokens = 800

# md_file = '/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/remote_control/remote_control_1.md'
# markdown file directories
# MD_FILES_DIR = '/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/remote_control/'
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/plans/"
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/auto_adapt/"
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/energy/"

# MD_FILES_DIR = '/Users/minghe/llm4faas/logs_questionnaire_in_English/remote_control/'
MD_FILES_DIR = "/Users/minghe/llm4faas/default_experiments/logs_questionnaire_in_English/plans/"
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_English/auto_adapt/"
# MD_FILES_DIR = "/Users/minghe/llm4faas/logs_questionnaire_in_English/energy/"

# MD_FILES_DIR = '/Users/minghe/llm4faas/logs_questionnaire_in_English/temp/'


# output file directory
OUTPUT_DIR = '../../functions_en/azure_en_functions/'


def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # print(content)
    return content


def save_python_code(code, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(code)


def main():
    # make sure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # go through all .md files in the directory
    for filename in os.listdir(MD_FILES_DIR):
        if filename.endswith('.md'):
            md_file_path = os.path.join(MD_FILES_DIR, filename)
            markdown_content = read_markdown(md_file_path)
            prompt = f"{markdown_content}"
            python_code = azure_generate_python_code(prompt)

            base_name = os.path.basename(md_file_path).replace('.md', '')
            output_file_name = os.path.join(OUTPUT_DIR, f'azure_{AZURE_MODEL}_{base_name}.py')

            # save the generated python code to a file
            save_python_code(python_code, output_file_name)
            print(f"Saved Python file to {output_file_name}")
            time.sleep(DELAY_SECONDS)


def azure_generate_python_code(prompt):
    client = AzureOpenAI(
        azure_endpoint=AZURE_ENDPOINT,
        api_key=AZURE_API_KEY,
        api_version=API_VERSION
    )

    response = client.chat.completions.create(
        model= AZURE_MODEL,  # model = "deployment_name".
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )

    response_content = response.choices[0].message.content.strip()

    # print(response_content)
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


if __name__ == "__main__":
    main()
