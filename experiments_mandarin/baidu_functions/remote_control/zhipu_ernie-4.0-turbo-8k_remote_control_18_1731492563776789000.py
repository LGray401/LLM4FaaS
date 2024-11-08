# Based on your functional description and the provided source code, you want to create a `function.py` file that contains the main function to turn on a light in a specified room. Below is the Python code for the `function.py` file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light

def turn_on_light(room_name):
    # Get the home plan
    home = home_plan()
    
    # Get the specified room
    room = get_room(home, room_name)
    
    if room is not None:
        # Get all actuators in the room
        actuators = get_room_actuators(home, room_name)
        
        if actuators is not None:
            # Iterate through actuators to find the light and turn it on
            for actuator in actuators:
                if isinstance(actuator, Light) and actuator.status == "off":
                    actuator.turn_on()
                    print(f"Light {actuator.id} in {room_name} is now ON.")
                    return
        else:
            print(f"No actuators found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")

if __name__ == "__main__":
    # Example usage: turn on the light in the LivingRoom
    turn_on_light("LivingRoom")