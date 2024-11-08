# Based on your functional description and the provided source code, I will create a `function.py` file that implements the main functionality of your smart home project. This file will control the temperature, humidity, and light intensity based on sensor readings and automatically manage the actuators accordingly.
# 
# Here’s the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()

    # Iterate through each room and manage the sensors and actuators
    for room in home:
        # Get the sensors and actuators for the current room
        sensors = room.sensors
        actuators = room.actuators

        temperature_sensor = next((sensor for sensor in sensors if sensor.sensor_type == "IndoorTemperature"), None)
        humidity_sensor = next((sensor for sensor in sensors if sensor.sensor_type == "Humidity"), None)
        light_sensor = next((sensor for sensor in sensors if sensor.sensor_type == "LightIntensive"), None)

        ac_unit = next((actuator for actuator in actuators if actuator.actuator_type == "AC"), None)
        humidifier = next((actuator for actuator in actuators if actuator.actuator_type == "Humidifier"), None)
        light = next((actuator for actuator in actuators if actuator.actuator_type == "Light"), None)

        # Manage temperature
        if temperature_sensor:
            current_temp = temperature_sensor.get_reading()
            if current_temp is not None:
                logger.info(f"{room.name} - Current Temperature: {current_temp}°C")
                if ac_unit:
                    ac_unit.adjust_temperature(current_temp)

        # Manage humidity
        if humidity_sensor:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                logger.info(f"{room.name} - Current Humidity: {current_humidity}%")
                if humidifier:
                    if current_humidity < HUMIDITY_HIGH:
                        humidifier.increase_humidity()
                    else:
                        humidifier.decrease_humidity()

        # Manage light intensity
        if light_sensor:
            current_light = light_sensor.get_reading()
            if current_light is not None:
                logger.info(f"{room.name} - Current Light Intensity: {current_light} lux")
                if light:
                    if current_light < LIGHT_INTENSITY_HIGH:
                        light.turn_on()
                    else:
                        light.turn_off()

if __name__ == "__main__":
    main()