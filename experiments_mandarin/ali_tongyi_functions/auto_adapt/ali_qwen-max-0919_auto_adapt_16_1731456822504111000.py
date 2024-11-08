# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to control your smart home system. The main function will read the sensor values, compare them against predefined thresholds (from `config.py`), and then control the actuators accordingly.
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    while True:
        # Get all sensors and actuators
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        humidity_sensors = get_all_sensors(home, "Humidity")
        light_sensors = get_all_sensors(home, "LightIntensive")

        heaters = get_all_actuators(home, "Heater")
        acs = get_all_actuators(home, "AC")
        humidifiers = get_all_actuators(home, "Humidifier")
        lights = get_all_actuators(home, "Light")

        # Process temperature
        for sensor in temperature_sensors:
            if sensor.status == "on":
                current_temperature = sensor.get_reading()
                if current_temperature is not None:
                    for heater in heaters:
                        if heater.room_name == sensor.room_name:
                            heater.adjust_temperature(current_temperature)
                    for ac in acs:
                        if ac.room_name == sensor.room_name:
                            ac.adjust_temperature(current_temperature)

        # Process humidity
        for sensor in humidity_sensors:
            if sensor.status == "on":
                current_humidity = sensor.get_reading()
                if current_humidity is not None:
                    for humidifier in humidifiers:
                        if humidifier.room_name == sensor.room_name:
                            if current_humidity < HUMIDITY_LOW:
                                humidifier.turn_on()
                                humidifier.increase_humidity()
                            elif current_humidity > HUMIDITY_HIGH:
                                humidifier.turn_on()
                                humidifier.decrease_humidity()
                            else:
                                humidifier.turn_off()

        # Process light intensity
        for sensor in light_sensors:
            if sensor.status == "on":
                current_light_intensity = sensor.get_reading()
                if current_light_intensity is not None:
                    for light in lights:
                        if light.room_name == sensor.room_name:
                            if current_light_intensity < LIGHT_INTENSITY_LOW:
                                light.turn_on()
                                light.set_brightness_level("high")
                            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                                light.turn_on()
                                light.set_brightness_level("low")
                            else:
                                light.turn_off()

        # Wait for a short period before the next iteration
        time.sleep(10)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()