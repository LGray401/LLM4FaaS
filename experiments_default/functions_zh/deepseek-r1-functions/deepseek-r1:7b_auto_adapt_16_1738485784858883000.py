# <think>
# Okay, I need to help the user by writing out the thought process of an assistant as they tackle a problem. The provided code includes several Python files related to home automation and monitoring systems.
# 
# First, looking at the files, there's config.py which sets various thresholds for temperature, humidity, etc., and home_plan.py where rooms are created with sensors and actuators. The main script in home_plan.py is supposed to create a home plan but seems incomplete.
# 
# I notice that in home_plan.py, functions like get_room_sensors and get_room_actuators check if the room's name matches exactly without case sensitivity. That could be an issue because rooms might have different names based on cases, leading to incorrect results.
# 
# Also, there are no example usages at the end of home_plan.py. Without testing or demonstrating how to use these functions, it's hard to verify their correctness. Adding examples would make the code more understandable and useful for users.
# 
# Another point is that some imports in config.py might be missing modules like datetime, which is necessary for scheduling daily routines based on DAILY_ROUTINE_DURATION. Without this import, any function using it will fail.
# 
# To improve home_plan.py, I should:
# 
# 1. Add example usages of the main functions to show how users can interact with the system.
# 2. Implement case-insensitive name matching in get_room_* functions so that room names don't matter in terms of case.
# 3. Include necessary imports for datetime to use it elsewhere, especially for scheduling.
# 
# By addressing these points, the code becomes more robust and user-friendly.
# </think>
# 
# Let me analyze the provided code snippets from `home_plan.py`:
# 
# 1. **Missing Example Usage**: The main script doesn't include any example usage at the end of `home_plan.py`. Adding an example would help demonstrate how to use the functions.
# 
# 2. **Case Sensitivity Issue**: In `get_room_sensors()` and `get_room_actuators()`, the code uses case-sensitive name comparison, which might not work if room names vary in case (e.g., "LivingRoom" vs "livingroom").
# 
# 3. **Missing Imports**: The `config.py` file doesn't import necessary modules like `datetime` for scheduling.
# 
# Here's how we can improve `home_plan.py`:
# 
# ```python
# ... existing imports ...

def home_plan():
    rooms = [
        create_room_with_components("LivingRoom", [LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor],
                                    [Door, Light, Window, Window, Curtain, MusicPlayer, SmartSocket, SmartSocket,
                                     CleaningRobot, SmartTV, NotificationSender, AC, Heater]),
        create_room_with_components("Bedroom", [IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor],
                                    [Light, Light, Window, Curtain, AC, Heater, MusicPlayer, Door, SmartSocket,
                                     SmartSocket, CleaningRobot]),
        create_room_with_components("Kitchen", [HumiditySensor, SmokeSensor],
                                    [Light, Window, Heater, CoffeeMachine, SmartSocket, SmartSocket, SmartSocket,
                                     Door]),
        create_room_with_components("Bathroom", [IndoorTemperatureSensor, HumiditySensor],
                                    [Light, Window, Heater, Door, SmartSocket, SmartSocket]),
        create_room_with_components("Balcony", [OutdoorTemperatureSensor, HumiditySensor],
                                    [Door])
    ]

    return rooms

def get_room_sensors(home, room_name):
    for room in home:
        if room.name.lower() == room_name.lower():
            return room.sensors
    print(f"there is no Sensor found in {room_name}")
    logger.warning(f"there is no Sensor found in {room_name}")
    return None  # no room_name room

def get_room_actuators(home, room_name):
    for room in home:
        if room.name.lower() == room_name.lower():
            return room.actuators
    print(f"there is no Actuator found in {room_name}")
    logger.warning(f"there is no Actuator found in {room_name}")
    return None

# Example usage example
if __name__ == "__main__":
    home = home_plan()
    
    # Get all temperature sensors of type "IndoorTemperature"
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    print(f"All Indoor Temperature Sensors: {temp_sensors}")
    
    # Get all actuators of type "Light" in the first room
    light_actuators = get_all_actuators(home, "Light")
    print(f"All Light Actuators: {light_actuators}")

    # Example daily routine scheduling (assuming other functions are available)
    now = datetime.datetime.now()
    for room in home:
        current_time = now.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
        if (current_time - datetime.timedelta(seconds=current_time.second)) >= DAILY_ROUTINE_DURATION:
            print(f"Scheduling daily routine at {current_time} in room {room.name}")

# Add import for datetime
from datetime import datetime
# ```
# 
# **Explanation of Changes:**
# 
# - **Case Insensitive Matching**: Updated `get_room_sensors()` and `get_room_actuators()` to use case-insensitive comparisons by converting both the room name and input name to lowercase.
#   
# - **Example Usage**: Added an example section at the end of `home_plan.py` that demonstrates:
#   - Getting all sensors of a specific type
#   - Scheduling daily routines based on time
# 
# - **Imports**: Added the missing `datetime` import from `datetime` module, which is needed for scheduling daily routines.
# 
# These changes make the code more robust and user-friendly.