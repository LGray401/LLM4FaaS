from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators, \
    get_room
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time


def main():
    # Create home plan
    home = home_plan()

    # Temperature control loop
    while True:
        # Get all indoor temperature sensors
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        # Get all heaters
        heaters = get_all_actuators(home, "Heater")
        # Get all ACs
        acs = get_all_actuators(home, "AC")

        # Check temperature readings and adjust actuators
        for sensor in indoor_temp_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                room = get_room(home, sensor.room_name)
                if room is not None:
                    for heater in heaters:
                        if heater.room_name == room.name:
                            heater.adjust_temperature(reading)
                    for ac in acs:
                        if ac.room_name == room.name:
                            ac.adjust_temperature(reading)

        # Humidity control loop
        # Get all humidity sensors
        humidity_sensors = get_all_sensors(home, "Humidity")
        # Get all humidifiers
        humidifiers = get_all_actuators(home, "Humidifier")

        # Check humidity readings and adjust actuators
        for sensor in humidity_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                room = get_room(home, sensor.room_name)
                if room is not None:
                    for humidifier in humidifiers:
                        if humidifier.room_name == room.name:
                            if reading < HUMIDITY_LOW:
                                humidifier.increase_humidity()
                            elif reading > HUMIDITY_HIGH:
                                humidifier.decrease_humidity()

        # Light control loop
        # Get all light intensive sensors
        light_intensive_sensors = get_all_sensors(home, "LightIntensive")
        # Get all lights
        lights = get_all_actuators(home, "Light")

        # Check light intensity readings and adjust actuators
        for sensor in light_intensive_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                room = get_room(home, sensor.room_name)
                if room is not None:
                    for light in lights:
                        if light.room_name == room.name:
                            if reading < LIGHT_INTENSITY_LOW:
                                light.turn_on()
                                light.set_brightness_level("high")
                            elif reading > LIGHT_INTENSITY_HIGH:
                                light.turn_off()

        # Smoke detection loop
        # Get all smoke sensors
        smoke_sensors = get_all_sensors(home, "Smoke")
        # Get all notification senders
        notification_senders = get_all_actuators(home, "NotificationSender")

        # Check smoke readings and send notifications
        for sensor in smoke_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                if reading > 0:
                    room = get_room(home, sensor.room_name)
                    if room is not None:
                        for notification_sender in notification_senders:
                            if notification_sender.room_name == room.name:
                                notification_sender.notification_sender("Smoke detected in " + sensor.room_name + "!")
                                logger.warning("Smoke detected in " + sensor.room_name + "!")

        # Cleaning robot routine
        # Get all cleaning robots
        cleaning_robots = get_all_actuators(home, "CleaningRobot")

        # Start daily cleaning routine for each robot
        for robot in cleaning_robots:
            robot.daily_routine()

        # Wait for a short duration before checking again
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions to define the home plan and access room information.
#    - `home.config`: Contains configuration settings like temperature thresholds and durations.
#    - `home.logger_config`: Sets up logging for debugging and monitoring.
#    - `time`: Used to introduce pauses in the control loops.

# 2. **`main()` function:**
#    - **Home plan creation:** Calls `home_plan()` to create the home layout.
#    - **Control loops:**
#      - **Temperature control:**
#        - Gets all indoor temperature sensors and heaters/ACs.
#        - Iterates through sensors, retrieves readings, and adjusts heaters/ACs based on temperature thresholds.
#      - **Humidity control:**
#        - Gets all humidity sensors and humidifiers.
#        - Iterates through sensors, retrieves readings, and controls humidifiers to increase/decrease humidity as needed.
#      - **Light control:**
#        - Gets all light intensive sensors and lights.
#        - Iterates through sensors, retrieves readings, and turns lights on/off and adjusts brightness based on light levels.
#      - **Smoke detection:**
#        - Gets all smoke sensors and notification senders.
#        - Iterates through sensors, checks for smoke, and sends notifications if detected.
#      - **Cleaning robot routine:**
#        - Gets all cleaning robots.
#        - Starts the daily cleaning routine for each robot.

# 3. **Pause and repeat:**
#    - After each control loop iteration, the code waits for a short duration (defined in `TEMP_CHANGE_DURATION_WINDOW`) before checking again.

# **Key concepts:**

# - **Sensor and Actuator Interaction:** The code constantly reads sensor values (temperature, humidity, light intensity, smoke) and then controls actuators (heaters, ACs, humidifiers, lights, notification senders, cleaning robots) to adjust the home environment accordingly.
# - **Thresholds:** Configuration settings like `TEMP_LOW`, `TEMP_HIGH`, etc., define the thresholds for triggering actions.
# - **Time Delays:** The `time.sleep()` function introduces pauses to prevent the code from constantly checking sensors and overworking the system.

# **To run this code:**

# 1. Ensure you have the necessary Python modules installed (import statements should help with this).
# 2. Save the code as `function.py` in the `functions` folder.
# 3. Make sure all other code files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`) are in the `home` folder.
# 4. Run the script using `python function.py`.

# This will simulate a smart home system that reacts to changes in temperature, humidity, light intensity, and smoke detection, and executes actions like adjusting temperature, controlling humidity, turning lights on/off, sending notifications, and initiating cleaning robot routines.
