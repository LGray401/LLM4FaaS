# Based on the provided functional description and source code, here's a `function.py` file that includes a main function to adjust the status of a given device in a room:

# function.py
import sys

# Assuming that the home, sensor, and actuator modules are located in the 'home' and 'functions' directories
sys.path.append('home')
sys.path.append('functions')

from home_plan import home_plan
from sensor import Sensor
from actuator import Actuator

def adjust_device_status(room_name, device_type, action):
    home = home_plan()
    room = get_room(home, room_name)
    if room is None:
        print(f"Room '{room_name}' not found.")
        return

    if device_type == "light":
        device = get_device_by_type(room, "Light", action)
        if device:
            if action == "on":
                device.turn_on()
            elif action == "off":
                device.turn_off()
            elif action == "brighten":
                device.set_brightness_level("high")
            elif action == "dim":
                device.set_brightness_level("low")
            else:
                print("Invalid action for light. Use 'on', 'off', 'brighten', or 'dim'.")
    else:
        print(f"Device type '{device_type}' not supported.")

def get_device_by_type(room, device_type, action):
    for actuator in room.actuators:
        if actuator.actuator_type == device_type:
            if action in ["on", "off", "brighten", "dim"]:
                return actuator
    return None

def get_room(home, room_name):
    for room in home:
        if room.name == room_name:
            return room
    return None

def main():
    # Example usage:
    # Adjust the light in the living room to be on
    adjust_device_status("LivingRoom", "light", "on")

if __name__ == "__main__":
    main()