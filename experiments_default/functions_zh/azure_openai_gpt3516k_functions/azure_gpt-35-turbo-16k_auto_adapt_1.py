# Sure, here is the 'function.py' file based on your functional description and the given source code:

import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators, print_home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW


def main():
    # Retrieve home plan
    home = home_plan()

    # Print home plan
    # print_home_plan(home)

    # Get all sensors
    all_sensors = get_all_sensors(home, "IndoorTemperature") + get_all_sensors(home, "Humidity") + get_all_sensors(
        home, "LightIntensive")

    # Get all actuators
    all_actuators = get_all_actuators(home, "AC") + get_all_actuators(home, "Heater") + get_all_actuators(home, "Light")

    # Perform temperature, humidity, and light intensity adjustment based on functional description
    for sensor in all_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            # Adjust temperature
            current_temperature = sensor.get_reading()
            if current_temperature < TEMP_LOW:
                for actuator in all_actuators:
                    if isinstance(actuator, Heater):
                        actuator.set_target_temperature(TEMP_HIGH)
                        actuator.turn_on()
                        actuator.adjust_temperature(current_temperature)
            elif current_temperature > TEMP_HIGH:
                for actuator in all_actuators:
                    if isinstance(actuator, AC):
                        actuator.set_target_temperature(TEMP_LOW)
                        actuator.turn_on()
                        actuator.adjust_temperature(current_temperature)
        elif isinstance(sensor, HumiditySensor):
            # Adjust humidity
            current_humidity = sensor.get_reading()
            if current_humidity < HUMIDITY_LOW:
                for actuator in all_actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.turn_on()
                        actuator.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                for actuator in all_actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.turn_on()
                        actuator.decrease_humidity()
        elif isinstance(sensor, LightIntensiveSensor):
            # Adjust light intensity
            current_light_intensity = sensor.get_reading()
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                for actuator in all_actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_on()
                        actuator.set_brightness_level("medium")
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                for actuator in all_actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_on()
                        actuator.set_brightness_level("low")

    # Wait for a while to observe the changes
    time.sleep(5)

    # Print updated home plan
    # print_home_plan(home)


if __name__ == "__main__":
    main()