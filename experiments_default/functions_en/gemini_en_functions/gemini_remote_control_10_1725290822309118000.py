from home.home_plan import get_room, get_room_actuators
from home.actuator import Window
from home.logger_config import logger

def open_windows(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    windows = get_room_actuators(home, room_name, "Window")
    if windows is None:
        return

    for window in windows:
        window.turn_on()
        logger.info(f"Opening window {window.id} in {room_name}")
        print(f"Opening window {window.id} in {room_name}")

if __name__ == "__main__":
    # Example usage (replace with your actual home plan)
    home = home_plan()  # Assuming you have a function 'home_plan' to create your home layout
    open_windows(home, "LivingRoom")

# **Explanation:**

# 1. **Imports:**
#    - `get_room` and `get_room_actuators` are imported from `home.home_plan` to retrieve the specified room and its actuators.
#    - `Window` is imported from `home.actuator` to work with window objects.
#    - `logger` is imported for logging information.

# 2. **`open_windows` function:**
#    - Takes the `home` object (representing your smart home plan) and the `room_name` as input.
#    - Calls `get_room` to find the desired room based on the `room_name`.
#    - If the room is found:
#      - Calls `get_room_actuators` to retrieve all the windows in that room.
#      - Iterates through each window and calls `turn_on()` to open them. 
#      - Logs the action of opening each window.
#    - If the room or the windows are not found, the function returns without doing anything.

# 3. **Example Usage:**
#    - The `if __name__ == "__main__":` block provides a simple example of how to use the function. 
#    - Replace `home = home_plan()` with the actual code that creates your `home` object. 
#    - Call `open_windows(home, "LivingRoom")` to open the windows in the "LivingRoom".

# **To use this code in your project:**

# 1. **Place `function.py` in the `functions` folder.**
# 2. **Ensure your `home_plan` module (from `home.home_plan`) creates your home layout correctly.**
# 3. **Call the `open_windows` function from your main script or other functions to control the windows.**

# **Remember:** This code assumes you have a `home` object representing your smart home layout and that you have window actuators defined in your `home_plan` module. Adjust the code according to your specific project structure and object definitions.
