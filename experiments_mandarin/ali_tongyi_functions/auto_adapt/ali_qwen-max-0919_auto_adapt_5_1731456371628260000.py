# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control and monitor the smart home. The main function will:
# 
# 1. Initialize the home plan.
# 2. Print the home plan.
# 3. Monitor and adjust the temperature, humidity, and light intensity based on the given thresholds.
# 4. Provide some basic interactions with the actuators.
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def initialize_home():
    home = home_plan()
    print_home_plan(home)
    return home

def print_home_plan(home):
    for room in home:
        room.print_info()

def monitor_and_adjust(home):
    while True:
        # Monitor and adjust temperature
        for sensor in get_all_sensors(home, "IndoorTemperature"):
            current_temp = sensor.get_reading()
            if current_temp is not None:
                if current_temp < TEMP_LOW:
                    for heater in get_all_actuators(home, "Heater"):
                        if heater.room_name == sensor.room_name:
                            heater.set_target_temperature(TEMP_HIGH)
                            heater.adjust_temperature(current_temp)
                elif current_temp > TEMP_HIGH:
                    for ac in get_all_actuators(home, "AC"):
                        if ac.room_name == sensor.room_name:
                            ac.set_target_temperature(TEMP_LOW)
                            ac.adjust_temperature(current_temp)

        # Monitor and adjust humidity
        for sensor in get_all_sensors(home, "Humidity"):
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    for humidifier in get_all_actuators(home, "Humidifier"):
                        if humidifier.room_name == sensor.room_name:
                            humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    for humidifier in get_all_actuators(home, "Humidifier"):
                        if humidifier.room_name == sensor.room_name:
                            humidifier.decrease_humidity()

        # Monitor and adjust light intensity
        for sensor in get_all_sensors(home, "LightIntensive"):
            current_light_intensity = sensor.get_reading()
            if current_light_intensity is not None:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    for light in get_all_actuators(home, "Light"):
                        if light.room_name == sensor.room_name:
                            light.turn_on()
                            light.set_brightness_level("high")
                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                    for light in get_all_actuators(home, "Light"):
                        if light.room_name == sensor.room_name:
                            light.turn_off()

        # Sleep for a while before the next check
        time.sleep(DAILY_ROUTINE_DURATION)

def main():
    home = initialize_home()
    try:
        monitor_and_adjust(home)
    except KeyboardInterrupt:
        print("Smart Home system is shutting down.")
        for actuator in get_all_actuators(home, "Heater"):
            actuator.turn_off()
        for actuator in get_all_actuators(home, "AC"):
            actuator.turn_off()
        for actuator in get_all_actuators(home, "Humidifier"):
            actuator.turn_off()
        for actuator in get_all_actuators(home, "Light"):
            actuator.turn_off()
        print("All actuators are turned off.")

if __name__ == "__main__":
    main()