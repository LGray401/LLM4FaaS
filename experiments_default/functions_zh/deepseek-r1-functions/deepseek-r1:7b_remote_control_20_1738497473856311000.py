# <think>
# Okay, I need to write a Python program that simulates a home automation system based on the provided code. Let's see what each part does and how they interact.
# 
# First, looking at config.py, it defines some thresholds for temperature, humidity, light intensity, etc., which probably control when certain sensors trigger actions.
# 
# The main script is home_plan(), which creates rooms with various sensors and actuators. Each room has its own setup of these components. For example, the LivingRoom has a LightIntensiveSensor and others like Door, MusicPlayer, etc.
# 
# In the code for Room class in the Room creation function, each sensor adds itself to the room's sensors list, and similarly for actuators. The print_info method prints out all the sensors and actuators in each room with their IDs.
# 
# The functions get_room, get_room_sensors, and get_room_actuators are meant to retrieve specific rooms or their components from the home structure. They check if a room exists by name and then return either the sensors or actuators of that room.
# 
# Wait, but looking at create_room_with_components, it's adding multiple instances for each sensor type in sensor_types. For example, LivingRoom adds three sensors: LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor. But wait, if you have [LightIntensiveSensor], then room.add_sensor(sensor_type(name)) will call the constructor with name as an argument.
# 
# Wait no, actually, create_room_with_components loops through each sensor_type in sensor_types and adds them to the room by calling add_sensor with sensor_type(name). So for example, if a sensor is LightIntensiveSensor, it's created per type. But then when you have multiple of the same type, like two Light sensors in a bedroom, how are they handled? Because each time, it creates an instance.
# 
# Wait no, looking at create_room_with_components, for each sensor_type (e.g., [LightIntensiveSensor, ...]), room.add_sensor(sensor_type(name)). So if you have multiple instances of the same sensor type, like two Light sensors in the bedroom, they are added as separate entries. Similarly for actuators.
# 
# So the home_plan function builds up a list of rooms by creating each one with their respective components.
# 
# The main part to run is at the bottom where it creates 'home' and then calls print_home_plan, which prints out all the rooms' info.
# 
# But when I look at the if __name__ == "__main__" block, there's code that seems to get room sensors or actuators. But in this case, perhaps it's just an example for testing.
# 
# Now, looking back at the user instructions: they provided several files and want me to write a program based on them. The assistant needs to process these components into rooms, add their sensors and actuators, then output information about each room.
# 
# Wait, maybe I need to create a script that, when run, takes home_plan() as input and outputs the room's details, including all their sensors and actuators, similar to how print_home_plan works.
# 
# So perhaps in the main function, after creating 'home', it loops through each room and prints its info using room.print_info().
# 
# Looking at Room's print_info method: for each sensor in self.sensors, it just prints "-" followed by the sensor.id. Similarly for actuators.
# 
# But some of these sensors are not shown as having their own IDs; perhaps because they inherit from a common base class or something similar? For example, LightIntensiveSensor and IndoorTemperatureSensor might be subclasses with an 'id' attribute that's unique per instance.
# 
# In any case, the program needs to:
# 
# 1. Create all rooms using home_plan().
# 2. Print each room's details.
# 3. Possibly interact with get_room functions if needed.
# 
# Wait, but in the example code at the bottom of home_plan(), they have some calls like get_room_sensors or get_room_actuators, which return lists based on a given room name and sensor type.
# 
# But for this problem, perhaps I just need to run through each room and print their information as per the Room's print_info method.
# 
# So in the main script after home_plan(), we can loop over each room in 'home' (the list of created rooms) and call room.print_info().
# 
# Additionally, maybe there are other functionalities like getting all sensors or actuators for a particular type. But perhaps that's beyond the current scope.
# 
# Wait, but looking at config.py, some variables define thresholds for temperature change, humidity levels, etc., which might affect how sensors operate. For example, when the temperature goes above TEMP_HIGH, an action is triggered by a sensor.
# 
# But in the provided code, I don't see any event handling or rules being implemented based on these thresholds. So perhaps that's part of a different feature not required here.
# 
# So putting it all together: The main steps are:
# 
# 1. Create rooms using home_plan().
# 2. For each room, print its sensors and actuators.
# 3. Use the get_room functions as needed (like fetching specific rooms or their components).
# 
# But in this case, since I'm just to write a program based on these files without additional features, perhaps it's sufficient to create the rooms and print them.
# 
# Wait, but looking back at the code structure:
# 
# The Room class has an __init__ method that adds all sensors and actuators. So each room is initialized with its components.
# 
# But when I look at home_plan(), for example, in the LivingRoom creation: sensor_types are [LightIntensiveSensor], but then also have multiple instances of other sensors like IndoorTemperatureSensor? Or wait no—no, looking again:
# 
# The function create_room_with_components adds all the sensors and actuators as per their types. So if a room is created with sensor_types = [LightIntensiveSensor], it creates one instance for that type (assuming each sensor_type is a class). But when you have multiple instances in the same room, like two Light sensors, they are added separately.
# 
# Wait, no: Looking at create_room_with_components, for example:
# 
# def home_plan():
#     rooms = []
#     # LivingRoom
#     name = "living_room"
#     room = Room(name)
#     sensor_types = [LightIntensiveSensor]
#     actuator_types = [Door, ...]
#     room.add_sensors([LightIntensiveSensor(name) for _ in sensor_types])
#     ...
# So if sensor_types has multiple instances of the same class (e.g., two Light sensors), then each is added as a separate instance.
# 
# Wait no, because the first argument to create_room_with_components is a list. For example:
# 
# In the code: rooms.append( Room(name) )
# 
# But let's look at how each room is built in home_plan():
# 
# For example:
# living_room = Room("living_room")
# living_room.add_sensors([LightIntensiveSensor(name)])
# living_room.add_sensors([IndoorTemperatureSensor(name), ...])
# Similarly for actuators.
# 
# Wait, no: Looking at the code:
# 
# In home_plan(), for living_room, it's added as a list of sensors and actuators. For example:
# sensors = [LightIntensiveSensor(name)]
# sensors += [IndoorTemperatureSensor(name)] * 3
# So that would add one LightIntensive, three IndoorTemp.
# 
# Wait no: the code is:
# 
# sensors = []
# ...
# sensors += [LightIntensiveSensor(name)]
# sensors += [IndoorTemperatureSensor(name) for _ in range(3)]
# 
# Similarly for actuators. So each room's sensors and actuators are lists created by adding multiple instances of their respective classes.
# 
# So, when a room has many sensors or actuators, they're all added as separate entries to the room's list.
# 
# Each sensor and actuator probably have an 'id' attribute that allows them to be uniquely identified. So in Room's print_info method, for each sensor, it prints "-" followed by its id.
# 
# Now, about the main function: The code at the bottom shows how get_room can be used, but perhaps I need to write a script that does something like this:
# 
# - Create home via home_plan().
# - For each room, retrieve all sensors and actuators.
# But in our case, since we just have the list of rooms, maybe it's enough to loop through them and print their info.
# 
# So putting it together: The program needs to create the rooms as per home_plan(), then for each room, call print_info() which lists all its sensors and actuators with their IDs.
# 
# Now, considering how to write this code:
# 
# The main part would be after creating 'home' (the list of Room objects), loop through each room in home and call print_info(room). But looking at the provided code structure, is there a print_home_plan function? No, it seems that in the example, they have some calls but no actual output.
# 
# So perhaps I need to add this functionality. Alternatively, since the user hasn't specified whether to implement any specific functions beyond what's given, maybe just creating rooms and printing their info.
# 
# Thus, the main code would be:
# 
# if __name__ == "__main__":
#     home = home_plan()
#     for room in home:
#         print(room.print_info())
# 
# But wait, looking at Room's print_info method: it returns a string with each sensor and actuator listed. So when you call print(room.print_info()), it prints that string.
# 
# Alternatively, perhaps we need to extract the list of sensors and actuators from each room and process them.
# 
# Wait, but in the provided code for the Room class:
# 
# def print_info(self):
#     print("Room: " + self.name)
#     print("Sensors:")
#     for sensor in self.sensors:
#         print(f"- {sensor.id}")
#     print()
#     print("Actuators:")
#     for actuator in self.actuators:
#         print(f"- {actuator.id}")
# 
# So each room's print_info method prints the name, followed by sensors and actuators with their IDs.
# 
# Therefore, to make this work, I need to have a Room class that has 'sensors' and 'actuators' attributes. But in the code provided, it seems like when creating a room, we add sensors via add_sensors() and similarly for actuators.
# 
# Wait no: Looking at home_plan(), each room is created as:
# 
# room = Room(name)
# 
# Then, for sensors:
# 
# sensors = []
# 
# # Add some LightIntensiveSensors
# sensors += [LightIntensiveSensor(name)] * 3
# 
# # Add some more, like IndoorTemperatureSensor
# sensors += [IndoorTemperatureSensor(name) for _ in range(3)]
# 
# So room.add_sensors(sensors)
# 
# Similarly for actuators.
# 
# Thus, each room has 'sensors' and 'actuators' attributes as lists of sensor/actuator objects.
# 
# Now, to implement this code:
# 
# I'll need to write the Room class with add_sensors() and add_actuators() methods that take a list of objects (sensors or actuators) and add them to the respective lists in the room. Then, each room's print_info() method will loop through these lists.
# 
# So first, implement the Room class:
# 
# class Room:
#     def __init__(self, name):
#         self.name = name
#         self.sensors = []
#         self.actuators = []
# 
#     def add_sensors(self, sensors_list):
#         for sensor in sensors_list:
#             self.sensors.append(sensor)
# 
#     def add_actuators(self, actuators_list):
#         for actuator in actuators_list:
#             self.actuators.append(actuator)
# 
#     def print_info(self):
#         print(f"Room: {self.name}")
#         print("Sensors:")
#         for sensor in self.sensors:
#             print(f"- {sensor.id}")
#         print()
#         print("Actuators:")
#         for actuator in self.actuators:
#             print(f"- {actuator.id}")
# 
# Then, implement the home_plan() function:
# 
# def home_plan():
#     rooms = []
#     
#     # Living Room
#     name = "living_room"
#     room = Room(name)
#     sensors = [LightIntensiveSensor(name)] * 3 + [IndoorTemperatureSensor(name) for _ in range(3)]
#     actuators = [Door(name), ... ] ? Wait, no: Looking at the provided code:
# 
# In home_plan(), after adding to the room's sensors and actuators.
# 
# For example:
# sensors are added as a list with LightIntensiveSensor instances, each having 'name' attribute set. Similarly for actuators like Door.
# 
# Thus, in home_plan():
# 
# def home_plan():
#     rooms = []
#     
#     # Living Room
#     name = "living_room"
#     room = Room(name)
#     sensors = [LightIntensiveSensor(name)] * 3 + [IndoorTemperatureSensor(name) for _ in range(3)]
#     actuators = [Door(name), SwivelChair(name), Bookshelf(name), CoffeeTable(name), ...
#                   # other actuators
#     ]
#     room.add_sensors(sensors)
#     room.add_actuators(actuators)
#     rooms.append(room)
# 
# And similarly for other rooms like Dining Room, Kitchen, etc.
# 
# Once home_plan() is correctly implemented and all rooms are created with their respective sensors and actuators, then the main script can loop through each room and print its info.
# 
# Putting it all together:
# 
# But wait, in the provided code snippet, there's no import of these classes. So I'll need to include necessary imports or define them within home_plan()?
# 
# Alternatively, perhaps I should write a complete Python file that defines the Room class and functions, then creates rooms as per home_plan(), then prints their info.
# 
# So the full program would be:
# 
# 1. Define the Room class.
# 2. Define helper functions like add_sensors and add_actuators if necessary (but in this case, perhaps better to have them within home_plan() or outside?).
# 3. Implement home_plan() as per the structure given in the problem statement.
# 
# Wait, but looking back at the provided code:
# 
# The helper functions are not shown; instead, the room is created and then the sensors and actuators are added via loops.
# 
# So perhaps it's better to implement home_plan() without helper functions, directly adding each sensor and actuator.
# 
# But that might be tedious for multiple rooms with many components. For example, in the provided code:
# 
# def home_plan():
#     rooms = []
#     
#     # Living Room
#     name = "living_room"
#     room = Room(name)
#     sensors = []
#     sensors += [LightIntensiveSensor(name)] * 3
#     sensors += [IndoorTemperatureSensor(name) for _ in range(3)]
#     # and so on...
#     room.add_sensors(sensors)
#     ...
# Similarly for other rooms.
# 
# Thus, to make this manageable, perhaps it's better to create a helper function that adds a type of sensor or actuator multiple times. But since each sensor is unique (based on name), creating instances with the same name would result in different objects but sharing some attributes.
# 
# Wait, no: Each LightIntensiveSensor instance has its own 'name' attribute, which could be set to the room's name when created.
# 
# Thus, for the living room:
# 
# sensors = []
# sensors.append(LightIntensiveSensor(name))
# sensors.append(LightIntensiveSensor(name))
# sensors.append(LightIntensiveSensor(name))
# sensors.append(IndoorTemperatureSensor(name))
# ... etc.
# 
# But this is error-prone if there are many sensors and actuators. So perhaps a loop that creates all the necessary instances for each room type, multiplying as needed.
# 
# Alternatively, given time constraints, perhaps implement home_plan() directly by adding the required components.
# 
# Once the code structure is correct, then the main script can call home_plan(), which returns a list of rooms, then iterate over them and print their info using the print_info method.
# 
# Testing this approach:
# 
# For example, in the living room:
# 
# - 3 LightIntensiveSensors with name 'living_room'
# - 3 IndoorTemperatureSensors with name 'living_room'
# - etc.
# 
# Each sensor has an id attribute (probably unique per object).
# 
# Thus, when printed, each will show as "- 123", where 123 is the id of that particular instance.
# 
# So the code should correctly create rooms and print their info.
# 
# Now, in terms of writing this:
# 
# First, write the Room class with __init__, add_sensors, add_actuators, and print_info methods.
# 
# Then, implement home_plan() as per the problem's structure.
# 
# But wait, looking at the initial provided code snippet:
# 
# The helper functions (like add_sensors) are called to add a list of sensors. Thus, in home_plan(), for each room, after creating it, we have to create a list of all sensors and call add_sensors on them.
# 
# Therefore, within home_plan():
# 
# For the living room:
# sensors = []
# for i in range(3):
#     sensors.append(LightIntensiveSensor(name))
# for i in range(3):
#     sensors.append(IndoorTemperatureSensor(name))
# room.add_sensors(sensors)
# Same for other rooms.
# 
# Thus, this approach is manageable but requires a lot of code duplication. To avoid that, perhaps write helper functions inside home_plan() to add multiple instances.
# 
# But since the problem statement doesn't specify any constraints on the code's conciseness beyond what's in the initial snippet, it's acceptable to proceed with direct implementation.
# 
# Thus, putting all together:
# 
# Implement Room class as defined above, then define home_plan(), create each room by adding appropriate sensors and actuators, then print their info.
# 
# Testing this should output the correct structure of rooms with their respective sensors and actuators.
# </think>
# 
# To solve this problem, we need to create a set of rooms with specific sensors and actuators. Each room will have its own list of sensors and actuators, which can be added programmatically. The goal is to define each room's characteristics and print out the information for each room in a structured format.
# 
# ### Approach
# 1. **Define a Room Class**: This class will encapsulate the properties and methods needed to represent a room. Each room will have a name, a list of sensors, and a list of actuators.
# 2. **Add Sensors and Actuators**: For each room type (e.g., Living Room, Dining Room), we will create instances of sensor and actuator classes and add them to the respective lists in the room object.
# 3. **Print Room Information**: Each room's information will be printed in a structured format that includes the room name, followed by its sensors and actuators.
# 
# ### Solution Code
# ```python
class Room:
    def __init__(self, name):
        self.name = name
        self.sensors = []
        self.actuators = []

    def add_sensors(self, sensors_list):
        for sensor in sensors_list:
            self.sensors.append(sensor)

    def add_actuators(self, actuators_list):
        for actuator in actuators_list:
            self.actuators.append(actuator)

    def print_info(self):
        print(f"Room: {self.name}")
        print("Sensors:")
        for sensor in self.sensors:
            print(f"- {sensor.id}")
        print()
        print("Actuators:")
        for actuator in self.actuators:
            print(f"- {actuator.id}")


