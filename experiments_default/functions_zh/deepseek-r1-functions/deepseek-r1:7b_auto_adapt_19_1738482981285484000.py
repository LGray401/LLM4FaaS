# <think>
# Okay, I need to figure out what the user is asking for. They provided several Python files: preparation.py, config.py, home_plan.py, and a logger_config.py which seems to be missing but probably handles logging.
# 
# Looking at their code, they have a Room class in home_plan.py that aggregates sensors and actuators. The main script section runs get_all_actuators(home, "Light") when __name__ is "__main__". So the task might involve analyzing or modifying how room components are collected based on sensor types and actuator types.
# 
# I see functions like create_room_with_components which take a name and lists of sensors and actuators. The home_plan function creates rooms with specific components for each room type.
# 
# In get_all_sensors, it iterates over all rooms and their sensors to find those matching the sensor_type parameter. Similarly, get_all_actuators loops through each room's actuators looking for matches based on actuator_type.
# 
# The user is probably asking about how these functions work, especially when retrieving all light-related components from a home setup. Alternatively, they might want to modify how these functions behave or debug something specific in their code.
# 
# Perhaps the issue is that get_all_actuators isn't returning the expected number of lights because it's checking for actuator_type as passed into the function. But looking at the code, each Actuator class probably has an 'actuator_type' attribute which could be a string like "Light" or similar.
# 
# Wait, in the home_plan() example, they're calling get_all_actuators(home, "Light"). Let me check what's inside home. In create_room_with_components for LivingRoom, the actuator types include Door, Light, etc. So if the function is correctly filtering based on 'actuator_type' being "Light", it should return all lights in each room.
# 
# But maybe there's a case where not all lights are detected because their class name isn't exactly matching. Alternatively, perhaps some actuators have different naming conventions or inheritance issues.
# 
# Another thought: Are the sensor types correctly passed to create_room_with_components? For example, for sensor_types [LightIntensiveSensor], is that properly creating the sensors?
# 
# Wait, looking at room print info in home_plan(), when they add sensors like LightIntensiveSensor and others. So if get_all_sensors is working as intended.
# 
# But perhaps there's an error elsewhere. The user might be encountering a problem where lights aren't being picked up correctly by get_all_actuators. Maybe the actuator_type isn't matching because of case sensitivity or different naming conventions in some classes, like 'Light' vs 'lights'.
# 
# Alternatively, maybe the Actuator class has more attributes than just 'actuator_type', causing an issue when comparing.
# 
# Another angle: Perhaps the __name__ section is not correctly calling get_all_actuators, but that seems unlikely since it's a main script call. Or perhaps there's a typo in "Light" vs another case where some classes are not detected.
# 
# Wait, looking at home_plan() function:
# 
# In create_room_with_components for LivingRoom, the actuator_types include [Door, Light, Window, Window, Curtain, ...]. So when get_all_actuators is called with "Light", it should find all instances of Light in each room's actuators. But if a room has two Lights and another has none, maybe the function isn't correctly counting.
# 
# But perhaps the issue is that the actuator_type parameter expects exact matches, but some classes have different names when added to home. For example, maybe in one room, it's 'Lights' instead of 'Light', which would cause get_all_actuators to miss them.
# 
# Alternatively, looking at the config.py, they define various thresholds and durations. But how does that relate? Maybe not directly related unless the code is using those values elsewhere.
# 
# Another possibility: The Room class in home_plan.py might have an issue with sensor or actuator addition. For example, when add_actuator is called with an instance of an actuator type, but if the instances are created correctly based on room name (like 'Balcony' for OutdoorTemperatureSensor), maybe some are missing.
# 
# Wait, looking at create_room_with_components: it adds sensors and actuators by calling sensor_type(name). For example, in create_room_with_components("LivingRoom", [LightIntensiveSensor, ...], ...), it's adding the sensors correctly. But perhaps when adding actuators, there might be duplicates or missed instances.
# 
# Alternatively, maybe some of the actuator_types are being added multiple times incorrectly. Looking at the code:
# 
# In create_room_with_components for LivingRoom: [Door, Light, Window, Window, Curtain, MusicPlayer, SmartSocket, SmartSocket, CleaningRobot, SmartTV, NotificationSender, AC, Heater]. That's 13 items.
# 
# Wait, perhaps in another room, like bedroom, it has two Lights as well. So when get_all_actuators is called for "Light", it should return all instances of Light across rooms.
# 
# But if the function isn't correctly identifying them because of case sensitivity or different naming, that could be an issue.
# 
# Another thing to check: Are the actuator types being passed into create_room_with_components correct? For example, in home_plan.py's main section after get_all_actuators, perhaps some actuator types are not defined elsewhere. But looking at the code provided, it seems all necessary classes are imported or created.
# 
# Wait a minute—maybe I should consider potential errors like circular imports or incorrect class definitions that prevent instances from being added properly to rooms.
# 
# Alternatively, perhaps in create_room_with_components, when adding sensors and actuators based on room name (e.g., 'Balcony' for OutdoorTemperatureSensor), but the sensor types aren't correctly passed or there's a typo.
# 
# Another angle: The get_all_sensors function uses isinstance(s, Sensor) which relies on correct inheritance. If any sensor is not properly subclassed of Sensor, it might be excluded from the results.
# 
# But given that all sensors and actuators are being added in create_room_with_components, perhaps the problem lies elsewhere.
# 
# Wait, I should also consider if the main script in home_plan.py isn't correctly calling get_all_actuators. Looking at it: after defining the functions, it calls:
# 
# home = Home()  # Assuming Home is a class that initializes rooms
# # Then creates each room with create_room_with_components
# 
# Then calls get_all_actuators(home, "Light")
# 
# But perhaps in creating the home instance, some actuator types are missing or not being added correctly. For example, if a room doesn't have any actuators and thus no instances of Light, but the function should return them regardless.
# 
# Alternatively, maybe the issue is that get_all_actuators only returns one instance per room instead of all, causing an undercount.
# 
# Another thought: Maybe the actuator_type passed to get_all_actuators isn't matching exactly with how they're added. For example, if in create_room_with_components for a room, the actuator type is "SmartSocket", but when called from home_plan, it's looking for "SmartSocket" as well.
# 
# Alternatively, perhaps the function needs to consider case sensitivity or other naming nuances.
# 
# But given that all these functions seem logically correct based on the code provided, maybe the issue isn't in these parts. Perhaps the problem is elsewhere, such as how the actuator instances are being initialized or how they're counted.
# 
# Wait, looking back at get_all_sensors: it uses a list comprehension to iterate over each room's sensors and check if isinstance(s, Sensor). Maybe some sensor types aren't correctly subclasses of Sensor, causing them not to be included when they should. But again, this is speculative without seeing the actual classes.
# 
# Alternatively, perhaps the user has a typo in their code where "Light" isn't properly quoted or matched against different cases.
# 
# But since I need to provide an answer based on what's given, here's my thought process and possible solution:
# 
# Firstly, ensure that all actuator types are correctly passed into create_room_with_components. For instance, if any room is missing an actuator type like Light because it was mistakenly added as "Lights", then get_all_actuators won't find them.
# 
# Secondly, check the actuator_type parameter in get_all_actuators: make sure that when calling with 'Light', all instances of that class are returned. It's possible that some classes have subclasses or aliases causing mismatches.
# 
# Thirdly, verify that no room is missing from being added to home due to any issues in create_room_with_components.
# 
# Another possibility is that the function get_all_actuators is not correctly handling multiple rooms and their respective actuator types. For example, if a room has two instances of Light, they should both be returned when 'Light' is passed as the filter.
# 
# Wait, looking at home_plan.py's main script:
# 
# It creates each room with create_room_with_components using room names (e.g., "LivingRoom") and passes in specific actuator types. Then calls get_all_actuators with the entire home object and "Light".
# 
# In get_all_actuators: it loops through all rooms and their actuators, checking if each actuator's type matches.
# 
# So perhaps the function is working correctly but just returns an empty list because no Light instances were added to any room. But that seems unlikely since they're part of the actuator_types in create_room_with_components.
# 
# Alternatively, maybe some actuator types are not being properly handled due to inheritance or attribute comparisons. For example, if an actuator's name isn't exactly "Light", but is a subclass with different attributes causing the isinstance check to fail.
# 
# But without seeing the actual classes, it's hard to say.
# 
# In any case, perhaps the user wants help in debugging why get_all_actuators isn't returning the expected number of lights. So I'll suggest possible steps:
# 
# 1. Check if all Light instances are correctly added to their respective rooms.
# 2. Verify that the actuator_type passed into get_all_actuators matches exactly how they're created (case-sensitive).
# 3. Ensure there's no typo or import issue with any classes used in create_room_with_components.
# 4. Test each room individually by calling get_all_actuators on it to see if lights are correctly returned.
# 
# Alternatively, the problem could be that some rooms don't have any actuator types defined for Lights, so they're not included when they should be.
# 
# But given all this, I'll draft a possible answer based on these points.
# </think>
# 
# To address the issue of retrieving all Light instances from each room using `get_all_actuators`, follow these steps:
# 
# 1. **Ensure Correct Initialization**: Verify that every Light instance is correctly added to its respective room when initializing rooms in `create_room_with_components`.
# 
# 2. **Check Actuator Type Case Sensitivity**: Confirm that the actuator_type "Light" exactly matches how instances are created, ensuring case sensitivity and no typos.
# 
# 3. **Subclass Verification**: Ensure all sensor and actuator classes correctly extend from their respective base classes (e.g., `Sensor` for sensors and `Actuator` for actuators).
# 
# 4. **Debugging Individual Rooms**: Test each room separately to see if Lights are present when calling `get_all_actuators` on it individually.
# 
# Here is a code snippet that implements these steps:
# 
# ```python
from home import Home, Room

