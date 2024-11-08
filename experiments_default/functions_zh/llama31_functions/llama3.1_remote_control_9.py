# The code you've shared appears to be a home automation system with various sensors and actuators. Here's a high-level overview of the key components:
# 
# ### Sensor Classes
# 
# *   `LightIntensiveSensor`
# *   `IndoorTemperatureSensor`
# *   `HumiditySensor`
# *   `OutdoorTemperatureSensor`
# *   `SmokeSensor`
# 
# These classes are likely used to represent different types of sensors in your home automation system. Each sensor has a unique ID and might have additional attributes like the type of measurement it takes (e.g., temperature, humidity).
# 
# ### Actuator Classes
# 
# *   `Door`
# *   `Light`
# *   `Window`
# *   `Curtain`
# *   `MusicPlayer`
# *   `SmartSocket`
# *   `CoffeeMachine`
# *   `CleaningRobot`
# *   `SmartTV`
# *   `NotificationSender`
# *   `AC`
# *   `Heater`
# 
# These classes are used to represent various actuators in your home automation system, which can perform different actions like turning lights on/off or controlling temperature.
# 
# ### Room Class
# 
# The `Room` class represents a room in your home and has attributes:
# 
# *   `name`: The name of the room.
# *   `sensors`: A list of sensors present in the room.
# *   `actuators`: A list of actuators present in the room.
# 
# This class can be used to manage the components within each room, such as adding or removing sensors and actuators.
# 
# ### Utility Functions
# 
# The provided code includes several utility functions:
# 
# *   `create_room_with_components(name, sensor_types, actuator_types)`: Creates a new room with the specified name and components.
# *   `home_plan()`: Returns a list of rooms in your home automation system, including their components.
# *   `print_home_plan(home)`: Prints out the plan for each room in your home automation system.
# 
# These functions help simplify the process of managing your home automation system by providing pre-defined configurations for common scenarios.
# 
# ### Room Retrieval Functions
# 
# The code includes two functions to retrieve specific rooms or their components:
# 
# *   `get_room(home, room_name)`: Retrieves a room by its name from the provided home plan.
# *   `get_room_sensors(home, room_name)`: Returns the list of sensors in the specified room.
# *   `get_room_actuators(home, room_name)`: Returns the list of actuators in the specified room.
# 
# These functions enable you to access specific rooms and their components within your home automation system.
# 
# ### Sensor/Actuator Retrieval Functions
# 
# The provided code also includes two functions to retrieve all sensors or actuators of a specific type:
# 
# *   `get_all_sensors(home, sensor_type)`: Returns all instances of the specified sensor type in the provided home plan.
# *   `get_all_actuators(home, actuator_type)`: Returns all instances of the specified actuator type in the provided home plan.
# 
# These functions help you retrieve specific types of sensors or actuators within your home automation system.
# 
# ### Main Execution
# 
# In the main execution block (`if __name__ == "__main__":`), an example is shown where you can test these functions by creating a home plan, retrieving rooms and their components, and getting all instances of certain sensor/actuator types.