# <think>
# Okay, I need to help the user with their code. They provided three files: preparation.py, config.py, and home_plan.py. Let me look through each one.
# 
# Starting with preparation.py. It has classes like SmartSocket, Door, etc., which are part of a logger_config module that's imported but not shown here. Then there's a Room class with sensors and actuators. The create_room_with_components function adds various components to the room.
# 
# In home_plan.py, they're creating rooms using create_room_with_components and then trying to get all sensors or actuators for a specific type. They call functions like get_all_sensors and get_all_actuators.
# 
# Wait, in preparation.py's Actuator class, there's an __init__ method that takes name and id as parameters. But when creating instances like SmartSocket(name), it doesn't pass these. That might be a problem because the actuator won't know its type or ID correctly.
# 
# Looking at home_plan.py, they're trying to get all sensors of type "IndoorTemperature" using get_all_sensors. Similarly for actuators. The functions iterate through rooms and collect sensors where sensor_type matches. But maybe in preparation.py's Actuator class, the sensor_type isn't being set properly when initializing.
# 
# Also, I noticed that the Room class has a print_info method which prints each sensor with just their id. That might not be very informative as it won't show the actual sensor type or name.
# 
# The user probably wants to fix how sensors and actuators are created in preparation.py so that they have proper types and IDs. Also, they might need help improving the print_info method for better clarity when rooms are printed.
# 
# Another thought: maybe the way get_room_sensors and get_room_actuators work is inefficient because they loop through all rooms each time. Perhaps moving this logic into the Room class or using a different data structure could be more efficient, but that might be beyond the current scope.
# 
# So, to summarize my thoughts:
# 
# 1. The Actuator's __init__ method in preparation.py isn't correctly setting name and id, which are needed for identification.
# 2. The sensor_type check in get_all_sensors might not work if the sensors' type attribute is not correctly set during creation.
# 3. The Room's print_info method could be improved to display more informative data beyond just IDs.
# 
# I should provide a step-by-step explanation on how to fix these issues, maybe by adding name and id parameters when creating Actuator instances and ensuring that sensor_type is properly handled. Also, enhancing the print_info method would make debugging easier.
# </think>
# 
# Looking at your code, I notice a few issues:
# 
# 1. The `Actuator` class in `preparation.py` doesn't initialize with `name` or `id` parameters
# 2. The `get_all_sensors` and `get_all_actuators` functions might not be working correctly due to how sensor types are matched
# 
# Here's how we can fix these issues:
# 
# 1. First, let's modify the Actuator class initialization in preparation.py:
# 
# preparation.py
# ```python
<<<<<<< SEARCH
    def __init__(self, name):
=======
    def __init__(self, name, actuator_type):
        self.name = name
        self.actuator_type = actuator_type
>>>>>>> REPLACE
# ```
# 
# 2. Then let's modify the get_all_sensors and get_room_sensors functions to properly filter by sensor type:
# 
# home_plan.py
# ```python
<<<<<<< SEARCH
    for room in home:
        # if room.name.lower() == room_name.lower():
        if room.name == room_name:
            # room.print_info()
            return room.sensors

    print(f"there is no Sensor found in {room_name}")
    logger.warning(f"there is no Sensor found in {room_name}")
    return None  # no room_name room
=======
    for room in home:
        if room.name == room_name:
            sensor_list = []
            for sensor in room.sensors:
                if isinstance(sensor, sensor_type) and hasattr(sensor, 'sensor_type') and sensor.sensor_type == sensor_type:
                    sensor_list.append(sensor)
            return sensor_list

    print(f"there is no Sensor found in {room_name}")
    logger.warning(f"there is no Sensor found in {room_name}")
    return None  # no room_name room
>>>>>>> REPLACE
# ```
# 
# To test these changes, you can use this command to run the example:
# 
# ```bash
python home_plan.py
# ```
# 
# These changes will:
# 1. Properly initialize Actuator instances with name and type
# 2. Improve the sensor filtering in get_room_sensors function
# 3. Make it easier to identify sensors by their types
# 
# You might also want to improve the print_info method in the Room class to make debugging easier:
# 
# Room.print_info():
# ```python
def print_info(self):
    print(f"\n{self.name}:")
    print("Sensors:")
    for sensor in self.sensors:
        print(f"{sensor.__class__.__name__} {sensor.name}")
    print("\nActuators:")
    for actuator in self.actuators:
        print(f"{actuator.__class__.__name__} {actuator.name}")
# ```
# 
# This will show the actual class names and IDs of sensors and actuators.