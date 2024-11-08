# Based on the provided functional description and the source code files, the `function.py` file will contain a main function that interacts with your smart home system to turn off the bedroom light. We'll utilize the `home_plan` function from `home_plan.py` to get the bedroom and then access its actuators to turn off the light.
# 
# Here's the implementation of `function.py`:

# function.py
from home.home_plan import home_plan
from home.actuator import Light

def main():
    # Get the home layout
    home = home_plan()
    
    # Find the bedroom
    bedroom = next((room for room in home if room.name == "Bedroom"), None)
    
    if bedroom:
        # Get all light actuators in the bedroom
        lights = [actuator for actuator in bedroom.actuators if isinstance(actuator, Light)]
        
        if lights:
            # Turn off all the lights in the bedroom
            for light in lights:
                light.turn_off()
        else:
            print("No light actuators found in the bedroom.")
    else:
        print("Bedroom not found in home.")

if __name__ == "__main__":
    main()