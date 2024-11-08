# Let's create the `function.py` file based on the given functional description and source code files. This file will contain the main function that will implement the morning plan, leave home plan, and movie plan as described.
# 
# Here’s the `function.py` file:

# functions/function.py
from home.home_plan import home_plan, get_all_actuators
from home.config import LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def morning_plan(home):
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

def leave_home_plan(home):
    lamps = get_all_actuators(home, "Light")
    for lamp in lamps:
        lamp.turn_off()

def movie_plan(home):
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

def main():
    home = home_plan()

    print("Executing Morning Plan...")
    morning_plan(home)

    print("\nExecuting Leave Home Plan...")
    leave_home_plan(home)

    print("\nExecuting Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()