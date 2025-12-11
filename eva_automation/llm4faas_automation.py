import os
import re
import subprocess
import threading
import time
import urllib
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

from experiments_repeat.openai_simple_generator import MD_FILES_DIR, GPT_OUTPUT_DIR, \
    get_results_single_md_nodejs

# get_results_single_md

TINYFAAS_DIR = '../tinyFaaS'
LLM_SCRIPT_PYTHON_VENV = '/Users/minghe/llm4faas/eva/scripts/myenv/bin/python3'
# TINYFAAS_ENV = "python3"
TINYFAAS_ENV = "nodejs"

# tinyFaaS Ports
MANAGEMENT_PORT = 8080
HTTP_PORT = 8000

# tinyFaaS Scripts-cwd is TINYFAAS_DIR
UPLOAD_SCRIPTS = "./scripts/upload.sh"
# URLs
MANAGEMENT_URL = f"http://localhost:{MANAGEMENT_PORT}/"

# LLM Scripts
# OLLAMA_SCRIPT_DIR = '../eva/scripts/ollama_simple_generate.py'

# GPT-4o Scripts
GPT4O_SCRIPT_DIR = '../experiments_repeat/openai_simple_generator.py'
SCRIPT_DIR = GPT4O_SCRIPT_DIR

# OUT_FILE = os.path.join('/Users/minghe/llm4faas/eva_latency/_out', "test_execution_durations.out")
OUT_FILE = os.path.join('/Users/minghe/llm4faas/eva_latency/_out', "nodejs_execution_durations.out")

log_data = {}
LLM_START_TIME = None
LLM_END_TIME = None

SCRIPT_LLM_START_TIME = None
SCRIPT_LLM_END_TIME = None


def write_to_out_file(fn_name):
    """write to .out file"""
    if fn_name in log_data:
        with open(OUT_FILE, "a") as f:
            log_entry = log_data[fn_name]

            upload_start_time = log_entry.get('upload_start_time')
            end_time_upload_fn = log_entry.get('end_time_upload_fn')
            trigger_start_time = log_entry.get('trigger_start_time')
            trigger_end_time = log_entry.get('trigger_end_time')
            llm_start_time = log_entry.get('llm_start_time')
            llm_end_time = log_entry.get('llm_end_time')
            script_llm_start_time = log_entry.get('script_llm_start_time')
            script_llm_end_time = log_entry.get('script_llm_end_time')

            log_message = f"{fn_name}, " \
                          f"{f'{upload_start_time}' if upload_start_time is not None else 'None'}, " \
                          f"{f'{end_time_upload_fn}' if end_time_upload_fn is not None else 'None'}, " \
                          f"{f'{trigger_start_time}' if trigger_start_time is not None else 'None'}, " \
                          f"{f'{trigger_end_time}' if trigger_end_time is not None else 'None'}, " \
                          f"{f'{llm_start_time}' if llm_start_time is not None else 'None'}, " \
                          f"{f'{llm_end_time}' if llm_end_time is not None else 'None'}, " \
                          f"{f'{script_llm_start_time}' if script_llm_start_time is not None else 'None'}, " \
                          f"{f'{script_llm_end_time}' if script_llm_end_time is not None else 'None'}\n "

            f.write(log_message)
            print(f"OUTPUT MSG: {log_message}")

        del log_data[fn_name]


def trigger_fn(fn_name):
    """trigger uploaded function"""
    url = f"http://localhost:{HTTP_PORT}/{fn_name}"

    start_time_trigger_fn = time.time_ns()
    end_time_trigger_fn = None
    print(f"Triggering function {fn_name} at {start_time_trigger_fn} in {url}")

    try:
        response = requests.post(url, timeout=30)

        if response.status_code == 200:
            end_time_trigger_fn = time.time_ns()
            print(f"Trigger {fn_name} successfully at {end_time_trigger_fn}")
        else:
            print(f"Function {fn_name} trigger failed with status code {response.status_code}: {response.text}")
            end_time_trigger_fn = f"Error code: {response.status_code}"
        return start_time_trigger_fn, end_time_trigger_fn
    except requests.Timeout:
        return start_time_trigger_fn, "Timeout after 30 seconds!"
    except requests.RequestException as e:
        print(f'Error triggering function {fn_name}: {e}')
        return start_time_trigger_fn, f"Error: {e}"


