# Based on your provided functional description and the code files in your smart home project, I'll create a `function.py` file that includes a main function. This function will allow you to control devices (i.e., actuators) based on the commands to turn them on, turn them off, or adjust their brightness.
# 
# Here's the `function.py` file:

# function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light

def control_device(room_name, device_name, action, brightness_level=None):
    # Get the home plan
    home = home_plan()
    
    # Find the specified room
    room = get_room(home, room_name)
    if not room:
        print(f"Room '{room_name}' not found.")
        return

    # Get the actuators in the room
    actuators = get_room_actuators(home, room_name)
    
    # Find the specified device
    device = next((actuator for actuator in actuators if actuator.actuator_type.lower() == device_name.lower()), None)
    
    if not device:
        print(f"Device '{device_name}' not found in room '{room_name}'.")
        return

    # Control the device based on the action
    if action == "开" or action == "turn on":
        device.turn_on()
        if isinstance(device, Light) and brightness_level:
            device.set_brightness_level(brightness_level)
    elif action == "关" or action == "turn off":
        device.turn_off()
    elif action == "调亮" or action == "brighten":
        if isinstance(device, Light):
            device.set_brightness_level("high")  # Adjust to high brightness
        else:
            print(f"Cannot brighten '{device_name}', it is not a light.")
    elif action == "调暗" or action == "dim":
        if isinstance(device, Light):
            device.set_brightness_level("low")  # Adjust to low brightness
        else:
            print(f"Cannot dim '{device_name}', it is not a light.")
    else:
        print(f"Action '{action}' is not recognized.")

def main():
    # Example usage
    control_device("LivingRoom", "Light", "开", "medium")  # Turn on the light with medium brightness
    control_device("LivingRoom", "Light", "调暗")          # Dim the light
    control_device("LivingRoom", "Light", "调亮")          # Brighten the light
    control_device("LivingRoom", "Light", "关")            # Turn off the light

if __name__ == "__main__":
    main()