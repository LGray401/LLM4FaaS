# To implement the "开窗户" (open the window) functionality, we need to create a `function.py` file that will contain the main function to open the window in a specific room. The main function will utilize the `Window` actuator from the `actuator.py` file and interact with the home plan and configurations defined in the other provided files.
# 
# Here is the `function.py` file:

# function.py
import sys
sys.path.append('..')  # Ensure the home directory is in the Python path

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Window

def open_window(room_name):
    # Create the home plan
    home = home_plan()
    
    # Get all actuators in the specified room
    actuators = get_room_actuators(home, room_name)
    
    if actuators is None:
        print(f"No actuators found in the room: {room_name}")
        return
    
    # Find and open the window
    for actuator in actuators:
        if isinstance(actuator, Window):
            actuator.turn_on()
            print(f"Window in {room_name} is now open.")
            return

    print(f"No window found in the room: {room_name}")

if __name__ == "__main__":
    room_name = 'LivingRoom'  # Example room name, you can change it as needed
    open_window(room_name)