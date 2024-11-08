# Based on the provided functional description and source code, I will create a `function.py` file that will manage the smart home environment to maintain the specified conditions for temperature, humidity, and light intensity. This file will be located in the `functions` folder and will contain the main function to control the smart home.
# 
# Here is the `function.py` file:

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Curtain, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def control_temperature(home):
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")

    for sensor in indoor_temp_sensors:
        current_temp = sensor.get_reading()
        if current_temp is not None:
            room_name = sensor.room_name
            for ac in acs:
                if ac.room_name == room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temp)
            for heater in heaters:
                if heater.room_name == room_name:
                    heater.set_target_temperature(TEMP_LOW)
                    heater.adjust_temperature(current_temp)

def control_humidity(home):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            room_name = sensor.room_name
            for humidifier in humidifiers:
                if humidifier.room_name == room_name:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                    elif current_humidity > HUMIDITY_HIGH:
                        humidifier.turn_on()
                        humidifier.decrease_humidity()
                    else:
                        humidifier.turn_off()

def control_light_intensity(home):
    light_sensors = get_all_sensors(home, "LightIntensive")
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        current_light_intensity = sensor.get_reading()
        if current_light_intensity is not None:
            room_name = sensor.room_name
            for curtain in curtains:
                if curtain.room_name == room_name:
                    if current_light_intensity > LIGHT_INTENSITY_HIGH:
                        curtain.turn_on()
                    else:
                        curtain.turn_off()
            for light in lights:
                if light.room_name == room_name:
                    if current_light_intensity < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    else:
                        light.turn_off()

def main():
    home = home_plan()

    while True:
        control_temperature(home)
        control_humidity(home)
        control_light_intensity(home)
        time.sleep(60)  # Run the control loop every 60 seconds

if __name__ == "__main__":
    main()