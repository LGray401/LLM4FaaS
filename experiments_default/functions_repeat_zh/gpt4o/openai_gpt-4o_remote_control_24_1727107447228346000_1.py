# Based on your description and the provided source code files, I will create a `function.py` file in the `functions` folder. This file will contain a main function that will turn off the lights in the bedroom.
# 
# Here's the content for `functions/function.py`:

import sys
import os

# To import from the home directory, we need to add the home directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../home')))

from home_plan import home_plan, get_room_actuators

def main():
    home = home_plan()
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    
    if bedroom_actuators is not None:
        for actuator in bedroom_actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
                print(f"Turned off light with ID: {actuator.id}")
    else:
        print("No actuators found in the bedroom.")

if __name__ == "__main__":
    main()