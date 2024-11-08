# <think>
# Okay, I'm trying to figure out how to approach this problem. Let's see what the user provided.
# 
# So, there are three Python files: config.py, logger_config.py, and home_plan.py. The main focus seems to be on creating a home plan with various rooms, sensors, and actuators, using logging configurations as well as some thresholds for temperature, humidity, etc.
# 
# First, I'll look at the user's query. They didn't provide an explicit question but included code files. Hmm, maybe they want help understanding how these components work together or perhaps debugging something?
# 
# But looking at their provided code, I can see that config.py sets various thresholds and durations for routines. The home_plan function creates rooms with specific sensors and actuators. Then, functions like get_room_sensors and get_room_actuators are defined to retrieve sensor and actuator information based on room names.
# 
# Wait, in the main block of home_plan.py, there's a call to get_all_actuators with "Light" type. That makes me think they want to collect all light actuators from each room where the type is 'Light'.
# 
# But I'm not sure what exactly the user wants. Since their initial question isn't clear, perhaps they need help understanding how to extend this code or debug a part of it.
# 
# Looking at the provided code, in home_plan.py's main block, after creating all rooms, they call get_all_actuators with 'Light'. The function iterates through each room and collects actuators where actuator_type matches. So if a room has multiple Light types (like multiple instances), they should be included.
# 
# But maybe the user is encountering an error or wants to see how it would work in practice.
# 
# Alternatively, perhaps they want to add more rooms or modify existing ones. Or maybe there's an issue with sensor and actuator type checking.
# 
# Another point: In home_plan(), for each room, they loop through actuator_types which include types like Door, Light, etc., but some are repeated (like SmartSocket appearing twice in LivingRoom). That might be a mistake or intentional to have multiple instances per room.
# 
# Also, the get_room_sensors and get_room_actuators functions check if room.name equals room_name. But what about case sensitivity? The docstring for create_room_with_components says it's using name as an argument without specifying lowercasing, so maybe that's a point of consideration.
# 
# Wait, in home_plan(), they call create_room_with_components with 'LivingRoom' and then later use "outdoor" when calling get_room(home_plan(), "outdoor"). But the rooms created don't have such sensors. So perhaps there's an issue where some rooms are missing certain components or incorrect room names aren't being handled.
# 
# Also, in get_room_sensors and get_room_actuators, they loop through each room but only check if the room's name exactly matches. If someone is passing a different case (like 'livingroom' instead of 'LivingRoom'), it won't find anything. That could be an oversight unless the function is intended to handle that.
# 
# Another thing: The get_all_sensors and get_all_actuators functions are supposed to collect sensors or actuators of a specific type, but in home_plan(), they're using get_room_sensors and get_room_actuators which only return data for exact room names. So perhaps the user is trying to gather all sensors regardless of room name.
# 
# Wait, no: In the main block, after creating 'home', it's calling get_all_actuators with "Light", which loops through each room and collects all actuators where actuator_type matches. That seems correct because if any room has a Light actuator, they should be included.
# 
# But perhaps in their case, there are no actuators of type Light yet, so the result is empty. Maybe they want to add some.
# 
# Alternatively, maybe the issue is with how the Room class works—adding sensors and actuators via add_sensor and add_actuator methods correctly appends them, but when printing info, it only shows "-" followed by id without proper sensor names.
# 
# Wait, in the print_info() method of Room:
# 
# print(f"\n{self.name}:")
# print("Sensors:")
# for sensor in self.sensors:
#     print("-", sensor.id)
# print("Actuators:")
# for actor in self.actuators:
#     print("-", actor.id)
# 
# This just prints "-" followed by id. It's not very informative because it doesn't show the actual sensor or actuator types. So perhaps this is a bug where they intended to display more detailed information but only get the id.
# 
# So, maybe the user wants to fix that so when printing info(), it shows all sensor and actuator details instead of just '-' and id.
# 
# Also, looking at config.py's DAILY_ROUTINE_DURATION, which is set to 5. Not sure if that's relevant here unless the home_plan function uses it somewhere else.
# 
# Putting it all together, perhaps the main issues are:
# 
# 1. The Room print_info() method doesn't display detailed sensor and actuator info.
# 2. Case sensitivity in room names when retrieving sensors/actuators.
# 3. Possible missing or incorrect actuator types in rooms (like not having a Light actuator where expected).
# 
# So, to help the user, I should suggest fixes for these issues.
# 
# First, updating print_info() method to show sensor and actuator details instead of just '-' and id.
# 
# Second, consider case sensitivity when retrieving room information. Maybe convert room names to lowercase before comparison or make all comparisons case-insensitive.
# 
# Third, ensure that each room has the correct types of sensors and actuators as intended in create_room_with_components calls.
# 
# So, the steps would involve:
# 
# - Modifying print_info() to display more details.
# - Updating get_room_ functions to handle case insensitivity.
# - Checking if the rooms have all necessary actuator types.
# 
# But without knowing exactly what the user wants to fix or achieve, I'm speculating. However, based on the code provided, these are common areas where issues might arise.
# </think>
# 
# Based on the provided files and their contents, here's an analysis of how they work together and potential issues:
# 
# ### 1. `config.py`: Configurations
# - This file defines various thresholds for temperature (`min_temp`, `max_temp`), humidity (`min_humidity`, `max_humidity`), and other settings like daily routine duration.
# - It also includes a list of `ACTUATOR_TYPES` which are used to identify different types of actuators.
# 
# ### 2. `logger_config.py`: Logging Configurations
# - This file sets up logging configurations, including specifying the log file name and level.
# - The `set_logging_config` function allows overriding default settings if needed.
# 
# ### 3. `home_plan.py`: Home Plan Generation
# - This file generates a home plan with rooms containing specific sensors and actuators.
# - The `create_room_with_components` function takes a room name and components (sensors/actuators) to include in that room.
# - The `home_plan` function creates multiple rooms with various sensor and actuator types.
# 
# ### Key Components:
# #### Room Structure
# Each room is defined with specific sensors and actuators. For example:
# ```python
room1 = create_room_with_components('LivingRoom', [
    TemperatureSensor(),
    ...

actuators for each room are also specified, e.g., Door, Light, etc.

#### Sensor and Actuator Types
- Sensors include `TemperatureSensor`, `HumiditySensor`, etc.
- Actuators include types like `Fan`, `Light`, `WaterPurifier`, etc.

### Potential Issues:
1. **Room Name Case Sensitivity**:
   - The current implementation of `get_room_sensors` and `get_room_actuators` checks for an exact match of the room name.
   - If rooms are created with different cases (e.g., 'Livingroom' vs 'livingroom'), they won't be found unless the comparison is case-insensitive.

2. **Missing Actuators**:
   - In the main block, `get_all_actuators('Light')` should collect all Light actuators from each room.
   - If no Light actuators are added to any rooms, this will return an empty list.

3. **Printable Room Information**:
   - The `print_info()` method in the Room class only prints '-' followed by the sensor/actuator ID without providing meaningful information.
   - This makes it difficult to understand which sensors and actuators are present in each room.

### Suggestions for Fixes:

#### 1. Improve Room Print Info
Update the `print_info()` method to display detailed information about each sensor and actuator instead of just '-' and ID.

# ```python
# def print_info(self):
#     print(f"\n{self.name}:")
#     print("Sensors:")
#     for sensor in self.sensors:
#         print(f"- {sensor.__class__.__name__}({sensor.id})")
#     print("\nActuators:")
#     for actuator in self.actuators:
#         print(f"- {actuator.__class__.__name__}({actuator.id})")
# ```

#### 2. Handle Case Insensitivity
Modify the `get_room_sensors` and `get_room_actuators` functions to perform case-insensitive comparisons when checking room names.

# ```python
# def get_room_sensors(sensors, room_name):
#     for room in self.rooms.values():
#         if room.name.lower() == room_name.lower():
#             return [sensor.copy() for sensor in room.sensors if isinstance(sensor, type(sensors))]
#     return []
# ```

#### 3. Ensure All Required Actuators are Added
In the `home_plan` function, make sure that each room has an actuator of the desired type (e.g., add a Light actuator to the LivingRoom).

### Conclusion:
The provided code structure is functional but could be improved for better logging and case sensitivity in room name matching. By updating these components, you can enhance the usability and reliability of the home planning system.

Would you like me to provide specific fixes or further details on any of these areas?