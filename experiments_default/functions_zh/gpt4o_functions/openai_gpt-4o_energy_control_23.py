# Based on your functional description and the provided source code, here is a 'function.py' file that meets your requirements. This file will be located in the 'functions' folder and should contain the main function to control the smart home based on the given conditions.
# 
# Please ensure that the 'home' folder and its files are accessible from this script.
# 
# Here is the 'function.py' code:

# functions/function.py

import datetime
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, Humidifier, Light, CleaningRobot
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, LIGHT_INTENSITY_HIGH, HUMIDITY_LOW

def main():
    home = home_plan()

    # Get all required sensors
    light_sensors = get_all_sensors(home, "LightIntensive")
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Get all required actuators
    heaters = get_all_actuators(home, "Heater")
    lights = get_all_actuators(home, "Light")
    humidifiers = get_all_actuators(home, "Humidifier")
    cleaning_robots = get_all_actuators(home, "CleaningRobot")

    # Check light intensity and turn off lights if necessary
    for sensor in light_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        if light_intensity and light_intensity > LIGHT_INTENSITY_HIGH:
            for light in lights:
                light.turn_off()

    # Check indoor temperature and turn on heaters if necessary
    for sensor in temp_sensors:
        sensor.turn_on()
        temperature = sensor.get_reading()
        if temperature and temperature < TEMP_LOW:
            for heater in heaters:
                heater.turn_on()

    # Check current time and day for cleaning robot operation
    current_datetime = datetime.datetime.now()
    current_hour = current_datetime.hour
    current_day = current_datetime.weekday()

    if 9 <= current_hour <= 17 and current_day < 5:  # Working hours are from 9 AM to 5 PM, Monday to Friday
        for robot in cleaning_robots:
            robot.turn_on()
            robot.daily_routine()

    # Check humidity and turn on humidifiers if necessary
    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity = sensor.get_reading()
        if humidity and humidity < HUMIDITY_LOW:
            for humidifier in humidifiers:
                humidifier.turn_on()
                humidifier.increase_humidity()

if __name__ == "__main__":
    main()