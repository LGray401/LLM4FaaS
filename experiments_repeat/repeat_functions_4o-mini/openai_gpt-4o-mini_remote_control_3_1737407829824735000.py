# Based on your functional description and the provided source code, I will create a `function.py` file that includes a main function to turn off the lights in the living room. The function will access the `Light` actuator associated with the living room and invoke the `turn_off()` method.
# 
# Here's how `function.py` will look:
# 
# ```python
# function.py
from home.home_plan import home_plan
from home.logger_config import logger

def main():
    # Create the home plan
    home = home_plan()
    
    # Get the living room
    living_room = next((room for room in home if room.name == "LivingRoom"), None)

    if living_room:
        # Get all light actuators in the living room
        lights = [actuator for actuator in living_room.actuators if actuator.actuator_type == "Light"]

        if lights:
            for light in lights:
                light.turn_off()  # Turn off each light actuator
            logger.info("All lights in the living room have been turned off.")
            print("All lights in the living room have been turned off.")
        else:
            logger.warning("No lights found in the living room.")
            print("No lights found in the living room.")
    else:
        logger.warning("Living room not found.")
        print("Living room not found.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **Imports**: The code imports the necessary components from the `home_plan` module to access the home structure and the `logger` for logging messages.
# - **Main Function**: 
#   - It first creates the home plan.
#   - It retrieves the living room from the home plan.
#   - It collects all the light actuators from the living room.
#   - If any lights are found, it iterates over them and calls the `turn_off()` method for each light.
#   - It logs and prints messages based on the actions performed, such as successfully turning off the lights or not finding any lights.
#   
# ### Saving the File
# You should create a new file named `function.py` in the `functions` folder and copy the above code into it. This will allow you to run the function and turn off the lights in the living room as specified in your functional description.