# Based on your functional description of "开窗关空调" (Open the window and turn off the air conditioner), I will create a `function.py` file that implements the main functionality to open a window and turn off the air conditioning unit in your smart home.
# 
# Here's the content of the `function.py` file that you requested:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH

def control_window_and_ac(room_name):
    # Get the home plan
    home = home_plan()
    
    # Get the room based on the provided room name
    room = next((room for room in home if room.name == room_name), None)

    if room is None:
        print(f"Room '{room_name}' not found.")
        return

    # Get the window and AC actuators in the room
    window = next((actuator for actuator in room.actuators if isinstance(actuator, Window)), None)
    ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)

    # Open the window
    if window:
        window.turn_on()  # Assuming turning on the window means to open it
    else:
        print("No window actuator found in the room.")

    # Turn off the AC
    if ac:
        ac.turn_off()
    else:
        print("No AC actuator found in the room.")

def main():
    # Example usage
    room_name = "LivingRoom"  # Change this to your target room name
    control_window_and_ac(room_name)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation of the Code:
# - **Imports**: The `function.py` file imports necessary components from `home_plan` to access the home structure and actuators.
# - **`control_window_and_ac` Function**: This function takes a room name as an argument, retrieves the corresponding room from the home plan, and finds the window and AC actuators in that room. It then opens the window and turns off the AC.
# - **`main` Function**: The main function is provided as an entry point for the script. It specifies a room name (which can be changed) and calls the `control_window_and_ac` function with that room name.
# 
# You can place this `function.py` file in the `functions` folder of your project structure. This script is designed to be easily extendable and can be modified to suit any additional requirements you may have.