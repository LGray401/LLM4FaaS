# This code defines a home automation system with various rooms, sensors, and actuators. Here's a breakdown of the code:
# 
# **Components**
# 
# The code defines several components:
# 
# * `Room`: A class representing a room in the home. It has methods to add sensors and actuators.
# * `Sensor` and `Actuator`: Base classes for sensors and actuators, respectively. They have attributes like `id`, `sensor_type`, and `actuator_type`.
# * Specific sensor and actuator types are defined as subclasses of `Sensor` and `Actuator`, such as:
# 	+ `LightIntensiveSensor`
# 	+ `IndoorTemperatureSensor`
# 	+ `HumiditySensor`
# 	+ `Door`
# 	+ `Light`
# 	+ `Window`
# 	+ `Curtain`
# 	+ `MusicPlayer`
# 	+ `SmartSocket`
# 	+ `CleaningRobot`
# 	+ `SmartTV`
# 	+ `NotificationSender`
# 	+ `AC`
# 	+ `Heater`
# 
# **Home Plan**
# 
# The code defines a `home_plan` function that creates a home with multiple rooms, each with its own set of sensors and actuators.
# 
# * The `create_room_with_components` function is used to create a room with the specified components (sensors and actuators).
# * The `home_plan` function returns a list of rooms, which represents the home plan.
# 
# **Utilities**
# 
# The code defines several utility functions:
# 
# * `print_home_plan`: Prints the home plan.
# * `get_room`: Returns a specific room by name.
# * `get_room_sensors`: Returns all sensors in a specific room.
# * `get_room_actuators`: Returns all actuators in a specific room.
# * `get_all_sensors`: Returns all sensors of a specific type throughout the entire home.
# * `get_all_actuators`: Returns all actuators of a specific type throughout the entire home.
# 
# **Config**
# 
# The code defines a separate file called `config.py` that contains configuration settings, such as temperature and humidity thresholds.
# 
# Overall, this code provides a solid foundation for a home automation system with various sensors and actuators. It also includes utility functions to interact with the system.