def home_plan():
    rooms = []

    # Living Room
    name = "living_room"
    room = Room(name)
    sensors = []
    for _ in range(3):
        sensors.append(LightIntensiveSensor(name))
    for _ in range(3):
        sensors.append(IndoorTemperatureSensor(name))
    room.add_sensors(sensors)
    
    # Dining Room
    name = "dining_room"
    room = Room(name)
    sensors = []
    for _ in range(2):
        sensors.append(LightIntensiveSensor(name))
    room.add_sensors(sensors)

    # Kitchen
    name = "kitchen"
    room = Room(name)
    sensors = []
    for _ in range(4):
        sensors.append(LightIntensiveSensor(name))
    for _ in range(2):
        sensors.append(IndoorTemperatureSensor(name))
    room.add_sensors(sensors)

    # Bathroom
    name = "bathroom"
    room = Room(name)
    sensors = []
    for _ in range(3):
        sensors.append(LightIntensiveSensor(name))
    act = []
    for _ in range(2):
        act.append(WaterSensor(name))  # Assuming WaterSensor is another type of sensor
    room.add_sensors(sensors)
    room.add_actuators(act)

    return rooms

# Create the list of rooms
room_list = home_plan()

for room in room_list:
    room.print_info()
# ```
# 
# ### Explanation
# - **Room Class**: This class initializes with a name and empty lists for sensors and actuators. It includes methods to add these elements, which are used when creating each room.
# - **Adding Components**: For each defined room type (Living Room, Dining Room, etc.), we create the necessary sensor and actuator instances and append them to the respective room's list using the `add_sensors` and `add_actuators` methods.
# - **Printing Information**: Each room's details are printed by iterating over its sensors and actuators, displaying their IDs in a structured format.
# 
# This approach ensures that each room is defined with specific components, making it easy to extend or modify as needed. The structured printing of each room's information provides clear and organized output.