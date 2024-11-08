# To create a smart home application based on the given functional description and source code, we need to develop a script that integrates the existing components (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) and implements the specified plans: "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN". 
# 
# Here's how we can structure the `smart_home.py` script to achieve this functionality:
# 
# ### `smart_home.py`
# 
# ```python
from home.home_plan import home_plan, get_all_actuators

def execute_morning_plan(home):
    print("\nExecuting Morning Plan: 小雨 请开灯")
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()

def execute_leave_home_plan(home):
    print("\nExecuting Leave Home Plan: 小雨 请打开窗帘")
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

def execute_movie_plan(home):
    print("\nExecuting Movie Plan: 小雨 请打开电视机")
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        tv.turn_on()

def main():
    home = home_plan()
    
    # Execute plans
    execute_morning_plan(home)
    execute_leave_home_plan(home)
    execute_movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation
# 
# 1. **Import Required Modules:**
#    - We import the necessary functions from `home_plan`.
# 
# 2. **Define Plan Execution Functions:**
#    - `execute_morning_plan(home)`: Turns on all lights in the home.
#    - `execute_leave_home_plan(home)`: Opens all curtains in the home.
#    - `execute_movie_plan(home)`: Turns on all TVs in the home.
# 
# 3. **Main Function:**
#    - The `main()` function initializes the home plan and executes each of the defined plans.
# 
# 4. **Entry Point:**
#    - The script checks if it's run as the main program and calls the `main()` function.
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, navigate to the directory containing your `smart_home.py` script and the `home` folder. Then run the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This will execute the script and simulate the smart home plans by turning on the corresponding actuators as described in your functional description.