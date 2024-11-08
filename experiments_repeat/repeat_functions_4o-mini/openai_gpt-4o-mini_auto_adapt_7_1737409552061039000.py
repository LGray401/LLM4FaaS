# Based on your functional description and the provided code, I will create the `function.py` file that includes a main function to manage the smart home system. This function will check the readings from various sensors and control the actuators accordingly to address the conditions described in your functional description: high temperature, low humidity, and low light intensity. 
# 
# Here's the `function.py` code:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize home plan
    home = home_plan()

    for room in home:
        # Get sensors and actuators in the room
        temperature_sensors = room.sensors
        humidity_sensors = room.sensors
        light_sensors = room.sensors
        actuators = room.actuators
        
        # Get temperature readings
        for sensor in temperature_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                current_temp = sensor.get_reading()
                if current_temp is not None:
                    if current_temp > TEMP_HIGH:
                        logger.info(f"Temperature in {room.name} is too high: {current_temp}°C")
                        heater = next((a for a in actuators if isinstance(a, Heater)), None)
                        if heater:
                            heater.turn_on()
                            heater.set_target_temperature(TEMP_LOW)

        # Get humidity readings
        for sensor in humidity_sensors:
            if isinstance(sensor, HumiditySensor):
                current_humidity = sensor.get_reading()
                if current_humidity is not None:
                    if current_humidity < HUMIDITY_LOW:
                        logger.info(f"Humidity in {room.name} is too low: {current_humidity}%")
                        humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
                        if humidifier:
                            humidifier.turn_on()
                            humidifier.increase_humidity()

        # Get light intensity readings
        for sensor in light_sensors:
            if isinstance(sensor, LightIntensiveSensor):
                current_light = sensor.get_reading()
                if current_light is not None:
                    if current_light < LIGHT_INTENSITY_LOW:
                        logger.info(f"Light intensity in {room.name} is too low: {current_light} lux")
                        light = next((a for a in actuators if isinstance(a, Light)), None)
                        if light:
                            light.turn_on()
                            light.set_brightness_level("high")  # Set to high brightness

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Home Initialization**: The `home_plan()` function is called to initialize the home with rooms, sensors, and actuators.
# 2. **Sensor Readings**: The code iterates through each room to check the readings of temperature, humidity, and light intensity.
# 3. **Actuator Control**:
#    - If the temperature is too high, it activates the heater and sets a target temperature.
#    - If the humidity is too low, it activates the humidifier to increase humidity.
#    - If the light intensity is too low, it activates the light and sets it to high brightness.
# 4. **Logging**: The logger records the actions taken for monitoring purposes.
# 
# ### Note:
# Make sure you have the `functions` directory created in your project structure for this file to be placed correctly. You can adjust the logging and control behavior as per your specific requirements.