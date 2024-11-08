# Sure, based on the provided functional description and the source code files, here is the `function.py` file located in the `functions` folder. This file will contain the main function which will turn on temperature sensors, open windows, and turn on lights, etc.
# 
# ### function.py

import os
import sys

# Adjust the import paths to correctly reference the `home` directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'home'))

from sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from actuator import Window, Light
from home_plan import home_plan, get_all_sensors, get_all_actuators
from config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize home with rooms and components
    home = home_plan()

    # Turn on all temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        sensor.turn_on()

    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    for sensor in outdoor_temp_sensors:
        sensor.turn_on()

    # Open all windows
    windows = get_all_actuators(home, "Window")
    for window in windows:
        window.turn_on()

    # Turn on all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
    
    print("All temperature sensors are turned on, windows are opened, and lights are turned on.")

if __name__ == "__main__":
    main()