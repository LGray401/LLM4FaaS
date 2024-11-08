# Based on your functional description and the provided source code, I will create the `function.py` file that will turn off the lights in the bedroom. This file will include a main function that accesses the home plan, retrieves the bedroom's actuators, and specifically turns off the light.
# 
# Here's the content for `function.py`:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light

def main():
    # Create the home plan
    home = home_plan()
    
    # Get the bedroom
    bedroom = get_room(home, "Bedroom")
    
    if bedroom:
        # Get all actuators in the bedroom
        bedroom_actuators = get_room_actuators(home, "Bedroom")
        
        # Turn off the lights in the bedroom
        for actuator in bedroom_actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

if __name__ == "__main__":
    main()