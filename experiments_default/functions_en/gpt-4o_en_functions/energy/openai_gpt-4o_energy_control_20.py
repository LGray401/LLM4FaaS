# Let's create the `function.py` file based on the provided functional description and the code in your other files. This file will be responsible for automatically adjusting the indoor temperature, humidity, and light intensity based on sensor readings and using actuators to maintain desired environmental conditions.
# 
# Here's how `function.py` could look:
# 
# ### `function.py`

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW

def adjust_environment(room_name, home):
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)
    
    # Define the actuators
    heater = None
    ac = None
    humidifier = None
    light = None

    # Identify actuators
    for actuator in actuators:
        if isinstance(actuator, Heater):
            heater = actuator
        elif isinstance(actuator, AC):
            ac = actuator
        elif isinstance(actuator, Humidifier):
            humidifier = actuator
        elif isinstance(actuator, Light):
            light = actuator

    # Adjust temperature
    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            sensor.turn_on()
            current_temp = sensor.get_reading()
            if current_temp is not None:
                if heater:
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(current_temp)
                if ac:
                    ac.set_target_temperature(TEMP_LOW)
                    ac.adjust_temperature(current_temp)
            sensor.turn_off()

    # Adjust humidity
    for sensor in sensors:
        if isinstance(sensor, HumiditySensor):
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                if humidifier:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.turn_on()
                    elif current_humidity > HUMIDITY_HIGH:
                        humidifier.turn_off()
            sensor.turn_off()

    # Adjust light intensity
    for sensor in sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            current_light = sensor.get_reading()
            if current_light is not None:
                if light:
                    if current_light < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    elif current_light > LIGHT_INTENSITY_HIGH:
                        light.turn_off()
            sensor.turn_off()
    
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)

def main():
    home = home_plan()
    while True:
        for room in home:
            adjust_environment(room.name, home)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()