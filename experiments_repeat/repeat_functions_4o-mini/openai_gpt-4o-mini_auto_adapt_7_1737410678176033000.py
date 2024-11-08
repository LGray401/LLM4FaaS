# Based on the functional description provided, I will create a `function.py` file that implements the main functionality for your smart home project. This file will check the readings from the sensors and control the actuators based on the specified conditions regarding temperature, humidity, and light intensity.
# 
# Here is the content for `function.py`:
# 
# ```python
# function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    home = home_plan()

    for room in home:
        # Retrieve sensors and actuators for the room
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]

        heater = next((actuator for actuator in room.actuators if actuator.actuator_type == "Heater"), None)
        ac = next((actuator for actuator in room.actuators if actuator.actuator_type == "AC"), None)
        humidifier = next((actuator for actuator in room.actuators if actuator.actuator_type == "Humidifier"), None)
        light = next((actuator for actuator in room.actuators if actuator.actuator_type == "Light"), None)

        # Check temperature
        for sensor in temperature_sensors:
            sensor.turn_on()  # Ensure the sensor is on
            temperature = sensor.get_reading()
            if temperature is not None:
                if temperature < TEMP_LOW:
                    if heater:
                        heater.set_target_temperature(22)  # Set desired temperature
                        heater.adjust_temperature(temperature)
                elif temperature > TEMP_HIGH:
                    if ac:
                        ac.set_target_temperature(22)  # Set desired temperature
                        ac.adjust_temperature(temperature)

        # Check humidity
        for sensor in humidity_sensors:
            sensor.turn_on()  # Ensure the sensor is on
            humidity = sensor.get_reading()
            if humidity is not None:
                if humidity < HUMIDITY_LOW:
                    if humidifier:
                        humidifier.increase_humidity()

        # Check light intensity
        for sensor in light_sensors:
            sensor.turn_on()  # Ensure the sensor is on
            light_intensity = sensor.get_reading()
            if light_intensity is not None:
                if light_intensity < LIGHT_INTENSITY_LOW:
                    if light:
                        light.turn_on()  # Turn on the light if it's too dark

        # Allow time for the system to stabilize
        time.sleep(2)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - The `main` function starts by creating the home plan, which sets up all rooms with their sensors and actuators.
# - It iterates through each room, retrieves the relevant sensors (temperature, humidity, and light intensity), and actuators (heater, AC, humidifier, and light).
# - For each type of sensor, it turns on the sensor, retrieves the readings, and checks against preset thresholds defined in `config.py`.
# - If the temperature is too low, it turns on the heater; if it's too high, it turns on the AC. 
# - If the humidity is too low, it activates the humidifier. 
# - If the light intensity is too low, it turns on the light.
# - There is a brief sleep period to allow the system to stabilize before the next iteration.
# 
# This structure provides a basic control system for the smart home based on the given functional requirements.