# Define your sensor and actuator classes here

def create_room_with_components(room_name, sensors=None, actuators=None):
    room = Room(room_name)
    if sensors:
        for sensor in sensors:
            # Ensure each sensor is correctly initialized
            room.add_sensor(sensor(room_name))  # Example initialization method
    if actuators:
        for actuator in actuators:
            room.add_actuator(actuator(room_name))
    return room

def get_all_sensors(home):
    sensors = []
    for room in home.rooms:
        for s in room.sensors:
            if isinstance(s, Sensor):
                sensors.append(s)
    return sensors

def get_all_actuators(home, actuator_type):
    actuators = []
    for room in home.rooms:
        for a in room.actuators:
            # Use exact type matching to ensure correct instances are included
            if isinstance(a, actuator_type):
                actuators.append(a)
    return actuators

# Main script
home = Home()
# Create rooms and add sensors/actuators as needed
home.add_room(create_room_with_components("LivingRoom", ["SmartSocket"]))
home.add_room(create_room_with_components("DiningRoom", ["Light", "SmartSocket"]))

lights = get_all_actuators(home, Light)
print("Lights found:", lights)
# ```
# 
# **Explanation:**
# 
# - **create_room_with_components**: This function initializes rooms and adds specified sensors/actuators. Ensure that all necessary classes extend from `Sensor` or `Actuator`.
# 
# - **get_all_sensors**: Retrieves all sensor instances across home rooms.
# 
# - **get_all_actuators**: Filters and returns only the actuation types matching the given type (e.g., "Light"). Using exact type matching ensures correct inclusion of instances.
# 
# This approach systematically verifies each part of the code to ensure that Light (or any other actuator type) is correctly identified and returned.