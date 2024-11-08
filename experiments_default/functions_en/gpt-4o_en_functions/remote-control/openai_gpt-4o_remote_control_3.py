# Based on the provided functional description and source code, I will create the `function.py` file. The main function will turn off all the lights in the living room. Here is the code for `function.py`:

# function.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from home.home_plan import home_plan, get_room_actuators

def main():
    home = home_plan()
    
    # Get all actuators in the living room
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    if not living_room_actuators:
        print("No actuators found in Living Room.")
        return
    
    # Turn off all lights in the living room
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_off()

if __name__ == "__main__":
    main()