# Based on your functional description of turning on the lights, I will create the `function.py` file that includes a main function to handle this operation. The main function will interact with the existing classes in your project to find the appropriate light actuator and turn it on.
# 
# Here’s the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators
from home.logger_config import logger

def turn_on_lights():
    # Create a home plan
    home = home_plan()
    
    # Retrieve all light actuators in the home
    light_actuators = get_all_actuators(home, "Light")
    
    if not light_actuators:
        print("No light actuators found in the house.")
        logger.warning("No light actuators found in the house.")
        return
    
    # Turn on all light actuators found
    for light in light_actuators:
        light.turn_on()

if __name__ == "__main__":
    turn_on_lights()