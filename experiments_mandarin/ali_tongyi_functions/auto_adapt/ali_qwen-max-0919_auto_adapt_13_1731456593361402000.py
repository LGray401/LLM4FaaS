# Based on the provided functional description and source code, I will create a `function.py` file that includes a main function to control the smart home environment according to the given requirements. The main function will:
# 
# 1. Initialize the home plan.
# 2. Check and adjust the temperature, humidity, and light intensity in each room based on the provided thresholds and desired conditions.
# 3. Log the actions and readings.
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators, print_home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def check_and_adjust_temperature(room):
    sensors = get_room_sensors(home, room.name)
    actuators = get_room_actuators(home, room.name)

    for sensor in sensors:
        if isinstance(sensor, (IndoorTemperatureSensor, OutdoorTemperatureSensor)):
            sensor.turn_on()
            current_temp = sensor.get_reading()
            sensor.turn_off()

            if current_temp is not None:
                for actuator in actuators:
                    if isinstance(actuator, Heater):
                        actuator.set_target_temperature(26)
                        actuator.adjust_temperature(current_temp)
                    elif isinstance(actuator, AC):
                        actuator.set_target_temperature(26)
                        actuator.adjust_temperature(current_temp)

def check_and_adjust_humidity(room):
    sensors = get_room_sensors(home, room.name)
    actuators = get_room_actuators(home, room.name)

    for sensor in sensors:
        if isinstance(sensor, HumiditySensor):
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            sensor.turn_off()

            if current_humidity is not None:
                for actuator in actuators:
                    if isinstance(actuator, Humidifier):
                        if current_humidity < HUMIDITY_LOW:
                            actuator.increase_humidity()
                        elif current_humidity > HUMIDITY_HIGH:
                            actuator.decrease_humidity()

def check_and_adjust_light_intensity(room):
    sensors = get_room_sensors(home, room.name)
    actuators = get_room_actuators(home, room.name)

    for sensor in sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            current_light_intensity = sensor.get_reading()
            sensor.turn_off()

            if current_light_intensity is not None:
                for actuator in actuators:
                    if isinstance(actuator, Light):
                        if current_light_intensity < LIGHT_INTENSITY_HIGH:
                            actuator.turn_on()
                            actuator.set_brightness_level("high")
                        else:
                            actuator.turn_off()

def main():
    global home
    home = home_plan()
    print_home_plan(home)

    while True:
        for room in home:
            check_and_adjust_temperature(room)
            check_and_adjust_humidity(room)
            check_and_adjust_light_intensity(room)
        
        # Wait for a while before the next check
        time.sleep(60)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()