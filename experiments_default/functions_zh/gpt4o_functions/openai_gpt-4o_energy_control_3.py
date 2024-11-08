# Based on the functional description "开窗关空调" (which translates to "Open window and turn off air conditioner") and the provided source codes, I will create a `function.py` file that will implement the main function to achieve this functionality.
# 
# To achieve this, the main function will:
# 1. Open the window in a specified room.
# 2. Turn off the air conditioner (AC) in the specified room.
# 
# Here's the `function.py` that implements this:
# 
# ## function.py

import time
from home.home_plan import home_plan, get_room_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW

def open_window_turn_off_ac(room_name):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    
    if not actuators:
        print(f"No actuators found in {room_name}.")
        return
    
    window_opened = False
    ac_turned_off = False

    for actuator in actuators:
        if actuator.actuator_type == "Window" and not window_opened:
            actuator.turn_on()
            window_opened = True
            print(f"Opened window in {room_name}.")
        
        if actuator.actuator_type == "AC" and not ac_turned_off:
            actuator.turn_off()
            ac_turned_off = True
            print(f"Turned off AC in {room_name}.")
        
        if window_opened and ac_turned_off:
            break
    
    if not window_opened:
        print(f"No window actuator found in {room_name}.")
    if not ac_turned_off:
        print(f"No AC actuator found in {room_name}.")
    
    # Wait for the duration specified in the config
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    room_name = "LivingRoom"  # Example room name
    open_window_turn_off_ac(room_name)