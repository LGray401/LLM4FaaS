from home.home_plan import home_plan, get_room, get_room_actuators, get_all_actuators
from home.logger_config import logger


def turn_off_all_lights(home):
    """Turns off all lights in the home."""
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
        print(f"Turning off light: {light.id}")
        logger.info(f"Turning off light: {light.id}")


def turn_off_all_water_sources(home):
    """Turns off all water sources in the home (assumes no specific water actuators are defined)."""
    print("Turning off all water sources (no specific water actuators defined).")
    logger.info("Turning off all water sources (no specific water actuators defined).")


def main():
    """Main function to execute the functional description."""
    home = home_plan()
    turn_off_all_lights(home)
    turn_off_all_water_sources(home)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions to create the home plan, get rooms, actuators, and sensors.
#    - `home.logger_config`: Used for logging messages.

# 2. **`turn_off_all_lights(home)` function:**
#    - Gets all actuators of type "Light" from the `home` plan.
#    - Iterates through each light and calls its `turn_off()` method.
#    - Prints and logs a message indicating the light being turned off.

# 3. **`turn_off_all_water_sources(home)` function:**
#    - Since no specific water actuators are defined, this function simply prints a message indicating that it's turning off all water sources (as a placeholder).

# 4. **`main()` function:**
#    - Creates a `home` object using `home_plan()`.
#    - Calls `turn_off_all_lights()` to turn off all lights in the home.
#    - Calls `turn_off_all_water_sources()` to simulate turning off water sources.

# 5. **`if __name__ == "__main__":` block:**
#    - Ensures that the `main()` function is executed only when the script is run directly (not when imported as a module).

# **To run this function.py file:**

# 1. Ensure you have the other files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) in the 'home' folder.
# 2. Place the `function.py` file in the 'functions' folder.
# 3. Run the `function.py` file from the terminal: `python functions/function.py`

# This will execute the code and turn off all lights in your simulated smart home.
