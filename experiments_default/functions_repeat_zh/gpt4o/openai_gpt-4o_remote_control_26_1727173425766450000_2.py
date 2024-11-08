# Based on the functional description and the provided source code files, I will create the `function.py` file to be located in the `functions` folder. This file will contain a main function that can adjust (turn on, turn off, brighten, dim) specific devices within the smart home system.
# 
# Here is the code for `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light, Heater, AC, Humidifier

def main():
    home = home_plan()

    # Example to demonstrate controlling a specific device
    room_name = "LivingRoom"
    device_type = "Light"
    action = "turn_on"
    level_name = "high"  # used only for brightness adjustment

    # Get actuators in the specified room
    actuators = get_room_actuators(home, room_name)

    if not actuators:
        print(f"No actuators found in room: {room_name}")
        return

    # Find the device of the specified type and perform the action
    for actuator in actuators:
        if actuator.actuator_type == device_type:
            if action == "turn_on":
                actuator.turn_on()
            elif action == "turn_off":
                actuator.turn_off()
            elif action == "brighten" and isinstance(actuator, Light):
                actuator.set_brightness_level(level_name)
            elif action == "dim" and isinstance(actuator, Light):
                actuator.set_brightness_level(level_name)
            else:
                print(f"Unknown action or device type: {action} for {device_type}")
            break
    else:
        print(f"No {device_type} found in room: {room_name}")

if __name__ == "__main__":
    main()