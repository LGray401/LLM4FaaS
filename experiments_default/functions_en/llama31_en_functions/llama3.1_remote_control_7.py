# This is a Python code snippet that appears to be part of an IoT home automation system. The code defines various classes and functions for managing rooms, sensors, and actuators in the system.
# 
# Here's a breakdown of the code:
# 
# **Classes**
# 
# 1. `Room`: Represents a room in the house with its name, sensors, and actuators.
# 2. `Sensor` (not shown): A base class for sensors.
# 3. `Actuator` (not shown): A base class for actuators.
# 
# **Functions**
# 
# 1. `create_room_with_components(name, sensor_types, actuator_types)`: Creates a room with specified sensors and actuators.
# 2. `home_plan()`: Returns a list of rooms with their components (sensors and actuators).
# 3. `print_home_plan(home)`: Prints the home plan, including all rooms and their components.
# 4. `get_room(home, room_name)`: Retrieves a specific room by name from the home plan.
# 5. `get_room_sensors(home, room_name)` and `get_room_actuators(home, room_name)`: Return the sensors or actuators of a specific room.
# 6. `get_all_sensors(home, sensor_type)` and `get_all_actuators(home, actuator_type)`: Return all instances of a specific sensor type or actuator type from the home plan.
# 
# **Config**
# 
# The code includes a separate file called `config.py` that defines constants for temperature thresholds (low/high), humidity thresholds (low/high), light intensity thresholds (low/high), and daily routine duration. These values are used in the system to determine whether certain actions should be taken based on sensor readings.
# 
# Overall, this code snippet appears to be part of a larger IoT home automation system that uses sensors and actuators to monitor and control various aspects of the home environment.