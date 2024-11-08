# To create the `function.py` file that contains the main function to turn off the bedroom light according to your functional description "请把卧室的灯关了" (which translates to "Please turn off the bedroom light"), you can follow these steps:
# 
# 1. Import necessary modules and functions.
# 2. Create a function to turn off the bedroom light.
# 3. Implement the main function to execute the light off command.
# 
# Here's the `function.py` file:
# 
# ### `functions/function.py`

from home.home_plan import home_plan, get_room_actuators
from home.logger_config import logger

def turn_off_bedroom_light(home):
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    if bedroom_actuators:
        for actuator in bedroom_actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
                logger.info(f"Turned off light: {actuator.id}")
                print(f"Turned off light: {actuator.id}")
    else:
        print("No actuators found in the bedroom.")
        logger.warning("No actuators found in the bedroom.")

def main():
    home = home_plan()
    turn_off_bedroom_light(home)

if __name__ == "__main__":
    main()