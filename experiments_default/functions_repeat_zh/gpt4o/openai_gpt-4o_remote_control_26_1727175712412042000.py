# Based on the functional description and the provided source code, I will create a `function.py` file that will allow you to control (turn on, turn off, adjust brightness) the devices in your smart home project. The `function.py` file will utilize the classes and methods defined in `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 
# Here is the `function.py` file located in the `functions` folder:

# function.py
from home.home_plan import home_plan, get_room_actuators, get_room
import sys

def control_device(home, room_name, device_type, action, level=None):
    room = get_room(home, room_name)
    if not room:
        print(f"Room '{room_name}' not found.")
        return

    actuators = get_room_actuators(home, room_name)
    if not actuators:
        print(f"No actuators found in room '{room_name}'.")
        return

    for actuator in actuators:
        if actuator.actuator_type == device_type:
            if action == 'turn_on':
                actuator.turn_on()
            elif action == 'turn_off':
                actuator.turn_off()
            elif action == 'adjust_brightness':
                if hasattr(actuator, 'set_brightness_level') and level:
                    actuator.set_brightness_level(level)
                else:
                    print(f"Device '{device_type}' in room '{room_name}' does not support brightness adjustment or the level is not provided.")
            else:
                print(f"Invalid action '{action}'. Supported actions are 'turn_on', 'turn_off', 'adjust_brightness'.")
            return

    print(f"Device '{device_type}' not found in room '{room_name}'.")

def main():
    if len(sys.argv) < 5:
        print("Usage: python function.py <room_name> <device_type> <action> [<level>]")
        return

    room_name = sys.argv[1]
    device_type = sys.argv[2]
    action = sys.argv[3]
    level = sys.argv[4] if len(sys.argv) > 4 else None

    home = home_plan()
    control_device(home, room_name, device_type, action, level)

if __name__ == "__main__":
    main()