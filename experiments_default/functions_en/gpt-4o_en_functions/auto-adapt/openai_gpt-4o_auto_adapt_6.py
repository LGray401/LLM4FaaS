# Here's the `function.py` file that meets your functional requirements. This script will collect temperature, humidity, and light intensity readings from sensors and print them out.
# 
# `function.py`:

import os
import sys

# Add the 'home' directory to the sys.path to import modules from it
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
home_dir = os.path.join(parent_dir, 'home')
sys.path.append(home_dir)

from home.home_plan import home_plan, get_all_sensors
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def main():
    home = home_plan()

    # Get all sensors of each type
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    print("\nTemperature Readings:")
    for sensor in indoor_temp_sensors + outdoor_temp_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        sensor.turn_off()

    print("\nHumidity Readings:")
    for sensor in humidity_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        sensor.turn_off()

    print("\nLight Intensity Readings:")
    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        sensor.turn_off()

if __name__ == "__main__":
    main()