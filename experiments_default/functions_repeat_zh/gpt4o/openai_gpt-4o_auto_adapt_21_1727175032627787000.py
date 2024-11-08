# Based on the functional description and the provided source code for your smart home project, here's the `function.py` file located in the `functions` folder. This file will contain the main function to manage the home automation system as per the requirements:
# 
# - Automatically turn on the air conditioner when the temperature is above 26°C.
# - Maintain normal humidity levels.
# - Automatically close the curtains when the light intensity is high (e.g., during noon).
# 
# Here's the implementation:

# function.py
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Curtain, Humidifier
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH


def main():
    # Initialize home plan
    home = home_plan()

    # Get all relevant sensors and actuators
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    ac_units = get_all_actuators(home, "AC")
    curtains = get_all_actuators(home, "Curtain")
    humidifiers = get_all_actuators(home, "Humidifier")

    while True:
        # Temperature control
        for sensor in temp_sensors:
            sensor.turn_on()
            current_temp = sensor.get_reading()
            if current_temp and current_temp > TEMP_HIGH:
                for ac in ac_units:
                    if ac.room_name == sensor.room_name:
                        ac.set_target_temperature(TEMP_HIGH - 1)  # Set target slightly below threshold
                        ac.adjust_temperature(current_temp)

        # Humidity control (assuming normal levels are maintained)
        for sensor in humidity_sensors:
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            if current_humidity:
                for humidifier in humidifiers:
                    if humidifier.room_name == sensor.room_name:
                        if current_humidity < 30:
                            humidifier.increase_humidity()
                        elif current_humidity > 50:
                            humidifier.decrease_humidity()

        # Light intensity control
        for sensor in light_sensors:
            sensor.turn_on()
            current_light_intensity = sensor.get_reading()
            if current_light_intensity and current_light_intensity > LIGHT_INTENSITY_HIGH:
                for curtain in curtains:
                    if curtain.room_name == sensor.room_name:
                        curtain.turn_on()

        # Wait before next reading
        time.sleep(5)


if __name__ == "__main__":
    main()