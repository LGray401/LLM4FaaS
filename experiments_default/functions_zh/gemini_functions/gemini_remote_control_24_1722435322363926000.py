from home.home_plan import get_room, get_room_actuators
from home.actuator import Light
from home.logger_config import logger

def main():
    """
    This is the main function of the smart home system. It takes user commands and executes them.
    """
    home = get_room(home_plan(), "Bedroom")
    if home is not None:
        actuators = get_room_actuators(home, "Bedroom")
        if actuators is not None:
            for actuator in actuators:
                if actuator.actuator_type == "Light":
                    light = actuator
                    light.turn_off()
                    logger.info(f"Turned off the light in the bedroom.")
                    print(f"Turned off the light in the bedroom.")
                    return
        else:
            logger.warning("No actuators found in the bedroom.")
            print("No actuators found in the bedroom.")
    else:
        logger.warning("Bedroom not found in the home plan.")
        print("Bedroom not found in the home plan.")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - `from home.home_plan import get_room, get_room_actuators`: Imports the necessary functions to access the home plan and retrieve specific rooms and actuators.
#    - `from home.actuator import Light`: Imports the `Light` actuator class.
#    - `from home.logger_config import logger`: Imports the logger for logging events.

# 2. **`main()` Function:**
#    - **Get Bedroom:**
#      - Calls `get_room` to find the "Bedroom" in the home plan.
#      - If the "Bedroom" is found, it retrieves the actuators in the room using `get_room_actuators`.

#    - **Find Light Actuator:**
#      - Iterates through the actuators in the bedroom.
#      - If the actuator type is "Light," it's assumed to be the light in the bedroom.
#      - The `light` variable is assigned to the found `Light` actuator.

#    - **Turn Off Light:**
#      - Calls `light.turn_off()` to turn off the light in the bedroom.
#      - Logs the action using `logger.info()`.
#      - Prints a confirmation message to the console.

#    - **Error Handling:**
#      - If the bedroom, actuators, or the light actuator is not found, appropriate error messages are logged and printed to the console.

# 3. **`if __name__ == "__main__":`:**
#    - This ensures that the `main()` function is only executed when the script is run directly (not when imported as a module).

# **How to Use This Code:**

# 1. **Save:** Save the code as `function.py` in the `functions` folder of your project.
# 2. **Run:** Execute the `function.py` file. This will attempt to turn off the light in the bedroom based on the home plan.

# **Important Notes:**

# - **Home Plan:** Ensure that your `home_plan.py` file correctly defines the "Bedroom" and includes a "Light" actuator within it.
# - **Actuator Logic:** The `Light` actuator in `actuator.py` should have a working `turn_off()` method to handle the actual light control.
# - **Error Handling:** The code includes basic error handling, but you might want to expand on it for a more robust system.
