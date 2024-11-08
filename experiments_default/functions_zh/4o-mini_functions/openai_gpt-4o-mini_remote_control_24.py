# Based on your functional description of turning off the lights in the bedroom and the provided source code, I will create a `function.py` file that includes a main function to accomplish this task. 
# 
# The main function will involve locating the bedroom room, finding the light actuators associated with it, and then turning them off.
# 
# Here is the `function.py` code:

# function.py

from home.home_plan import home_plan, get_room, get_room_actuators

def turn_off_bedroom_lights():
    # Obtain the home structure
    home = home_plan()
    
    # Get the bedroom room
    bedroom = get_room(home, "Bedroom")
    
    if bedroom:
        # Get all light actuators in the bedroom
        lights = get_room_actuators(home, "Bedroom")
        
        # Turn off all lights found in the bedroom
        for light in lights:
            light.turn_off()
    else:
        print("Bedroom not found. Unable to turn off lights.")

if __name__ == "__main__":
    turn_off_bedroom_lights()