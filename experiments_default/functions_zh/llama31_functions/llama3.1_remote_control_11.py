# This code appears to be part of a smart home management system, where you can define rooms and their components (sensors and actuators) in a hierarchical manner. Here's a summary:
# 
# 1. The `Room` class represents a room in the house with methods to add sensors and actuators.
# 2. The `create_room_with_components` function creates a new `Room` instance by adding specified sensor and actuator types.
# 3. The `home_plan` function defines multiple rooms (LivingRoom, Bedroom, Kitchen, Bathroom, Balcony) with their respective components using the `create_room_with_components` function.
# 4. You have various functions to query the home plan:
# 	* `print_home_plan`: prints out all rooms and their sensors and actuators.
# 	* `get_room`: retrieves a specific room by name.
# 	* `get_room_sensors` and `get_room_actuators`: retrieve all sensors or actuators from a specific room, respectively.
# 	* `get_all_sensors` and `get_all_actuators`: find all occurrences of a sensor or actuator type across the entire home.
# 
# Some suggestions:
# 
# 1. **Naming conventions**: While you're using PEP 8-compliant variable names in some places (e.g., `create_room_with_components`), there are others that deviate from this standard (e.g., `print_home_plan`, `get_room_sensors`). Be consistent throughout the code.
# 2. **Comments and docstrings**: Most functions lack comments or docstrings, making it hard to understand their purpose without reading the surrounding code. Add these for better readability.
# 3. **Magic numbers**: The `TEMP_CHANGE_DURATION_WINDOW`, `DAILY_ROUTINE_DURATION` values are hardcoded in the config file. Consider defining them as constants with meaningful names and explanations.
# 
# Overall, your code is well-structured, but could benefit from some improvements in naming conventions, commenting, and consistency across different functions.