# Based on the functional description you provided, which is to turn off the lights in the bedroom, I will create the `function.py` file. This file will contain a main function that interacts with the existing classes to achieve this goal.
# 
# Here's the code for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Light

def turn_off_bedroom_lights():
    # Get the home plan (which includes rooms and their components)
    home = home_plan()
    
    # Locate the bedroom
    bedroom = next((room for room in home if room.name == "Bedroom"), None)
    
    if bedroom is not None:
        # Get all lights in the bedroom
        bedroom_lights = [actuator for actuator in bedroom.actuators if isinstance(actuator, Light)]
        
        if bedroom_lights:
            for light in bedroom_lights:
                light.turn_off()  # Turn off each light in the bedroom
        else:
            print("No lights found in the bedroom.")
    else:
        print("Bedroom not found in the home plan.")

def main():
    turn_off_bedroom_lights()

if __name__ == "__main__":
    main()