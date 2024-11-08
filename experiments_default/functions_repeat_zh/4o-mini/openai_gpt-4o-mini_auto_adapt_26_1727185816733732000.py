# Based on your functional description and the provided source code, I will create the `function.py` file in the `functions` folder. This file will contain a main function that manages the temperature, humidity, and light intensity as specified.
# 
# Here’s the implementation for `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
import time

def maintain_environment(home):
    for room in home:
        # Get temperature sensors and actuators
        temp_sensors = get_all_sensors(home, "IndoorTemperature")
        humidity_sensors = get_all_sensors(home, "Humidity")
        light_sensors = get_all_sensors(home, "LightIntensive")

        temp_actuators = get_all_actuators(home, "Heater") + get_all_actuators(home, "AC")
        humidifiers = get_all_actuators(home, "Humidifier")
        lights = get_all_actuators(home, "Light")

        # Maintain temperature
        for temp_sensor in temp_sensors:
            current_temp = temp_sensor.get_reading()
            if current_temp is not None:
                for actuator in temp_actuators:
                    if isinstance(actuator, Heater):
                        actuator.set_target_temperature(26)  # Set target temperature to 26°C
                        actuator.adjust_temperature(current_temp)
                    elif isinstance(actuator, AC):
                        actuator.set_target_temperature(26)  # Set target temperature to 26°C
                        actuator.adjust_temperature(current_temp)

        # Maintain humidity
        for humidity_sensor in humidity_sensors:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                for humidifier in humidifiers:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif current_humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

        # Maintain light intensity based on time of day or activity
        for light_sensor in light_sensors:
            # Sample logic for adjusting light based on time/activity
            current_light = light_sensor.get_reading()
            if current_light is not None:
                if is_working_time():  # Placeholder: replace with actual time check
                    for light in lights:
                        light.set_brightness_level("high")
                elif is_relaxing_time():  # Placeholder: replace with actual time check
                    for light in lights:
                        light.set_brightness_level("low")
                elif is_rest_time():  # Placeholder: replace with actual time check
                    for light in lights:
                        light.turn_off()

def is_working_time():
    # Implement logic to determine if it's working time
    return True  # Placeholder for working time logic

def is_relaxing_time():
    # Implement logic to determine if it's relaxing time
    return False  # Placeholder for relaxing time logic

def is_rest_time():
    # Implement logic to determine if it's rest time
    return False  # Placeholder for rest time logic

def main():
    home = home_plan()
    while True:
        maintain_environment(home)
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()