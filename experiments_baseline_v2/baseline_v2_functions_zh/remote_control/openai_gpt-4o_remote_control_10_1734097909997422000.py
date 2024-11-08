# To create a smart home application in Python based on the provided functional description "打开窗户" (which translates to "Open the window"), we'll leverage the `Window` actuator class from the `actuator.py` file. We will create a simple command-line application that initializes a home plan, finds a specific room, and opens the window in that room.
# 
# Here is the code for the main application:
# 
# ```python
from home.home_plan import home_plan, get_room_actuators
from home.actuator import Window

def open_window(room_name):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)

    if actuators is not None:
        for actuator in actuators:
            if isinstance(actuator, Window):
                actuator.turn_on()
                print(f"Window in {room_name} is now open.")
                return
        print(f"No window actuator found in {room_name}.")
    else:
        print(f"Room '{room_name}' does not exist.")

if __name__ == "__main__":
    room_name_to_open = "LivingRoom"  # Specify the room name where you want to open the window
    open_window(room_name_to_open)
# ```
# 
# To run this application in a Linux terminal, you need to create a new Python file, e.g., `open_window.py`, and place the above code in it. Ensure that this file is in the same directory level as the `home` folder containing your reference code files. Then, execute the following command in your terminal:
# 
# ```bash
# python open_window.py
# ```
# 
# Make sure that your Python environment is properly set up and that all dependencies are installed. This script assumes that the `home_plan.py` file correctly sets up the home structure with rooms and actuators. Adjust the `room_name_to_open` variable to specify the room where you want to open the window.