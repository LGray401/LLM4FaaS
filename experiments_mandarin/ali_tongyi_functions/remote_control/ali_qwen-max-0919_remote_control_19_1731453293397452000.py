# Based on your functional description and the provided source code, I will create a `function.py` file that contains a main function to open the living room's air conditioner (AC) and set it to 26 degrees Celsius. This file will be placed in the `functions` folder.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import AC
from home.config import TEMP_CHANGE_DURATION_WINDOW

def main():
    # Create the home plan
    home = home_plan()

    # Get the actuators for the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Find the AC in the LivingRoom
    ac = None
    for actuator in living_room_actuators:
        if isinstance(actuator, AC):
            ac = actuator
            break

    if ac is None:
        print("No AC found in the LivingRoom.")
        return

    # Set the target temperature to 26 degrees Celsius
    ac.set_target_temperature(26)

    # Turn on the AC
    ac.turn_on()

    # Simulate the time it takes for the temperature to change
    import time
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    # Check the status of the AC
    ac.get_status()

if __name__ == "__main__":
    main()