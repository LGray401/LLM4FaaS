# todo:
#  1. get the existing python function name
#  2. create a new folder with the function name under a specific folder
#  3. copy home folder to each folder
#  4. copy the function file to the folder, and rename it to fn.py
#  5. add an empty requirement.txt file to each folder
#  6. modify current fn.py by replacing 'if __name__ == "__main__":' with 'def fn(data, headers): main()', currently, triggering function returns 'module 'fn' has no attribute 'fn''
import os
import shutil
import ast

# Define paths
home_folder = "/Users/minghe/llm4faas/tinyFaaS/test/fns/llm/home"  # Change this to your home folder
# gpt4o-zh
source_folder = "/Users/minghe/llm4faas/experiments_default/functions_zh/gpt4o_functions"  # Folder containing the Python files
# test path
# source_folder  = '/Users/minghe/llm4faas/experiments_default/functions_zh/claude35-haiku'

destination_root = "./"  # Root where new folders will be created

os.makedirs(destination_root, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.endswith(".py"): 
        file_path = os.path.join(source_folder, filename)

        folder_name = os.path.splitext(filename)[0]
        folder_path = os.path.join(destination_root, folder_name)

        os.makedirs(folder_path, exist_ok=True)
        shutil.copytree(home_folder, os.path.join(folder_path, "home"), dirs_exist_ok=True)

        new_fn_path = os.path.join(folder_path, "fn.py")
        shutil.copy(file_path, os.path.join(folder_path, "fn.py"))

        requirement_path = os.path.join(folder_path, "requirements.txt")
        with open(requirement_path, "w", encoding="utf-8") as f:
            pass  

        # comment out 'if __name__ == "__main__":' and replace with 'def fn(data, headers):'
        with open(new_fn_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        inserted_fn = False 

        for line in lines:
            stripped_line = line.strip()
            if stripped_line == 'if __name__ == "__main__":':
                new_lines.append("# " + line)
                if not inserted_fn:
                    new_lines.append("def fn(data, headers):\n")  
                    inserted_fn = True
            else:
                new_lines.append(line)

        if not inserted_fn:
            new_lines.insert(0, "def fn(data, headers):\n\n")

        with open(new_fn_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

        print(f"已处理 {filename} -> {folder_path}")

print("所有文件处理完成！")
