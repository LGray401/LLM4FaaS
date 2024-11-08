# To create the `function.py` file in the `functions` folder, we'll write a main function that will handle the following tasks as described in the functional description:
# 
# 1. Adjusting the light to a suitable brightness.
# 2. Regulating indoor temperature.
# 3. Controlling the curtain switch.
# 4. Adjusting the humidifier to control room humidity.
# 
# Here's the `function.py` file you requested:

import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def adjust_light(home):
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading:
            if reading < LIGHT_INTENSITY_LOW:
                for light in lights:
                    if light.room_name == sensor.room_name:
                        light.turn_on()
                        light.set_brightness_level("high")
                        break
            elif reading > LIGHT_INTENSITY_HIGH:
                for light in lights:
                    if light.room_name == sensor.room_name:
                        light.turn_off()
                        break
            else:
                for light in lights:
                    if light.room_name == sensor.room_name:
                        light.turn_on()
                        light.set_brightness_level("medium")
                        break

def adjust_temperature(home):
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    for sensor in temp_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading:
            if reading < TEMP_LOW:
                for heater in heaters:
                    if heater.room_name == sensor.room_name:
                        heater.turn_on()
                        heater.set_target_temperature(TEMP_HIGH)
                        break
            elif reading > TEMP_HIGH:
                for ac in acs:
                    if ac.room_name == sensor.room_name:
                        ac.turn_on()
                        ac.set_target_temperature(TEMP_LOW)
                        break
            else:
                for heater in heaters:
                    if heater.room_name == sensor.room_name:
                        heater.turn_off()
                        break
                for ac in acs:
                    if ac.room_name == sensor.room_name:
                        ac.turn_off()
                        break

def adjust_curtains(home):
    curtains = get_all_actuators(home, "Curtain")

    for curtain in curtains:
        curtain.turn_on()

def adjust_humidifier(home):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading:
            if reading < HUMIDITY_LOW:
                for humidifier in humidifiers:
                    if humidifier.room_name == sensor.room_name:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                        break
            elif reading > HUMIDITY_HIGH:
                for humidifier in humidifiers:
                    if humidifier.room_name == sensor.room_name:
                        humidifier.turn_on()
                        humidifier.decrease_humidity()
                        break
            else:
                for humidifier in humidifiers:
                    if humidifier.room_name == sensor.room_name:
                        humidifier.turn_off()
                        break

def main():
    home = home_plan()
    adjust_light(home)
    adjust_temperature(home)
    adjust_curtains(home)
    adjust_humidifier(home)

if __name__ == "__main__":
    main()