# Based on the provided code and functional description, I will create the `function.py` file which will reside in the 'functions' folder. This file will contain the main function to control temperature, humidity, and light intensity according to the given requirements.
# 
# Here is the `function.py` file:

# function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW
import time

def maintain_temperature(home, target_temperature=26):
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp is not None:
            for heater in heaters:
                if heater.room_name == sensor.room_name:
                    heater.set_target_temperature(target_temperature)
                    heater.adjust_temperature(current_temp)
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(target_temperature)
                    ac.adjust_temperature(current_temp)


def maintain_humidity(home, target_humidity=60):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    if current_humidity < target_humidity:
                        humidifier.increase_humidity()
                    else:
                        humidifier.decrease_humidity()


def adjust_lighting(home, activity):
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    brightness_settings = {
        "work": "high",
        "relax": "medium",
        "rest": "off"
    }

    for light in lights:
        if activity in brightness_settings:
            if brightness_settings[activity] == "off":
                light.turn_off()
            else:
                light.turn_on()
                light.set_brightness_level(brightness_settings[activity])


def main():
    home = home_plan()

    while True:
        maintain_temperature(home)
        maintain_humidity(home)
        adjust_lighting(home, "work")  # Change this value to "relax" or "rest" based on your current activity

        time.sleep(60)  # Wait for 1 minute before the next check


if __name__ == "__main__":
    main()