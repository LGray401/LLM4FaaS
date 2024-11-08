# Based on your functional description of "关闭客厅的灯" (which translates to "turn off the lights in the living room"), I will create a `function.py` file that integrates the necessary components from the provided source code files to achieve this functionality.
# 
# Here's the `function.py` implementation:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan
from home.config import DAILY_ROUTINE_DURATION
from home.logger_config import logger

def turn_off_living_room_lights():
    # Get the home plan
    home = home_plan()
    
    # Find the living room
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    
    if living_room:
        # Get all light actuators in the living room
        lights = [actor for actor in living_room.actuators if actor.actuator_type == "Light"]
        
        if lights:
            # Turn off all lights in the living room
            for light in lights:
                light.turn_off()
            logger.info("All lights in the Living Room have been turned off.")
        else:
            print("No lights found in the Living Room.")
            logger.warning("No lights found in the Living Room.")
    else:
        print("Living Room not found in the home.")
        logger.warning("Living Room not found in the home.")

def main():
    turn_off_living_room_lights()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation of the Code:
# 
# 1. **Imports**: The necessary components are imported. This includes the `home_plan` function to retrieve the home layout and the logger for logging actions.
# 
# 2. **turn_off_living_room_lights Function**:
#    - Retrieves the home plan using `home_plan()`.
#    - Searches for the living room in the list of rooms.
#    - If found, it collects all light actuators from the living room.
#    - If light actuators are found, it calls the `turn_off()` method on each of them, logging the action. If no lights are found, it logs a warning.
# 
# 3. **Main Function**: The `main()` function calls `turn_off_living_room_lights()`, which is the entry point when the script is executed.
# 
# 4. **Execution**: The script can be run directly, and it will execute the turning off of the lights in the living room.
# 
# ### Directory Structure
# Make sure the `function.py` file is placed inside the `functions` directory as specified. The overall directory structure should look something like this:
# 
# ```
# project_root/
# │
# ├── home/
# │   ├── actuator.py
# │   ├── config.py
# │   ├── home_plan.py
# │   ├── logger_config.py
# │   └── sensor.py
# │
# └── functions/
#     └── function.py
# ```
# 
# You can now integrate this `function.py` into your smart home project! If you have any further requirements, feel free to ask.