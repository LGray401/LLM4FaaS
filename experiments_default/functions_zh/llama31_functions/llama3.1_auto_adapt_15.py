# This code defines a home automation system with various components such as sensors and actuators. Here's an explanation of the code:
# 
# **Room Class**
# 
# The `Room` class represents a room in the house, which can have multiple sensors and actuators.
# 
# *   `__init__`: Initializes the room with a name.
# *   `add_sensor` and `add_actuator`: Adds a sensor or actuator to the room's list of components.
# *   `print_info`: Prints out the room's name, its sensors, and actuators.
# 
# **Home Plan**
# 
# The `home_plan` function creates a home plan by defining multiple rooms with their respective sensors and actuators. The rooms are:
# 
# *   Living Room
# *   Bedroom
# *   Kitchen
# *   Bathroom
# *   Balcony
# 
# Each room has a list of sensors (e.g., temperature, humidity, light intensity) and actuators (e.g., lights, heaters, fans).
# 
# **Utility Functions**
# 
# Several utility functions are defined to interact with the home plan:
# 
# *   `print_home_plan`: Prints out the entire home plan.
# *   `get_room`: Returns a room object based on its name.
# *   `get_room_sensors` and `get_room_actuators`: Return lists of sensors or actuators for a given room.
# *   `get_all_sensors` and `get_all_actuators`: Return all instances of a specific sensor or actuator type across all rooms.
# 
# **Config File**
# 
# The code also includes a `config.py` file, which contains threshold values for temperature, humidity, light intensity, and other settings. These values are used to determine when a certain condition has been met (e.g., when the temperature drops below a certain value).
# 
# Overall, this code provides a basic structure for building a home automation system with multiple rooms and components.
# 
# **Example Usage**
# 
# You can use the code as follows:
# 
# *   Create a home plan using `home_plan()`.
# *   Print out the entire home plan using `print_home_plan(home_plan())`.
# *   Get a specific room object using `get_room(home_plan(), "Living Room")`.
# *   Get all sensors or actuators for a given room using `get_room_sensors(home_plan(), "Kitchen")` or `get_room_actuators(home_plan(), "Bedroom")`.
# *   Get all instances of a specific sensor or actuator type across all rooms using `get_all_sensors(home_plan(), "Temperature Sensor")` or `get_all_actuators(home_plan(), "Light Actuator")`.