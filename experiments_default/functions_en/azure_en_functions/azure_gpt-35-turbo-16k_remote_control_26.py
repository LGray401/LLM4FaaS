# Sure! Here is the 'function.py' file based on your functional description:

from home.home_plan import home_plan, get_room_actuators

def adjust_device(device_name, action):
    home = home_plan()
    for room in home:
        actuators = get_room_actuators(home, room.name)
        for actuator in actuators:
            if actuator.actuator_type.lower() == device_name.lower():
                if action.lower() == "on":
                    actuator.turn_on()
                elif action.lower() == "off":
                    actuator.turn_off()
                elif action.lower() == "brighten":
                    actuator.set_brightness_level("high")
                elif action.lower() == "dim":
                    actuator.set_brightness_level("low")
                else:
                    print("Invalid action. Please choose from 'on', 'off', 'brighten', or 'dim'.")
                return
    print(f"Device '{device_name}' not found in any room.")

if __name__ == "__main__":
    device_name = input("Enter the device name: ")
    action = input("Enter the action: ")
    adjust_device(device_name, action)