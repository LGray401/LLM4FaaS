# Based on the provided functional description and source code, the `function.py` file will contain a main function that allows you to adjust (turn on, turn off, brighten, and dim) various devices in a smart home. The function will interact with the classes and methods defined in your existing code files.
# 
# Below is the `function.py` file:
# 
# ### function.py

import sys
from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light, SmartTV, MusicPlayer, CoffeeMachine, Heater, AC, CleaningRobot

def adjust_device(room_name, device_type, action, level=None):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    
    if not actuators:
        print(f"No actuators found in room: {room_name}")
        return

    device = None
    for actuator in actuators:
        if actuator.actuator_type == device_type:
            device = actuator
            break

    if not device:
        print(f"No device of type {device_type} found in room: {room_name}")
        return
    
    if action == "turn_on":
        device.turn_on()
    elif action == "turn_off":
        device.turn_off()
    elif action == "brighten" and isinstance(device, Light):
        if not level:
            print("Please provide a brightness level (low, medium, high).")
        else:
            device.set_brightness_level(level)
    elif action == "dim" and isinstance(device, Light):
        device.turn_off()  # Assuming dim means turn off for simplicity
    elif action == "set_temperature" and isinstance(device, (Heater, AC)):
        if not level:
            print("Please provide a target temperature.")
        else:
            device.set_target_temperature(level)
    else:
        print(f"Action {action} is not supported for device type {device_type} or device type mismatch.")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python function.py <room_name> <device_type> <action> [<level>]")
    else:
        room_name = sys.argv[1]
        device_type = sys.argv[2]
        action = sys.argv[3]
        level = sys.argv[4] if len(sys.argv) > 4 else None
        adjust_device(room_name, device_type, action, level)