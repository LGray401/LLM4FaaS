# Based on your functional description and the provided source code, I will create a `function.py` file that will contain a main function. This function will turn off the lights in the bedroom as you requested. 
# 
# Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Light

def turn_off_bedroom_lights():
    # Get the home plan
    home = home_plan()
    
    # Find the bedroom
    bedroom = next((room for room in home if room.name == "Bedroom"), None)
    
    if bedroom is not None:
        # Get all light actuators in the bedroom
        lights = [actuator for actuator in bedroom.actuators if isinstance(actuator, Light)]
        
        # Turn off all lights
        for light in lights:
            light.turn_off()
    else:
        print("Bedroom not found.")

def main():
    turn_off_bedroom_lights()

if __name__ == "__main__":
    main()