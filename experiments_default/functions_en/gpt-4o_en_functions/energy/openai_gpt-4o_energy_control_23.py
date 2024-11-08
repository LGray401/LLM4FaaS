# Based on the provided functional description and the source code, here is the `function.py` file that will fulfill the requirements:

# functions/function.py

import datetime
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, LIGHT_INTENSITY_HIGH, HUMIDITY_LOW

def main():
    home = home_plan()

    # Check light intensity and turn off lights if necessary
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    for sensor in light_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        if light_intensity is not None and light_intensity > LIGHT_INTENSITY_HIGH:
            for light in lights:
                light.turn_off()

    # Check indoor temperature and turn on heater if necessary
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    for sensor in temp_sensors:
        sensor.turn_on()
        indoor_temp = sensor.get_reading()
        if indoor_temp is not None and indoor_temp < TEMP_LOW:
            for heater in heaters:
                heater.turn_on()

    # Check if it's a weekday and let the cleaning robot work
    today = datetime.datetime.now().strftime('%A')
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    if today in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        for robot in cleaning_robots:
            robot.turn_on()
            robot.daily_routine()

    # Check humidity and turn on humidifier if necessary when you come back from work
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    # Assume you come back from work at 6 PM
    current_time = datetime.datetime.now().time()
    if current_time > datetime.time(18, 0):
        for sensor in humidity_sensors:
            sensor.turn_on()
            humidity = sensor.get_reading()
            if humidity is not None and humidity < HUMIDITY_LOW:
                for humidifier in humidifiers:
                    humidifier.turn_on()
                    humidifier.increase_humidity()

if __name__ == "__main__":
    main()