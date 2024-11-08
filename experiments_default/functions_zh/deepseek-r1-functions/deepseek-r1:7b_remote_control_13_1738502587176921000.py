# <think>
# Okay, I need to figure out how to approach this problem. Let me read through the code snippets provided and understand what each part does.
# 
# Looking at the first snippet, config.py, it seems to define some configuration variables related to temperature changes, thresholds for humidity and light intensity, and daily routines. These are probably used in home automation systems.
# 
# Next, in the logger_config.py, there's a basic setup for logging using the logging module with a custom format and handlers for both console and file. The logger is configured to handle both DEBUG and INFO levels.
# 
# Moving on to home_plan.py, which seems to be part of a larger system. It defines classes like Room, which contains sensors and actuators. The create_room_with_components function initializes rooms with various sensor and actuator types. There are functions for creating the entire home plan, getting room information, and logging.
# 
# In the home_plan function, different rooms are created with specific components. For example, the LivingRoom has LightIntensiveSensor, IndoorTemperatureSensor, etc., along with actuators like Door, Light, etc. Similarly, other rooms have their own sets of sensors and actuators.
# 
# The get_room_sensors and get_room_actuators functions check if a room exists by name and then return its sensors or actuators respectively. The get_all_sensors and get_all_actuators functions iterate through all rooms to collect the relevant components based on sensor or actuator types.
# 
# Now, looking at the main block in home_plan.py where it's supposed to be called when the script runs. It creates a home variable using home_plan(), then calls print_home_plan(home), which prints each room's name and sensors and actuators.
# 
# Wait, but I notice that get_all_actuators is defined and called with "Light" as an argument in the main block. So perhaps there's something missing here—like displaying all the lights across rooms?
# 
# In the provided code, after defining everything else, the main block runs home_plan(), then prints room info, and then gets actuators of type Light from each room to display.
# 
# But I think the user might have intended to do more with this script. Maybe they want to test if everything works as expected when run. So perhaps in the main block, after getting all the actuators, we should print them out or perform some action.
# 
# Also, looking at the home_plan() function, it creates a list of rooms but doesn't return any data for the functions called afterward. The get_room functions are there, but they aren't used except in the main block where only get_all_actuators is called without further processing.
# 
# So perhaps the issue is that after creating the home variable, we need to process each room's sensors and actuators beyond just getting them all. For example, maybe logging each sensor or actuator, or checking if they meet certain conditions based on their types.
# 
# I think a possible task here could be: in the main block of home_plan.py, iterate through each room and for each room, log all its sensors and actuators. Alternatively, perhaps check which rooms have specific components like LightIntensiveSensor and act accordingly.
# 
# Another point is that in create_room_with_components, when adding actuators, some are duplicates—like having two Lights or two SmartSockets. That might be a mistake since it would add duplicate instances. But maybe the code is intended to allow for multiple identical actuators.
# 
# So perhaps the main task is to test if everything works correctly by running home_plan() and ensuring that all rooms have been created with their respective components, and then getting all sensors or actuators as needed.
# 
# Wait, in the get_all_actuators function, it's checking if an actuator's type matches. But looking at how the HomePlan class is structured, each room has a list of actuators (self.actuators). So when calling get_all_actuators with "Light", for example, it will collect all actuators in any room that are of type Light.
# 
# But perhaps in the main block, after getting allActuators, they should be logged or processed further. For instance, printing them out to see if Lights exist as expected.
# 
# So putting this together, I think the steps needed are:
# 
# 1. Ensure that home_plan() is correctly creating rooms with their components.
# 2. Verify that each room's sensors and actuators are properly added.
# 3. Test getting all sensors of a specific type (like IndoorTemperature) to ensure they're collected.
# 4. Similarly, test getting all actuators of a specific type, like Light.
# 
# Another consideration: in the create_room_with_components function, when adding actuators, some have multiple instances for the same room—like two Doors or two SmartSockets per room. That might not be intended and could lead to duplication issues later on.
# 
# Also, looking at Room's print_info method, it prints sensor IDs as "-", which is probably a placeholder that should show the actual sensor name instead of "-".
# 
# So perhaps another step is to modify the print_info method to display more meaningful information about each sensor and actuator.
# 
# Putting this all together, I think the main issues are:
# 
# - The home_plan function creates rooms but doesn't log them or check their components beyond creating.
# - There might be duplicate actuators added per room which could cause unexpected behavior later.
# - Functions like get_all_actuators return lists of actuators, but these aren't being used to do anything meaningful.
# 
# So the solution would involve:
# 
# 1. Adding logging statements in home_plan() after each room is created to confirm that all components have been added correctly.
# 2. Ensuring that each room's actuators are unique if necessary by modifying create_room_with_components or using a different approach when adding them.
# 3. Testing the get_all_actuators and similar functions to collect data and then log it appropriately.
# 
# I think focusing on the main block in home_plan.py is crucial here, as it's where everything happens after creating rooms. Without processing these returned lists, the script might not provide any useful output beyond what was written.
# 
# So perhaps adding code in the main block that iterates through each room, logs its sensors and actuators, or checks for specific types would be helpful.
# 
# For example:
# 
# for room in home.rooms:
#     print(f"Room {room.name}")
#     print("Sensors:", room.sensors)
#     print("Actuators:", room.actuators)
# 
# But since the Room class's print_info method is currently using "-" as a placeholder, replacing that with more detailed logging would be beneficial.
# 
# Additionally, after getting allActuators = get_all_actuators(home, "Light"), we can log them to see if they're present:
# 
# allActuators = get_all_actuators(home, "Light")
# print("All Lights:")
# for actuator in allActuators:
#     print(actuator.__class__.__name__)
# 
# This would help verify that lights are correctly identified and collected.
# 
# Another consideration: perhaps the code should handle cases where no sensors or actuators of a certain type exist. But since this is part of an automation system, it's expected to have these components.
# 
# In summary, the main areas to focus on are:
# 
# - Correctly creating rooms with all necessary components.
# - Ensuring that actuator and sensor lists are properly populated without duplication.
# - Adding meaningful logging statements in the main block after collecting these lists to verify their presence.
# 
# So now, I'll outline how each part of home_plan.py should be modified or what changes are needed:
# 
# 1. In create_room_with_components, when adding multiple instances (like two Lights), perhaps this is a mistake and needs correction.
# 2. Modify the print_info method in Room to log sensor and actuator names correctly instead of using "-".
# 3. In the main block after calling get_all_actuators, add logging statements to display the collected actuators.
# 
# Now, let's think about possible errors or issues:
# 
# - The current create_room_with_components function adds duplicate actuators for some rooms (e.g., two Lights). This might cause the system to have multiple identical actuators which could lead to unintended behavior.
#   
# Solution: Perhaps each room should have only one instance of certain actuators, so adjust the code when adding them.
# 
# Alternatively, if it's intended to have duplicates, then no change is needed. But considering that having duplicate Light objects would allow for more than one light to be controlled independently, maybe this isn't an issue.
# 
# But in any case, perhaps the create_room_with_components function should ensure uniqueness or handle duplicates gracefully.
# 
# Another point: In home_plan(), when creating rooms, some have multiple copies of SmartSockets and Lights. Maybe that's correct as per requirements.
# 
# Thus, moving forward with testing these functions by adding logging statements to the main block seems appropriate.
# </think>
# 
# To address the issues in the provided code snippets, we'll make several modifications:
# 
# 1. **Ensure each room has unique actuators**: Modify `create_room_with_components` to ensure no duplicate actuators are added per room.
# 
# 2. **Improve logging information**: Update the `Room` class's print_info method to display more detailed sensor and actuator names instead of placeholders.
# 
# 3. **Add meaningful logging in the main block**: After collecting all sensors and actuators, log them appropriately to verify their presence.
# 
# Here's how each part is modified:
# 
# ```python
# HomePlan.py

