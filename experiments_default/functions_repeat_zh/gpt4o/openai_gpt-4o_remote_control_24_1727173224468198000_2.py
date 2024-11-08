# Based on your functional description and the provided source code, I will create a `function.py` file in the `functions` folder. This file will contain the main function to turn off the lights in the bedroom.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    # Create the home plan
    home = home_plan()
    
    # Get the actuators in the bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    
    if bedroom_actuators is not None:
        # Turn off all lights in the bedroom
        for actuator in bedroom_actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
    else:
        print("No actuators found in the Bedroom.")

if __name__ == "__main__":
    main()