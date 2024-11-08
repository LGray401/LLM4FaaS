# Based on the content of the markdown file, you are working on a smart home project and you need a new Python file named `function.py` that should be located in the 'functions' folder. This file should contain a main function that implements the functionality of dimming the bedroom lights.
#
# To achieve this, you can create a function that interacts with the `Light` class in the `actuator.py` file. Specifically, you can use the `set_brightness_level` method of the `Light` class to dim the lights.
#
# Here is a simple implementation of the `function.py` file:
#
# ```python
from home.actuator import Light
from home.home_plan import get_room_actuators

def dim_bedroom_lights(home):
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    for actuator in bedroom_actuators:
        if isinstance(actuator, Light):
            actuator.set_brightness_level("low")

if __name__ == "__main__":
    from home.home_plan import home_plan
    home = home_plan()
    dim_bedroom_lights(home)
# ```
#
# In this code, we first get all the actuators in the bedroom. Then, we iterate over these actuators and check if they are instances of the `Light` class. If they are, we set their brightness level to "low", which effectively dims the lights.
#
# Please note that this code assumes that the `home` object, which represents the current state of the home, is available. If it's not, you'll need to create it before calling `dim_bedroom_lights`. The `home_plan` function from the `home_plan.py` file can be used to create this `home` object.