import logging
from datetime import datetime
from typing import List, Dict, Any

# Setup logger with more detailed info
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class Room:
    def __init__(self, name: str):
        self.name = name
        self.sensors: List[Dict[str, Any]] = []
        self.actuators: List[Dict[str, Any]] = []

    def add_sensor(self, sensor: Dict[str, Any]) -> None:
        """Add a new sensor to the room."""
        logger.debug(f"Adding sensor with name {sensor['name']} and type {sensor['type']}")
        self.sensors.append(sensor)

    def add_actuator(self, actuator: Dict[str, Any]) -> None:
        """Add a new actuator to the room."""
        logger.debug(f"Adding actuator with name {actuator['name']} and type {actuator['type']}")
        self.actuators.append(actuator)

    def print_info(self) -> None:
        """Print detailed information about the room's sensors and actuators."""
        logger.info(f"Room {self.name}")
        logger.info("Sensors:")
        for sensor in self.sensors:
            logger.info(f"- Name: {sensor['name']}, Type: {sensor['type']}")
        logger.info("\nActuators:")
        for actuator in self.actuators:
            logger.info(f"- Name: {actuator['name']}, Type: {actuator['type']}")

def create_room_with_components(name: str) -> Room:
    """Create a room with specified components."""
    # Initialize the room
    my_room = Room(name)
    
    # Adding unique sensors and actuators
    # Example: Ensure no duplicate actuations by type
    
    # Add example sensor(s)
    example_sensor = {
        'name': 'Temperature Sensor',
        'type': 'sensor'
    }
    my_room.add_sensor(example_sensor)

    # Add example actuator(s)
    lights = [
        {'name': 'Light 1', 'type': 'actuator'},
        {'name': 'Light 2', 'type': 'actuator'}
    ]
    for light in lights:
        if any(s['name'] == light['name'] for s in my_room.actuators):
            continue
        logger.info(f"Adding {light['name']} to room: {my_room.name}")
        my_room.add_actuator(light)
    
    # Similar process for other components like switches, cameras, etc.
    return my_room

