# Based on your functional description and provided source code files, I will create a `function.py` file that contains a main function to control the devices in your smart home project, allowing users to adjust (turn on, turn off, brighten, and dim) certain devices.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light

def main():
    home = home_plan()
    
    # User inputs for room and device action
    room_name = input("Enter the room name: ")
    action = input("Enter the action (on/off/brighten/dim): ")
    device_type = input("Enter the device type (e.g., Light): ")

    # Get the specific room
    room = get_room(home, room_name)
    if room is None:
        print(f"No room found with the name '{room_name}'.")
        return

    # Get all actuators in the room
    actuators = get_room_actuators(home, room_name)
    if actuators is None:
        print(f"No actuators found in the room '{room_name}'.")
        return

    # Find the specific actuator of the desired type
    device = next((actuator for actuator in actuators if actuator.actuator_type == device_type), None)

    if device is None:
        print(f"No device of type '{device_type}' found in the room '{room_name}'.")
        return

    # Perform the action based on user input
    if action.lower() == "on":
        device.turn_on()
    elif action.lower() == "off":
        device.turn_off()
    elif action.lower() == "brighten":
        if isinstance(device, Light):
            current_brightness = device.brightness_level
            if current_brightness < 90:  # max brightness level
                device.set_brightness_level("high" if current_brightness < 60 else "medium")
            else:
                print("The light is already at maximum brightness.")
        else:
            print(f"{device_type} does not support brightness adjustment.")
    elif action.lower() == "dim":
        if isinstance(device, Light):
            current_brightness = device.brightness_level
            if current_brightness > 0:  # min brightness level
                device.set_brightness_level("medium" if current_brightness > 30 else "low")
            else:
                print("The light is already at minimum brightness.")
        else:
            print(f"{device_type} does not support brightness adjustment.")
    else:
        print("Invalid action. Please enter 'on', 'off', 'brighten', or 'dim'.")

if __name__ == "__main__":
    main()