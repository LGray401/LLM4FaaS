# Here's the `function.py` file based on your functional description and provided source code. This file will contain a main function that maintains the desired temperature, humidity, and light intensity levels in the smart home.

# function.py
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Curtain, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH

def control_temperature(home):
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")

    for sensor in temperature_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp is not None:
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temp)
            for heater in heaters:
                if heater.room_name == sensor.room_name:
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(current_temp)
        sensor.turn_off()

def control_humidity(home):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    if current_humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()
                    else:
                        humidifier.increase_humidity()
        sensor.turn_off()

def control_light(home):
    light_sensors = get_all_sensors(home, "LightIntensive")
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        current_light = sensor.get_reading()
        if current_light is not None:
            for curtain in curtains:
                if curtain.room_name == sensor.room_name:
                    if current_light > LIGHT_INTENSITY_HIGH:
                        curtain.turn_on()
                    else:
                        curtain.turn_off()
            for light in lights:
                if light.room_name == sensor.room_name:
                    if current_light < LIGHT_INTENSITY_HIGH:
                        light.turn_on()
                    else:
                        light.turn_off()
        sensor.turn_off()

def main():
    home = home_plan()
    while True:
        control_temperature(home)
        control_humidity(home)
        control_light(home)
        time.sleep(60)  # Adjust the sleep time as needed

if __name__ == "__main__":
    main()