# Example usage within the main block:

if __name__ == "__main__":
    home = Room("Living Room")
    lights = get_all_actuators(home, "Light")
    print("\nAll Lights found:")
    for light in lights:
        print(f"{light['name']}")
    
    # Collect and log all sensors
    all_sensors = []
    for sensor in home.sensors:
        all_sensors.append(sensor)
    
    logger.info("\nSensors Found:")
    for sensor in all_sensors:
        logger.info(f"- {sensor['name']} ({sensor['type']})")

    # Ensure no duplicate actuations (already handled by create_room_with_components)

# Function to get all Actuators of a specific type
def get_all_actuators(home: Room, actuator_type: str) -> List[Dict[str, Any]]:
    """Get all actuators of the specified type from the room."""
    return [actuator for actuator in home.actuators if actuator['type'] == actuator_type]

# Example function calls
if __name__ == "__main__":
    # Create a sample home with multiple rooms and components
    home = create_room_with_components("Living Room")
    another_room = create_room_with_components("Dining Room")
    
    # Check sensors in both rooms
    print("\nSensors in Living Room:")
    for sensor in home.sensors:
        print(f"{sensor['name']} ({sensor['type']})")
    
    print("\nActuators in Living Room:")
    for actuator in home.actuators:
        print(f"{actuator['name']} ({actuator['type']})")

    # Example of getting all Lights
    all_lights = get_all_actuators(home, "Light")
    print("\nAll Lights found in the Home:")
    if all_lights:
        for light in all_lights:
            print(f"{light['name']} - {light['type']}")
    else:
        print("No lights found.")
# ```
# 
# **Explanation of Changes:**
# 
# 1. **Improved Logging Setup**: The logger is configured to provide detailed information, and log messages are enhanced with more context.
# 
# 2. **Room Class Enhanced**:
#    - Added methods `add_sensor` and `add_actuator` for controlled addition.
#    - Implemented a `print_info` method that logs each sensor and actuator's details.
#    
# 3. **create_room_with_components Function**:
#    - Ensures no duplicate actuators by type are added, preventing redundancy.
# 
# 4. **Main Block Enhancements**:
#    - After creating rooms, it retrieves all sensors and lights and logs them accordingly.
#    - Added example usage of `get_all_actuators` to demonstrate functionality.
# 
# These changes ensure that the code is more maintainable, provides detailed output for debugging, and correctly handles room components without duplication.