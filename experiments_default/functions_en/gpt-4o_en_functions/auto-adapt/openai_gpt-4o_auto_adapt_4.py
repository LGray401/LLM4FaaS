# Based on the provided functional description and source code, I'll create a `function.py` file that includes a main function to set up and control the smart home environment. This function will utilize the components from the other provided files to simulate a smart home setup.
# 
# Here's the `function.py` file:

import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create the home plan
    home = home_plan()

    # Get all relevant sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all relevant actuators
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Turn on all sensors and actuators
    for sensor in indoor_temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()

    for actuator in heaters + acs + humidifiers + lights:
        actuator.turn_on()

    # Simulate sensor readings and adjust actuators
    for _ in range(5):  # Simulate 5 cycles of readings
        for sensor in indoor_temp_sensors:
            current_temp = sensor.get_reading()
            if current_temp is not None:
                for heater in heaters:
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(current_temp)
                for ac in acs:
                    ac.set_target_temperature(TEMP_LOW)
                    ac.adjust_temperature(current_temp)

        for sensor in humidity_sensors:
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                for humidifier in humidifiers:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif current_humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

        for sensor in light_sensors:
            current_light = sensor.get_reading()
            if current_light is not None:
                for light in lights:
                    if current_light < LIGHT_INTENSITY_LOW:
                        light.set_brightness_level("high")
                    elif current_light > LIGHT_INTENSITY_HIGH:
                        light.set_brightness_level("low")
                    else:
                        light.set_brightness_level("medium")

        time.sleep(2)  # Wait for 2 seconds before the next cycle

    # Turn off all sensors and actuators
    for sensor in indoor_temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_off()

    for actuator in heaters + acs + humidifiers + lights:
        actuator.turn_off()

if __name__ == "__main__":
    main()