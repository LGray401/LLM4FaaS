import os

def process_file(file_path):
    """处理 Python 文件，将文件中的非python代码部分注释掉"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    def comment_out_non_python(content):
        result = []
        inside_python_block = False  # 用于标识是否在 ```python``` 代码块内

        # 按行遍历文件内容
        lines = content.split('\n')
        for line in lines:
            # 检查是否为 python 代码块的开始
            if '```python' in line:
                inside_python_block = True
                result.append(f"# {line}")  # 注释掉 ```python```
                continue  # 跳过该行，继续处理下一行

            # 检查是否为 python 代码块的结束
            if '```' in line and inside_python_block:
                inside_python_block = False
                result.append(f"# {line}")  # 注释掉 ```
                continue  # 跳过该行，继续处理下一行

            # 如果在 python 代码块内，则直接保留代码
            if inside_python_block:
                result.append(line)
            else:
                result.append(f"# {line}")  # 注释掉非代码部分

        return '\n'.join(result)

    # 对文件内容进行处理
    processed_content = comment_out_non_python(content)

    # 将处理后的内容写回原文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content)
    print(f"Processed and updated file: {file_path}")


def process_directory(directory):
    """处理文件夹中的所有 Python 文件"""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # 只处理 .py 文件
        if os.path.isfile(file_path) and filename.endswith('.py'):
            print(f"Processing Python file: {file_path}")
            process_file(file_path)


if __name__ == '__main__':
    target_directory = '/Users/minghe/llm4faas/experiments_baseline_v2/baseline_v2_functions_zh/plans'
    # target_directory = '/Users/minghe/llm4faas/experiments_baseline/baseline_functions_zh/auto_adapt'
    # target_directory = '/Users/minghe/llm4faas/experiments_baseline/baseline_functions_zh/remote_control'
    # target_directory = '/Users/minghe/llm4faas/experiments_baseline/baseline_functions_zh/plans'
    # target_directory = '/Users/minghe/llm4faas/experiments_baseline/baseline_functions_zh/energy'

    process_directory(target_directory)