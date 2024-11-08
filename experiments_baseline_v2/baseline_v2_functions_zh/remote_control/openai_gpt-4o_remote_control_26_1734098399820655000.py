# To create a smart home application based on your functional description and the provided source code, we need to add a main control script that interprets commands to adjust devices. The functional description "请帮我调整（开、关、调亮、调暗）某某设备。" translates to "Please help me adjust (turn on, turn off, brighten, dim) a certain device."
# 
# Here's how we can implement this:
# 
# ### New Script: `smart_home.py`
# 
# ```python
import sys
from home.home_plan import home_plan, get_all_actuators
from home.actuator import Light

def adjust_device(action, device_type, room_name):
    home = home_plan()
    actuators = get_all_actuators(home, device_type)

    for actuator in actuators:
        if actuator.room_name == room_name:
            if action == "开":
                actuator.turn_on()
            elif action == "关":
                actuator.turn_off()
            elif action == "调亮" and isinstance(actuator, Light):
                actuator.set_brightness_level("high")
            elif action == "调暗" and isinstance(actuator, Light):
                actuator.set_brightness_level("low")
            else:
                print(f"Action '{action}' is not valid for {device_type} in {room_name}.")
            return

    print(f"No {device_type} found in {room_name}.")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python smart_home.py <action> <device_type> <room_name>")
        print("Example: python smart_home.py 开 Light LivingRoom")
    else:
        action = sys.argv[1]
        device_type = sys.argv[2]
        room_name = sys.argv[3]
        adjust_device(action, device_type, room_name)
# ```
# 
# ### Explanation
# 
# 1. **Importing Modules**: We import necessary functions and classes from the existing modules.
# 2. **Function `adjust_device`**:
#    - **Parameters**: It takes `action`, `device_type`, and `room_name`.
#    - **Logic**: It retrieves the home configuration and finds the specified device in the specified room to perform the action.
# 3. **Main Execution**:
#    - The script checks command-line arguments to determine the action, device type, and room name.
#    - It calls `adjust_device` with these arguments.
# 
# ### Running the Script
# 
# To run this script in a Linux terminal, use the following command:
# 
# ```bash
# python smart_home.py <action> <device_type> <room_name>
# ```
# 
# - Replace `<action>` with `开` (turn on), `关` (turn off), `调亮` (brighten), or `调暗` (dim).
# - Replace `<device_type>` with the type of device you want to control (e.g., `Light`).
# - Replace `<room_name>` with the name of the room (e.g., `LivingRoom`).
# 
# ### Example Command
# 
# ```bash
# python smart_home.py 开 Light LivingRoom
# ```
# 
# This command will turn on the light in the living room. Adjust the `<action>`, `<device_type>`, and `<room_name>` as needed for different operations and rooms.