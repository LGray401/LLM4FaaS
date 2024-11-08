# Sure, based on the provided files and functional description, I will create the `function.py` file that will integrate all these components to achieve the desired functionality.
# 
# Here's the `function.py` file:

# functions/function.py
import os
import sys

# Add the home directory to the sys.path to allow imports from the home directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'home'))

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    temperature_sensor = None
    humidity_sensor = None
    light_intensity_sensor = None

    ac = None
    heater = None
    humidifier = None
    light = None

    for sensor in living_room_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature_sensor = sensor
        elif isinstance(sensor, HumiditySensor):
            humidity_sensor = sensor
        elif isinstance(sensor, LightIntensiveSensor):
            light_intensity_sensor = sensor

    for actuator in living_room_actuators:
        if isinstance(actuator, AC):
            ac = actuator
        elif isinstance(actuator, Heater):
            heater = actuator
        elif isinstance(actuator, Humidifier):
            humidifier = actuator
        elif isinstance(actuator, Light):
            light = actuator

    if temperature_sensor:
        temperature_sensor.turn_on()
        temperature = temperature_sensor.get_reading()
        print(f"今日温度: {temperature}度")

        if ac and heater:
            ac.set_target_temperature(TEMP_HIGH)
            heater.set_target_temperature(TEMP_LOW)
            ac.adjust_temperature(temperature)
            heater.adjust_temperature(temperature)

    if humidity_sensor:
        humidity_sensor.turn_on()
        humidity = humidity_sensor.get_reading()
        print(f"今日湿度: {humidity}")

        if humidifier:
            if humidity < HUMIDITY_LOW:
                humidifier.turn_on()
                humidifier.increase_humidity()
            elif humidity > HUMIDITY_HIGH:
                humidifier.turn_on()
                humidifier.decrease_humidity()
            else:
                humidifier.turn_off()

    if light_intensity_sensor:
        light_intensity_sensor.turn_on()
        light_intensity = light_intensity_sensor.get_reading()
        print(f"今日光照: {light_intensity}")

        if light:
            light.turn_on()
            if light_intensity < LIGHT_INTENSITY_LOW:
                light.set_brightness_level("high")
            elif light_intensity > LIGHT_INTENSITY_HIGH:
                light.set_brightness_level("low")
            else:
                light.set_brightness_level("medium")

if __name__ == "__main__":
    main()