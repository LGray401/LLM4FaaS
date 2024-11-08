# To create a `function.py` file that focuses on energy-saving functionality for your smart home project, we need to utilize the various sensors and actuators to control the environment within specified thresholds, as defined in `config.py`. Below is the implementation of `function.py` that will monitor sensor values and activate/deactivate actuators accordingly to save energy.
# 
# ### function.py

import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger

def save_energy(home):
    # Get all sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")

    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")
    lights = get_all_actuators(home, "Light")
    windows = get_all_actuators(home, "Window")

    # Iterate over sensors and adjust actuators accordingly
    for sensor in indoor_temp_sensors:
        if sensor.status == "on":
            reading = sensor.get_reading()
            adjust_heating_cooling(reading, sensor.room_name, heaters, ac_units, windows)

    for sensor in humidity_sensors:
        if sensor.status == "on":
            reading = sensor.get_reading()
            adjust_humidity(reading, sensor.room_name, windows)

    for sensor in light_intensity_sensors:
        if sensor.status == "on":
            reading = sensor.get_reading()
            adjust_lighting(reading, sensor.room_name, lights, windows)

def adjust_heating_cooling(current_temp, room_name, heaters, ac_units, windows):
    if current_temp is not None:
        if current_temp < TEMP_LOW:
            for heater in heaters:
                if heater.room_name == room_name:
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.turn_on()
        elif current_temp > TEMP_HIGH:
            for ac in ac_units:
                if ac.room_name == room_name:
                    ac.set_target_temperature(TEMP_LOW)
                    ac.turn_on()
        else:
            for heater in heaters:
                if heater.room_name == room_name:
                    heater.turn_off()
            for ac in ac_units:
                if ac.room_name == room_name:
                    ac.turn_off()

def adjust_humidity(current_humidity, room_name, windows):
    if current_humidity is not None:
        if current_humidity < HUMIDITY_LOW:
            # Close windows to increase humidity
            for window in windows:
                if window.room_name == room_name:
                    window.turn_off()
        elif current_humidity > HUMIDITY_HIGH:
            # Open windows to decrease humidity
            for window in windows:
                if window.room_name == room_name:
                    window.turn_on()

def adjust_lighting(current_light_intensity, room_name, lights, windows):
    if current_light_intensity is not None:
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            # Turn on lights
            for light in lights:
                if light.room_name == room_name:
                    light.turn_on()
                    light.set_brightness_level("high")
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            # Turn off lights
            for light in lights:
                if light.room_name == room_name:
                    light.turn_off()
            # Open windows if light is too low
            for window in windows:
                if window.room_name == room_name:
                    window.turn_on()
        else:
            # Adjust light brightness to medium
            for light in lights:
                if light.room_name == room_name:
                    light.set_brightness_level("medium")

def main():
    home = home_plan()
    while True:
        save_energy(home)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()