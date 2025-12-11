import json
import os
import time

from interpreter import interpreter


def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # print(content)
    return content


def find_markdown_file():
    directory = os.path.abspath('.')
    print(f"Directory: {directory}")
    for file_name in os.listdir(directory):
        if file_name.endswith('.md'):
            print(f"found: {file_name}")
            return file_name
    print("No .md file found")
    return None


def generate_response(prompt):
    interpreter.messages = []
    response = interpreter.chat(prompt, stream=False)


if __name__ == '__main__':

    # open-interpreter config
    interpreter.offline = True
    interpreter.auto_run = True
    # interpreter.llm.model = "ollama/llama3.1"
    # interpreter.llm.api_base = "http://localhost:11434"

    interpreter.llm.model = "gpt-4o"
    interpreter.llm.api_key = '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'
    interpreter.os = False
    # interpreter.llm.supports_vision = True

    interpreter.llm.supports_functions = True
    # interpreter.llm.context_window = 110000
    interpreter.llm.max_tokens = 1500
    interpreter.loop = True
    interpreter.llm.temperature = 0.7
    # interpreter.llm.max_output = 1500
    interpreter.llm.supports_functions = True

    interpreter.system_message += "You are a helpful assistant."

    # get content from md file
    md_file = find_markdown_file()
    if md_file is None:
        exit()

    content = read_markdown(md_file)

    # start
    interpreter.messages = []

    start_time = time.time_ns()
    # print(f"start_time: {start_time}")

    response = interpreter.chat(content, stream=False, display=True)

    end_time = time.time_ns()
    # print(f"end_time: {end_time}")

    duration = end_time - start_time

    response_with_time = {
        "start_time_ns": start_time,
        "end_time_ns": end_time,
        "duration": duration,
        "response": response
    }

    with open('response.json', 'w', encoding='utf-8') as f:
        json.dump(response_with_time, f, ensure_ascii=False, indent=4)
