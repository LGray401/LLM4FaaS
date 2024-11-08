# Based on the provided functional description and existing code files, I will create a `function.py` script that integrates the functionalities of the sensors and actuators to achieve the desired conditions: setting the temperature to 26 degrees, humidity to 50%, and light intensity to a medium level. 
# 
# Here's how the `function.py` file will look:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW
from home.logger_config import logger

def main():
    # Initialize home plan
    home = home_plan()

    # Target conditions
    target_temperature = 26
    target_humidity = 50
    target_light_intensity = "medium"

    # Find the Living Room to control
    living_room = next((room for room in home if room.name == "LivingRoom"), None)

    if not living_room:
        logger.error("Living Room not found!")
        return

    # Get sensors and actuators from the Living Room
    temperature_sensors = [sensor for sensor in living_room.sensors if sensor.sensor_type == "IndoorTemperature"]
    humidity_sensors = [sensor for sensor in living_room.sensors if sensor.sensor_type == "Humidity"]
    light_sensors = [sensor for sensor in living_room.sensors if sensor.sensor_type == "LightIntensive"]

    heater = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "Heater"), None)
    ac = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "AC"), None)
    humidifier = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "Humidifier"), None)
    light = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "Light"), None)

    # Ensure we have the necessary components
    if not temperature_sensors or not humidity_sensors or not light_sensors or not heater or not ac or not humidifier or not light:
        logger.error("One or more components are missing in the Living Room!")
        return

    # Read temperature
    current_temperature = temperature_sensors[0].get_reading()
    if current_temperature is None:
        logger.warning("Could not read temperature.")
    else:
        # Control heater or AC
        if current_temperature < target_temperature:
            heater.set_target_temperature(target_temperature)
            heater.adjust_temperature(current_temperature)
        elif current_temperature > target_temperature:
            ac.set_target_temperature(target_temperature)
            ac.adjust_temperature(current_temperature)

    # Read humidity
    current_humidity = humidity_sensors[0].get_reading()
    if current_humidity is None:
        logger.warning("Could not read humidity.")
    else:
        if current_humidity < target_humidity:
            humidifier.increase_humidity()
        elif current_humidity > target_humidity:
            humidifier.decrease_humidity()

    # Read light intensity
    current_light_intensity = light_sensors[0].get_reading()
    if current_light_intensity is None:
        logger.warning("Could not read light intensity.")
    else:
        if target_light_intensity == "medium":
            light.set_brightness_level("medium")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Initialization**: The script initializes the home plan and identifies the Living Room.
# 2. **Target Conditions**: Sets the desired conditions for temperature, humidity, and light intensity.
# 3. **Sensor and Actuator Retrieval**: It retrieves the necessary sensors and actuators for controlling the environment.
# 4. **Temperature Control**: Depending on the current temperature, it activates either the heater or the AC.
# 5. **Humidity Control**: It increases or decreases the humidity based on the current reading.
# 6. **Light Control**: Sets the light brightness to medium.
# 
# ### Usage:
# To execute the functionality, ensure you run this `function.py` script in an environment where the other modules (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`, and `logger_config.py`) are accessible. The script will log the actions taken and print relevant messages to the console.