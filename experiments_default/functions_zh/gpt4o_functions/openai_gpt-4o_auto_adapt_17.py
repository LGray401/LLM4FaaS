# Based on the functional description and the provided source code, I'll create a `function.py` file that will reside in the 'functions' folder. This file will contain the main function to control the smart home system based on the given temperature, humidity, and light intensity values.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    # Initialize home plan
    home = home_plan()

    # Desired values from functional description
    desired_temperature = 26
    desired_humidity = 40
    desired_light_intensity = 80

    # Adjust indoor temperature
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        for heater in heaters:
            heater.set_target_temperature(desired_temperature)
            heater.adjust_temperature(current_temp)
        for ac in acs:
            ac.set_target_temperature(desired_temperature)
            ac.adjust_temperature(current_temp)
        sensor.turn_off()

    # Adjust humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        for humidifier in humidifiers:
            if current_humidity < HUMIDITY_LOW:
                humidifier.turn_on()
                humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                humidifier.turn_on()
                humidifier.decrease_humidity()
            else:
                humidifier.turn_off()
        sensor.turn_off()

    # Adjust light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        current_light = sensor.get_reading()
        for light in lights:
            if current_light < LIGHT_INTENSITY_LOW:
                light.turn_on()
                light.set_brightness_level("high")
            elif current_light > LIGHT_INTENSITY_HIGH:
                light.turn_on()
                light.set_brightness_level("low")
            else:
                light.turn_on()
                light.set_brightness_level("medium")
        sensor.turn_off()

if __name__ == "__main__":
    main()