# Based on the provided functional description, here is the `function.py` file that will be located in the 'functions' folder. This file will contain the main function to adjust the appropriate brightness of the light, indoor temperature, curtain switch, and room humidifier.

# function.py
import time
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor, HumiditySensor
from home.actuator import Light, Heater, AC, Curtain, Humidifier
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW

def adjust_light_brightness(home):
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading is not None:
            for light in lights:
                if light.room_name == sensor.room_name:
                    light.turn_on()
                    if reading < LIGHT_INTENSITY_LOW:
                        light.set_brightness_level("high")
                    elif LIGHT_INTENSITY_LOW <= reading <= LIGHT_INTENSITY_HIGH:
                        light.set_brightness_level("medium")
                    else:
                        light.set_brightness_level("low")
        sensor.turn_off()

def adjust_temperature(home):
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    for sensor in temp_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading is not None:
            for heater in heaters:
                if heater.room_name == sensor.room_name:
                    heater.set_target_temperature(TEMP_LOW)
                    heater.adjust_temperature(reading)
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(reading)
        sensor.turn_off()

def adjust_curtain_switch(home):
    light_sensors = get_all_sensors(home, "LightIntensive")
    curtains = get_all_actuators(home, "Curtain")

    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading is not None:
            for curtain in curtains:
                if curtain.room_name == sensor.room_name:
                    if reading < LIGHT_INTENSITY_LOW:
                        curtain.turn_on()  # Open curtain
                    else:
                        curtain.turn_off()  # Close curtain
        sensor.turn_off()

def adjust_room_humidity(home):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading is not None:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    if reading < HUMIDITY_LOW:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                    elif reading > HUMIDITY_HIGH:
                        humidifier.turn_off()
                        humidifier.decrease_humidity()
        sensor.turn_off()

def main():
    home = home_plan()
    adjust_light_brightness(home)
    adjust_temperature(home)
    adjust_curtain_switch(home)
    adjust_room_humidity(home)

if __name__ == "__main__":
    main()