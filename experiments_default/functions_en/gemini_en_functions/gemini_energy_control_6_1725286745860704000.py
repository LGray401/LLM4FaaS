from home.home_plan import get_all_actuators, get_all_sensors
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.logger_config import logger

def activate_energy_saving_mode():
    """
    Activates energy saving mode by adjusting actuators based on sensor readings.

    This function iterates through all sensors and actuators,
    adjusting actuator settings to conserve energy based on current conditions.
    """
    home = get_all_actuators("all")
    all_sensors = get_all_sensors("all")
    logger.info("Activating energy saving mode...")

    for sensor in all_sensors:
        reading = sensor.get_reading()
        if reading is None:
            continue  # Sensor is off, skip to the next sensor

        if sensor.sensor_type == "IndoorTemperature":
            if reading < TEMP_LOW:
                # Adjust heater
                for heater in get_all_actuators(home, "Heater"):
                    heater.turn_on()
                    heater.set_target_temperature(TEMP_LOW)
            elif reading > TEMP_HIGH:
                # Adjust AC
                for ac in get_all_actuators(home, "AC"):
                    ac.turn_on()
                    ac.set_target_temperature(TEMP_HIGH)
            else:
                # Turn off both heater and AC
                for heater in get_all_actuators(home, "Heater"):
                    heater.turn_off()
                for ac in get_all_actuators(home, "AC"):
                    ac.turn_off()

        elif sensor.sensor_type == "Humidity":
            if reading < HUMIDITY_LOW:
                # Adjust humidifier
                for humidifier in get_all_actuators(home, "Humidifier"):
                    humidifier.increase_humidity()
            elif reading > HUMIDITY_HIGH:
                # Adjust dehumidifier (not implemented in this example)
                # ...
                pass
            else:
                # Turn off both humidifier and dehumidifier
                for humidifier in get_all_actuators(home, "Humidifier"):
                    humidifier.turn_off()
                # ...

        elif sensor.sensor_type == "LightIntensive":
            # Adjust light brightness (not implemented in this example)
            # ...
            pass

        # Add other sensor type checks and actuator adjustments as needed.

    logger.info("Energy saving mode activated.")

if __name__ == "__main__":
    activate_energy_saving_mode()

# **Explanation:**

# 1. **Import Necessary Modules:**
#    - `get_all_actuators` and `get_all_sensors` from `home.home_plan` to get lists of all actuators and sensors.
#    - `TEMP_LOW`, `TEMP_HIGH`, `HUMIDITY_LOW`, `HUMIDITY_HIGH` from `home.config` for temperature and humidity thresholds.
#    - `logger` from `home.logger_config` for logging.

# 2. **`activate_energy_saving_mode` Function:**
#    - Gets all actuators and sensors from the home plan.
#    - Iterates through each sensor:
#      - Reads the sensor value using `sensor.get_reading()`.
#      - Checks if the sensor is off (`reading is None`) and skips if it is.
#      - Implements logic based on the sensor type:
#        - **IndoorTemperature:** Adjusts heater or AC based on temperature being below `TEMP_LOW` or above `TEMP_HIGH`.
#        - **Humidity:** Adjusts humidifier based on humidity being below `HUMIDITY_LOW` or above `HUMIDITY_HIGH`. 
#        - **LightIntensive:**  You can add logic here to adjust light brightness.
#        - **Other Sensor Types:**  You can add logic for any other sensors you might have.
#    - Logs a message confirming that energy saving mode is activated.

# **Integration:**

# - Place this `function.py` file in the `functions` folder within your smart home project structure.
# - Ensure the other code files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`) are in the `home` folder.
# - You can call `activate_energy_saving_mode()` from your main script or any other script where you need to activate energy saving mode.

# **Remember:**
# - Replace placeholders like `# Adjust dehumidifier` and `# Adjust light brightness` with your actual implementation for those actuators.
# - Adjust the temperature, humidity, and light intensity thresholds in `config.py` to suit your needs.