# Given the functional description and the provided source code files, I'll create the `function.py` file that will contain the main function to control the smart home system based on the temperature, humidity, and light intensity.
# 
# Here is the `function.py` file content:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Window, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def monitor_temperature(home):
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    ac_units = get_all_actuators(home, "AC")
    windows = get_all_actuators(home, "Window")

    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temp_reading = sensor.get_reading()
        if temp_reading and temp_reading > TEMP_HIGH:
            for ac in ac_units:
                ac.set_target_temperature(TEMP_HIGH)
                ac.adjust_temperature(temp_reading)
            for window in windows:
                window.turn_off()

def monitor_humidity(home):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity_reading = sensor.get_reading()
        if humidity_reading and humidity_reading < HUMIDITY_LOW:
            for humidifier in humidifiers:
                humidifier.turn_on()
                humidifier.increase_humidity()

def monitor_light_intensity(home):
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        light_reading = sensor.get_reading()
        if light_reading:
            for light in lights:
                light.turn_on()
                if light_reading < LIGHT_INTENSITY_LOW:
                    light.set_brightness_level("high")
                elif light_reading < LIGHT_INTENSITY_HIGH:
                    light.set_brightness_level("medium")
                else:
                    light.set_brightness_level("low")

def main():
    home = home_plan()
    monitor_temperature(home)
    monitor_humidity(home)
    monitor_light_intensity(home)

if __name__ == "__main__":
    main()