# Based on your functional description and the provided source code, I will create a `function.py` file that allows you to adjust (turn on, turn off, brighten, dim) a specified device in the smart home setup. Below is the content for `function.py`:

# function.py
from home.home_plan import home_plan, get_room_actuators
from home.logger_config import logger

def adjust_device(room_name, device_name, action, brightness_level=None):
    """
    Adjusts the specified device in the given room.

    :param room_name: The name of the room where the device is located.
    :param device_name: The name of the device to be adjusted (e.g., Light).
    :param action: The action to perform ('turn_on', 'turn_off', 'brighten', 'dim').
    :param brightness_level: The brightness level to set (only applicable if action is 'brighten' or 'dim').
    """
    home = home_plan()  # Initialize the home plan
    room = None

    # Get the room
    for r in home:
        if r.name.lower() == room_name.lower():
            room = r
            break

    if room is None:
        print(f"Room '{room_name}' not found.")
        logger.warning(f"Room '{room_name}' not found.")
        return

    # Get the actuators in the room
    actuators = get_room_actuators(home, room_name)

    # Find the specific device
    device = None
    for actuator in actuators:
        if actuator.actuator_type.lower() == device_name.lower():
            device = actuator
            break

    if device is None:
        print(f"Device '{device_name}' not found in '{room_name}'.")
        logger.warning(f"Device '{device_name}' not found in '{room_name}'.")
        return

    # Perform the action
    if action == "turn_on":
        device.turn_on()
    elif action == "turn_off":
        device.turn_off()
    elif action == "brighten":
        if isinstance(device, Light):
            if brightness_level:
                device.set_brightness_level(brightness_level)
            else:
                print("Brightness level must be specified when brightening the light.")
                logger.warning("Brightness level must be specified when brightening the light.")
        else:
            print(f"Device '{device_name}' does not support brightening.")
            logger.warning(f"Device '{device_name}' does not support brightening.")
    elif action == "dim":
        if isinstance(device, Light):
            if brightness_level:
                device.set_brightness_level(brightness_level)
            else:
                print("Brightness level must be specified when dimming the light.")
                logger.warning("Brightness level must be specified when dimming the light.")
        else:
            print(f"Device '{device_name}' does not support dimming.")
            logger.warning(f"Device '{device_name}' does not support dimming.")
    else:
        print(f"Invalid action '{action}'. Available actions are: turn_on, turn_off, brighten, dim.")
        logger.warning(f"Invalid action '{action}'. Available actions are: turn_on, turn_off, brighten, dim.")

def main():
    # Example usage
    adjust_device("LivingRoom", "Light", "turn_on")
    adjust_device("LivingRoom", "Light", "brighten", brightness_level="high")
    adjust_device("LivingRoom", "Light", "dim", brightness_level="low")
    adjust_device("LivingRoom", "Light", "turn_off")

if __name__ == "__main__":
    main()