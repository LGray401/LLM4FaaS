# To create a smart home application based on your functional description and layout, we'll develop a simple command-line Python script. This script will simulate the activation of devices based on voice commands for different plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. We'll use a basic dictionary to map the commands to their corresponding actions within the smart home system.
# 
# Here's how you can implement this:
# 
# ```python
import sys

def morning_plan():
    # Turn on all lights in the Living Room
    print("Turning on all lights in the Living Room.")

def leave_home_plan():
    # Open the curtains in the Living Room
    print("Opening the curtains in the Living Room.")

def movie_plan():
    # Turn on the TV in the Living Room
    print("Turning on the TV in the Living Room.")

def execute_command(command):
    if command == "小雨 请开灯":
        morning_plan()
    elif command == "小雨 请打开窗帘":
        leave_home_plan()
    elif command == "小雨 请打开电视机":
        movie_plan()
    else:
        print("Unknown command.")

def main():
    if len(sys.argv) < 2:
        print("Please provide a command.")
        sys.exit(1)
    
    command = sys.argv[1]
    execute_command(command)

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Application
# 
# 1. Save the above script to a file named `smart_home.py`.
# 
# 2. Open your terminal and navigate to the directory where `smart_home.py` is located.
# 
# 3. You can run the application with the following command, passing the desired command as an argument:
# 
#    ```bash
#    python3 smart_home.py "小雨 请开灯"
#    ```
# 
#    Replace `"小雨 请开灯"` with any of the other commands to see the corresponding actions:
# 
#    - `"小雨 请开灯"` for the MORNING PLAN
#    - `"小雨 请打开窗帘"` for the LEAVE HOME PLAN
#    - `"小雨 请打开电视机"` for the MOVIE PLAN
# 
# This simple script simulates the functionality you described. In a real-world application, each function would interface with the actual smart home devices, likely through a home automation platform or API.