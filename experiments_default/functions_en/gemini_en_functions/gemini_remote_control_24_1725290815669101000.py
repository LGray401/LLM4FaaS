from home.home_plan import get_room, get_room_actuators
from home.logger_config import logger

def main():
    """
    Main function for the smart home system.
    """
    home = get_room(get_room_actuators, "Bedroom")
    for actuator in home.actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_off()
            logger.info("Bedroom light is now off.")
            print("Bedroom light is now off.")
            return

    logger.warning("No light found in Bedroom.")
    print("No light found in Bedroom.")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Imports the `get_room` function to access the room and its actuators.
#    - `home.logger_config`: Imports the `logger` object for logging.

# 2. **`main()` function:**
#    - Retrieves the `Bedroom` room using `get_room` and stores it in `home`.
#    - Iterates through the `actuators` list of the `Bedroom` room.
#    - If an actuator is a `Light` type, it calls the `turn_off()` method on that actuator to turn off the light.
#    - Logs and prints a confirmation message.
#    - If no `Light` actuator is found in the `Bedroom`, logs and prints a warning message.

# **How to use:**

# 1. Save this code as `functions/function.py`.
# 2. Make sure your `home` folder contains the other four files: `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 3. Run the `function.py` file: `python functions/function.py`.

# This will turn off the light in the Bedroom. 
