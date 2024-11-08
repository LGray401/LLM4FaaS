# Based on your functional description and the provided source code, I will create a `function.py` file that contains a main function to turn off the lights in the bedroom. The main function will locate and control the actuators (lights) in the specified room.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def turn_off_lights_in_room(room_name):
    """
    Turn off all lights in the specified room.
    
    :param room_name: The name of the room where the lights should be turned off.
    """
    # Create the home plan
    home = home_plan()
    
    # Get all actuators in the specified room
    actuators = get_room_actuators(home, room_name)
    
    if actuators:
        for actuator in actuators:
            if isinstance(actuator, Light):
                if actuator.status == "on":
                    actuator.turn_off()
                else:
                    print(f"Light {actuator.id} is already OFF.")
    else:
        print(f"No actuators found in {room_name}.")

if __name__ == "__main__":
    # Turn off the lights in the bedroom
    turn_off_lights_in_room("Bedroom")