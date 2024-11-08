# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to turn on the lights in the living room when prompted. Below is the implementation:
# 
# ### function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    
    if living_room:
        # Get all light actuators in the living room
        lights = [actuator for actuator in get_room_actuators(home, "LivingRoom") if actuator.actuator_type == "Light"]
        
        # Turn on all the lights
        for light in lights:
            light.turn_on()
    else:
        print("Living room not found in the home plan.")

if __name__ == "__main__":
    main()