def upload_single_fn(folder_path, output_file_name):
    """upload a single function to tinyFaaS and trigger it after uploading successfully"""
    fn_dir = os.path.join("../..", folder_path)

    alphanumeric_name = re.sub(r'[^a-zA-Z0-9]', '', output_file_name)
    start_time_upload_fn = time.time_ns()
    print(f"Uploading {folder_path} at {start_time_upload_fn} as {alphanumeric_name}...")

    try:
        upload_thread = subprocess.run(
            [UPLOAD_SCRIPTS, fn_dir, alphanumeric_name, TINYFAAS_ENV, "1"],
            check=True,
            cwd=TINYFAAS_DIR,
            capture_output=True)

        end_time_upload_fn = time.time_ns()
        print(f"Uploaded {folder_path} at {end_time_upload_fn}")

        trigger_start_time, trigger_end_time = trigger_fn(alphanumeric_name)

        # log_fn_name = folder_path.replace(FN_DIR, "")  # remove the prefix
        # log_fn_name = folder_path.replace(MD_FILES_DIR,"")  # remove the prefix
        log_fn_name = folder_path.replace(GPT_OUTPUT_DIR, "")
        if log_fn_name not in log_data:
            log_data[log_fn_name] = {}

        log_data[log_fn_name]["upload_start_time"] = start_time_upload_fn
        log_data[log_fn_name]["end_time_upload_fn"] = end_time_upload_fn
        log_data[log_fn_name]["trigger_start_time"] = trigger_start_time
        log_data[log_fn_name]["trigger_end_time"] = trigger_end_time
        log_data[log_fn_name]["llm_start_time"] = LLM_START_TIME
        log_data[log_fn_name]["llm_end_time"] = LLM_END_TIME
        log_data[log_fn_name]["script_llm_start_time"] = SCRIPT_LLM_START_TIME
        log_data[log_fn_name]["script_llm_end_time"] = SCRIPT_LLM_END_TIME

        write_to_out_file(log_fn_name)

        return folder_path

    except subprocess.CalledProcessError as e:
        print(f"Failed to upload {alphanumeric_name}: {e.stderr}")
        return None


def check_and_upload(fn_folder, output_file_name):
    upload_thread = threading.Thread(target=upload_single_fn, args=(fn_folder, output_file_name))

    upload_thread.start()
    upload_thread.join()


def start_automation():
    #  0. start tinyfaas
    #  start_time
    #  1. run llm script, and for every fn, return a fn_dir.
    #  2. process the fn.py, by replacing '__main__' with 'fn(data, header):
    #  3. start upload process.
    #  4. trigger fn and get result
    #  end_time
    global LLM_START_TIME, LLM_END_TIME, SCRIPT_LLM_START_TIME, SCRIPT_LLM_END_TIME
    if not os.path.exists(OUT_FILE):
        with open(OUT_FILE, "w") as f:
            f.write("fn_name, upload_start_time, upload_end_time, trigger_start_time, trigger_end_time, llm_start_time, llm_end_time, script_llm_start_time, script_llm_end_time\n")

    for md_file in os.listdir(MD_FILES_DIR):
        if md_file.endswith('.md'):
            md_file_path = os.path.join(MD_FILES_DIR, md_file)
            # stamp time here as well.

            automation_llm_start_time = time.time_ns()
            print(f"Automation starts processing {md_file_path} at {automation_llm_start_time}")

            # fn_folder, output_file_name, llm_script_end_time, llm_script_start_time = get_results_single_md(
            fn_folder, output_file_name, llm_script_end_time, llm_script_start_time = get_results_single_md_nodejs(
                md_file_path,
                GPT_OUTPUT_DIR
            )

            automation_llm_end_time = time.time_ns()
            print(f"Automation finishes processing {md_file_path} at {automation_llm_end_time}")

            LLM_START_TIME = automation_llm_start_time
            LLM_END_TIME = automation_llm_end_time

            SCRIPT_LLM_START_TIME = llm_script_start_time
            SCRIPT_LLM_END_TIME = llm_script_end_time

            check_and_upload(fn_folder, output_file_name)
            print("------------------------------------")
            time.sleep(5)


if __name__ == '__main__':
    start_automation()
