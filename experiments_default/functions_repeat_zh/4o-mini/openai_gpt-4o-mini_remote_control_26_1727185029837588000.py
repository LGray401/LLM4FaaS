# Based on your functional description and the provided code files, I will create a `functions.py` file. This file will include a main function that handles the functionality to adjust (turn on, turn off, increase brightness, decrease brightness) devices based on user input.
# 
# Here's how the `functions.py` file will look:

# functions/functions.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def adjust_device(room_name, device_name, action, brightness_level=None):
    # Get the home plan
    home = home_plan()
    
    # Find the specified room
    room = next((r for r in home if r.name == room_name), None)
    
    if not room:
        print(f"Room '{room_name}' not found.")
        return

    # Get the actuators in the room
    actuators = get_room_actuators(home, room_name)
    
    # Find the specified device
    device = next((a for a in actuators if a.actuator_type == device_name), None)
    
    if not device:
        print(f"Device '{device_name}' not found in room '{room_name}'.")
        return

    # Perform the action
    if action == "open" or action == "turn on":
        device.turn_on()
        if isinstance(device, Light) and brightness_level:
            device.set_brightness_level(brightness_level)
    elif action == "close" or action == "turn off":
        device.turn_off()
    elif action == "brighten":
        if isinstance(device, Light):
            current_level = device.brightness_level
            if current_level < 90:  # assuming 90 is the max brightness
                device.set_brightness_level("high")  # adjust as needed
            else:
                print(f"{device.id} is already at maximum brightness.")
    elif action == "dim":
        if isinstance(device, Light):
            current_level = device.brightness_level
            if current_level > 0:  # assuming 0 is the minimum brightness
                device.set_brightness_level("low")  # adjust as needed
            else:
                print(f"{device.id} is already at minimum brightness.")
    else:
        print(f"Action '{action}' is not recognized.")

def main():
    # Example calls, you can modify these based on your needs
    adjust_device("LivingRoom", "Light", "turn on", "medium")
    adjust_device("LivingRoom", "Light", "brighten")
    adjust_device("LivingRoom", "Light", "dim")
    adjust_device("LivingRoom", "Light", "turn off")

if __name__ == "__main__":
    main()