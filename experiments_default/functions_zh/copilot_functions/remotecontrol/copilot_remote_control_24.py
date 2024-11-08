# Based on the functional description and the provided source code, it seems like you want to turn off the light in the bedroom. Here is a Python function that you can add to your `function.py` file to achieve this:
#
# ```python
from home.actuator import Light
from home.home_plan import get_room_actuators

def turn_off_light_in_room(home, room_name):
    actuators = get_room_actuators(home, room_name)
    if actuators is not None:
        for actuator in actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
                return f"Turned off the light in {room_name}"
    return f"No light found in {room_name}"

# Usage:
# home = home_plan()  # Assuming home_plan is a function that initializes your home
# print(turn_off_light_in_room(home, "Bedroom"))
# ```
#
# This function takes in the `home` object and the name of the room as parameters. It retrieves all the actuators in the specified room and checks if any of them is a `Light`. If a `Light` is found, it turns it off. If no `Light` is found, it returns a message indicating that no light was found in the specified room.