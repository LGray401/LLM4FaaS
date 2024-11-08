# Based on your functional description, it seems you want to create a function that can adjust (turn on, turn off, brighten, dim) a specific device within a smart home setup. Since the other components are already defined in the provided source code, I will create a `function.py` file within the `functions` folder to handle these adjustments.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators

def main(operation, device_type, room_name=None, brightness_level=None):
    home = home_plan()
    
    # Fetch the actuators from the home plan
    if room_name:
        actuators = get_room_actuators(home, room_name)
    else:
        actuators = get_all_actuators(home, device_type)
    
    if not actuators:
        print(f"No actuators found for device type: {device_type} in room: {room_name}")
        return
    
    for actuator in actuators:
        if actuator.actuator_type == device_type:
            if operation == "turn_on":
                actuator.turn_on()
            elif operation == "turn_off":
                actuator.turn_off()
            elif operation == "brighten" and device_type == "Light":
                actuator.set_brightness_level(brightness_level)
            elif operation == "dim" and device_type == "Light":
                actuator.set_brightness_level(brightness_level)
            else:
                print(f"Invalid operation: {operation} for device type: {device_type}")
            break

if __name__ == "__main__":
    # Example usage
    import sys
    if len(sys.argv) < 3:
        print("Usage: function.py <operation> <device_type> [room_name] [brightness_level]")
    else:
        operation = sys.argv[1]
        device_type = sys.argv[2]
        room_name = sys.argv[3] if len(sys.argv) > 3 else None
        brightness_level = sys.argv[4] if len(sys.argv) > 4 else None
        main(operation, device_type, room_name, brightness_level)