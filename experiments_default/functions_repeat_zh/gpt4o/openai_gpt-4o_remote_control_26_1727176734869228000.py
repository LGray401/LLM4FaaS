# Based on the provided functional description and the source code, I will create the `function.py` file which will be located in the `functions` folder. This file will contain the main function to adjust (turn on, turn off, adjust brightness up, adjust brightness down) a specified device.
# 
# Here's the `function.py`:

import sys
import os

# Adding the 'home' folder to the system path to import the modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'home'))

from home.home_plan import home_plan, get_all_actuators
from home.actuator import Light, Heater, AC, CoffeeMachine, CleaningRobot, Door

def main(device_name, action, value=None):
    home = home_plan()
    device_class = None

    # Mapping device name to the corresponding class
    device_mapping = {
        "Light": Light,
        "Heater": Heater,
        "AC": AC,
        "CoffeeMachine": CoffeeMachine,
        "CleaningRobot": CleaningRobot,
        "Door": Door,
    }

    # Check if the device is in the mapping
    if device_name in device_mapping:
        device_class = device_mapping[device_name]
    else:
        print(f"Unknown device: {device_name}")
        return

    # Get all actuators of the specified type
    devices = get_all_actuators(home, device_name)
    
    if not devices:
        print(f"No devices found of type {device_name}")
        return

    for device in devices:
        if action == "turn_on":
            device.turn_on()
        elif action == "turn_off":
            device.turn_off()
        elif action == "adjust_brightness":
            if isinstance(device, Light):
                if value in ["low", "medium", "high"]:
                    device.set_brightness_level(value)
                else:
                    print(f"Invalid brightness value: {value}")
            else:
                print(f"Device {device_name} does not support brightness adjustment.")
        else:
            print(f"Unknown action: {action}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python function.py <device_name> <action> [value]")
        sys.exit(1)

    device_name = sys.argv[1]
    action = sys.argv[2]
    value = sys.argv[3] if len(sys.argv) > 3 else None

    main(device_name, action, value)