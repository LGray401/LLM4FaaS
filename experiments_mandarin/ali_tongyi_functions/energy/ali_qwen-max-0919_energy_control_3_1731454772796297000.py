# Based on your functional description, you want to create a function that opens the window and turns off the air conditioner (AC) in a given room. I will provide you with the `function.py` file that contains the main function to achieve this. This function will locate the specified room, open the window, and turn off the AC.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import get_room_actuators, get_room
from home.actuator import Window, AC

def open_window_and_turn_off_ac(room_name):
    """
    Opens the window and turns off the AC in the specified room.
    
    :param room_name: The name of the room where the actions should be performed.
    """
    # Get the home plan
    home = home_plan()
    
    # Find the specified room
    room = get_room(home, room_name)
    if not room:
        print(f"Room '{room_name}' not found.")
        return
    
    # Get the actuators in the specified room
    actuators = get_room_actuators(home, room_name)
    
    # Find the window and AC in the room
    window = None
    ac = None
    for actuator in actuators:
        if isinstance(actuator, Window):
            window = actuator
        elif isinstance(actuator, AC):
            ac = actuator
    
    # Open the window
    if window:
        window.turn_on()
        print(f"Window in {room_name} is now open.")
    else:
        print(f"No window found in {room_name}.")
    
    # Turn off the AC
    if ac:
        ac.turn_off()
        print(f"AC in {room_name} is now off.")
    else:
        print(f"No AC found in {room_name}.")

if __name__ == "__main__":
    # Example usage
    open_window_and_turn_off_ac("LivingRoom")