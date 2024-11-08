# This is a Python script that defines a home automation system with various rooms and components. Here's a breakdown of the code:
# 
# **Components**
# 
# The script defines several classes for sensors and actuators:
# 
# * `Sensor` (abstract class)
# 	+ `LightIntensiveSensor`
# 	+ `IndoorTemperatureSensor`
# 	+ `HumiditySensor`
# 	+ `OutdoorTemperatureSensor`
# 	+ `SmokeSensor`
# * `Actuator` (abstract class)
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
# These classes inherit from the abstract `Sensor` and `Actuator` classes, respectively.
# 
# **Room Class**
# 
# The `Room` class represents a room in the home automation system. It has attributes for:
# 
# * `name`: the name of the room
# * `sensors`: a list of sensors in the room
# * `actuators`: a list of actuators in the room
# 
# The `add_sensor` and `add_actuator` methods allow adding sensors and actuators to the room.
# 
# **Home Plan**
# 
# The `home_plan` function creates a home automation system with various rooms, each containing specific sensors and actuators. The function returns a list of rooms.
# 
# **Functions**
# 
# Several functions are defined to interact with the home automation system:
# 
# * `print_home_plan`: prints the home plan, including all rooms and their components
# * `get_room`: returns a room by name
# * `get_room_sensors` and `get_room_actuators`: return lists of sensors or actuators in a specific room
# * `get_all_sensors` and `get_all_actuators`: return lists of all sensors or actuators matching specific types
# 
# **Config**
# 
# The script includes a separate file, `config.py`, which defines constants for:
# 
# * wait duration (`TEMP_CHANGE_DURATION_WINDOW`)
# * temperature thresholds (`TEMP_LOW` and `TEMP_HIGH`)
# * humidity thresholds (`HUMIDITY_LOW` and `HUMIDITY_HIGH`)
# * light intensity thresholds (`LIGHT_INTENSITY_LOW` and `LIGHT_INTENSITY_HIGH`)
# * daily routine duration (`DAILY_ROUTINE_DURATION`)
# 
# These constants can be used throughout the script.
# 
# Overall, this script provides a basic structure for a home automation system with various components and functions to interact with it.