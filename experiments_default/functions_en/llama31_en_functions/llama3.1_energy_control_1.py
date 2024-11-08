# This is a Python script that appears to be part of a smart home automation system. It defines classes and functions for various components, such as sensors and actuators, and uses them to create a home plan with multiple rooms.
# 
# Here's a breakdown of the code:
# 
# **Components**
# 
# The script defines several classes:
# 
# * `Room`: represents a room in the house, with attributes for name, sensors, and actuators.
# * `Sensor` (not shown): likely an abstract base class or interface for sensors, with attributes for id and sensor type.
# * Various sensor-specific classes: e.g., `LightIntensiveSensor`, `IndoorTemperatureSensor`, etc.
# 
# Similarly, it defines several actuator classes:
# 
# * `Actuator` (not shown): likely an abstract base class or interface for actuators, with attributes for id and actuator type.
# * Various actuator-specific classes: e.g., `Door`, `Light`, etc.
# 
# **Home Plan**
# 
# The script uses the `create_room_with_components` function to create a home plan with multiple rooms. Each room is created by specifying its name and adding various sensors and actuators using the corresponding class constructors.
# 
# For example, the "LivingRoom" has:
# 
# * 3 sensors: `LightIntensiveSensor`, `IndoorTemperatureSensor`, and `HumiditySensor`
# * 10 actuators: `Door`, `Light`, `Window`, etc.
# 
# **Functions**
# 
# The script defines several functions to interact with the home plan:
# 
# * `print_home_plan`: prints out the details of each room in the home plan.
# * `get_room`: retrieves a specific room from the home plan by name.
# * `get_room_sensors` and `get_room_actuators`: retrieve all sensors or actuators in a given room, respectively.
# * `get_all_sensors` and `get_all_actuators`: retrieve all sensors or actuators of a specific type throughout the entire home plan.
# 
# **Configuration**
# 
# The script includes a separate file called `config.py`, which contains some constants for temperature thresholds, humidity ranges, light intensity values, and other settings. These values are not used in this code snippet, but may be used elsewhere in the system.
# 
# Overall, this code provides a basic framework for building and managing a home plan with various sensors and actuators, using object-oriented programming principles and modular design.