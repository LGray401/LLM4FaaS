# Given the functional description and the provided source code, I'll create a `function.py` file that utilizes the functionalities of the sensors and actuators as per your requirements. The main function will initialize the sensors and actuators, get their readings, and perform actions based on the provided threshold values from `config.py`.
# 
# Here's the `function.py` file:

# functions/function.py

import os
import sys
import time

# Ensure the home module can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create home plan
    home = home_plan()

    # Get all rooms
    rooms = ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"]
    
    for room_name in rooms:
        print(f"\nManaging {room_name}...")

        # Get sensors and actuators for the room
        sensors = get_room_sensors(home, room_name)
        actuators = get_room_actuators(home, room_name)

        # Initialize actuators
        heater = next((act for act in actuators if isinstance(act, Heater)), None)
        ac = next((act for act in actuators if isinstance(act, AC)), None)
        humidifier = next((act for act in actuators if isinstance(act, Humidifier)), None)
        light = next((act for act in actuators if isinstance(act, Light)), None)

        # Activate sensors
        for sensor in sensors:
            sensor.turn_on()

        # Read and manage temperature
        for sensor in sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                temp = sensor.get_reading()
                if temp is not None:
                    if temp < TEMP_LOW:
                        if heater:
                            heater.set_target_temperature(TEMP_HIGH)
                            heater.adjust_temperature(temp)
                    elif temp > TEMP_HIGH:
                        if ac:
                            ac.set_target_temperature(TEMP_LOW)
                            ac.adjust_temperature(temp)

        # Read and manage humidity
        for sensor in sensors:
            if isinstance(sensor, HumiditySensor):
                humidity = sensor.get_reading()
                if humidity is not None:
                    if humidity < HUMIDITY_LOW and humidifier:
                        humidifier.turn_on()
                    elif humidity > HUMIDITY_HIGH and humidifier:
                        humidifier.turn_off()

        # Read and manage light intensity
        for sensor in sensors:
            if isinstance(sensor, LightIntensiveSensor):
                light_intensity = sensor.get_reading()
                if light_intensity is not None:
                    if light_intensity < LIGHT_INTENSITY_LOW and light:
                        light.turn_on()
                        light.set_brightness_level("high")
                    elif light_intensity > LIGHT_INTENSITY_HIGH and light:
                        light.turn_off()

        # Turn off sensors after use
        for sensor in sensors:
            sensor.turn_off()

if __name__ == "__main__":
    main()