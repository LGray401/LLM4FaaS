# Based on the provided functional description and source code, we can create a `function.py` file in the `functions` folder to implement the functionality: "Please turn off the bedroom light."
# 
# Here's the `function.py` file:
# 
# ### function.py

import sys
sys.path.insert(0, '../home')
from home.home_plan import home_plan, get_room_actuators
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()

    # Get actuators in the Bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")

    if bedroom_actuators is None:
        print("No actuators found in the Bedroom.")
        return

    # Find and turn off the light in the Bedroom
    for actuator in bedroom_actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_off()

if __name__ == "__main__":
    main()