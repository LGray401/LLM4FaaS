# Based on your functional description and the provided source code, I will create a `function.py` file located in the `functions` folder. This file will contain a main function that allows you to adjust (turn on, turn off, brighten, dim) various devices.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room_actuators

def adjust_device(home, room_name, device_type, action, brightness_level=None):
    actuators = get_room_actuators(home, room_name)
    
    if not actuators:
        print(f"No actuators found in room {room_name}.")
        return

    for actuator in actuators:
        if actuator.actuator_type == device_type:
            if action == "turn_on":
                actuator.turn_on()
            elif action == "turn_off":
                actuator.turn_off()
            elif action == "brighten" and device_type == "Light" and brightness_level:
                actuator.set_brightness_level(brightness_level)
            elif action == "dim" and device_type == "Light" and brightness_level:
                actuator.set_brightness_level(brightness_level)
            else:
                print(f"Invalid action: {action} for device type: {device_type}")
            break
    else:
        print(f"No {device_type} found in room {room_name}.")

def main():
    home = home_plan()
    
    # Adjust devices here as needed
    adjust_device(home, "LivingRoom", "Light", "turn_on")
    adjust_device(home, "LivingRoom", "Light", "brighten", "medium")
    adjust_device(home, "LivingRoom", "Light", "dim", "low")
    adjust_device(home, "LivingRoom", "Light", "turn_off")
    
if __name__ == "__main__":
    main()