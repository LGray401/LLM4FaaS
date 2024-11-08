# Sure, I'll create the `function.py` file which will be located in the 'functions' folder. This file will contain the main function which will use the provided functional description to control the smart home environment.

# functions/function.py

import sys
import os

# Add the home directory to the sys.path so we can import modules from it
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'home'))

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    # Create the home plan
    home = home_plan()

    # Set target values based on functional description
    target_temp = 24
    target_humidity = 30
    target_light_intensity = 45

    # Get all sensors of interest
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all actuators of interest
    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Activate sensors and get readings
    for sensor in indoor_temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()

    # Adjust temperature
    for sensor in indoor_temp_sensors:
        current_temp = sensor.get_reading()
        if current_temp is not None:
            for heater in heaters:
                heater.set_target_temperature(target_temp)
                heater.adjust_temperature(current_temp)
            for ac in ac_units:
                ac.set_target_temperature(target_temp)
                ac.adjust_temperature(current_temp)

    # Adjust humidity
    for sensor in humidity_sensors:
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            for humidifier in humidifiers:
                if current_humidity < target_humidity:
                    humidifier.turn_on()
                    humidifier.increase_humidity()
                else:
                    humidifier.turn_off()
                    humidifier.decrease_humidity()

    # Adjust light intensity
    for sensor in light_sensors:
        current_light_intensity = sensor.get_reading()
        if current_light_intensity is not None:
            for light in lights:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                    light.set_brightness_level("high")
                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                    light.turn_off()
                else:
                    light.turn_on()
                    light.set_brightness_level("medium")

    # Turn off sensors
    for sensor in indoor_temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()