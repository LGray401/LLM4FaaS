# Let's create the `function.py` file based on the given functional description and source code. The main function will be designed to demonstrate the following:
# 
# 1. Turning on sensors and actuators.
# 2. Getting readings from sensors.
# 3. Adjusting actuators based on the sensor readings.
# 4. Printing status and notifications.
# 
# Here's the `function.py` file that accomplishes the specified tasks:

import sys
import os

# Assuming the home directory is in the parent directory of this script
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'home')))

from sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from actuator import Heater, AC, Light
from home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators
from config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def main():
    # Create home plan
    home = home_plan()
    print_home_plan(home)

    # Get sensors and actuators from the LivingRoom
    room_name = "LivingRoom"
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    # Turn on all sensors and actuators
    for sensor in sensors:
        sensor.turn_on()

    for actuator in actuators:
        actuator.turn_on()

    # Get readings from sensors
    temperature = None
    humidity = None
    light_intensity = None

    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature = sensor.get_reading()
        elif isinstance(sensor, HumiditySensor):
            humidity = sensor.get_reading()
        elif isinstance(sensor, LightIntensiveSensor):
            light_intensity = sensor.get_reading()

    # Adjust actuators based on sensor readings
    for actuator in actuators:
        if isinstance(actuator, Heater) and temperature is not None:
            if temperature < TEMP_LOW:
                actuator.set_target_temperature(TEMP_LOW)
                actuator.adjust_temperature(temperature)
            elif temperature > TEMP_HIGH:
                actuator.turn_off()
        elif isinstance(actuator, AC) and temperature is not None:
            if temperature > TEMP_HIGH:
                actuator.set_target_temperature(TEMP_HIGH)
                actuator.adjust_temperature(temperature)
            elif temperature < TEMP_LOW:
                actuator.turn_off()
        elif isinstance(actuator, Light) and light_intensity is not None:
            if light_intensity < LIGHT_INTENSITY_LOW:
                actuator.set_brightness_level("high")
            elif light_intensity > LIGHT_INTENSITY_HIGH:
                actuator.set_brightness_level("low")

    # Print status of all sensors and actuators
    for sensor in sensors:
        sensor.get_status()

    for actuator in actuators:
        actuator.get_status()

    # Turn off all sensors and actuators
    for sensor in sensors:
        sensor.turn_off()

    for actuator in actuators:
        actuator.turn_off()


if __name__ == "__main__":
    main()