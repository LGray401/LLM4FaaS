# # functions/control_devices.py
#
# def control_device(home, room_name, device_type, action):
#     """
#     Control a device or devices at home remotely.
#
#     Parameters:
#         home (list): The list of rooms in the home.
#         room_name (str): The name of the room where the device is located.
#         device_type (str): The type of device to control.
#         action (str): The action to perform on the device.
#
#     Returns:
#         str: A message indicating the result of the action.
#     """
#     for room in home:
#         if room.name == room_name:
#             for actuator in room.actuators:
#                 if actuator.actuator_type == device_type:
#                     if action == "turn_on":
#                         actuator.turn_on()
#                         return f"{device_type} in {room_name} is now ON."
#                     elif action == "turn_off":
#                         actuator.turn_off()
#                         return f"{device_type} in {room_name} is now OFF."
#                     # Add more actions here if needed
#             return f"No {device_type} found in {room_name}."
#     return f"No room named {room_name} found in the home."
#
# if __name__ == "__main__":
#     # Example usage
#     # original
#     # from home_plan import home_plan
#     # from home.home_plan import home_plan
#     from ..home.home_plan import home_plan
#
#     # Get the home plan
#     home = home_plan()
#
#     # Control a device (e.g., turn on the light in the living room)
#     result = control_device(home, "LivingRoom", "Light", "turn_on")
#     print(result)
# functions/control_devices.py
import sys
import os

# Add the parent directory of the current directory to the Python path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

# Now you can import the home_plan module
from home.home_plan import home_plan


def control_device(home, room_name, device_type, action):
    """
    Control a device or devices at home remotely.

    Parameters:
        home (list): The list of rooms in the home.
        room_name (str): The name of the room where the device is located.
        device_type (str): The type of device to control.
        action (str): The action to perform on the device.

    Returns:
        str: A message indicating the result of the action.
    """
    for room in home:
        if room.name == room_name:
            for actuator in room.actuators:
                if actuator.actuator_type == device_type:
                    if action == "turn_on":
                        actuator.turn_on()
                        return f"{device_type} in {room_name} is now ON."
                    elif action == "turn_off":
                        actuator.turn_off()
                        return f"{device_type} in {room_name} is now OFF."
                    # Add more actions here if needed
            return f"No {device_type} found in {room_name}."
    return f"No room named {room_name} found in the home."

if __name__ == "__main__":
    # Example usage
    # Get the home plan
    home = home_plan()

    # Control a device (e.g., turn on the light in the living room)
    result = control_device(home, "LivingRoom", "Light", "turn_on")
    print(result)
