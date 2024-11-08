# Based on your functional description "请把卧室的灯关了" (Please turn off the lights in the bedroom), I will create a `function.py` file that will handle the functionality of turning off the lights in the bedroom.
# 
# Here's how your `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.logger_config import logger

def turn_off_bedroom_lights():
    # Get the home plan
    home = home_plan()
    
    # Find the bedroom room
    bedroom = next((room for room in home if room.name == "Bedroom"), None)
    
    if bedroom is None:
        logger.warning("Bedroom not found in the home plan.")
        print("Bedroom not found in the home plan.")
        return

    # Get all lights in the bedroom
    lights = [actuator for actuator in bedroom.actuators if actuator.actuator_type == "Light"]
    
    if not lights:
        logger.warning("No lights found in the bedroom.")
        print("No lights found in the bedroom.")
        return
    
    # Turn off all lights
    for light in lights:
        light.turn_off()

    logger.info("All lights in the bedroom have been turned off.")
    print("All lights in the bedroom have been turned off.")

def main():
    turn_off_bedroom_lights()

if __name__ == "__main__":
    main()