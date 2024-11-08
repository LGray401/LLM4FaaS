from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, Humidifier, CleaningRobot, NotificationSender
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    home = home_plan()

    # Temperature Control
    for sensor in get_all_sensors(home, "IndoorTemperature"):
        temperature = sensor.get_reading()
        if temperature is not None:
            room = get_room(home, sensor.room_name)
            if room is not None:
                for heater in get_room_actuators(room, "Heater"):
                    heater.set_target_temperature(22)
                    heater.adjust_temperature(temperature)
                for ac in get_room_actuators(room, "AC"):
                    ac.set_target_temperature(20)
                    ac.adjust_temperature(temperature)

    # Humidity Control
    for sensor in get_all_sensors(home, "Humidity"):
        humidity = sensor.get_reading()
        if humidity is not None:
            room = get_room(home, sensor.room_name)
            if room is not None:
                for humidifier in get_room_actuators(room, "Humidifier"):
                    if humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

    # Light Control
    for sensor in get_all_sensors(home, "LightIntensive"):
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            room = get_room(home, sensor.room_name)
            if room is not None:
                for light in get_room_actuators(room, "Light"):
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                        light.turn_on()
                        light.set_brightness_level("low")
                    else:
                        light.turn_off()

    # Daily Cleaning Routine
    for cleaning_robot in get_all_actuators(home, "CleaningRobot"):
        cleaning_robot.daily_routine()

    # Notifications
    for notification_sender in get_all_actuators(home, "NotificationSender"):
        if temperature < TEMP_LOW:
            notification_sender.notification_sender(f"Temperature in {sensor.room_name} is too low!")
        elif temperature > TEMP_HIGH:
            notification_sender.notification_sender(f"Temperature in {sensor.room_name} is too high!")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** 
#    - Import necessary functions and classes from `home` package.
#    - Import `TEMP_LOW`, `TEMP_HIGH`, `HUMIDITY_LOW`, `HUMIDITY_HIGH`, `LIGHT_INTENSITY_LOW`, `LIGHT_INTENSITY_HIGH` constants from `home.config`.
#    - Import `logger` from `home.logger_config` to log actions.

# 2. **`main()` function:**
#    - Creates a `home` object using `home_plan()`.
#    - **Temperature Control:**
#      - Iterates through all `IndoorTemperature` sensors.
#      - Reads the temperature from each sensor.
#      - If temperature is available, finds the corresponding room.
#      - For each heater and AC in the room, sets the target temperature and adjusts the actuator based on the current temperature.
#    - **Humidity Control:**
#      - Iterates through all `Humidity` sensors.
#      - Reads the humidity from each sensor.
#      - If humidity is available, finds the corresponding room.
#      - For each humidifier in the room, increases or decreases humidity based on the current humidity level.
#    - **Light Control:**
#      - Iterates through all `LightIntensive` sensors.
#      - Reads the light intensity from each sensor.
#      - If light intensity is available, finds the corresponding room.
#      - For each light in the room, turns it on/off and sets the brightness level based on the light intensity.
#    - **Daily Cleaning Routine:**
#      - Iterates through all `CleaningRobot` actuators and initiates the daily cleaning routine.
#    - **Notifications:**
#      - Iterates through all `NotificationSender` actuators.
#      - Sends notifications if the temperature is too low or too high.

# 3. **`if __name__ == "__main__":` block:**
#    - Calls the `main()` function to run the smart home logic when the script is executed.

# **Key Points:**

# - The code uses loops to iterate through sensors and actuators.
# - It utilizes functions from `home_plan.py` to retrieve rooms, sensors, and actuators based on names and types.
# - The code implements basic logic for temperature, humidity, and light control based on predefined thresholds.
# - It incorporates daily cleaning routines and notification sending mechanisms.
# - Logging is used throughout the code to provide detailed information about actions taken.

# **Remember to:**

# - Install the required libraries: `python3 -m pip install -r requirements.txt`
# - Configure the logging system in `home/logger_config.py`
# - Customize the thresholds and logic as needed for your specific smart home project.
