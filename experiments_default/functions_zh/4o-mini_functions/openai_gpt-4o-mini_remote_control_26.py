# Based on your functional description and the provided source code, I will create a `function.py` file that implements a main function to adjust (turn on, turn off, brighten, or dim) a specific device in your smart home system.
# 
# Here is the `function.py` implementation:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light

def adjust_device(room_name, device_name, action, brightness_level=None):
    # Retrieve the home plan
    home = home_plan()
    
    # Get the specified room
    room = get_room(home, room_name)
    if not room:
        print(f"Room '{room_name}' not found.")
        return
    
    # Get actuators in the room
    actuators = get_room_actuators(home, room_name)
    if not actuators:
        print(f"No actuators found in room '{room_name}'.")
        return
    
    # Find the specified device
    device = None
    for actuator in actuators:
        if actuator.actuator_type == device_name:
            device = actuator
            break
    
    if not device:
        print(f"Device '{device_name}' not found in room '{room_name}'.")
        return
    
    # Perform the specified action
    if action.lower() == '开':
        device.turn_on()
    elif action.lower() == '关':
        device.turn_off()
    elif action.lower() == '调亮':
        if isinstance(device, Light) and brightness_level:
            device.set_brightness_level(brightness_level)
        else:
            print(f"Device '{device_name}' does not support brightness adjustment or brightness level not specified.")
    elif action.lower() == '调暗':
        if isinstance(device, Light) and brightness_level:
            # Assuming '调暗' means to set a lower brightness level
            if brightness_level in device.brightness_levels:
                current_level_index = list(device.brightness_levels.keys()).index(brightness_level)
                if current_level_index > 0:
                    new_level = list(device.brightness_levels.keys())[current_level_index - 1]
                    device.set_brightness_level(new_level)
                else:
                    print(f"Cannot dim the light further, already at lowest level.")
            else:
                print(f"Invalid brightness level for dimming: {brightness_level}.")
        else:
            print(f"Device '{device_name}' does not support brightness adjustment or brightness level not specified.")
    else:
        print(f"Unknown action: {action}. Please use '开', '关', '调亮', or '调暗'.")

def main():
    # Example usage
    adjust_device("LivingRoom", "Light", "调亮", "medium")
    adjust_device("LivingRoom", "Light", "关")
    adjust_device("Bedroom", "Light", "开")
    adjust_device("Bedroom", "Light", "调暗", "high")

if __name__ == "__main__":
    main()