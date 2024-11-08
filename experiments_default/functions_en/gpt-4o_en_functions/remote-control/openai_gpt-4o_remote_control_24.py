# Based on the provided functional description and source code files, I will create the `function.py` file that turns off the bedroom light. The `function.py` file will be located in the `functions` folder and will contain a main function that accomplishes the required task.
# 
# Here's the `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.logger_config import logger


def main():
    home = home_plan()
    
    # Get actuators in the bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    
    if bedroom_actuators:
        for actuator in bedroom_actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
                logger.info(f"Turned off {actuator.id}")

if __name__ == "__main__":
    main()