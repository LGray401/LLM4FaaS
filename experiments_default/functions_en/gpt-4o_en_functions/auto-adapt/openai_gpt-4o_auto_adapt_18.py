# Based on the provided functional description and source code, here's the `function.py` file. This file will be located in the `functions` folder and will include a `main` function. The `main` function will read the values for temperature, humidity, and light intensity and perform the necessary actions.

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators

def main():
    # Functional Description values
    target_temperature = 28  # degrees
    target_humidity = 26  # percentage
    target_light_intensity = 26  # lux

    # Create home plan
    home = home_plan()

    # Get all sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")

    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Function to adjust temperature
    def adjust_temperature(current_temp):
        for heater in heaters:
            heater.set_target_temperature(target_temperature)
            heater.adjust_temperature(current_temp)
        for ac_unit in ac_units:
            ac_unit.set_target_temperature(target_temperature)
            ac_unit.adjust_temperature(current_temp)
    
    # Function to adjust humidity
    def adjust_humidity(current_humidity):
        for humidifier in humidifiers:
            if current_humidity < target_humidity:
                humidifier.increase_humidity()
            elif current_humidity > target_humidity:
                humidifier.decrease_humidity()

    # Function to adjust light intensity
    def adjust_light_intensity(current_light_intensity):
        for light in lights:
            if current_light_intensity < target_light_intensity:
                light.set_brightness_level("high")
            elif current_light_intensity > target_light_intensity:
                light.set_brightness_level("low")

    # Read sensor values and adjust actuators accordingly
    for sensor in temperature_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        adjust_temperature(current_temp)
        sensor.turn_off()

    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        adjust_humidity(current_humidity)
        sensor.turn_off()

    for sensor in light_intensity_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        adjust_light_intensity(current_light_intensity)
        sensor.turn_off()

if __name__ == "__main__":
    main()