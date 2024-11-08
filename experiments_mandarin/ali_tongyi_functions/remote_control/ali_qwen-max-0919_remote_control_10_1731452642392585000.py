# Based on the provided functional description and source code, you want to create a `function.py` file that contains a main function to open windows in a specified room. Here is the `function.py` file that you can place in the `functions` folder:

# functions/function.py

from home.home_plan import get_room_actuators, home_plan
from home.actuator import Window

def open_windows_in_room(room_name):
    """
    Open all windows in the specified room.
    
    :param room_name: The name of the room where the windows should be opened.
    """
    # Get the home plan
    home = home_plan()
    
    # Get all actuators in the specified room
    actuators = get_room_actuators(home, room_name)
    
    if actuators is None:
        print(f"No actuators found in {room_name}.")
        return
    
    # Find and open all windows in the room
    for actuator in actuators:
        if isinstance(actuator, Window):
            actuator.turn_on()
            print(f"Window {actuator.id} in {room_name} is now OPEN.")
        else:
            print(f"{actuator.id} is not a window, skipping...")

def main():
    # Example usage: Open all windows in the "LivingRoom"
    room_name = "LivingRoom"
    open_windows_in_room(room_name)

if __name__ == "__main__":
    main()