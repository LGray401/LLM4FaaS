# Based on your functional description and the provided source code, I will create a `function.py` file that allows you to control the actuators in your smart home project. The functions will enable you to turn on, turn off, brighten, and dim specific devices.
# 
# Here is the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators, get_room
from home.actuator import Light

def adjust_device(room_name, device_name, action, brightness_level=None):
    """
    Adjust a device in the specified room.
    
    :param room_name: Name of the room.
    :param device_name: Name of the device to be adjusted.
    :param action: Action to perform on the device ('on', 'off', 'brighten', 'dim').
    :param brightness_level: Brightness level to set (only for 'brighten' or 'dim').
    """
    home = home_plan()
    room = get_room(home, room_name)
    
    if room is None:
        print(f"Room '{room_name}' not found.")
        return
    
    actuators = get_room_actuators(home, room_name)

    if actuators is None:
        print(f"No actuators found in '{room_name}'.")
        return

    device = None
    for actuator in actuators:
        if actuator.actuator_type.lower() == device_name.lower():
            device = actuator
            break

    if device is None:
        print(f"Device '{device_name}' not found in '{room_name}'.")
        return
    
    if action == 'on':
        device.turn_on()
    elif action == 'off':
        device.turn_off()
    elif action == 'brighten':
        if isinstance(device, Light) and brightness_level in device.brightness_levels:
            device.set_brightness_level(brightness_level)
        else:
            print(f"Invalid brightness level '{brightness_level}' or device is not a Light.")
    elif action == 'dim':
        if isinstance(device, Light):
            # Assuming dimming means setting to a lower brightness level
            levels = list(device.brightness_levels.keys())
            current_level = device.brightness_level

            if current_level > 0:
                current_index = levels.index(current_level)
                if current_index < len(levels) - 1:
                    new_level = levels[current_index + 1]
                    device.set_brightness_level(new_level)
                else:
                    print("Already at the lowest brightness level.")
            else:
                print("Light is off. Please turn it on first.")
        else:
            print("Device is not a Light.")
    else:
        print(f"Unknown action '{action}'.")

def main():
    # Example usage
    adjust_device("LivingRoom", "Light", "on")
    adjust_device("LivingRoom", "Light", "brighten", "high")
    adjust_device("LivingRoom", "Light", "dim")
    adjust_device("LivingRoom", "Light", "off")

if __name__ == "__main__":
    main()