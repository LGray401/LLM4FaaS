# Based on your functional description and the provided source code, I will create a `function.py` file that contains a main function to close the air conditioner (AC) in a specified room. The `function.py` file will be placed in the `functions` folder.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import get_room_actuators, home_plan

def main(room_name):
    # Initialize the home plan
    home = home_plan()
    
    # Get the actuators in the specified room
    actuators = get_room_actuators(home, room_name)
    
    if not actuators:
        print(f"No actuators found in {room_name}.")
        return
    
    # Find the AC actuator in the room
    ac = None
    for actuator in actuators:
        if actuator.actuator_type == "AC":
            ac = actuator
            break
    
    if ac:
        # Turn off the AC
        ac.turn_off()
        print(f"AC in {room_name} has been turned off.")
    else:
        print(f"No AC found in {room_name}.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m functions.function <room_name>")
    else:
        room_name = sys.argv[1]
        main(room_name)