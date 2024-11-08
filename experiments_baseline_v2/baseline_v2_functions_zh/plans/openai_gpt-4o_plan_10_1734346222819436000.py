# To create a smart home application based on your functional description and the provided source code, we'll define a new Python script. This script will implement the specified plans using the available actuators from the `actuator.py` file.
# 
# Here's how the application will be structured:
# 
# 1. **MORNING PLAN**: Open curtains.
# 2. **LEAVE HOME PLAN**: Turn off lights and close windows.
# 3. **MOVIE PLAN**: Turn on the TV.
# 
# Below is the implementation of the smart home application:
# 
# ```python
# smart_home.py

from home.home_plan import home_plan, get_all_actuators

def execute_morning_plan(home):
    print("Executing Morning Plan: 打开窗帘")
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

def execute_leave_home_plan(home):
    print("Executing Leave Home Plan: 关闭灯光，窗户")
    lights = get_all_actuators(home, "Light")
    windows = get_all_actuators(home, "Window")
    for light in lights:
        light.turn_off()
    for window in windows:
        window.turn_off()

def execute_movie_plan(home):
    print("Executing Movie Plan: 打开电视")
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        tv.turn_on()

if __name__ == "__main__":
    home = home_plan()
    
    # Choose which plan to execute
    plan_to_execute = input("Enter the plan to execute (morning, leave_home, movie): ").strip().lower()

    if plan_to_execute == "morning":
        execute_morning_plan(home)
    elif plan_to_execute == "leave_home":
        execute_leave_home_plan(home)
    elif plan_to_execute == "movie":
        execute_movie_plan(home)
    else:
        print("Invalid plan selected.")
# ```
# 
# ### Command to Run the Application
# 
# Assuming the script is saved as `smart_home.py` in the same directory as the `home` folder, you can run it from the terminal using:
# 
# ```bash
# python smart_home.py
# ```
# 
# ### Explanation
# 
# - **MORNING PLAN**: The script finds all curtain actuators and turns them on.
# - **LEAVE HOME PLAN**: It finds all light and window actuators and turns them off.
# - **MOVIE PLAN**: It turns on all SmartTV actuators.
# 
# This script uses your existing home components and the actuator classes to simulate the different plans. You can run the script and enter the desired plan to execute the respective actions.