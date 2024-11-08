# Based on your functional description and the provided source code, I will create a `function.py` file that contains a main function to turn off the AC in a specified room. Here is the implementation:
# 
# ### function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import AC

def turn_off_ac(room_name):
    # Get the home plan
    home = home_plan()
    
    # Get the specified room
    room = get_room(home, room_name)
    
    if room is not None:
        # Get the actuators in the room
        actuators = get_room_actuators(home, room_name)
        
        if actuators is not None:
            # Iterate through the actuators to find the AC and turn it off
            for actuator in actuators:
                if isinstance(actuator, AC):
                    if actuator.status == "on":
                        actuator.turn_off()
                        print(f"AC in {room_name} has been turned off.")
                    else:
                        print(f"AC in {room_name} is already off.")
                    break
            else:
                print(f"No AC found in {room_name}.")
        else:
            print(f"No actuators found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")

if __name__ == "__main__":
    # Example usage: turn off the AC in the LivingRoom
    turn_off_ac("LivingRoom")