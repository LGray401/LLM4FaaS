from home.home_plan import get_room_actuators, home_plan


def control_device(home, room_name, device_type, feature=None, value=None):
    """
    Controls a device or multiple devices in a room remotely.

    Args:
        home: A list containing the rooms and their components (obtained from home_plan.py).
        room_name: The name of the room containing the device(s) to control.
        device_type: The type of device (e.g., "Light", "Heater").
        feature: An optional argument specifying an additional mode for the device (e.g., "brightness" for Light).
        value: An optional argument specifying the value for the feature (e.g., 50 for setting brightness to 50%).

    Returns:
        A message indicating the success or failure of the operation.
    """

    # Find the room with the specified name
    room = get_room_actuators(home, room_name)
    if not room:
        return f"There is no room named {room_name} in your home plan."

    # Find the actuators of the specified device type in that room
    devices = [actuator for actuator in room if actuator.actuator_type == device_type]
    if not devices:
        return f"There are no {device_type} devices in {room_name}."

    # Control the devices based on feature and value
    if feature:
        # Handle devices with additional modes (e.g., Light brightness)
        for device in devices:
            # Check if the device has the specified feature
            if hasattr(device, feature):
                # Call the corresponding function with the provided value
                getattr(device, feature)(value)
                return f"{device_type} {feature} in {room_name} set to {value}"
            else:
                return f"{device_type} in {room_name} doesn't support {feature} control."
    else:
        # Simple on/off control for devices without additional modes
        if device_type in ["Light", "Heater", "AC", "CoffeeMachine", "MusicPlayer", "CleaningRobot", "NotificationSender"]:
            for device in devices:
                if device.status == "off":
                    device.turn_on()
                    return f"{device_type} in {room_name} turned on"
                else:
                    device.turn_off()
                    return f"{device_type} in {room_name} turned off"
        else:
            return f"{device_type} doesn't currently support remote on/off control."

    return "Success"  # Shouldn't reach here, but added for completeness

if __name__ == '__main__':
    # Assuming you have the home data structure from home_plan.py
    home = home_plan()  # This call retrieves the room and component information

    # # Turn on the light in the kitchen
    # result = control_device(home, "Kitchen", "Light")
    # print(result)
    # control_device(home, "LivingRoom", "Heater")
    # result = control_device(home, "LivingRoom", "Heater")
    # print(result)

    # result = control_device(home, "Bedroom", "Light")
    # print(result)
    # result = control_device(home, "Kitchen", "CoffeeMachine")
    # print(result)  #

    result = control_device(home, "Bedroom", "Light", "set_brightness_level", "low")
    print(result)
