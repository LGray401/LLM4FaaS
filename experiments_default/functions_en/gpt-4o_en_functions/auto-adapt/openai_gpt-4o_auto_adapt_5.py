# Based on the provided functional description and source code, I'll create a `function.py` file that will be located in the `functions` folder and will contain a main function. The main function will simulate a control loop for a smart home system using the given temperature, humidity, and light intensity values. 
# 
# Here's the `function.py` file:

# function.py
import sys
import os

# Add the home directory to the sys path
home_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'home'))
sys.path.append(home_dir)

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Given values
    temperature = 24
    humidity = 30
    light_intensity = 45

    # Control logic for temperature
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")

    for sensor in indoor_temperature_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        for heater in heaters:
            heater.set_target_temperature(TEMP_HIGH)
            heater.adjust_temperature(current_temp)
        for ac in ac_units:
            ac.set_target_temperature(TEMP_LOW)
            ac.adjust_temperature(current_temp)
        sensor.turn_off()

    # Control logic for humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity < HUMIDITY_LOW:
            for humidifier in humidifiers:
                humidifier.turn_on()
                humidifier.increase_humidity()
        elif current_humidity > HUMIDITY_HIGH:
            for humidifier in humidifiers:
                humidifier.turn_on()
                humidifier.decrease_humidity()
        sensor.turn_off()

    # Control logic for light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        for light in lights:
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                light.turn_on()
                light.set_brightness_level("high")
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                light.turn_off()
        sensor.turn_off()

if __name__ == "__main__":
    main()