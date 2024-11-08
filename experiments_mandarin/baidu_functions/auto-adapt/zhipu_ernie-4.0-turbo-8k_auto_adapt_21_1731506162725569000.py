# Based on your functional description and the provided source code, here is the `function.py` file that you can use in your smart home project. This file contains the main function that will handle the temperature, humidity, and light intensity adjustments as specified.

# function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def adjust_temperature(sensors, actuators):
    """
    Adjust the temperature based on the sensor readings.
    Turn on the AC if the temperature is above the threshold.
    """
    for sensor in sensors:
        if sensor.sensor_type == "IndoorTemperature" and sensor.status == "on":
            reading = sensor.get_reading()
            if reading > TEMP_HIGH:
                for actuator in actuators:
                    if actuator.actuator_type == "AC":
                        actuator.turn_on()
                        logger.info(f"Turned on AC in {actuator.room_name} due to high temperature: {reading}°C")
                        # Optionally, set a target temperature for the AC
                        actuator.set_target_temperature(25)  # Example target temperature
            else:
                for actuator in actuators:
                    if actuator.actuator_type == "AC":
                        actuator.turn_off()
                        logger.info(f"Turned off AC in {actuator.room_name} due to normal temperature: {reading}°C")


def adjust_humidity(sensors, actuators):
    """
    Placeholder function for humidity adjustment.
    Currently, it just logs the humidity readings.
    """
    for sensor in sensors:
        if sensor.sensor_type == "Humidity" and sensor.status == "on":
            reading = sensor.get_reading()
            logger.info(f"Humidity in {sensor.room_name} is {reading}%")
            # Add logic to adjust humidifiers or dehumidifiers if necessary


def adjust_light_intensity(sensors, actuators):
    """
    Adjust the light intensity based on the sensor readings.
    Turn on the curtains if the light intensity is above the threshold.
    """
    for sensor in sensors:
        if sensor.sensor_type == "LightIntensive" and sensor.status == "on":
            reading = sensor.get_reading()
            if reading > LIGHT_INTENSITY_HIGH:
                for actuator in actuators:
                    if actuator.actuator_type == "Curtain":
                        actuator.turn_on()
                        logger.info(f"Turned on curtains in {actuator.room_name} due to high light intensity: {reading} lux")
            else:
                for actuator in actuators:
                    if actuator.actuator_type == "Curtain":
                        actuator.turn_off()
                        logger.info(f"Turned off curtains in {actuator.room_name} due to normal light intensity: {reading} lux")


def main():
    """
    Main function to run the smart home adjustments.
    """
    home = home_plan()
    
    # Get all temperature sensors and AC actuators
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    ac_actuators = get_all_actuators(home, "AC")
    
    # Get all humidity sensors and humidifier actuators (placeholder for now)
    humidity_sensors = get_all_sensors(home, "Humidity")
    # Humidifier actuators logic should be added here if needed
    
    # Get all light intensity sensors and curtain actuators
    light_sensors = get_all_sensors(home, "LightIntensive")
    curtain_actuators = get_all_actuators(home, "Curtain")
    
    # Adjust the temperature
    adjust_temperature(temp_sensors, ac_actuators)
    
    # Adjust the humidity (placeholder)
    adjust_humidity(humidity_sensors, [])  # Pass an empty list for actuators as placeholder
    
    # Adjust the light intensity
    adjust_light_intensity(light_sensors, curtain_actuators)


if __name__ == "__main__":
    main()