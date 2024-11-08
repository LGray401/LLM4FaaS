# Based on your provided functional description and source code files, I will create a `function.py` file that turns on the lights in your smart home system. This function will utilize the classes and methods defined in your existing files.
# 
# Here is the content of `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators
from home.actuator import Light

def turn_on_all_lights(home):
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()

def main():
    # Create the home plan
    home = home_plan()
    
    # Turn on all the lights
    turn_on_all_lights(home)

if __name__ == "__main__":
    main()