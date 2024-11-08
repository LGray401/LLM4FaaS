# Based on the content of the markdown file, it appears that you are working on a smart home project and you need a new Python file named `function.py` to be created in the 'functions' folder. This file should contain a main function that fulfills the functional description you provided, which is "关闭客厅的灯" (turn off the living room light).
#
# Given the source code you provided, it seems that the `Light` class in `actuator.py` has the method `turn_off()` which can be used to turn off the light. However, to create a function that turns off the light in the living room, we need to know how to identify the specific light actuator for the living room.
#
# Here is a simple implementation of the `function.py` file:
#
# ```python
from home.actuator import Light
from home.home_plan import get_room_actuators

def main():
    home = home_plan()  # Assuming home_plan() returns the current state of the home
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()
            break

if __name__ == "__main__":
    main()
# ```
#
# This script first retrieves all actuators in the living room. It then iterates over these actuators, and when it finds an instance of the `Light` class, it calls the `turn_off()` method on it. This should turn off the light in the living room. Please note that this script assumes that there is only one light in the living room. If there are multiple lights, you may need to adjust the script to turn off all of them or a specific one based on your requirements.