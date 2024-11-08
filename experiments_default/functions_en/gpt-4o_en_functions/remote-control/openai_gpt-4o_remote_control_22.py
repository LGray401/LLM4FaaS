# Based on the functional description and provided source code files, here's how you can create the `function.py` file to achieve the required functionality. The `function.py` will contain a main function that turns on the lights in the living room, bedroom, and bathroom, the air conditioners in the living room and bedroom, the heater in the bathroom, and the TV in the living room.
# 
# The `function.py` will be located in the `functions` folder, and it will use the classes and functions from the provided source code files in the `home` folder.
# 
# ### `functions/function.py`

import sys
sys.path.append('..')  # to import modules from the parent directory

from home.home_plan import home_plan, get_room_actuators
from home.logger_config import logger

def main():
    home = home_plan()
    
    # Define the rooms and the actuators we need to turn on
    actions = {
        "LivingRoom": ["Light", "AC", "SmartTV"],
        "Bedroom": ["Light", "AC"],
        "Bathroom": ["Light", "Heater"]
    }

    for room_name, actuator_types in actions.items():
        actuators = get_room_actuators(home, room_name)
        if actuators is not None:
            for actuator in actuators:
                if actuator.actuator_type in actuator_types:
                    actuator.turn_on()
        else:
            logger.warning(f"No actuators found in {room_name}")

if __name__ == "__main__":
    main()