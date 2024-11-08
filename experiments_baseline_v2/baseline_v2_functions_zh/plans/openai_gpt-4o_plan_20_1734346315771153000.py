# To create a smart home application based on your functional description, we need to define the routines for the "MORNING PLAN," "LEAVE HOME PLAN," and "MOVIE PLAN." We will use the `actuator.py` and `home_plan.py` modules to interact with the actuators needed to perform each plan.
# 
# Here is the application code that implements the requested functionality:
# 
# ```python
# smart_home.py

from home.home_plan import home_plan, get_all_actuators

def morning_plan(home):
    # MORNING PLAN: 打开窗帘 (Open Curtains)
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

def leave_home_plan(home):
    # LEAVE HOME PLAN: 关灯 (Turn Off Lights)
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def movie_plan(home):
    # MOVIE PLAN: 调节灯光亮度 (Adjust Light Brightness)
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")  # Set brightness to low for movie atmosphere

def main():
    home = home_plan()
    print("Choose a plan to execute:")
    print("1. Morning Plan")
    print("2. Leave Home Plan")
    print("3. Movie Plan")
    choice = input("Enter the number of the plan: ")

    if choice == "1":
        morning_plan(home)
    elif choice == "2":
        leave_home_plan(home)
    elif choice == "3":
        movie_plan(home)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **Morning Plan**: Opens all curtains in the house.
# - **Leave Home Plan**: Turns off all lights in the house.
# - **Movie Plan**: Sets the brightness of all lights to low.
# 
# ### To Run the Application:
# 1. Save the code above in a file named `smart_home.py`.
# 2. Ensure that the `home` folder containing the reference files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`) is in the same directory as `smart_home.py`.
# 3. Open a terminal and navigate to the directory containing `smart_home.py`.
# 4. Run the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This will prompt you to choose a plan to execute. Enter the corresponding number to run the desired routine.