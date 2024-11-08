from home.home_plan import home_plan, get_room, get_room_actuators, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, OutdoorTemperatureSensor
from home.actuator import AC, Heater, Window
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def open_windows_to_cool_down(home):
    """Opens windows to cool down the house when the temperature and light intensity are high."""

    # Get all ACs
    acs = get_all_actuators(home, "AC")

    # Check if any AC is on
    ac_on = any(ac.status == "on" for ac in acs)

    # Get all windows
    windows = get_all_actuators(home, "Window")

    # Get all indoor temperature sensors
    indoor_temp_sensors = get_all_actuators(home, "IndoorTemperature")
    # Get all light intensity sensors
    light_intensity_sensors = get_all_actuators(home, "LightIntensive")

    # Check if all conditions are met
    if not ac_on:
        if any(sensor.get_reading() > TEMP_HIGH for sensor in indoor_temp_sensors):
            if any(sensor.get_reading() > LIGHT_INTENSITY_HIGH for sensor in light_intensity_sensors):
                print("Opening windows to cool down the house.")
                logger.info("Opening windows to cool down the house.")
                for window in windows:
                    window.turn_on()


if __name__ == "__main__":
    home = home_plan()
    open_windows_to_cool_down(home)

# **Explanation:**

# 1. **Imports:**
#    - Imports necessary classes and constants from the `home` module.
# 2. **`open_windows_to_cool_down(home)` function:**
#    - Takes the `home` object (representing the home plan) as input.
#    - Gets all ACs, windows, and indoor temperature/light intensity sensors from the home plan.
#    - Checks if any AC is already on.
#    - If no AC is on, checks if any indoor temperature sensor reading is above `TEMP_HIGH` and if any light intensity sensor reading is above `LIGHT_INTENSITY_HIGH`.
#    - If both conditions are met, it prints a message and turns on all windows.

# **How to use:**

# 1. **Create a `functions` folder** in your project directory.
# 2. **Save the code above as `function.py`** within the `functions` folder.
# 3. **Call `open_windows_to_cool_down()`** in your main script after creating the `home` object using `home_plan()`. 

# **Example Usage:**

from home.home_plan import home_plan
from functions.function import open_windows_to_cool_down

# Create the home plan
home = home_plan()

# Call the function to open windows if needed
open_windows_to_cool_down(home)
