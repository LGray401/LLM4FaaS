# Based on your functional description and provided code snippets, I'll provide a `function.py` file that includes a `main` function that integrates the various components and features of your smart home system.

# function.py
import os
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

# Set up the logger configuration
# Assuming logger_config is already defined elsewhere in your project
from home.logger_config import logger

def main():
    # Load the home plan
    home = home_plan()

    # Initialize actuators
    ac = AC("LivingRoom")
    heater = Heater("LivingRoom")
    humidifier = Humidifier("LivingRoom")

    # Main loop
    while True:
        # Check indoor temperature
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        for sensor in temperature_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                logger.info(f"Indoor Temperature in {sensor.room_name}: {reading}°C")
                if reading > TEMP_HIGH:
                    ac.turn_on()
                    logger.info("AC turned on due to high temperature.")
                elif reading < TEMP_LOW:
                    heater.turn_on()
                    logger.info("Heater turned on due to low temperature.")

        # Check humidity
        humidity_sensors = get_all_sensors(home, "Humidity")
        for sensor in humidity_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                logger.info(f"Humidity in {sensor.room_name}: {reading}%")
                if reading > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()
                    logger.info("Humidifier turned on to decrease humidity.")
                elif reading < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                    logger.info("Humidifier turned on to increase humidity.")

        # Check light intensity
        light_intensity_sensors = get_all_sensors(home, "LightIntensive")
        for sensor in light_intensity_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                logger.info(f"Light Intensity in {sensor.room_name}: {reading} lux")
                if reading > LIGHT_INTENSITY_HIGH:
                    # Logic to dim the lights
                    logger.info("Dimming lights due to high light intensity.")
                elif reading < LIGHT_INTENSITY_LOW:
                    # Logic to brighten the lights
                    logger.info("Brightening lights due to low light intensity.")

        # Sleep for a while before checking again
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()