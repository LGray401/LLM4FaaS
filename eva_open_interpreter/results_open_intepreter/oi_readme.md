# Get responses from Open Interpreter
## setup oi folders
We create a folder for each user response including the structured prompt and the python script to get responses from open-interpreter
The script is ['eva_open_interpreter/setup_experiments.py']

## get responses from Open Interpreter
The script is ['eva_open_interpreter/run_open_interpreter.py']
Specifically, we record the timestamp of start/end time of the process here as well.
The end_time can be the time the process is complete/timeout/exception.

# Analysis results of Open Interpreter
## check_open_interpreter_results.py
1. check if oi response contains a python file locally, and if it contains a json file, i.e., the chat process is complete.
2. oi process met rate-limit-error quite often, so we have a Boolean record for rate limit occurrence during the generation process.
3. store the results in the 'task_results.csv' with JSON/PYTHON/BOTH/NONE
4. if only Json file is in the response, we will extract oi-generated python code and the oi-tested console output in 'process_json_file'
5. the outputs are stored as 'oi_[task_name_id].py' and 'oi_[task_name_id].log'
6. In 'oi_function_output.py', we test the 'oi_[task_name_id].py' file and have a 'real_[task_name_id].log' file as well.

## oi_function_output.py
1. We run the oi-generated python code and get the local console output.
2. We also check the command line instruction that oi provided, sometimes, a command start with 'python' does not work in an environment with 'python3' as the default python version.

## oi_latency.py
1. get 'start_time' and 'end_time' from the 'logfile.text' for case.
2. if there is a timeout, then, latency is 'time_out_duration'(30s)

## oi_success_rate.py
the function logic is similar to llm4faas success rate calculation.
