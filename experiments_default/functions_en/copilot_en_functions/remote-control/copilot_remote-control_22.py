# Based on the content of the markdown file, you are working on a smart home project and you need a `function.py` file. This file should contain a main function that performs the following tasks:
#
# - Turn on the lights in the living room, bedroom, and bathroom
# - Turn on the air conditioners in the living room and bedroom
# - Turn on the heater in the bathroom
# - Turn on the TV in the living room
#
# The `function.py` file should be located in the 'functions' folder. The four code files in your project, i.e., `sensor.py`, `actuator.py`, `home_plan.py` and `config.py`, are in the 'home' folder.
#
# Here is a suggestion for the `function.py` file:
#
# ```python
from home.actuator import Light, AC, Heater, SmartTV
from home.home_plan import home_plan, get_room, get_room_actuators

def main():
    home = home_plan()

    # Turn on the lights in the living room, bedroom, and bathroom
    for room_name in ["LivingRoom", "Bedroom", "Bathroom"]:
        room = get_room(home, room_name)
        for actuator in get_room_actuators(home, room_name):
            if isinstance(actuator, Light):
                actuator.turn_on()

    # Turn on the air conditioners in the living room and bedroom
    for room_name in ["LivingRoom", "Bedroom"]:
        room = get_room(home, room_name)
        for actuator in get_room_actuators(home, room_name):
            if isinstance(actuator, AC):
                actuator.turn_on()

    # Turn on the heater in the bathroom
    room = get_room(home, "Bathroom")
    for actuator in get_room_actuators(home, "Bathroom"):
        if isinstance(actuator, Heater):
            actuator.turn_on()

    # Turn on the TV in the living room
    room = get_room(home, "LivingRoom")
    for actuator in get_room_actuators(home, "LivingRoom"):
        if isinstance(actuator, SmartTV):
            actuator.turn_on()

if __name__ == "__main__":
    main()
# ```
#
# This script will turn on the lights, air conditioners, heater, and TV in the specified rooms. Please note that this script assumes that the `home_plan.py`, `actuator.py`, and `sensor.py` files are in the same directory as the `function.py` file. If they are not, you will need to adjust the import statements accordingly.