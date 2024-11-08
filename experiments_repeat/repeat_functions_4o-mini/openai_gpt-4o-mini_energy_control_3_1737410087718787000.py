# Based on your functional description "开窗关空调" (which translates to "open the window and turn off the air conditioning"), I will create a `function.py` file that implements the necessary logic to interact with the `Window` and `AC` actuators in your smart home project.
# 
# Here's how the `function.py` file will look:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan
from home.actuator import Window, AC
from home.logger_config import logger

def open_window_and_turn_off_ac(room_name):
    # Get the home plan (the structure of rooms and their components)
    home = home_plan()
    
    # Find the specified room
    room = None
    for r in home:
        if r.name == room_name:
            room = r
            break

    if room is None:
        logger.warning(f"Room '{room_name}' not found in the home plan.")
        print(f"Room '{room_name}' not found.")
        return

    # Get the Window and AC actuators in the room
    window = next((actuator for actuator in room.actuators if isinstance(actuator, Window)), None)
    ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)

    if window:
        window.turn_on()  # Open the window
        logger.info(f"Opened the window in {room_name}.")
        print(f"Opened the window in {room_name}.")
    else:
        logger.warning(f"No window actuator found in {room_name}.")
        print(f"No window in {room_name}.")

    if ac:
        ac.turn_off()  # Turn off the AC
        logger.info(f"Turned off the AC in {room_name}.")
        print(f"Turned off the AC in {room_name}.")
    else:
        logger.warning(f"No AC actuator found in {room_name}.")
        print(f"No AC in {room_name}.")

def main():
    # Example usage
    room_name = "LivingRoom"  # Specify the room name here
    open_window_and_turn_off_ac(room_name)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation of the Code:
# 
# 1. **Imports**: The necessary classes and functions are imported from other modules in your project.
# 2. **Function `open_window_and_turn_off_ac`**: This function takes a room name as input, retrieves the room's details from the home plan, and checks for the presence of a window and an AC actuator in that room.
# 3. **Turning on the Window**: If a window actuator is found, it is turned on (opened).
# 4. **Turning off the AC**: If an AC actuator is found, it is turned off.
# 5. **Logging**: Logs are created for each action taken, and appropriate messages are printed to the console.
# 6. **Main Function**: The main function calls the `open_window_and_turn_off_ac` function with a specified room name.
# 
# Make sure to place this `function.py` file in the `functions` folder as specified. You can modify the `room_name` variable in the `main` function to specify which room you want to operate on.