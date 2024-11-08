# <think>
# Okay, I need to help the user by providing a step-by-step explanation of their code. Let me look at what they've provided.
# 
# First, there's the Preparation section with several files: config.py, logger_config.py (which is imported as logger), and home_plan.py which seems to be part of the main script but was moved into Preparation due to its length. The main.py is also in Preparation because it's longer than 100 lines.
# 
# The user has included three Python files: config.py, home_plan.py, and a function from main.py called get_room_sensors, get_room_actuators, etc., which are part of the home planning system.
# 
# I notice that the code revolves around creating rooms with various sensors and actuators. The Room class in home_plan.py adds these components. There's also functionality to retrieve information about rooms, sensors, and actuators.
# 
# In config.py, there are several constants related to temperature, humidity, light intensity, and routines. These might be used for thresholds or conditions when monitoring room parameters.
# 
# The main script section seems to involve functions that allow getting all sensors or actuators of a specific type across all rooms. The get_room_sensors function returns sensors in the specified room if they match the sensor type, else it logs a warning.
# 
# I think I should explain how each part works, starting from the configuration constants, moving through the Room class and its methods, then into the home_plan function which sets up rooms with various components. Finally, explaining the utility functions for retrieving sensors and actuators of specific types across all rooms.
# 
# I need to make sure that my explanation is clear, breaking down each component's purpose, how data flows through the system, and any important interactions between classes like Room, Room.Sensors, and Room.Actuators.
# 
# Also, I should highlight how logging works in this setup, ensuring that errors and warnings are properly captured. Additionally, explaining the main script functions get_room_sensors, get_room_actuators, etc., so users understand what these functions do and when they might be useful.
# 
# I should structure my explanation with sections: starting with configuration, moving to room creation, then utility functions, and finally the main execution flow. This will help readers follow along step by step without getting overwhelmed.
# </think>
# 
# Let me explain how this codebase works in a clear, step-by-step manner:
# 
# 1. **Configuration Setup**:
# - Constants are defined in `config.py` for temperature and humidity thresholds, light intensity levels, and daily routines.
# 
# 2. **Room Class Structure**:
#    - A `Room` class is created with methods to manage sensors and actuators.
#      - `add_sensor()` and `add_actuator()` allow adding specific sensor or actuator types to a room.
#      - `print_info()` displays all sensors and actuators in the room.
# 
# 3. **Home Plan Creation**:
#    - The `create_room_with_components()` function adds predefined sensors and actuators to rooms based on specified types.
#    - Multiple rooms are created with different components (sensors and actuators) for various areas like LivingRoom, Bedroom, etc.
# 
# 4. **Utility Functions**:
#    - `get_room()`: Retrieves a room by name along with its sensors and actuators.
#    - `get_room_sensors()` and `get_room_actuators()`: Return sensors or actuators of specific types found in the specified room.
#    - `get_all_sensors()` and `get_all_actuators()`: Aggregate all sensors or actuators across rooms matching a given type.
# 
# 5. **Main Execution**:
#    - The main script demonstrates how to create home plans, retrieve sensor information, and log warnings for missing components.
# 
# This system allows for modular setup of rooms with various smart home components, providing flexibility in monitoring and controlling environmental conditions through configured thresholds and automation routines.