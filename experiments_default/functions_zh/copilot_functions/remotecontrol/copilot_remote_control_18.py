# Based on the functional description and the provided source code, it seems like you want to create a function that turns on the light in a smart home system. The function should be located in a new file named `function.py` in the `functions` folder.
#
# Here is a simple function that turns on all the lights in the home:
#
# ```python
from home.actuator import Light
from home.home_plan import get_all_actuators

def turn_on_all_lights(home):
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_on()

if __name__ == "__main__":
    home = home_plan()  # Assuming home_plan() is a function that initializes your home
    turn_on_all_lights(home)
# ```
#
# This function retrieves all the light actuators in the home and turns them on. You can call this function to turn on all the lights in your smart home system. Please replace `home_plan()` with the actual function or method you use to initialize your home.