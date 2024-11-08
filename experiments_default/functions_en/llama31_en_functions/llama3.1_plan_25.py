# This code is for a smart home system. It defines classes for various components of the house like sensors and actuators, and a `Room` class to organize them.
# 
# The main file (`main.py`) contains functions to create a home plan with specified rooms and their corresponding sensors and actuators. It also includes functions to print out the home plan, get a specific room, its sensors or actuators, all sensors of a certain type, and all actuators of a certain type.
# 
# In addition, there is a separate file (`config.py`) for storing configuration parameters such as temperature thresholds, humidity range, light intensity limits, and daily routine duration.
# 
# Here's how you can use this code:
# 
# 1. Create your home plan with specific rooms and their components using the `home_plan()` function.
# 2. Print out the home plan using the `print_home_plan()` function.
# 3. Get a specific room by its name using the `get_room()` function.
# 4. Get all sensors or actuators of a certain type in any room using the `get_all_sensors()` and `get_all_actuators()` functions respectively.
# 
# You can modify this code to suit your needs, such as adding more types of components, modifying configuration parameters, or implementing smart home automation logic.
# 
# Here are some possible improvements:
# 
# 1. **Error Handling**: The current implementation assumes that a room with the specified name exists. You could add try-except blocks to handle cases where the room is not found.
# 2. **Type Hints**: Adding type hints for function parameters and return types would improve code readability and facilitate static analysis.
# 3. **Config Management**: Instead of storing configuration parameters directly in the `config.py` file, consider using an external configuration management system like a YAML or JSON file that can be easily modified without changing the code.
# 
# Overall, this code provides a solid foundation for building a smart home system with various sensors and actuators organized into different rooms. You can extend it to support more advanced features like automation logic, voice control integration, or machine learning-based energy consumption optimization.