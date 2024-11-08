# Based on the provided functional description and source code, I'll create a `function.py` file that will contain the main function to adjust (turn on, turn off, brighten, dim) a specified device in your smart home project. This main function will interact with the components defined in `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 
# Here's the `function.py` file:

import sys
from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def adjust_device(room_name, device_type, action, level=None):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    
    if not actuators:
        print(f"No actuators found in room: {room_name}")
        return
    
    for actuator in actuators:
        if actuator.actuator_type == device_type:
            if action == "turn on":
                actuator.turn_on()
            elif action == "turn off":
                actuator.turn_off()
            elif action == "brighten" and isinstance(actuator, Light):
                if level:
                    actuator.set_brightness_level(level)
                else:
                    actuator.set_brightness_level("high")
            elif action == "dim" and isinstance(actuator, Light):
                if level:
                    actuator.set_brightness_level(level)
                else:
                    actuator.set_brightness_level("low")
            else:
                print(f"Action '{action}' is not supported for device type '{device_type}'")
            return
    
    print(f"No device of type '{device_type}' found in room: {room_name}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python function.py <room_name> <device_type> <action> [level]")
        sys.exit(1)

    room_name = sys.argv[1]
    device_type = sys.argv[2]
    action = sys.argv[3]
    level = sys.argv[4] if len(sys.argv) > 4 else None

    adjust_device(room_name, device_type, action, level)