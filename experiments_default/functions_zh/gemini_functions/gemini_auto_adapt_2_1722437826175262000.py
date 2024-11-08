from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators, \
    get_room
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger

# def main():
#     # Get home plan
#     home = home_plan()

#     # Get sensors
#     temperature_sensors = get_all_sensors(home, "IndoorTemperature")
#     humidity_sensors = get_all_sensors(home, "Humidity")
#     light_intensity_sensors = get_all_sensors(home, "LightIntensive")

#     # Get actuators
#     acs = get_all_actuators(home, "AC")
#     heaters = get_all_actuators(home, "Heater")
#     windows = get_all_actuators(home, "Window")
#     humidifiers = get_all_actuators(home, "Humidifier")
#     lights = get_all_actuators(home, "Light")

#     # Control based on sensor readings
#     for temperature_sensor in temperature_sensors:
#         temperature = temperature_sensor.get_reading()
#         if temperature is not None:
#             if temperature > TEMP_HIGH:
#                 for ac in acs:
#                     ac.turn_on()
#                 for window in windows:
#                     window.turn_off()
#             elif temperature < TEMP_LOW:
#                 for heater in heaters:
#                     heater.turn_on()

#     for humidity_sensor in humidity_sensors:
#         humidity = humidity_sensor.get_reading()
#         if humidity is not None:
#             if humidity > HUMIDITY_HIGH:
#                 for humidifier in humidifiers:
#                     humidifier.decrease_humidity()
#             elif humidity < HUMIDITY_LOW:
#                 for humidifier in humidifiers:
#                     humidifier.increase_humidity()

#     for light_intensity_sensor in light_intensity_sensors:
#         light_intensity = light_intensity_sensor.get_reading()
#         if light_intensity is not None:
#             if light_intensity > LIGHT_INTENSITY_HIGH:
#                 for light in lights:
#                     light.set_brightness_level("low")
#             elif light_intensity < LIGHT_INTENSITY_LOW:
#                 for light in lights:
#                     light.set_brightness_level("high")

#     # Main loop
#     while True:
#         # Update sensor readings and control actuators
#         # ... (code from previous sections)

#         # Sleep for a short duration
#         time.sleep(TEMP_CHANGE_DURATION_WINDOW)

# if __name__ == '__main__':
#     main()


def temperature_control(home):
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")
    windows = get_all_actuators(home, "Window")

    for temperature_sensor in temperature_sensors:
        temperature = temperature_sensor.get_reading()
        if temperature is not None:
            if temperature > TEMP_HIGH:
                for ac in acs:
                    ac.turn_on()
                for window in windows:
                    window.turn_off()
            elif temperature < TEMP_LOW:
                for heater in heaters:
                    heater.turn_on()
            else:
                for ac in acs:
                    ac.turn_off()
                for heater in heaters:
                    heater.turn_off()
                for window in windows:
                    window.turn_on()


def humidity_control(home):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for humidity_sensor in humidity_sensors:
        humidity = humidity_sensor.get_reading()
        if humidity is not None:
            if humidity > HUMIDITY_HIGH:
                for humidifier in humidifiers:
                    humidifier.decrease_humidity()
            elif humidity < HUMIDITY_LOW:
                for humidifier in humidifiers:
                    humidifier.increase_humidity()


def light_intensity_control(home):
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for light_intensity_sensor in light_intensity_sensors:
        light_intensity = light_intensity_sensor.get_reading()
        if light_intensity is not None:
            if light_intensity > LIGHT_INTENSITY_HIGH:
                for light in lights:
                    light.set_brightness_level("low")
            elif light_intensity < LIGHT_INTENSITY_LOW:
                for light in lights:
                    light.set_brightness_level("high")


def main():
    # Get home plan
    home = home_plan()

    while True:
        temperature_control(home)
        humidity_control(home)
        light_intensity_control(home)

        # Sleep for a short duration
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


if __name__ == '__main__':
    main()

# **Explanation:**

# 1. **Imports:**
#    - Import necessary functions and constants from `home.home_plan`, `home.config`, and `home.logger_config`.

# 2. **Control Functions:**
#    - `temperature_control(home)`:
#      - Retrieves all `IndoorTemperature` sensors and `AC`, `Heater`, and `Window` actuators.
#      - Iterates through temperature sensors, getting readings.
#      - If temperature is above `TEMP_HIGH`:
#        - Turn on all `AC`s and close all `Windows`.
#      - If temperature is below `TEMP_LOW`:
#        - Turn on all `Heaters`.
#      - Otherwise:
#        - Turn off `AC`s, `Heaters`, and open `Windows`.

#    - `humidity_control(home)`:
#      - Retrieves all `Humidity` sensors and `Humidifier` actuators.
#      - Iterates through humidity sensors, getting readings.
#      - If humidity is above `HUMIDITY_HIGH`:
#        - Decrease humidity in all `Humidifiers`.
#      - If humidity is below `HUMIDITY_LOW`:
#        - Increase humidity in all `Humidifiers`.

#    - `light_intensity_control(home)`:
#      - Retrieves all `LightIntensive` sensors and `Light` actuators.
#      - Iterates through light intensity sensors, getting readings.
#      - If light intensity is above `LIGHT_INTENSITY_HIGH`:
#        - Set all `Lights` to "low" brightness.
#      - If light intensity is below `LIGHT_INTENSITY_LOW`:
#        - Set all `Lights` to "high" brightness.

# 3. **`main()` Function:**
#    - Gets the home plan using `home_plan()`.
#    - Enters an infinite loop:
#      - Calls `temperature_control()`, `humidity_control()`, and `light_intensity_control()` to manage the smart home based on sensor readings.
#      - Sleeps for `TEMP_CHANGE_DURATION_WINDOW` seconds before checking sensor readings again.

# **How to Use:**

# 1. **Ensure Setup:**
#    - Make sure you have the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files in the `home` folder.
#    - Place the `function.py` file in the `functions` folder.
# 2. **Run the Code:**
#    - Navigate to the `functions` folder in your terminal.
#    - Run the `function.py` file using `python function.py`.

# **Important:**

# - This code provides a basic framework. You'll need to modify and extend it based on your specific smart home setup and desired functionalities.
# - Implement the `_generate_reading()` method in your sensor subclasses to provide actual readings instead of random values.
# - Include logic to handle user interactions, events, and other aspects of your smart home system.
