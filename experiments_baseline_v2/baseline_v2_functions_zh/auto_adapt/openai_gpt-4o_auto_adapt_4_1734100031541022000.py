# Based on the functional description and the reference source code files you provided, I'll create a Python script that simulates a smart home application. This script will utilize the existing `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` modules to monitor and control the smart home environment according to the specified temperature, humidity, and light intensity.
# 
# I'll write a script named `smart_home.py` that initializes the home setup, checks the sensor readings, and adjusts the actuators accordingly.
# 
# ### `smart_home.py`
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Define target values based on functional description
    target_temperature = 20
    target_humidity = 50
    target_light_intensity = 15

    # Get all sensors and actuators
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Turn on sensors and actuators
    for sensor in temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()

    for actuator in heaters + acs + humidifiers + lights:
        actuator.turn_on()

    # Adjust temperature
    for sensor in temp_sensors:
        current_temp = sensor.get_reading()
        if current_temp is not None:
            for heater in heaters:
                heater.set_target_temperature(target_temperature)
                heater.adjust_temperature(current_temp)
            for ac in acs:
                ac.set_target_temperature(target_temperature)
                ac.adjust_temperature(current_temp)

    # Adjust humidity
    for sensor in humidity_sensors:
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            for humidifier in humidifiers:
                if current_humidity < target_humidity:
                    humidifier.increase_humidity()
                elif current_humidity > target_humidity:
                    humidifier.decrease_humidity()

    # Adjust light intensity
    for sensor in light_sensors:
        current_light_intensity = sensor.get_reading()
        if current_light_intensity is not None:
            for light in lights:
                # Assume lights have a method to set brightness based on percentage (not present in the original code)
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    light.set_brightness_level("high")
                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                    light.set_brightness_level("low")
                else:
                    light.set_brightness_level("medium")

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run
# 
# To execute this script in a Linux terminal, navigate to the directory containing the `home` folder and the `smart_home.py` script, and run the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This script will simulate a smart home environment by turning on sensors and actuators, reading the current conditions, and adjusting the actuators to match the desired temperature, humidity, and light intensity levels as specified in the functional description.