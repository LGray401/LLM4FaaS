import os
import re
import csv

# todo:
#  0. 遍历所有文件夹，找到其中的logfile.txt文件
#  1. 找到[start_time] Start Time - path; \n ; [end_time] Standard Output:
#  2. 如果找到的是[timeout]，记录为timeout。
#  2. extract: start_time, end_time, path
#  3. save the result to csv.


def extract_logfile(path):
    start_time, end_time, script_path = None, None, None
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            start_match = re.search(r'\[(\d+)] Start Time - (.+)', line)
            end_match = re.search(r'\[(\d+)] Standard Output:', line)
            timeout_match = re.search(r'\[(\d+)] Execution timed out - (.+)', line)

            if start_match:
                start_time = start_match.group(1)
                script_path = start_match.group(2)
            elif end_match:
                end_time = end_match.group(1)
            elif timeout_match:
                start_time = "timeout"
                script_path = timeout_match.group(2)
                end_time = timeout_match.group(1)

    return start_time, end_time, script_path

def find_logfiles(root_dir):
    results = []
    for root, _, files in os.walk(root_dir):
        if "logfile.txt" in files:
            logfile_path = os.path.join(root, "logfile.txt")
            extracted_data = extract_logfile(logfile_path)
            if extracted_data[1] or extracted_data[0] == "timeout":  # 确保提取的数据完整或标记超时
                results.append(extracted_data)
    return results

def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["start_time", "end_time", "path"])
        writer.writerows(data)

if __name__ == "__main__":
    root_directory = "."  # 修改为你的根目录
    output_csv = os.path.join("/Users/minghe/llm4faas/eva_latency/_out/", "oi_latency.csv")

    log_data = find_logfiles(root_directory)
    save_to_csv(log_data, output_csv)
    print(f"Saved results to {output_csv}")
