# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to turn off the lights in the bedroom. This file will be located in the `functions` folder.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light

def turn_off_bedroom_lights():
    # Get the home plan
    home = home_plan()
    
    # Get the bedroom
    bedroom = get_room(home, "Bedroom")
    
    if bedroom:
        # Get all lights in the bedroom
        actuators = get_room_actuators(home, "Bedroom")
        
        if actuators:
            for actuator in actuators:
                if isinstance(actuator, Light) and actuator.status == "on":
                    actuator.turn_off()
                    print(f"Light {actuator.id} in Bedroom is turned off.")
                elif isinstance(actuator, Light) and actuator.status == "off":
                    print(f"Light {actuator.id} in Bedroom is already off.")
        else:
            print("No actuators found in the Bedroom.")
    else:
        print("Bedroom not found in the home plan.")

if __name__ == "__main__":
    turn_off_bedroom_lights()