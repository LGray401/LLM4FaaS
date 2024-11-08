# This is a well-structured and organized codebase for a home automation system. It defines various sensors and actuators, as well as rooms within the home. Here's a breakdown of the code:
# 
# **Classes**
# 
# The code defines several classes to represent different components of the home automation system:
# 
# * `Room`: Represents a room within the home. It has attributes for name, sensors, and actuators.
# * `Sensor` (not shown in this code snippet): A base class for various types of sensors.
# * `Actuator` (not shown in this code snippet): A base class for various types of actuators.
# 
# **Components**
# 
# The code defines several specific components:
# 
# * `LightIntensiveSensor`: Represents a light-intensive sensor.
# * `IndoorTemperatureSensor`: Represents an indoor temperature sensor.
# * `HumiditySensor`: Represents a humidity sensor.
# * `Door`: Represents a door actuator.
# * `Light`: Represents a light actuator.
# * `Window`: Represents a window actuator.
# * `Curtain`: Represents a curtain actuator.
# * `MusicPlayer`: Represents a music player actuator.
# * `SmartSocket`: Represents a smart socket actuator.
# * `CleaningRobot`: Represents a cleaning robot actuator.
# * `SmartTV`: Represents a smart TV actuator.
# * `AC`: Represents an air conditioner actuator.
# * `Heater`: Represents a heater actuator.
# 
# **Functions**
# 
# The code defines several functions to interact with the home automation system:
# 
# * `create_room_with_components`: Creates a room with specified sensors and actuators.
# * `home_plan`: Returns a list of rooms within the home, each with their respective sensors and actuators.
# * `print_home_plan`: Prints out the home plan, including all rooms and their components.
# * `get_room`: Retrieves a specific room by name from the home plan.
# * `get_room_sensors`/`get_room_actuators`: Retrieves all sensors or actuators within a specific room.
# * `get_all_sensors`/`get_all_actuators`: Retrieves all instances of a specific sensor or actuator type across all rooms.
# 
# **config.py**
# 
# The code includes a separate file called `config.py`, which contains configuration settings for the home automation system, such as temperature and humidity thresholds, as well as duration windows.
# 
# Overall, this codebase provides a solid foundation for a home automation system, with a clear structure and organization. It allows users to define rooms within their home, add various sensors and actuators, and interact with these components through a set of functions.