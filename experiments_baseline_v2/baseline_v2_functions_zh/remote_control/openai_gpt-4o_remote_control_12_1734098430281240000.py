# To implement the functional description "开窗户" (which translates to "Open the window" in English), you need to create a simple Python script that will interact with your existing code to open a window in a specified room. We'll leverage the classes and functions defined in `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 
# Let's create a new Python script called `open_window.py` that will open a window in a specified room if it exists.
# 
# ### `open_window.py`
# ```python
from home.home_plan import home_plan, get_room_actuators
from home.actuator import Window

def open_window_in_room(room_name):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    
    if actuators is None:
        print(f"No actuators found in {room_name}.")
        return

    window_found = False
    for actuator in actuators:
        if isinstance(actuator, Window):
            actuator.turn_on()  # Assuming turning on the window means opening it
            window_found = True
            break  # Open the first window found in the room

    if not window_found:
        print(f"No window actuator found in {room_name}.")

if __name__ == "__main__":
    room_name = input("Enter the room name where you want to open the window: ")
    open_window_in_room(room_name)
# ```
# 
# ### Explanation
# - The script imports necessary functions and classes from your existing modules.
# - It defines a function `open_window_in_room` that takes a `room_name` as an argument.
# - It retrieves the actuators for the specified room using `get_room_actuators`.
# - It iterates through the actuators to find a `Window` actuator, and if found, it calls `turn_on()` to open the window.
# - If no window is found, it prints a message indicating that.
# 
# ### Running the Application
# To run this script in a Linux terminal, you can use the following command:
# 
# ```bash
# python3 open_window.py
# ```
# 
# This will execute the script, prompt you to enter the room name, and then attempt to open a window in that room if one exists.
# 
# Make sure to place `open_window.py` in the same directory where your `home` folder (containing `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) is located, or adjust the import paths accordingly if your directory structure is different.