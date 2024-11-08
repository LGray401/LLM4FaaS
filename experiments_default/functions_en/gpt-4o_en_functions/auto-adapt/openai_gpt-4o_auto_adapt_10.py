# Based on the provided functional description and source code of your smart home project, I will create a `function.py` file that integrates the functionalities of the sensor and actuator classes, and uses the home plan to create a main function to manage the temperature, humidity, and light intensity based on the given conditions.
# 
# Here's the `function.py` file:

# functions/function.py
import os
import sys

# Ensure the 'home' folder is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'home'))

from home_plan import home_plan, get_all_sensors, get_all_actuators
from config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    # Create the home plan
    home = home_plan()

    # Check and manage indoor temperature
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temp = sensor.get_reading()
        if temp is not None:
            for heater in heaters:
                if heater.room_name == sensor.room_name:
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(temp)
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_LOW)
                    ac.adjust_temperature(temp)
        sensor.turn_off()

    # Check and manage humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity = sensor.get_reading()
        if humidity is not None:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    if humidity < HUMIDITY_LOW:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                    elif humidity > HUMIDITY_HIGH:
                        humidifier.turn_on()
                        humidifier.decrease_humidity()
                    else:
                        humidifier.turn_off()
        sensor.turn_off()

    # Check and manage light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    
    for sensor in light_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            for light in lights:
                if light.room_name == sensor.room_name:
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                        light.turn_off()
                    else:
                        light.turn_on()
                        light.set_brightness_level("medium")
        sensor.turn_off()

if __name__ == "__main__":
    main()