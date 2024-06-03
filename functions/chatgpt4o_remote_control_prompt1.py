from home.home_plan import home_plan, get_room_actuators

def control_device(home, room_name, device_type, mode=None):
    """
    Control a device or devices in a specific room of the home.

    Parameters:
        home (list): List of Room objects representing the home structure.
        room_name (str): Name of the room where the device is located.
        device_type (str): Type of the device to control (e.g., "Light", "Heater", "AC").
        mode (str, optional): Mode to set for the device. If None, toggle device state.

    Returns:
        str: Confirmation message indicating the action performed.
    """
    room_actuators = get_room_actuators(home, room_name)
    if room_actuators:
        matched_devices = [device for device in room_actuators if device.actuator_type == device_type]
        if matched_devices:
            if mode is None:
                for device in matched_devices:
                    if device.status == "on":
                        device.turn_off()
                    else:
                        device.turn_on()
                return f"{device_type} in {room_name} toggled."
            else:
                for device in matched_devices:
                    if hasattr(device, "set_mode"):
                        device.set_mode(mode)
                    else:
                        return f"{device_type} in {room_name} does not support different modes."
                return f"{device_type} in {room_name} set to {mode} mode."
        else:
            return f"No {device_type} found in {room_name}."
    else:
        return f"No actuators found in {room_name}."

# Example usage:
if __name__ == "__main__":
    home_structure = home_plan()
    print(control_device(home_structure, "LivingRoom", "Light", "set_brightness_level"))  # Turn on LivingRoom Light in low mode
    # print(control_device(home_structure, "Bedroom", "Heater", mode=3))  # Set Bedroom Heater to mode 3
    # print(control_device(home_structure, "Kitchen", "AC"))  # Toggle Kitchen AC state
    print(control_device(home_structure, "LivingRoom", "MusicPlayer", "turn_on"))  # Toggle Kitchen AC state

