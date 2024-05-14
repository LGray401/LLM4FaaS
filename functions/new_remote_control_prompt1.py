from home.home_plan import get_room, get_room_actuators


def control_device(home, room_name, device_type, action, **kwargs):
    """
    Control a device or devices in a specific room remotely.

    Parameters:
        home (list): List of Room objects representing the smart home.
        room_name (str): Name of the room where the device is located.
        device_type (str): Type of the device to control.
        action (str): Action to perform on the device.
        **kwargs: Additional keyword arguments for specific modes or features.

    Returns:
        bool: True if the device control was successful, False otherwise.
    """
    room = get_room(home, room_name)

    if room:
        actuators = get_room_actuators(home, room_name)
        if actuators:
            for actuator in actuators:
                if actuator.actuator_type == device_type:
                    if action == "turn_on":
                        actuator.turn_on()
                        return True
                    elif action == "turn_off":
                        actuator.turn_off()
                        return True
                    # Add additional actions for specific devices or modes here
                    # For example:
                    elif action == "set_brightness":
                        if "brightness_level" in kwargs:
                            actuator.set_brightness_level(kwargs["brightness_level"])
                            return True
                    else:
                        print("Unsupported action for this device.")
                        return False
            print(f"No {device_type} found in {room_name}.")
            return False
        else:
            print(f"No actuators found in {room_name}.")
            return False
    else:
        print(f"No room named {room_name} found in the home.")
        return False


if __name__ == "__main__":
    # Example usage
    # original
    # from home_plan import home_plan
    from home.home_plan import home_plan


    # Get the home plan
    home = home_plan()

    # Control a device (e.g., turn on the light in the living room)
    result1 = control_device(home, "LivingRoom", "Light", "turn_on")
    result = control_device(home, "LivingRoom", "Light", "set_brightness", brightness_level="high")

    # result = control_device(home, "Bedroom", "Light", "set_brightness", brightness_level="medium")
    print(result1, result)


# version 1-- without specifying the folder structure
# def control_device(home, room_name, device_type, action, **kwargs):
#     """
#     Control a device or devices in a specific room remotely.
#
#     Parameters:
#         home (list): List of Room objects representing the smart home.
#         room_name (str): Name of the room where the device is located.
#         device_type (str): Type of the device to control.
#         action (str): Action to perform on the device.
#         **kwargs: Additional keyword arguments for specific modes or features.
#
#     Returns:
#         bool: True if the device control was successful, False otherwise.
#     """
#     room = get_room(home, room_name)
#     if room:
#         actuators = get_room_actuators(home, room_name)
#         if actuators:
#             for actuator in actuators:
#                 if actuator.actuator_type == device_type:
#                     if action == "turn_on":
#                         actuator.turn_on()
#                         return True
#                     elif action == "turn_off":
#                         actuator.turn_off()
#                         return True
#                     # Add additional actions for specific devices or modes here
#                     # For example:
#                     # elif action == "set_brightness":
#                     #     if "brightness_level" in kwargs:
#                     #         actuator.set_brightness_level(kwargs["brightness_level"])
#                     #         return True
#                     else:
#                         print("Unsupported action for this device.")
#                         return False
#             print(f"No {device_type} found in {room_name}.")
#             return False
#         else:
#             print(f"No actuators found in {room_name}.")
#             return False
#     else:
#         print(f"No room named {room_name} found in the home.")
#         return False
#
# # Example usage:
# # control_device(home, "LivingRoom", "Light", "turn_on")
# # control_device(home, "Bedroom", "AC", "turn_on")
# # control_device(home, "Kitchen", "Coffee", "turn_on")
# # control_device(home, "Bathroom", "Door", "turn_on")
# # control_device(home, "Balcony", "Window", "turn_on")
