import os
import subprocess
import csv
import re

PROJECT_ROOT = "/Users/minghe/llm4faas/"  
# llm4faas
# SOURCE_DIR = "/Users/minghe/llm4faas/experiments_default/functions_zh/gpt4o_functions"

# no-faas baseline
# SOURCE_DIR = "/Users/minghe/llm4faas/experiments_baseline_v2/baseline_v2_functions_zh/auto_adapt"
# SOURCE_DIR = "/Users/minghe/llm4faas/experiments_baseline_v2/baseline_v2_functions_zh/energy"
# SOURCE_DIR = "/Users/minghe/llm4faas/experiments_baseline_v2/baseline_v2_functions_zh/remote_control"
# SOURCE_DIR = "/Users/minghe/llm4faas/experiments_baseline_v2/baseline_v2_functions_zh/plans"

# human_developer
# SOURCE_DIR = "/Users/minghe/llm4faas/experiments_human_developer/auto_adapt"
# SOURCE_DIR = "/Users/minghe/llm4faas/experiments_human_developer/energy"
# SOURCE_DIR = "/Users/minghe/llm4faas/experiments_human_developer/remote_control"
# SOURCE_DIR = "/Users/minghe/llm4faas/experiments_human_developer/plans"

# open_interpreter
# partical...

# repeat-gpt4o
# SOURCE_DIR = "/Users/minghe/llm4faas/experiments_repeat/repeat_functions"

# repeat-gpt4omini
# SOURCE_DIR = '/Users/minghe/llm4faas/experiments_repeat/repeat_functions_4o-mini'



def run_pylint(directory):
    output_folder = os.path.join(directory, "pylint_reports")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    scores = [] 

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                absolute_path = os.path.abspath(file_path)  
                relative_path = os.path.relpath(file_path, PROJECT_ROOT)  
                report_filename = f"{os.path.splitext(relative_path)[0].replace(os.sep, '_')}.txt"
                report_path = os.path.join(output_folder, report_filename)

                print(f"Running pylint on {absolute_path}...")

                result = subprocess.run(
                    ["pylint", absolute_path],  
                    cwd=PROJECT_ROOT,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                with open(report_path, "w", encoding="utf-8") as report_file:
                    report_file.write(result.stdout)
                    report_file.write(result.stderr)


                score_match = re.search(r"Your code has been rated at ([\d\.]+)/10", result.stdout)
                score = float(score_match.group(1)) if score_match else None

                
                scores.append((absolute_path, score))
                print(f"Report saved to {report_path}, Score: {score}")


    source_dir_name = os.path.basename(os.path.normpath(directory)) 
    csv_filename = f"score_{source_dir_name}.csv"
    csv_path = os.path.join(output_folder, csv_filename) 


    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Absolute Path", "Score"])  
        writer.writerows(scores)  

    print(f"Score CSV saved at {csv_path}")

if __name__ == "__main__":

    source_directory = os.path.join(PROJECT_ROOT, SOURCE_DIR)
    run_pylint(source_directory)

