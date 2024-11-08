# Sure, I can help you create the `function.py` file based on your functional description and the provided source code. This file will include the main function that integrates the functionalities described for temperature, humidity, and light intensity regulation.
# 
# Here's the `function.py` file:

import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize home plan
    home = home_plan()

    # Get all relevant sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    while True:
        # Temperature Control
        for sensor in indoor_temp_sensors:
            sensor.turn_on()
            current_temp = sensor.get_reading()
            if current_temp is not None and current_temp > TEMP_HIGH:
                for ac in acs:
                    if ac.room_name == sensor.room_name:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(current_temp)

        # Humidity Control
        for sensor in humidity_sensors:
            sensor.turn_on()
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

        # Light Intensity Control
        for sensor in light_sensors:
            sensor.turn_on()
            current_light_intensity = sensor.get_reading()
            if current_light_intensity is not None:
                for light in lights:
                    if light.room_name == sensor.room_name:
                        if current_light_intensity < LIGHT_INTENSITY_LOW:
                            light.turn_on()
                            light.set_brightness_level("high")
                        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                            light.turn_off()
                        else:
                            light.set_brightness_level("medium")

        # Pause before next iteration
        time.sleep(5)

if __name__ == "__main__":
    main()