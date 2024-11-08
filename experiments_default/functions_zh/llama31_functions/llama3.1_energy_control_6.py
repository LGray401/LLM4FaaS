# This code is a Python implementation of a smart home system. It defines classes for sensors and actuators, and uses these to create a home plan with various rooms and their corresponding components.
# 
# Here's a breakdown of the code:
# 
# **Classes**
# 
# * `Room`: Represents a room in the house. It has methods to add sensors and actuators.
# * `Sensor` and `Actuator`: Base classes for different types of sensors and actuators. They have an `id` attribute and can be added to a room.
# 
# **Concrete Sensor and Actuator Classes**
# 
# * `LightIntensiveSensor`, `IndoorTemperatureSensor`, `HumiditySensor`, etc.: Specific sensor classes that inherit from `Sensor`.
# * `Door`, `Light`, `Window`, `Curtain`, `MusicPlayer`, etc.: Specific actuator classes that inherit from `Actuator`.
# 
# **Functions**
# 
# * `create_room_with_components`: Creates a room with the specified sensors and actuators.
# * `home_plan`: Returns a list of rooms, each with their corresponding components.
# * `print_home_plan`: Prints out the home plan with all rooms and their components.
# * `get_room`, `get_room_sensors`, `get_room_actuators`, `get_all_sensors`, and `get_all_actuators`: Helper functions to retrieve specific information about a room or its components.
# 
# **config.py**: This is a separate file that contains configuration variables, such as temperature thresholds and wait durations. These values can be adjusted as needed.
# 
# The code uses a modular approach, with each component (sensor or actuator) having its own class. The `Room` class serves as a container for these components. The functions provided can be used to query the home plan and retrieve specific information about the rooms and their components.
# 
# Overall, this is a well-structured and maintainable codebase that can serve as a foundation for building a more complex smart home system.