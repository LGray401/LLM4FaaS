# Below is a `function.py` file that you can put in the `functions` folder. This file contains a main function that uses the provided classes and methods from your existing source code files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) to implement the functional descriptions you provided.

import os
import sys

# Adjust the path to allow importing from the 'home' package
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'home'))

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW


def main():
    # Create the home plan
    home = home_plan()

    # Check temperature sensors and adjust temperature
    indoor_temp_sensors = get_all_sensors(home, 'IndoorTemperature')
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temp_reading = sensor.get_reading()
        if temp_reading is not None and temp_reading > TEMP_HIGH:
            print("Temperature:", "屋里太热了")
            acs = get_all_actuators(home, 'AC')
            for ac in acs:
                ac.set_target_temperature(TEMP_HIGH)
                ac.adjust_temperature(temp_reading)

    # Check humidity sensors and adjust humidity
    humidity_sensors = get_all_sensors(home, 'Humidity')
    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity_reading = sensor.get_reading()
        if humidity_reading is not None and humidity_reading < HUMIDITY_LOW:
            print("Humidity:", "屋里有点干")
            humidifiers = get_all_actuators(home, 'Humidifier')
            for humidifier in humidifiers:
                humidifier.increase_humidity()

    # Check light intensity sensors and adjust light
    light_sensors = get_all_sensors(home, 'LightIntensive')
    for sensor in light_sensors:
        sensor.turn_on()
        light_reading = sensor.get_reading()
        if light_reading is not None and light_reading < LIGHT_INTENSITY_LOW:
            print("Light Intensity:", "屋里太暗了")
            lights = get_all_actuators(home, 'Light')
            for light in lights:
                light.turn_on()
                light.set_brightness_level("high")


if __name__ == "__main__":
    main()