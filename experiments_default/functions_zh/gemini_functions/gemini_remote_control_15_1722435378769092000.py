# function.py
import time
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")

    while True:
        # Sensor Reading
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        for indoor_temp_sensor in indoor_temp_sensors:
            indoor_temp_sensor.turn_on()
            current_temperature = indoor_temp_sensor.get_reading()
            indoor_temp_sensor.turn_off()

            # Actuator Actions based on Sensor Reading
            if current_temperature < TEMP_LOW:
                heaters = get_all_actuators(home, "Heater")
                for heater in heaters:
                    heater.turn_on()
                    heater.set_target_temperature(TEMP_HIGH)
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            elif current_temperature > TEMP_HIGH:
                acs = get_all_actuators(home, "AC")
                for ac in acs:
                    ac.turn_on()
                    ac.set_target_temperature(TEMP_LOW)
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            else:
                heaters = get_all_actuators(home, "Heater")
                for heater in heaters:
                    heater.turn_off()
                acs = get_all_actuators(home, "AC")
                for ac in acs:
                    ac.turn_off()

        humidity_sensors = get_all_sensors(home, "Humidity")
        for humidity_sensor in humidity_sensors:
            humidity_sensor.turn_on()
            current_humidity = humidity_sensor.get_reading()
            humidity_sensor.turn_off()

            if current_humidity < HUMIDITY_LOW:
                humidifiers = get_all_actuators(home, "Humidifier")
                for humidifier in humidifiers:
                    humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                humidifiers = get_all_actuators(home, "Humidifier")
                for humidifier in humidifiers:
                    humidifier.decrease_humidity()

        light_intensive_sensors = get_all_sensors(home, "LightIntensive")
        for light_intensive_sensor in light_intensive_sensors:
            light_intensive_sensor.turn_on()
            current_light_intensity = light_intensive_sensor.get_reading()
            light_intensive_sensor.turn_off()

            if current_light_intensity < LIGHT_INTENSITY_LOW:
                lights = get_room_actuators(living_room, "Light")
                for light in lights:
                    light.turn_on()
                    light.set_brightness_level("high")
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                lights = get_room_actuators(living_room, "Light")
                for light in lights:
                    light.turn_on()
                    light.set_brightness_level("low")

        # Smoke Sensor
        smoke_sensors = get_all_sensors(home, "Smoke")
        for smoke_sensor in smoke_sensors:
            smoke_sensor.turn_on()
            smoke_reading = smoke_sensor.get_reading()
            smoke_sensor.turn_off()
            if smoke_reading > 30:
                notification_senders = get_all_actuators(home, "NotificationSender")
                for notification_sender in notification_senders:
                    notification_sender.turn_on()
                    notification_sender.notification_sender("Smoke detected! Evacuate immediately.")
                    notification_sender.turn_off()

        # Cleaning Robot Routine
        cleaning_robots = get_all_actuators(home, "CleaningRobot")
        for cleaning_robot in cleaning_robots:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

        time.sleep(1)  # Simulate a delay for real-time sensor updates

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - Import necessary modules from your `home` package:
#      - `home_plan`: For working with the home plan and finding rooms/devices.
#      - `sensor`: To access sensor types like `IndoorTemperatureSensor`, etc.
#      - `actuator`: To access actuator types like `Heater`, `AC`, `Light`, etc.
#      - `config`: To use constants like temperature thresholds.

# 2. **`main()` Function:**
#    - **Home Plan:** Creates the home plan using `home_plan()`.
#    - **Loop:** Runs an infinite loop to continuously monitor and control the smart home.
#    - **Sensor Readings:** Iterates through sensors of different types:
#      - **Temperature:**
#        - Turns on temperature sensors.
#        - Reads temperature from each sensor.
#        - Turns off the sensors.
#        - **Temperature Control:**
#          - If the temperature is below `TEMP_LOW`, turns on heaters and sets target temperature to `TEMP_HIGH`.
#          - If the temperature is above `TEMP_HIGH`, turns on ACs and sets target temperature to `TEMP_LOW`.
#          - If the temperature is within the range, turns off heaters and ACs.
#      - **Humidity:** Similar to temperature control, using `HUMIDITY_LOW` and `HUMIDITY_HIGH` thresholds.
#      - **Light Intensity:**  Similar to temperature control, using `LIGHT_INTENSITY_LOW` and `LIGHT_INTENSITY_HIGH` thresholds.
#      - **Smoke:**  
#        - Turns on smoke sensors.
#        - Reads smoke level from each sensor.
#        - Turns off the sensors.
#        - **Smoke Alarm:**  If smoke level is above a threshold, sends an evacuation notification.
#      - **Cleaning Robot:** Starts the daily routine for cleaning robots.
#    - **Delay:** Includes a `time.sleep(1)` to simulate a delay for real-time sensor updates.

# **Key Improvements:**

# - **Sensor Control:** Sensors are turned on before reading and turned off afterward for efficiency.
# - **Actuator Logic:** Clearer logic for controlling actuators based on sensor readings and thresholds.
# - **Notifications:** A notification system using `NotificationSender` is implemented for smoke detection.
# - **Cleaning Robot:** The cleaning robot has a daily routine.
# - **Modular Design:** Code is organized into functions and classes for better maintainability.

# **How to Use:**

# 1. **Run:** Execute the `function.py` file from your project directory.
# 2. **Test:** This code will simulate sensor readings and actuator actions based on the thresholds defined in `config.py`. You can modify the thresholds and other values in `config.py` to customize your smart home behavior.

# This code provides a foundational structure for a smart home system. You can expand upon it by adding more sensors, actuators, rules, and automation features.
