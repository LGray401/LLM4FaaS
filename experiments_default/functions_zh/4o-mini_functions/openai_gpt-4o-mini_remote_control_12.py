# Given your functional description "开窗户" (which translates to "open the window"), I will create a `function.py` file that utilizes the existing classes from your project to open a window in your smart home system. 
# 
# The main function will access the home plan, find the window actuator in a specific room, and then execute the command to open it.
# 
# Here's how your `function.py` file will look:
# 
# ### function.py

from home.home_plan import home_plan, get_all_actuators
from home.logger_config import logger

def open_window(room_name):
    # Get the home configuration
    home = home_plan()
    
    # Find the window actuators in the specified room
    window_actuators = get_all_actuators(home, "Window")
    
    # Filter for the specified room
    room_windows = [window for window in window_actuators if window.room_name == room_name]
    
    if room_windows:
        # Open the first found window actuator in the room
        window = room_windows[0]
        window.turn_on()  # Simulate the action of opening the window
        logger.info(f"Opened window {window.id} in {room_name}.")
        print(f"Opened window {window.id} in {room_name}.")
    else:
        logger.warning(f"No window found in {room_name}.")
        print(f"No window found in {room_name}.")

def main():
    # Example usage: open the window in the LivingRoom
    open_window("LivingRoom")

if __name__ == "__main__":
    main()