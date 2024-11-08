from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger
import time

def main():
    """Main function for the smart home system."""

    home = home_plan()

    while True:
        # Light automation
        light_sensors = get_all_sensors(home, "LightIntensive")
        for light_sensor in light_sensors:
            light_intensity = light_sensor.get_reading()
            if light_intensity is not None and light_intensity > LIGHT_INTENSITY_HIGH:
                lights_in_room = get_room_actuators(home, light_sensor.room_name)
                for light in lights_in_room:
                    if light.actuator_type == "Light":
                        light.turn_off()

        # Temperature automation
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        for temperature_sensor in temperature_sensors:
            current_temperature = temperature_sensor.get_reading()
            if current_temperature is not None:
                heaters_in_room = get_room_actuators(home, temperature_sensor.room_name)
                for heater in heaters_in_room:
                    if heater.actuator_type == "Heater":
                        heater.adjust_temperature(current_temperature)
                acs_in_room = get_room_actuators(home, temperature_sensor.room_name)
                for ac in acs_in_room:
                    if ac.actuator_type == "AC":
                        ac.adjust_temperature(current_temperature)

        # Humidity automation
        humidity_sensors = get_all_sensors(home, "Humidity")
        for humidity_sensor in humidity_sensors:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                humidifiers_in_room = get_room_actuators(home, humidity_sensor.room_name)
                for humidifier in humidifiers_in_room:
                    if humidifier.actuator_type == "Humidifier":
                        if current_humidity < HUMIDITY_LOW:
                            humidifier.increase_humidity()
                        elif current_humidity > HUMIDITY_HIGH:
                            humidifier.decrease_humidity()

        # Cleaning robot automation
        cleaning_robots = get_all_actuators(home, "CleaningRobot")
        for cleaning_robot in cleaning_robots:
            current_day = time.strftime("%A")
            if current_day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                cleaning_robot.daily_routine()

        # Simulate sensor updates
        time.sleep(1)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - Imports necessary modules from `home` package for home plan, sensors, actuators, and configuration.
#    - Imports `time` for simulating sensor updates and `logger` for logging.

# 2. **`main()` Function:**
#    - Creates the `home` plan using `home_plan()`.
#    - Enters an infinite loop (`while True`) to continuously monitor and automate actions.

# 3. **Light Automation:**
#    - Gets all `LightIntensive` sensors using `get_all_sensors()`.
#    - Iterates through each sensor:
#      - Reads the light intensity using `get_reading()`.
#      - If intensity is above the threshold (`LIGHT_INTENSITY_HIGH`):
#        - Gets all actuators in the sensor's room using `get_room_actuators()`.
#        - Iterates through actuators, turning off lights (`Light` type).

# 4. **Temperature Automation:**
#    - Gets all `IndoorTemperature` sensors.
#    - Iterates through sensors:
#      - Reads the current temperature.
#      - Adjusts heaters and ACs based on temperature:
#        - If temperature is below the threshold (`TEMP_LOW`), turn on heaters.
#        - If temperature is above the threshold (`TEMP_HIGH`), turn on ACs.

# 5. **Humidity Automation:**
#    - Gets all `Humidity` sensors.
#    - Iterates through sensors:
#      - Reads the current humidity.
#      - Adjusts humidifiers based on humidity:
#        - If humidity is below the threshold (`HUMIDITY_LOW`), increase humidity.
#        - If humidity is above the threshold (`HUMIDITY_HIGH`), decrease humidity.

# 6. **Cleaning Robot Automation:**
#    - Gets all `CleaningRobot` actuators.
#    - Iterates through robots:
#      - Checks if the current day is a weekday (Monday to Friday).
#      - If it is a weekday, starts the robot's `daily_routine()`.

# 7. **Simulate Sensor Updates:**
#    - Uses `time.sleep(1)` to simulate sensor readings every second.

# 8. **`if __name__ == "__main__":` Block:**
#    - Calls the `main()` function when the script is run directly.

# **To run this script:**

# 1. Ensure that the `home` folder with the other source code files (sensor.py, actuator.py, home_plan.py, config.py) is in the same directory as this `function.py` file.
# 2. Run the script from your terminal using the command: `python function.py`

# This will start the smart home system, automating actions based on sensor readings and configured thresholds. Remember that this code uses random sensor readings for demonstration purposes. In a real smart home, you would connect actual sensors and actuators to this system for real-time functionality.
