import os
import subprocess
from test.function_directory import FOLDER_PATHS

TIMEOUT = 30
# folder path where the generated functions are stored
# folder_path = FOLDER_PATH

folder_paths = FOLDER_PATHS

for folder_path in folder_paths:
    print(f'!!!!!Executing functions in {folder_path}!!!')
# Iterate through all generated function files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.py'):
            # full path of the file
            file_path = os.path.join(folder_path, filename)

            # save to .log
            log_file_path = os.path.join(folder_path, filename.replace('.py', '.log'))

            with open(log_file_path, 'w') as log_file:
                try:
                    # start subprocess and catch stdout & stderr
                    process = subprocess.Popen(
                        ['python3', file_path],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )

                    # catch stdout & stderr when timeout
                    stdout, stderr = process.communicate(timeout=TIMEOUT)

                    # write stdout & stderr to log file
                    log_file.write("Standard Output:\n")
                    log_file.write(stdout)
                    log_file.write("\nStandard Error:\n")
                    log_file.write(stderr)
                    log_file.write(f"\nReturn code: {process.returncode}\n")

                except subprocess.TimeoutExpired:
                    log_file.write("Error: Execution timed out\n")
                    process.kill()
                    outs, errs = process.communicate()  # get the remaining output
                    log_file.write("Standard Output:\n")
                    log_file.write(outs)
                    log_file.write("\nStandard Error:\n")
                    log_file.write(errs)
                except FileNotFoundError:
                    log_file.write(f"Error: File not found {file_path}\n")
                except Exception as e:
                    log_file.write(f"Unexpected error: {str(e)}\n")

            print(f'Executed {filename}, output saved to {log_file_path}')
