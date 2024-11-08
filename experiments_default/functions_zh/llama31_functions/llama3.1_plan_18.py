# The provided code is a Python implementation of a home automation system, which includes various components such as sensors and actuators. Here's an explanation of the code:
# 
# **Room Class**
# 
# The `Room` class represents a room in the house. It has methods to add sensors and actuators, and a method to print information about the room.
# 
# **create_room_with_components function**
# 
# This function creates a new room with the specified name, adds the given sensor types as sensors, and adds the given actuator types as actuators.
# 
# **home_plan function**
# 
# This function returns a list of rooms, where each room has its own set of sensors and actuators. The rooms are created using the `create_room_with_components` function.
# 
# **print_home_plan function**
# 
# This function prints out the home plan by calling the `print_info` method on each room in the list returned by `home_plan`.
# 
# **get_room function**
# 
# This function takes a room name as input and returns the corresponding room object from the home plan. If no matching room is found, it returns `None`.
# 
# **get_room_sensors and get_room_actuators functions**
# 
# These two functions take a room name as input and return the list of sensors or actuators in that room.
# 
# **get_all_sensors and get_all_actuators functions**
# 
# These two functions take a sensor type or actuator type as input and return all instances of that type across all rooms in the home plan.
# 
# The `config.py` file contains configuration parameters for the system, such as temperature thresholds, humidity ranges, and light intensity ranges.
# 
# **Example Usage**
# 
# In the `if __name__ == "__main__":` block, an example usage is shown where the `get_room_actuators` function is called with a room name to get all actuators in that room.