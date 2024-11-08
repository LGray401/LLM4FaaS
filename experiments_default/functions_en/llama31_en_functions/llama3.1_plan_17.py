# This is a Python script that defines various home automation components and their relationships. Here's a breakdown of the code:
# 
# **Components**
# 
# The script starts by importing several component classes from another module (`home.logger_config`):
# 
# * `AC`, `CoffeeMachine`, `SmartSocket`, `Door`, `CleaningRobot`, and `SmartTV`
# 
# These classes are not defined in this script, so they must be implemented elsewhere.
# 
# **Room Class**
# 
# A `Room` class is defined to represent a room in the home. Each room has:
# 
# * A name (`self.name`)
# * A list of sensors (`self.sensors`) and actuators (`self.actuators`)
# * Methods to add sensors and actuators to the room
# * A method to print information about the room
# 
# **Home Plan**
# 
# The `home_plan()` function creates a list of rooms, each with its own set of sensors and actuators. The rooms are defined as:
# 
# * Living Room: various sensors (e.g., LightIntensiveSensor) and actuators (e.g., Door, Light)
# * Bedroom: similar to the living room
# * Kitchen: some sensors (HumiditySensor, SmokeSensor) and actuators (Light, Window, Heater)
# * Bathroom: some sensors (IndoorTemperatureSensor, HumiditySensor) and actuators (Light, Window, Heater)
# * Balcony: outdoor temperature and humidity sensors
# 
# **Utility Functions**
# 
# Several utility functions are defined to interact with the home plan:
# 
# * `print_home_plan(home)`: prints information about each room in the home
# * `get_room(home, room_name)`: returns a room by name (or None if not found)
# * `get_room_sensors(home, room_name)`: returns a list of sensors in a given room (or None if not found)
# * `get_room_actuators(home, room_name)`: returns a list of actuators in a given room (or None if not found)
# 
# These functions are used to retrieve information about the home and its components.
# 
# **Config**
# 
# The script also defines a `config.py` file with some constants related to temperature, humidity, light intensity, and daily routines. These values can be adjusted as needed.
# 
# Overall, this script provides a basic structure for representing a home automation system, including rooms, sensors, and actuators. The utility functions enable easy access to information about the home and its components.