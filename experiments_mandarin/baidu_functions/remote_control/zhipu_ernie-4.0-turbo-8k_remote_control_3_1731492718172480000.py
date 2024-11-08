# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to turn off the lights in the living room. Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light

def turn_off_living_room_lights():
    # Get the home plan
    home = home_plan()
    
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    
    if living_room:
        # Get all actuators in the living room
        actuators = get_room_actuators(home, "LivingRoom")
        
        if actuators:
            # Turn off all lights in the living room
            for actuator in actuators:
                if isinstance(actuator, Light) and actuator.status == "on":
                    actuator.turn_off()
        else:
            print("No actuators found in the living room.")
    else:
        print("Living room not found in the home plan.")

if __name__ == "__main__":
    turn_off_living_room_lights()