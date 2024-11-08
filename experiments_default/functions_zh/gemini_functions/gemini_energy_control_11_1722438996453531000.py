from home.home_plan import home_plan, get_all_actuators, get_all_sensors
from home.sensor import IndoorTemperatureSensor
from home.actuator import Window
from home.logger_config import logger

def main():
    home = home_plan()
    # Get all IndoorTemperatureSensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all Windows
    windows = get_all_actuators(home, "Window")

    # Check temperature and open windows if necessary
    for temperature_sensor in temperature_sensors:
        temperature = temperature_sensor.get_reading()
        if temperature is not None and temperature > 26:
            for window in windows:
                window.turn_on()
                logger.info(f"Window {window.id} is opened to cool down.")
                print(f"Window {window.id} is opened to cool down.")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`:  Imports the `home_plan` function to create the home structure and functions like `get_all_actuators` and `get_all_sensors`.
#    - `home.sensor`: Imports the `IndoorTemperatureSensor` class to access temperature readings.
#    - `home.actuator`: Imports the `Window` class to control the windows.
#    - `home.logger_config`: Imports the `logger` object for logging.

# 2. **Define the `main` function:**
#    - This function is the entry point for the script.
#    - It gets the home structure using `home_plan()`.
#    - It then retrieves all `IndoorTemperatureSensor` objects using `get_all_sensors` and all `Window` objects using `get_all_actuators`.

# 3. **Iterate through temperature sensors and windows:**
#    - The script iterates through each `IndoorTemperatureSensor`.
#    - For each sensor, it gets the temperature reading using `get_reading()`.
#    - If the temperature is above 26 degrees Celsius:
#      - The script iterates through all `Window` objects.
#      - It turns on each window using `turn_on()`, effectively opening them.
#      - A log message is printed indicating that the windows are opened.

# 4. **Run the `main` function:**
#    - The `if __name__ == "__main__":` block ensures that the `main` function is executed only when the script is run directly, not when it's imported as a module.

# **To use this script:**

# 1. **Place it in the `functions` folder:** Make sure the `function.py` file is located in the `functions` folder within your smart home project structure.
# 2. **Run the script:** Execute the script from your project's root directory. It will read the temperature from the sensors, open the windows if needed, and log the actions.

# This script provides a basic example of using sensors and actuators to automate window opening based on temperature. You can extend this logic to incorporate other sensors, actuators, and conditions to create more complex automation rules for your smart home.
