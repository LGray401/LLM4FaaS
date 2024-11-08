# Sure, based on the functional description for energy saving and the provided source code, here is a `function.py` file that will be located in the 'functions' folder. This file will contain a main function that will manage energy-saving functionalities by monitoring sensors and actuating devices accordingly.
# 
# ### function.py

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, Window, Curtain
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW

def energy_saving_mode(home):
    # Get all relevant sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    lights = get_all_actuators(home, "Light")
    windows = get_all_actuators(home, "Window")
    curtains = get_all_actuators(home, "Curtain")

    # Turn off unnecessary lights
    for light in lights:
        light.turn_off()

    # Adjust indoor temperature
    for sensor in indoor_temp_sensors:
        current_temp = sensor.get_reading()
        if current_temp is not None:
            for heater in heaters:
                if heater.room_name == sensor.room_name:
                    if current_temp < TEMP_LOW:
                        heater.set_target_temperature(TEMP_HIGH)
                        heater.adjust_temperature(current_temp)
                    if current_temp > TEMP_HIGH:
                        heater.turn_off()

            for ac in acs:
                if ac.room_name == sensor.room_name:
                    if current_temp > TEMP_HIGH:
                        ac.set_target_temperature(TEMP_LOW)
                        ac.adjust_temperature(current_temp)
                    if current_temp < TEMP_LOW:
                        ac.turn_off()

    # Adjust humidity
    for sensor in humidity_sensors:
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            if current_humidity < HUMIDITY_LOW:
                for window in windows:
                    if window.room_name == sensor.room_name:
                        window.turn_on()
            elif current_humidity > HUMIDITY_HIGH:
                for window in windows:
                    if window.room_name == sensor.room_name:
                        window.turn_off()

    # Adjust curtain based on light intensity
    for sensor in light_sensors:
        current_light = sensor.get_reading()
        if current_light is not None:
            for curtain in curtains:
                if curtain.room_name == sensor.room_name:
                    if current_light < LIGHT_INTENSITY_LOW:
                        curtain.turn_on()
                    elif current_light > LIGHT_INTENSITY_HIGH:
                        curtain.turn_off()

    # Adjust temperature based on outdoor temperature
    for sensor in outdoor_temp_sensors:
        outdoor_temp = sensor.get_reading()
        if outdoor_temp is not None:
            if outdoor_temp < TEMP_LOW:
                for window in windows:
                    if window.room_name == sensor.room_name:
                        window.turn_off()
            elif outdoor_temp > TEMP_HIGH:
                for window in windows:
                    if window.room_name == sensor.room_name:
                        window.turn_on()

def main():
    home = home_plan()
    while True:
        energy_saving_mode(home)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()