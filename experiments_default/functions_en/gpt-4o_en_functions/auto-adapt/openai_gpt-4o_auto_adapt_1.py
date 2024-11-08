# Based on the provided functional description and source code files, here is the `function.py` file that should be placed in the `functions` folder. This file contains the main function to adjust the temperature, humidity, and light intensity according to your specifications.

import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW

def adjust_temperature(target_temperature):
    sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")

    for sensor in sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        for ac in acs:
            if ac.room_name == sensor.room_name:
                ac.set_target_temperature(target_temperature)
                ac.adjust_temperature(current_temp)
        for heater in heaters:
            if heater.room_name == sensor.room_name:
                heater.set_target_temperature(target_temperature)
                heater.adjust_temperature(current_temp)
        sensor.turn_off()

def adjust_humidity(target_humidity):
    sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        for humidifier in humidifiers:
            if humidifier.room_name == sensor.room_name:
                if current_humidity < target_humidity:
                    humidifier.turn_on()
                    humidifier.increase_humidity()
                else:
                    humidifier.turn_off()
                    humidifier.decrease_humidity()
        sensor.turn_off()

def adjust_light_intensity():
    sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in sensors:
        sensor.turn_on()
        current_light = sensor.get_reading()
        for light in lights:
            if light.room_name == sensor.room_name:
                light.turn_on()
                if current_light < 300:
                    light.set_brightness_level("high")
                elif 300 <= current_light < 600:
                    light.set_brightness_level("medium")
                else:
                    light.set_brightness_level("low")
        sensor.turn_off()

def main():
    global home
    home = home_plan()

    print("Adjusting Temperature to 26°C")
    adjust_temperature(26)
    
    print("Adjusting Humidity to 40%")
    adjust_humidity(40)
    
    print("Adjusting Light Intensity to Moderate")
    adjust_light_intensity()

if __name__ == "__main__":
    main()