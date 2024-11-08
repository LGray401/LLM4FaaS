# Given your requirement and the provided source code, I'll create a `function.py` file which includes the main function to achieve the desired functionalities: maintaining the temperature at 26°C, maintaining humidity at 60%, and adjusting the light intensity based on the activity (working, relaxing, resting).
# 
# Here's the `function.py`:

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators

def main():
    # Initialize home plan
    home = home_plan()

    # Set target parameters
    TARGET_TEMPERATURE = 26  # Celsius
    TARGET_HUMIDITY = 60  # Percentage
    WORKING_LIGHT_LEVEL = 'high'
    RELAXING_LIGHT_LEVEL = 'medium'
    RESTING_LIGHT_LEVEL = 'off'

    # Get all sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Turn on all sensors and actuators
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()

    for actuator in heaters + ac_units + humidifiers + lights:
        actuator.turn_on()

    while True:
        # Monitor and control temperature
        for sensor in temperature_sensors:
            current_temp = sensor.get_reading()
            if current_temp is not None:
                for heater in heaters:
                    heater.set_target_temperature(TARGET_TEMPERATURE)
                    heater.adjust_temperature(current_temp)
                for ac in ac_units:
                    ac.set_target_temperature(TARGET_TEMPERATURE)
                    ac.adjust_temperature(current_temp)

        # Monitor and control humidity
        for sensor in humidity_sensors:
            current_humidity = sensor.get_reading()
            if current_humidity is not None and current_humidity < TARGET_HUMIDITY:
                for humidifier in humidifiers:
                    humidifier.increase_humidity()
            elif current_humidity is not None and current_humidity > TARGET_HUMIDITY:
                for humidifier in humidifiers:
                    humidifier.decrease_humidity()

        # Monitor and control light intensity
        activity = input("Enter activity (working, relaxing, resting): ").strip().lower()
        if activity == 'working':
            for light in lights:
                light.set_brightness_level(WORKING_LIGHT_LEVEL)
        elif activity == 'relaxing':
            for light in lights:
                light.set_brightness_level(RELAXING_LIGHT_LEVEL)
        elif activity == 'resting':
            for light in lights:
                light.turn_off()

        # Wait before next cycle
        time.sleep(5)

if __name__ == "__main__":
    main()