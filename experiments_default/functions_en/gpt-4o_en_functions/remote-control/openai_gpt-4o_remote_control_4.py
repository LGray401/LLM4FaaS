# Based on the provided functional description and the source code, here is the `function.py` file that will turn off the lights in the living room. This file will be placed in the `functions` folder and will include the main function as required.
# 
# ### functions/function.py

import sys
import os

# Add the home directory to the sys.path to import modules from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'home')))

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def turn_off_lights_in_living_room():
    # Initialize the home plan
    home = home_plan()
    
    # Get all actuators in the living room
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    if not living_room_actuators:
        print("No actuators found in the living room.")
        return

    # Iterate through the actuators and turn off the lights
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

    print("All lights in the living room have been turned off.")

if __name__ == "__main__":
    turn_off_lights_in_living_room()