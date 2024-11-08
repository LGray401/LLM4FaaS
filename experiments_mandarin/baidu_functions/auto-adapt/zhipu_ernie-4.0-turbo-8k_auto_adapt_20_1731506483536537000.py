# Based on your functional description and the provided source code, here is the `function.py` file that contains the main function to control the smart home environment. This file will be located in the `functions` folder.
# 
# ### function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def adjust_temperature(sensors, actuators):
    for sensor in sensors:
        if sensor.sensor_type == "IndoorTemperature":
            reading = sensor.get_reading()
            if reading is not None:
                for actuator in actuators:
                    if actuator.actuator_type == "AC" and reading > TEMP_HIGH:
                        actuator.turn_on()
                        logger.info(f"Turned on AC in {actuator.room_name} due to high temperature: {reading}°C")
                    elif actuator.actuator_type == "Heater" and reading < TEMP_HIGH - 5:  # Example threshold
                        actuator.turn_on()
                        logger.info(f"Turned on Heater in {actuator.room_name} due to low temperature: {reading}°C")
                    else:
                        actuator.turn_off()
                        logger.info(f"Turned off {actuator.actuator_type} in {actuator.room_name}")

def adjust_humidity(sensors, actuators):
    for sensor in sensors:
        if sensor.sensor_type == "Humidity":
            reading = sensor.get_reading()
            if reading is not None:
                for actuator in actuators:
                    if actuator.actuator_type == "Humidifier":
                        if reading < HUMIDITY_LOW:
                            actuator.increase_humidity()
                            logger.info(f"Increasing humidity in {actuator.room_name} due to low humidity: {reading}%")
                        elif reading > HUMIDITY_HIGH:
                            actuator.decrease_humidity()
                            logger.info(f"Decreasing humidity in {actuator.room_name} due to high humidity: {reading}%")

def adjust_light_intensity(sensors, actuators):
    for sensor in sensors:
        if sensor.sensor_type == "LightIntensive":
            reading = sensor.get_reading()
            if reading is not None:
                for actuator in actuators:
                    if actuator.actuator_type == "Light":
                        if reading < LIGHT_INTENSITY_LOW:
                            actuator.turn_on()
                            actuator.set_brightness_level("high")
                            logger.info(f"Turned on light in {actuator.room_name} and set to high due to low light intensity: {reading} lux")
                        elif reading > LIGHT_INTENSITY_HIGH:
                            actuator.turn_off()
                            logger.info(f"Turned off light in {actuator.room_name} due to high light intensity: {reading} lux")
                        else:
                            actuator.set_brightness_level("medium")
                            logger.info(f"Set light in {actuator.room_name} to medium brightness")

def main():
    home = home_plan()
    
    # Adjust temperature
    for room in home:
        sensors = get_all_sensors([room], "IndoorTemperature")
        actuators = get_all_actuators([room], "AC") + get_all_actuators([room], "Heater")
        adjust_temperature(sensors, actuators)
    
    # Adjust humidity
    for room in home:
        sensors = get_all_sensors([room], "Humidity")
        actuators = get_all_actuators([room], "Humidifier")
        adjust_humidity(sensors, actuators)
    
    # Adjust light intensity
    for room in home:
        sensors = get_all_sensors([room], "LightIntensive")
        actuators = get_all_actuators([room], "Light")
        adjust_light_intensity(sensors, actuators)

if __name__ == "__main__":
    main()