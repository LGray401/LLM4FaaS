from home.home_plan import home_plan, get_room_actuators, get_room


def control_device(home, room_name, device_types, action):
    """
    Control a device or several devices in a specified room.

    :param home: List of Room objects representing the home setup
    :param room_name: String, name of the room where the device is located
    :param device_types: List of device types (as strings) to control
    :param action: String, either "turn_on" or "turn_off"
    :return: None
    """
    room = get_room(home, room_name)
    if not room:
        print(f"Room '{room_name}' not found.")
        return

    actuators = get_room_actuators(home, room_name)
    if not actuators:
        print(f"No actuators found in '{room_name}'.")
        return

    for device_type in device_types:
        devices = [actuator for actuator in actuators if actuator.actuator_type == device_type]
        if not devices:
            print(f"No devices of type '{device_type}' found in '{room_name}'.")
            continue

        for device in devices:
            if action == "turn_on":
                device.turn_on()
            elif action == "turn_off":
                device.turn_off()
            else:
                print(f"Invalid action '{action}' for device '{device.id}'.")

if __name__ == "__main__":
    # Example usage
    home = home_plan()
    # control_device(home, "LivingRoom", ["Light", "AC"], "turn_on") # ✅
    # control_device(home, "Bedroom", ["Light"], "turn_off")# ✅
    # control_device(home, "Kitchen", ["CoffeeMachine"], "turn_on")# ✅
    # control_device(home, "Kitchen", ["Light"], "set_brightness_level")  # ❎
    control_device(home, "LivingRoom", ["CoffeeMachine", "Light", "AC"], "turn_on") # ✅

