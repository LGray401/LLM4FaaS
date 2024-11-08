# Based on the functional description and the provided source code, I will create a `function.py` file in the `functions` folder. This file will include a main function that allows you to control the devices (turn on, turn off, brighten, dim) in your smart home project.
# 
# Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.logger_config import logger

def adjust_device(room_name, device_type, action, brightness_level=None):
    """
    Adjust a device in the specified room.
    
    :param room_name: Name of the room where the device is located.
    :param device_type: Type of device (e.g., 'Light', 'Heater', etc.).
    :param action: Action to perform ('on', 'off', 'brighten', 'dim').
    :param brightness_level: Level to set brightness (only for lights).
    """
    home = home_plan()
    room = get_room(home, room_name)
    
    if room is None:
        print(f"Room '{room_name}' not found.")
        return
    
    actuators = get_room_actuators(home, room_name)
    device = next((actuator for actuator in actuators if actuator.actuator_type == device_type), None)

    if device is None:
        print(f"Device '{device_type}' not found in room '{room_name}'.")
        return
    
    if action == 'on':
        device.turn_on()
    elif action == 'off':
        device.turn_off()
    elif action == 'brighten':
        if isinstance(device, Light):
            if brightness_level is not None:
                device.set_brightness_level(brightness_level)
            else:
                print("Brightness level must be provided for brightening.")
        else:
            print(f"'{device_type}' in '{room_name}' cannot be brightened.")
    elif action == 'dim':
        if isinstance(device, Light):
            if brightness_level is not None:
                # Assuming you want to set to a lower level
                device.set_brightness_level(brightness_level)
            else:
                print("Brightness level must be provided for dimming.")
        else:
            print(f"'{device_type}' in '{room_name}' cannot be dimmed.")
    else:
        print(f"Action '{action}' is not recognized.")

def main():
    # Example usage
    adjust_device("LivingRoom", "Light", "on")
    adjust_device("LivingRoom", "Light", "brighten", "high")
    adjust_device("LivingRoom", "Light", "dim", "low")
    adjust_device("LivingRoom", "Light", "off")

if __name__ == "__main__":
    main()