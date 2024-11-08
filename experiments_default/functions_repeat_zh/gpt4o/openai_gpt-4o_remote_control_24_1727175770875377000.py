# Based on the provided functional description and the source code, we need to create a `function.py` file that will contain the main function to turn off the lights in the bedroom. Here's how the `function.py` file should look:
# 
# ### functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    # Create the home plan
    home = home_plan()

    # Get the actuators in the bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")

    if not bedroom_actuators:
        print("No actuators found in the Bedroom.")
        return

    # Turn off all lights in the bedroom
    for actuator in bedroom_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()
            print(f"Turned off: {actuator.id}")

if __name__ == "__main__":
    main()