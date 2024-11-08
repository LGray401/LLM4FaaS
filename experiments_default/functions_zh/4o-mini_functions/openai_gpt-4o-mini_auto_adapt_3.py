# Based on your functional description and the provided code files, I'll create a `function.py` file. This file will contain a main function that orchestrates the smart home functionality, particularly focusing on the temperature, humidity, and light intensity readings. 
# 
# Here’s the content for the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize the home with rooms and components
    home = home_plan()

    # Iterate through each room to gather readings from sensors
    for room in home:
        print(f"\n--- {room.name} ---")
        
        # Get sensors
        temperature_sensors = room.sensors
        humidity_sensors = room.sensors
        light_sensors = room.sensors

        # Read and process temperature
        for sensor in temperature_sensors:
            if isinstance(sensor, (IndoorTemperatureSensor, OutdoorTemperatureSensor)):
                sensor.turn_on()
                temperature_reading = sensor.get_reading()
                if temperature_reading is not None:
                    if temperature_reading < TEMP_LOW:
                        logger.warning(f"Temperature in {room.name} is too low: {temperature_reading}°C.")
                    elif temperature_reading > TEMP_HIGH:
                        logger.warning(f"Temperature in {room.name} is too high: {temperature_reading}°C.")
                    else:
                        logger.info(f"Temperature in {room.name} is normal: {temperature_reading}°C.")
                sensor.turn_off()

        # Read and process humidity
        for sensor in humidity_sensors:
            if isinstance(sensor, HumiditySensor):
                sensor.turn_on()
                humidity_reading = sensor.get_reading()
                if humidity_reading is not None:
                    if humidity_reading < HUMIDITY_LOW:
                        logger.warning(f"Humidity in {room.name} is too low: {humidity_reading}%.")
                    elif humidity_reading > HUMIDITY_HIGH:
                        logger.warning(f"Humidity in {room.name} is too high: {humidity_reading}%.")
                    else:
                        logger.info(f"Humidity in {room.name} is normal: {humidity_reading}%.")
                sensor.turn_off()

        # Read and process light intensity
        for sensor in light_sensors:
            if isinstance(sensor, LightIntensiveSensor):
                sensor.turn_on()
                light_reading = sensor.get_reading()
                if light_reading is not None:
                    if light_reading < LIGHT_INTENSITY_LOW:
                        logger.warning(f"Light intensity in {room.name} is too low: {light_reading} lux.")
                    elif light_reading > LIGHT_INTENSITY_HIGH:
                        logger.warning(f"Light intensity in {room.name} is too high: {light_reading} lux.")
                    else:
                        logger.info(f"Light intensity in {room.name} is normal: {light_reading} lux.")
                sensor.turn_off()

if __name__ == "__main__":
    main()