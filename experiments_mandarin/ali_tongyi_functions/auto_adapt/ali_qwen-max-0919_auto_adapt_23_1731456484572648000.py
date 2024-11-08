# Based on your provided functional description and source code, I will create a `function.py` file that contains the main function. This main function will control the smart home system according to the given temperature, humidity, and light intensity settings.
# 
# ### Functional Description
# - **Temperature:** 23°C
# - **Humidity:** 人感觉舒适 (Comfortable for humans)
# - **Light Intensity:** 柔和 (Soft)
# 
# ### Steps to Implement
# 1. **Initialize the Home Plan:** Load the rooms and their components.
# 2. **Set the Target Temperature, Humidity, and Light Intensity:** Based on the given functional description.
# 3. **Adjust Actuators Based on Sensor Readings:**
#    - Adjust the temperature using heaters and ACs.
#    - Adjust the humidity using humidifiers.
#    - Adjust the light intensity using lights.
# 
# ### `function.py`

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

# Constants from config.py
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def adjust_temperature(room, target_temperature):
    current_temperature = None
    for sensor in get_room_sensors(home, room.name):
        if isinstance(sensor, IndoorTemperatureSensor):
            sensor.turn_on()
            current_temperature = sensor.get_reading()
            sensor.turn_off()
            break

    if current_temperature is not None:
        for actuator in get_room_actuators(home, room.name):
            if isinstance(actuator, Heater) or isinstance(actuator, AC):
                actuator.set_target_temperature(target_temperature)
                actuator.adjust_temperature(current_temperature)

def adjust_humidity(room, target_humidity):
    current_humidity = None
    for sensor in get_room_sensors(home, room.name):
        if isinstance(sensor, HumiditySensor):
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            sensor.turn_off()
            break

    if current_humidity is not None:
        for actuator in get_room_actuators(home, room.name):
            if isinstance(actuator, Humidifier):
                if current_humidity < target_humidity:
                    actuator.increase_humidity()
                else:
                    actuator.decrease_humidity()

def adjust_light_intensity(room, target_light_intensity):
    current_light_intensity = None
    for sensor in get_room_sensors(home, room.name):
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            current_light_intensity = sensor.get_reading()
            sensor.turn_off()
            break

    if current_light_intensity is not None:
        for actuator in get_room_actuators(home, room.name):
            if isinstance(actuator, Light):
                if current_light_intensity < target_light_intensity:
                    actuator.set_brightness_level("high")
                elif current_light_intensity > target_light_intensity:
                    actuator.set_brightness_level("low")
                else:
                    actuator.set_brightness_level("medium")

def main():
    global home
    home = home_plan()

    # Set target values based on the functional description
    target_temperature = 23
    target_humidity = 50  # Comfortable for humans
    target_light_intensity = 500  # Soft light

    while True:
        for room in home:
            adjust_temperature(room, target_temperature)
            adjust_humidity(room, target_humidity)
            adjust_light_intensity(room, target_light_intensity)

        time.sleep(60)  # Adjust every minute

if __name__ == "__main__":
    main()