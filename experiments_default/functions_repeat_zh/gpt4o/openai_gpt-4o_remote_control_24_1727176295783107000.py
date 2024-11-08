# Based on the provided functional description and the source code files, I will create a `function.py` file that contains a main function to turn off the light in the bedroom. Here's how the `function.py` will look:

# function.py
from home.home_plan import home_plan, get_room_actuators
from home.logger_config import logger

def main():
    # Create the home plan
    home = home_plan()
    
    # Get all actuators in the bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    
    # Check if there are actuators in the bedroom
    if bedroom_actuators:
        # Iterate through the actuators to find the lights and turn them off
        for actuator in bedroom_actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
                print(f"Turned off {actuator.id}")
                logger.info(f"Turned off {actuator.id}")
    else:
        print("No actuators found in the bedroom.")
        logger.warning("No actuators found in the bedroom.")

if __name__ == "__main__":
    main()