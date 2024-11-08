# Based on the functional description and the source code you provided, I'll create a `function.py` file that will be located in the `functions` folder. This file will contain a main function that will adjust the temperature, humidity, and light intensity as specified.
# 
# Let's proceed with the creation of `function.py`:
# 
# ### functions/function.py

import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Adjust Temperature
    target_temperature = 26.0  # Celsius
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
        sensor.turn_off()
    
    # Sleep to simulate time for temperature change
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    # Adjust Humidity
    target_humidity = 40  # Percentage
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
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
        sensor.turn_off()

    # Adjust Light Intensity
    target_light_level = "medium"
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        current_light = sensor.get_reading()
        if current_light is not None:
            for light in lights:
                if light.room_name == sensor.room_name:
                    light.turn_on()
                    light.set_brightness_level(target_light_level)
        sensor.turn_off()

    print("Home environment adjusted according to the functional description.")

if __name__ == "__main__":
    main()