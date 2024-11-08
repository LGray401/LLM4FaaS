# Based on your functional description and the provided source code, here's a `function.py` file that contains a main function to support the different smart home plans you mentioned: Morning Plan, Leave Home Plan, and Movie Plan. This `function.py` file will be located in the `functions` folder.

# functions/function.py
import sys
import time
from home.home_plan import home_plan, get_all_actuators

def morning_plan(home):
    print("Executing Morning Plan...")
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("high")
    print("Morning Plan executed.")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
    print("Leave Home Plan executed.")

def movie_plan(home):
    print("Executing Movie Plan...")
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")
    print("Movie Plan executed.")

def main(plan_name):
    home = home_plan()

    if plan_name == "MORNING":
        morning_plan(home)
    elif plan_name == "LEAVE_HOME":
        leave_home_plan(home)
    elif plan_name == "MOVIE":
        movie_plan(home)
    else:
        print(f"Unknown plan: {plan_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python function.py <PLAN_NAME>")
        sys.exit(1)

    plan_name = sys.argv[1].upper()
    main(plan_name)