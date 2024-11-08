# <think>
# Okay, I need to help the user by analyzing their code and figuring out what they're asking for. Let me start by looking at each file they provided.
# 
# First up is `sensors.py`. It defines various sensors like LightIntensiveSensor and TemperatureSensor. These sensors have methods to check if conditions are met and emit alerts based on thresholds from `config.py`.
# 
# Next, in `actuators.py`, there's a base class for actuators with an actuator_type attribute. Specific actuators include Door, SmartTV, etc., each implementing their own logic when triggered.
# 
# The `logger_config.py` sets up logging using the logger utility, which is imported elsewhere.
# 
# Now looking at `room_plan.py`. It creates multiple rooms with various sensors and actuators based on predefined types. The home_plan function uses create_room_with_components to add these components. Then there are several functions like get_room that retrieve information about sensors and actuators in a room.
# 
# The user provided some example code at the bottom, which is supposed to be executed. It seems they're trying to find all "Light" actuators across their home setup using get_all_actuators.
# 
# Wait, but in `room_plan.py`, when creating rooms, for example:
# 
# create_room_with_components("LivingRoom", [LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor],
#                             [Door, Light, Window, Window, Curtain, MusicPlayer, SmartSocket, SmartSocket,
#                              CleaningRobot, SmartTV, NotificationSender, AC, Heater])
# 
# Here, the actuators include multiple Lights. So when the home is built, each "LivingRoom" has one or more Light actuators.
# 
# The user's example code calls get_all_actuators(home, "Light") which should return all the Light actuator instances from each room.
# 
# But in their current setup, do they have enough dependencies installed? They might need to install requests and logging if these are missing. Also, ensuring that Python is set up with the correct virtual environment or packages.
# 
# Another thing: looking at `sensors.py`, there's no import statement for the config module when accessing sensor types like IndioorTemperatureSensor. So they probably need to import Config or use from config import * somewhere.
# 
# Wait, but in their code, they have from config import TEMP_LOW etc., so perhaps that's okay.
# 
# Now, looking at `room_plan.py`, after defining create_room_with_components and home_plan, the user runs if __name__ == "__main__": block. But currently, it's just getting get_all_actuators and printing them, but maybe they're missing some dependencies or functions aren't properly defined.
# 
# Potential issues:
# 
# 1. Missing imports: Check that all modules are imported correctly.
# 2. Dependencies: Ensure requests and logging are installed if used elsewhere.
# 3. Functionality: Maybe the way rooms are created doesn't include all the necessary components, leading to incorrect sensor and actuator lists.
# 
# The user probably wants to verify that when they run get_all_actuators(home, "Light"), it correctly returns all Light actuators from their home setup. So I need to see if there are any errors in how these functions are written or called.
# 
# For example, the function get_room_sensors is defined but not used. Similarly for other helper functions like get_room_actuators—though looking at the code, they might be redundant because the home_plan returns a list of rooms each with their own actuators and sensors.
# 
# So perhaps the main issue is ensuring all the dependencies are correctly installed and that sensor types are imported properly.
# </think>
# 
# To help you better understand and work with your code, I'll go through it step by step:
# 
# 1. **Sensors**: Defined as classes like LightIntensiveSensor, TemperatureSensor, etc., which have methods to check conditions and emit alerts.
# 
# 2. **Actuators**: Classes that can be triggered when certain conditions are met, such as Door, SmartTV, etc.
# 
# 3. **Room Class**: Manages sensors and actuators for a specific room type.
# 
# 4. **Helper Functions**:
#    - `create_room_with_components`: Creates rooms with specified sensor and actuator types.
#    - `get_room`, `get_all_sensors`, `get_all_actuators`: Functions to retrieve information about rooms, sensors, and actuators.
# 
# 5. **Configuration**: Sets thresholds for temperature, humidity, light intensity, etc.
# 
# To run the example successfully:
# 
# 1. Make sure you have Python installed with proper logging setup.
# 2. Install any missing dependencies (like requests if used elsewhere).
# 3. Ensure all configuration files are correctly imported.
# 
# For your `room_plan.py`, here's how it works:
# 
# - Creates multiple rooms with specified components using create_room_with_components
# - Defines functions to retrieve room information, sensors, and actuators
# - The example execution at the bottom tries to collect all "Light" actuators
# 
# You might need to ensure that:
# 1. All modules are properly imported (e.g., importing Config if needed)
# 2. The project structure includes all necessary virtual environments or packages