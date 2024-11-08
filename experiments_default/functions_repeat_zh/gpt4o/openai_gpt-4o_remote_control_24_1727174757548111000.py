# Given your functional description and the provided source code, I'll create the `function.py` file to turn off the bedroom's lights. 
# 
# The main function will locate the bedroom in the home plan and turn off all lights in that room. Below is the `function.py` file:
# 
# ### `functions/function.py`

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light


def turn_off_bedroom_lights():
    # Load the home plan
    home = home_plan()

    # Get the Bedroom
    bedroom = get_room(home, "Bedroom")
    if not bedroom:
        print("Bedroom not found in the home plan.")
        return

    # Get all actuators in the Bedroom
    actuators = get_room_actuators(home, "Bedroom")
    if not actuators:
        print("No actuators found in the Bedroom.")
        return

    # Turn off all lights in the Bedroom
    for actuator in actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()


if __name__ == "__main__":
    turn_off_bedroom_lights()