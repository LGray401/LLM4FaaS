# Based on the provided functional description and the source code files, I will create a `function.py` file that will maintain the indoor temperature at 26°C, the humidity at 60%, and adjust the light intensity according to your activities (work, relax, rest).
# 
# Here's the `function.py` file:
# 
# ### functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION

def maintain_temperature(home):
    target_temperature = 26  # Target temperature in Celsius
    sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    for sensor in sensors:
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
        sensor.turn_off()

def maintain_humidity(home):
    target_humidity = 60  # Target humidity in percentage
    sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    if current_humidity < target_humidity:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                    elif current_humidity > target_humidity:
                        humidifier.turn_on()
                        humidifier.decrease_humidity()
                    else:
                        humidifier.turn_off()
        sensor.turn_off()

def adjust_lighting(home, activity):
    lights = get_all_actuators(home, "Light")
    brightness_levels = {
        "work": "high",
        "relax": "medium",
        "rest": "low"
    }

    if activity not in brightness_levels:
        raise ValueError(f"Unknown activity: {activity}. Valid activities are: {list(brightness_levels.keys())}")

    for light in lights:
        light.turn_on()
        light.set_brightness_level(brightness_levels[activity])
        if activity == "rest":
            light.turn_off()

def main():
    home = home_plan()

    while True:
        print("Maintaining temperature and humidity...")
        maintain_temperature(home)
        maintain_humidity(home)
        
        print("Adjusting lighting for work...")
        adjust_lighting(home, "work")
        time.sleep(DAILY_ROUTINE_DURATION)

        print("Adjusting lighting for relax...")
        adjust_lighting(home, "relax")
        time.sleep(DAILY_ROUTINE_DURATION)

        print("Adjusting lighting for rest...")
        adjust_lighting(home, "rest")
        time.sleep(DAILY_ROUTINE_DURATION)

if __name__ == "__main__":
    main()