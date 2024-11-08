# Based on the content of the markdown file, you are working on a smart home project and you need a new Python file named `function.py` that should be located in the 'functions' folder. This file should contain a main function that turns off the bedroom light.
#
# Here is a simple implementation of the `function.py` file:
#
# ```python
from home.actuator import Light
from home.home_plan import home_plan, get_room, get_room_actuators

def main():
    # Get the current home plan
    home = home_plan()

    # Get the bedroom
    bedroom = get_room(home, "Bedroom")

    # If the bedroom exists
    if bedroom:
        # Get all the actuators in the bedroom
        bedroom_actuators = get_room_actuators(home, "Bedroom")

        # If there are actuators in the bedroom
        if bedroom_actuators:
            # Loop through each actuator
            for actuator in bedroom_actuators:
                # If the actuator is a Light
                if isinstance(actuator, Light):
                    # Turn off the light
                    actuator.turn_off()

if __name__ == "__main__":
    main()
# ```
#
# This script first retrieves the current home plan, then it finds the bedroom and all the actuators in the bedroom. It loops through each actuator and if the actuator is a Light, it turns off the light.