# Based on your functional description and the provided source code for your smart home project, I will create a `function.py` file that includes a main function to control the devices (turn on, turn off, brighten, and dim). This function will allow you to adjust specific actuators in your smart home system.
# 
# Here's the `function.py` code:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light

def adjust_device(room_name, device_name, action, brightness_level=None):
    """
    Adjust a specific device in the specified room.
    
    :param room_name: Name of the room where the device is located
    :param device_name: Name of the device (actuator)
    :param action: Action to perform (turn_on, turn_off, brighten, dim)
    :param brightness_level: Level to set for brightness (only applicable for brightening/dimming)
    """
    home = home_plan()
    room = get_room(home, room_name)
    
    if room is None:
        print(f"Room '{room_name}' not found.")
        return

    actuators = get_room_actuators(home, room_name)

    device = None
    for actuator in actuators:
        if actuator.actuator_type.lower() == device_name.lower():
            device = actuator
            break

    if device is None:
        print(f"Device '{device_name}' not found in room '{room_name}'.")
        return

    if action == "turn_on":
        device.turn_on()
    elif action == "turn_off":
        device.turn_off()
    elif action == "brighten":
        if isinstance(device, Light) and brightness_level:
            device.set_brightness_level(brightness_level)
            print(f"Brightened '{device_name}' in '{room_name}' to '{brightness_level}'.")
        else:
            print(f"Cannot brighten '{device_name}'. Make sure it's a Light and provide a brightness level.")
    elif action == "dim":
        if isinstance(device, Light) and brightness_level:
            # Assuming you have predefined levels
            brightness_levels = {
                "low": "low",
                "medium": "medium",
                "high": "high"
            }
            if brightness_level in brightness_levels:
                device.set_brightness_level(brightness_levels[brightness_level])
                print(f"DIMMED '{device_name}' in '{room_name}' to '{brightness_level}'.")
            else:
                print(f"Invalid brightness level '{brightness_level}'. Use one of: {', '.join(brightness_levels.keys())}.")
        else:
            print(f"Cannot dim '{device_name}'. Make sure it's a Light and provide a brightness level.")
    else:
        print(f"Invalid action '{action}'. Available actions: turn_on, turn_off, brighten, dim.")

def main():
    # Example usage
    adjust_device("LivingRoom", "Light", "turn_on")
    adjust_device("LivingRoom", "Light", "brighten", "high")
    adjust_device("LivingRoom", "Light", "dim", "low")
    adjust_device("LivingRoom", "Light", "turn_off")

if __name__ == "__main__":
    main()