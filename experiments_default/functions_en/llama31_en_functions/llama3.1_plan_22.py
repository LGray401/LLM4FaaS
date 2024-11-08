# This is a Python script that defines classes and functions for simulating home automation. Here's a breakdown of the code:
# 
# **Class `Room`**
# 
# * Represents a room in the house with its own sensors and actuators.
# * Has methods to add sensors and actuators, print information about the room.
# 
# **Function `create_room_with_components`**
# 
# * Creates a new Room object with specified sensor types and actuator types.
# * Adds instances of each type to the room's sensors and actuators lists.
# 
# **Function `home_plan`**
# 
# * Defines a list of rooms in the house, each with its own set of sensors and actuators.
# * Uses `create_room_with_components` to create Room objects for each room.
# * Returns the list of Room objects.
# 
# **Functions for querying the home plan**
# 
# * `get_room`: returns a specific Room object by name.
# * `get_room_sensors`/`get_room_actuators`: return lists of sensors or actuators in a specific Room.
# * `get_all_sensors`/`get_all_actuators`: return lists of all sensors or actuators of a certain type across all rooms.
# 
# **Config file (`config.py`)**
# 
# * Defines constants for temperature, humidity, and light intensity thresholds.
# * Specifies the duration of daily routines.
# 
# The script is organized into two main parts: the `Room` class and its associated functions in one file, and the `home_plan()` function and related query functions in another file. This separation makes it easier to understand and maintain the code.
# 
# However, there are a few issues with the code:
# 
# 1. The `get_room()` function returns None if the room is not found, but this value is then used as-is in subsequent calls (e.g., `room.print_info()`). It would be better to raise an exception or return a specific error message.
# 2. The `get_all_sensors()` and `get_all_actuators()` functions iterate over all rooms, which could be inefficient if the home plan contains many rooms. Consider using a more efficient data structure (e.g., a dictionary with room names as keys) to store the Room objects.
# 3. Some function names are not descriptive (e.g., `print_home_plan()`, `get_room_sensors()`). Consider renaming these functions to better reflect their purpose.
# 
# To improve the code, consider addressing these issues and adding more documentation to explain the purpose of each function and class.