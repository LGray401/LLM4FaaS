# This is a Python script that defines classes and functions to manage home automation devices. Here's a breakdown of the code:
# 
# **Importing Modules**
# 
# The script starts by importing various modules, including `logger_config` from `home.logger_config`, which suggests that there's a logging configuration file in the `home` package.
# 
# **Class Definitions**
# 
# The script defines several classes:
# 
# 1. `Room`: Represents a room in the home with attributes `name`, `sensors`, and `actuators`. It has methods to add sensors and actuators, as well as print information about the room.
# 2. `Sensor` and `Actuator`: These are abstract base classes that represent sensors and actuators, respectively. They have attributes `id`, `sensor_type` (for sensors), and `actuator_type` (for actuators).
# 
# **Function Definitions**
# 
# The script defines several functions:
# 
# 1. `create_room_with_components`: Creates a room with the specified name, sensor types, and actuator types.
# 2. `home_plan`: Generates a home plan by creating rooms with various components (sensors and actuators).
# 3. `print_home_plan`: Prints the generated home plan.
# 4. `get_room`, `get_room_sensors`, and `get_room_actuators`: These functions retrieve information about a specific room, its sensors, or actuators.
# 
# **Utility Functions**
# 
# The script also defines utility functions:
# 
# 1. `get_all_sensors` and `get_all_actuators`: Retrieve all sensors or actuators of a specific type from the home plan.
# 2. `print_home_plan`, which prints the generated home plan.
# 
# **Main Execution**
# 
# The script includes a `if __name__ == "__main__":` block, which allows it to be executed as a standalone script. In this case, it generates a home plan and retrieves information about all lights in the plan.
# 
# **config.py**
# 
# The script also includes a separate file named `config.py`, which defines constants for temperature, humidity, light intensity, and daily routine duration. These values can be used throughout the script to configure the behavior of sensors and actuators.
# 
# Overall, this code provides a basic framework for managing home automation devices in Python. It allows you to create rooms with various components, retrieve information about specific rooms or devices, and generate a home plan.