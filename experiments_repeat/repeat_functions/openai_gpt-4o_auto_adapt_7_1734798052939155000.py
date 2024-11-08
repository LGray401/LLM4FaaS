# Based on the functional description and the provided source code files, I will create a `function.py` file that implements the main function for your smart home project. This function will utilize the sensors and actuators to adjust the home environment according to the specified conditions:
# 
# - Temperature: "屋里太热了" (It's too hot inside)
# - Humidity: "屋里有点干" (It's a bit dry inside)
# - Light Intensity: "屋里太暗了" (It's too dark inside)
# 
# Here's the implementation for `function.py`:
# 
# ```python
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Light

def adjust_home_environment(home):
    # Adjust temperature
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    ac_units = get_all_actuators(home, "AC")
    for sensor in temperature_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        for ac in ac_units:
            ac.set_target_temperature(TEMP_HIGH)
            ac.adjust_temperature(current_temp)

    # Adjust humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity < HUMIDITY_LOW:
            for humidifier in humidifiers:
                humidifier.turn_on()
                humidifier.increase_humidity()

    # Adjust light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity < LIGHT_INTENSITY_HIGH:
            for light in lights:
                light.turn_on()
                light.set_brightness_level("high")

def main():
    home = home_plan()
    adjust_home_environment(home)

if __name__ == "__main__":
    main()
# ```
# 
# This script does the following:
# 
# 1. **Temperature Adjustment**: It retrieves all indoor temperature sensors and AC units, turns on the sensors, gets the current temperature, and adjusts the AC units to ensure the temperature is kept below the `TEMP_HIGH` threshold.
# 
# 2. **Humidity Adjustment**: It retrieves all humidity sensors and humidifiers, turns on the sensors, checks the current humidity, and turns on humidifiers if the humidity is below the `HUMIDITY_LOW` threshold.
# 
# 3. **Light Intensity Adjustment**: It retrieves all light intensity sensors and light actuators, turns on the sensors, checks the current light intensity, and turns on the lights with high brightness if the light intensity is below the `LIGHT_INTENSITY_HIGH` threshold.
# 
# Please make sure this file is saved as `function.py` in the 'functions' folder of your project. This script assumes the logger setup is already correctly configured in `home.logger_config`.