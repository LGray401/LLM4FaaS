# Based on your functional description and the provided source code, I will create a `function.py` file that contains a main function to adjust (turn on, turn off, brighten, dim) specific devices. This script will be placed in the `functions` folder.
# 
# Here's the `function.py`:

# functions/function.py

from home.sensor import *
from home.actuator import *
from home.home_plan import *

def find_device_by_id(devices, device_id):
    for device in devices:
        if device.id == device_id:
            return device
    return None

def adjust_device(home, device_id, action, *args):
    room = get_room(home, "LivingRoom")  # Assuming we are working with the LivingRoom, you can modify this as needed
    if not room:
        print(f"Room not found.")
        return

    # Find the device by ID
    device = find_device_by_id(room.sensors + room.actuators, device_id)
    if not device:
        print(f"Device with ID {device_id} not found.")
        return

    if action == "turn_on":
        device.turn_on()
    elif action == "turn_off":
        device.turn_off()
    elif action == "set_brightness_level" and isinstance(device, Light):
        if len(args) != 1:
            print("Usage: set_brightness_level <level>")
            return
        level = args[0]
        device.set_brightness_level(level)
    elif action == "adjust_temperature" and (isinstance(device, Heater) or isinstance(device, AC)):
        if len(args) != 1:
            print("Usage: adjust_temperature <target_temperature>")
            return
        target_temperature = args[0]
        device.set_target_temperature(target_temperature)
        current_temperature = random.uniform(TEMP_LOW, TEMP_HIGH)  # Simulate current temperature
        device.adjust_temperature(current_temperature)
    else:
        print(f"Unsupported action: {action}")

def main():
    # Create the home plan
    home = home_plan()

    # Example usage
    # Adjust a light in the LivingRoom
    light_id = "/Actuator/Light/LivingRoom/1"
    adjust_device(home, light_id, "turn_on")
    adjust_device(home, light_id, "set_brightness_level", "high")
    adjust_device(home, light_id, "turn_off")

    # Adjust an AC in the LivingRoom
    ac_id = "/Actuator/AC/LivingRoom/1"
    adjust_device(home, ac_id, "turn_on")
    adjust_device(home, ac_id, "adjust_temperature", 22)

if __name__ == "__main__":
    main()