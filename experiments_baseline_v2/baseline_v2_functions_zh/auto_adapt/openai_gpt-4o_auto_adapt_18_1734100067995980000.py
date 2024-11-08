# To create a smart home application based on your functional description and the provided code references, we need to develop a Python script that will use the existing classes and methods to simulate a smart home environment. The script will instantiate sensors and actuators, get readings from sensors, and adjust actuators according to specific conditions.
# 
# Here's a Python script that meets your requirements:
# 
# ```python
# main.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def control_temperature(room):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)

    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            sensor.turn_on()
            current_temp = sensor.get_reading()

            for actuator in actuators:
                if isinstance(actuator, AC):
                    actuator.set_target_temperature(TEMP_HIGH)
                    actuator.adjust_temperature(current_temp)
                elif isinstance(actuator, Heater):
                    actuator.set_target_temperature(TEMP_LOW)
                    actuator.adjust_temperature(current_temp)

def control_humidity(room):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)

    for sensor in sensors:
        if isinstance(sensor, HumiditySensor):
            sensor.turn_on()
            current_humidity = sensor.get_reading()

            for actuator in actuators:
                if isinstance(actuator, Humidifier):
                    if current_humidity < HUMIDITY_LOW:
                        actuator.increase_humidity()
                    elif current_humidity > HUMIDITY_HIGH:
                        actuator.decrease_humidity()

def control_light_intensity(room):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)

    for sensor in sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            current_light_intensity = sensor.get_reading()

            for actuator in actuators:
                if isinstance(actuator, Light):
                    actuator.turn_on()
                    if current_light_intensity < LIGHT_INTENSITY_LOW:
                        actuator.set_brightness_level("high")
                    elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                        actuator.set_brightness_level("low")
                    else:
                        actuator.set_brightness_level("medium")

if __name__ == "__main__":
    home = home_plan()

    # Control systems for each room
    for room in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"]:
        control_temperature(room)
        control_humidity(room)
        control_light_intensity(room)
# ```
# 
# ### How to Run
# 
# To execute this script in a Linux terminal, you can use the following command:
# 
# ```bash
# python3 main.py
# ```
# 
# ### Explanation
# 
# - **Temperature Control**: Uses `IndoorTemperatureSensor` to read current temperature and adjusts `AC` and `Heater` actuators based on thresholds defined in `config.py`.
#   
# - **Humidity Control**: Uses `HumiditySensor` to read current humidity and adjusts the `Humidifier`.
#   
# - **Light Intensity Control**: Uses `LightIntensiveSensor` to read current light intensity and adjusts the brightness of `Light` actuators.
# 
# Make sure to have the `home` directory with the provided Python files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) in the same directory as this `main.py` script. This script simulates a simple environment where sensors read data and actuators respond according to the conditions specified in the configuration file.