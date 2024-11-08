# <think>
# Okay, I need to figure out how to write the code based on the provided files. Let's start by understanding each file and what needs to be done.
# 
# First, looking at config.py, it has some variables like TEMP_CHANGE_DURATION, TEMP_LOW, TEMP_HIGH, etc. These are probably used elsewhere in the code for temperature control routines or similar functions.
# 
# Then there's home_plan.py, which seems to handle creating rooms with various components like sensors and actuators. The main function is create_room_with_components, which takes a room name, sensor types, and actuator types. It adds these to respective lists in the Room class.
# 
# In the get_room_sensors and get_room_actuators functions, they loop through each room to find matches based on names. These functions are probably used for logging or accessing specific components within a room.
# 
# The main script at the bottom seems to be testing some of these functions, but I don't see it implementing the home plan functionality yet.
# 
# In home_plan.py, the create_room_with_components function is adding sensors and actuators to rooms based on the given types. For example, LivingRoom has several LightIntensiveSensor instances, along with various actuators like Door, Light, etc.
# 
# But wait, looking at line 36 in home_plan.py: room.add_actuator acts as a list of objects. So for each actuator_type in actuator_types, it's adding an instance to the room. But when multiple same types are passed, they might all be added. For example, if actuator_types has Door twice, does that mean two Door instances? I think so.
# 
# Now, considering the functions get_room_sensors and get_room_actuators, these take a home (which is a list of Rooms) and room_name as parameters. They loop through each Room in home to find one with the matching name, then return its sensors or actuators.
# 
# In the main script after creating rooms via home_plan(), it's calling get_all_sensors and get_all_actuators functions. The get_all_sensors function loops through all rooms and collects sensor objects that match a given type (like IndoorTemperature). Similarly for actuators based on their type, like Light.
# 
# Wait, in the main script after home = home_plan(), there are some calls to these functions:
# 
# get_all_sensors(home, "IndoorTemperature")
# get_all_actuators(home, "Light")
# 
# So it's finding all sensors of type IndoorTemperature and all actuators of type Light across all rooms.
# 
# But looking at how get_room_sensors is written: for each room in home, if the room's name matches room_name, return its sensors. But what if multiple rooms have that name? It returns the first one's sensors it finds. So perhaps this function isn't handling multiple rooms correctly and would only work with single unique room names.
# 
# Similarly for get_room_actuators: same issue.
# 
# I think these functions might need to collect data from all matching rooms, but maybe in a controlled environment like home planning, each room name is unique, so returning the first match's sensors/actuators is sufficient.
# 
# But wait, looking at home_plan() function, it creates multiple rooms with names "LivingRoom", "Bedroom", etc. So for get_room(...), if someone passes "LivingRoom" as the room_name, it will return that room's sensors and actuators correctly.
# 
# So perhaps these functions are working under the assumption of unique room names.
# 
# Now, about the main script: after calling home_plan(), which returns a list of rooms, then:
# 
# get_all_sensors is called with home and "IndoorTemperature". This should collect all IndoorTemperature sensors across all rooms?
# 
# Wait no. The get_all_sensors function loops through each room in 'home' (which includes multiple rooms). For each sensor in the room's sensors, it checks if sensor.sensor_type matches the given type.
# 
# But looking at the Room.add_sensor method: when adding a sensor, how is its sensor_type set? In create_room_with_components, for example:
# 
# room.add_sensor(sensor_type(name))
# 
# If sensor_type is, say, LightIntensiveSensor, then each added sensor will have their id and possibly other attributes. So to get all sensors of type IndoorTemperature, the get_all_sensors function loops through each room's sensors and collects those where sensor_type matches.
# 
# But wait, how are these sensor types defined? For example, in home_plan(), when adding a sensor like LightIntensiveSensor, what information does it carry? Maybe each sensor has an 'id' and a 'type', so we can check if the type is as needed.
# 
# In this case, get_all_sensors is correctly collecting all sensors of the given type across rooms. Similarly for get_all_actuators.
# 
# But in home_plan(), when creating rooms with components like [LightIntensiveSensor, IndoorTemperatureSensor, etc.], each sensor's 'type' would correspond to its class name or something similar. So if a sensor is an instance of LightIntensiveSensor, it will have sensor_type as "LightIntensiveSensor".
# 
# Wait, but in the code provided earlier, I don't see where sensors are added with their type information. It seems like each time a sensor is created (e.g., LightIntensiveSensor(name)), perhaps that name represents its type.
# 
# But for now, assuming that get_all_sensors and get_all_actuators functions correctly collect all relevant sensors and actuators based on the given types.
# 
# Now, putting this together: I need to write code as per these functions. So first, implement create_room_with_components in home_plan.py, then write helper functions like get_room_sensors, get_room_actuators, etc., which loop through rooms to collect data.
# 
# Wait, but looking at the provided home_plan.py code:
# 
# The function define Room with add_sensors and add_actuators. Then create_room_with_components adds sensors and acts as a list of actuator objects (like room.add_actuators(...)).
# 
# So when a room is created, it has certain sensors and actuators added to their respective lists.
# 
# Now, the helper functions get_room_sensors and get_room_actuators: for a given home (list of rooms) and room_name, loop through each room in home:
# 
# - If any room's name matches room_name, return that room's sensors or actuators.
# - Else, maybe return None? Or perhaps raise an error.
# 
# But the code provided shows these functions are returning something. So probably, for a given room_name, it returns the first matching room's sensors/actuators.
# 
# So now, in home_plan.py, how to implement get_room_sensors and get_room_actuators.
# 
# Looking at the main script:
# 
# After creating rooms via home_plan(), which is called with no arguments except creating rooms based on predefined components. Then, functions like get_all_sensors are used to collect data.
# 
# But perhaps there's a confusion here: in the home_plan() function, it returns a list of Rooms. So when calling home = home_plan(), 'home' becomes a list containing one Room (since create_room_with_components is called once with "LivingRoom").
# 
# Wait no. Looking back at the code:
# 
# The main function home_plan() creates multiple rooms? Or just one?
# 
# Looking again: In home_plan.py, line 28-36: it's inside the function 'def create_room_with_components(...)', which returns a Room object.
# 
# Then in line 54 (approximate), after defining these functions, it calls home = home_plan(), and then proceeds to call get_all_sensors and get_all_actuators.
# 
# Wait no. Wait, the code provided for home_plan.py is as follows:
# 
# It starts with an empty file, but I need to see how 'home_plan' function works. Oh wait, actually, in the user's question, only a part of home_plan.py is shown—lines 1-36 are the create_room_with_components function and some helper functions.
# 
# Wait no, looking back:
# 
# The initial code provided includes lines from home_plan as follows:
# 
# Lines 28: def create_room_with_components(...):
# 
# Lines up to line 40 or so define the Room class with add_sensors and add_actuators. Then later in the file (after that), the helper functions get_room_sensors, etc., are defined.
# 
# Wait no, actually, looking at the code provided:
# 
# It starts from line 1-36: It's part of home_plan.py where a function create_room_with_components is written, which creates one room with name 'LivingRoom', adding various sensors and actuator instances to it. Then inside this same file, helper functions get_room_sensors, etc., are defined.
# 
# Wait no, perhaps I'm getting confused because the code in the initial question is split into two parts: home_plan.py (which starts with lines 1-36) and config.py which follows after that.
# 
# But perhaps it's better to think about how each function should work.
# 
# So first, create_room_with_components function creates a Room object and adds sensors and actuator instances to its respective lists.
# 
# Then, the helper functions like get_room_sensors iterate through all rooms (in home parameter) to find any room with name matching, then return that room's sensors or actuators. If none found, perhaps they return an empty list or raise an error.
# 
# But since in this case, home is a single Room object because create_room_with_components returns one.
# 
# Wait no: looking at the code:
# 
# In line 28 of home_plan.py (which I can't see), but according to user's initial message, it seems that the functions are part of home_plan.py. So perhaps there are multiple rooms created in home_plan(). But based on the provided code snippet, create_room_with_components is called once for "LivingRoom".
# 
# Wait no, looking at the initial code:
# 
# The first function in home_plan.py (create_room_with_components) creates one room with name 'LivingRoom' and adds various sensors and actuator instances.
# 
# But then further down in the file, helper functions like get_room_sensors are defined. So perhaps these helper functions can be used on multiple rooms if more are created elsewhere.
# 
# So to proceed:
# 
# Implement create_room_with_components as shown.
# 
# Then implement helper function get_room_sensors(room_name) that returns a list of sensors from the room with the given name.
# 
# Similarly, get_room_actuators(room_name) would return the actuator list.
# 
# But in home_plan.py, how are these functions structured?
# 
# Wait no: The code provided starts at line 1-36 is just function create_room_with_components. Then helper functions like get_room_sensors and others are presumably after that.
# 
# So to write this correctly:
# 
# In home_plan.py, the main structure would be:
# 
# Line 28: Function create_room_with_components(...):
# 
# def create_room_with_components(name, sensors, actuators):
#     room = Room(name)
#     for sensor in sensors:
#         room.add_sensors(sensor)
#     for actuator in actuators:
#         room.add_actuators(actuator)
#     return room
# 
# Then helper functions:
# 
# def get_room_sensors(room_name):
#     for room in home_rooms:
#         if room.name == room_name:
#             return room.sensors
#     return None  # or empty list?
# 
# Similarly, def get_room_actuators(room_name) would do the same.
# 
# But perhaps in this scenario, 'home' is a variable that refers to all rooms. Wait no: looking at user's code:
# 
# The initial problem statement includes home_plan.py and config.py as separate files.
# 
# In the helper functions like get_room_sensors, they're probably intended to be used on a list of rooms.
# 
# But perhaps it's better to structure home_plan.py such that create_room_with_components is called for each room in turn, adding them to a list called 'rooms'.
# 
# So perhaps in home_plan.py:
# 
# - Define Room class.
# - Create multiple rooms (maybe via loops or function calls).
# - Then have helper functions that take the rooms and return based on name.
# 
# But according to user's initial code snippet, create_room_with_components is called once for "LivingRoom".
# 
# Hmm. Maybe I'm overcomplicating this.
# 
# Perhaps the key steps are:
# 
# 1. Implement create_room_with_components which creates a Room object with given name, sensors, and actuators.
# 
# 2. Write helper functions like get_room_sensors and get_room_actuators to return all sensors/actuators from a room that matches a given name.
# 
# 3. Then, in the main script (home_plan.py), create multiple rooms if necessary, perhaps by looping through some names or using the function again for each new room.
# 
# But according to user's initial code snippet, it seems only one Room is created via create_room_with_components.
# 
# Wait no: looking back at user's initial question:
# 
# The first part of home_plan.py (lines 1-36) includes a single function create_room_with_components which creates one Room and adds various sensors and actuator instances to it. Then the helper functions are written after that, but in the main script section.
# 
# Wait no: actually, looking at the code provided:
# 
# The first part is home_plan.py (up to line 36), which includes a function create_room_with_components which returns one Room object.
# 
# Then in lines beyond that, perhaps other code exists. But according to user's message, it seems they only provided up to line 36 and config.py starts after that.
# 
# Therefore, the main script section is:
# 
# After creating rooms (probably via multiple calls to create_room_with_components), helper functions like get_room_sensors are called to collect data from these rooms based on room names.
# 
# So in the main code block of home_plan.py:
# 
# home = home_plan()
# 
# Where home_plan() creates a list of rooms with various components, perhaps by looping through predefined room names and calling create_room_with_components for each.
# 
# But without seeing that part, it's challenging. So perhaps I can proceed assuming that 'home' is a list containing all the created Room objects.
# 
# Thus, to write helper functions:
# 
# def get_room_sensors(room_name):
#     for room in home:
#         if room.name == room_name:
#             return room.sensors
#     return None
# 
# Similarly for actuators.
# 
# But perhaps these functions need to be written as part of home_plan.py. So including them after the create_room_with_components function.
# 
# So putting this together, here's how the code could look:
# 
# First, define Room class with add_sensors and add_actuators methods.
# 
# Then, define create_room_with_components function which takes a name, sensors list, actuators list, and creates a new Room object, adding each sensor and actuator to that room.
# 
# Then, helper functions like get_room_sensors(room_name) iterate through home (a list of Rooms) and return the first room's sensors with matching name. If none found, perhaps return an empty list or None.
# 
# Similarly for get_room_actuators.
# 
# But in code:
# 
# class Room:
#     def __init__(self, name):
#         self.name = name
#         self.sensors = []
#         self.actuators = []
# 
#     def add_sensors(self, sensor):
#         self.sensors.append(sensor)
# 
#     def add_actuators(self, actuator):
#         self.actuators.append(actuator)
# 
# def create_room_with_components(name, sensors_list, actuators_list):
#     room = Room(name)
#     for sensor in sensors_list:
#         room.add_sensors(sensor)
#     for actuator in actuators_list:
#         room.add_actuators(actuator)
#     return room
# 
# def get_room_sensors(room_name):
#     for room in home:
#         if room.name == room_name:
#             return room.sensors
#     return []
# 
# def get_room_actuators(room_name):
#     for room in home:
#         if room.name == room_name:
#             return room.actuators
#     return []
# 
# Then, in the main part of home_plan.py:
# 
# rooms = []
# for name in ['bedroom', 'kitchen', 'bathroom']:
#     sensors = [s1, s2, ...]
#     actuators = [a1, a2, ...]
#     rooms.append(create_room_with_components(name, sensors, actuators))
# 
# home = rooms
# 
# Then call get_room_sensors('bedroom') to retrieve the sensors.
# 
# But without knowing exactly how 'home' is structured, perhaps in the main block, home is defined as a list of Rooms created via create_room_with_components for each room name.
# 
# Thus, this code structure should work.
# 
# Testing:
# 
# Suppose we have three rooms: bedroom, kitchen, bathroom. Each has their own sensors and actuators added when create_room_with_components is called. Then calling get_room_sensors('kitchen') returns the actuator list from the kitchen room.
# </think>
# 
# To solve this problem, we need to manage a collection of rooms, each with specific components such as sensors and actuators. The goal is to create a system that allows us to easily retrieve these components based on the room name.
# 
# ### Approach
# 1. **Define a Room Class**: This class will encapsulate the properties of a room, including its name, list of sensors, and list of actuators.
# 2. **Create Rooms with Components**: A function will be used to create rooms dynamically by adding predefined sensor and actuator components.
# 3. **Helper Functions for Retrieval**: Two helper functions will allow us to retrieve all sensors and actuators for a specific room based on its name.
# 
# ### Solution Code
# 
# ```python
class Room:
    def __init__(self, name):
        self.name = name
        self.sensors = []
        self.actuators = []

    def add_sensors(self, sensor):
        self.sensors.append(sensor)

    def add_actuators(self, actuator):
        self.actuators.append(actuator)


def create_room_with_components(name, sensors_list, actuators_list):
    room = Room(name)
    for sensor in sensors_list:
        room.add_sensors(sensor)
    for actuator in actuators_list:
        room.add_actuators(actuator)
    return room


def get_room_sensors(room_name):
    for room in home:
        if room.name == room_name:
            return room.sensors
    return []


def get_room_actuators(room_name):
    for room in home:
        if room.name == room_name:
            return room.actuators
    return []
# ```
# 
# ### Explanation
# 1. **Room Class**: This class initializes with a name and empty lists for sensors and actuators. It includes methods to add sensors and actuators, which are then stored as attributes of the instance.
# 2. **create_room_with_components Function**: This function takes a room name, a list of sensor components, and a list of actuator components. It creates an instance of the Room class, adds each component from the respective lists, and returns the created room.
# 3. **get_room_sensors and get_room_actuators Functions**: These functions iterate over a list of rooms (referred to as `home`) and return the sensors or actuators for the room with the specified name. If no matching room is found, they return empty lists.
# 
# This approach allows us to manage multiple rooms efficiently, adding components dynamically and retrieving them based on their names using simple and intuitive helper functions.