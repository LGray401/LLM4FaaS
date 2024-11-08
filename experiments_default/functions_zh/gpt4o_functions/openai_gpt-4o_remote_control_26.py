# Given the functional description and the source code provided, I'll create a `function.py` file that will include a main function to help adjust (turn on, turn off, increase brightness, decrease brightness) the devices in your smart home.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators, get_all_actuators
from home.actuator import Light

def adjust_device(action, device_type, room_name=None, level=None):
    home = home_plan()
    devices = []

    # Get devices from a specific room or all devices of a type
    if room_name:
        devices = get_room_actuators(home, room_name)
    else:
        devices = get_all_actuators(home, device_type)

    # Filter devices by type
    target_devices = [device for device in devices if device.actuator_type == device_type]

    for device in target_devices:
        if action == "turn_on":
            device.turn_on()
        elif action == "turn_off":
            device.turn_off()
        elif action == "increase_brightness" and isinstance(device, Light):
            if level:
                device.set_brightness_level(level)
            else:
                print("Please provide a brightness level (low, medium, high).")
        elif action == "decrease_brightness" and isinstance(device, Light):
            if level:
                device.set_brightness_level(level)
            else:
                print("Please provide a brightness level (low, medium, high).")
        else:
            print(f"Action {action} is not supported for device type {device_type}.")


if __name__ == "__main__":
    # Example usage
    adjust_device(action="turn_on", device_type="Light", room_name="LivingRoom")
    adjust_device(action="turn_off", device_type="Light", room_name="LivingRoom")
    adjust_device(action="increase_brightness", device_type="Light", room_name="LivingRoom", level="high")
    adjust_device(action="decrease_brightness", device_type="Light", room_name="LivingRoom", level="low")