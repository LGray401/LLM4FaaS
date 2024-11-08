from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time
import random


def turn_on_light(home, room_name, light_brightness_level):
    room = get_room(home, room_name)
    if room is not None:
        lights = get_room_actuators(home, room_name)
        for light in lights:
            if light.actuator_type == "Light":
                light.turn_on()
                light.set_brightness_level(light_brightness_level)


def turn_off_light(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        lights = get_room_actuators(home, room_name)
        for light in lights:
            if light.actuator_type == "Light":
                light.turn_off()


def adjust_temperature(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        indoor_temp_sensors = get_room_sensors(home, room_name)
        for sensor in indoor_temp_sensors:
            if sensor.sensor_type == "IndoorTemperature":
                current_temp = sensor.get_reading()
                if current_temp is not None:
                    heaters = get_room_actuators(home, room_name)
                    for heater in heaters:
                        if heater.actuator_type == "Heater":
                            heater.adjust_temperature(current_temp)
                    acs = get_room_actuators(home, room_name)
                    for ac in acs:
                        if ac.actuator_type == "AC":
                            ac.adjust_temperature(current_temp)


def adjust_humidity(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        humidity_sensors = get_room_sensors(home, room_name)
        for sensor in humidity_sensors:
            if sensor.sensor_type == "Humidity":
                current_humidity = sensor.get_reading()
                if current_humidity is not None:
                    humidifiers = get_room_actuators(home, room_name)
                    for humidifier in humidifiers:
                        if humidifier.actuator_type == "Humidifier":
                            if current_humidity < HUMIDITY_LOW:
                                humidifier.increase_humidity()
                            elif current_humidity > HUMIDITY_HIGH:
                                humidifier.decrease_humidity()


def adjust_light_intensity(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        light_intensity_sensors = get_room_sensors(home, room_name)
        for sensor in light_intensity_sensors:
            if sensor.sensor_type == "LightIntensive":
                current_intensity = sensor.get_reading()
                if current_intensity is not None:
                    lights = get_room_actuators(home, room_name)
                    for light in lights:
                        if light.actuator_type == "Light":
                            if current_intensity < LIGHT_INTENSITY_LOW:
                                light.turn_on()
                                light.set_brightness_level("high")
                            elif current_intensity > LIGHT_INTENSITY_HIGH:
                                light.turn_off()


def turn_on_coffee_machine(home, room_name, coffee_type):
    room = get_room(home, room_name)
    if room is not None:
        coffee_machines = get_room_actuators(home, room_name)
        for coffee_machine in coffee_machines:
            if coffee_machine.actuator_type == "CoffeeMachine":
                coffee_machine.turn_on()
                coffee_machine.make_coffee(coffee_type)


def turn_off_coffee_machine(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        coffee_machines = get_room_actuators(home, room_name)
        for coffee_machine in coffee_machines:
            if coffee_machine.actuator_type == "CoffeeMachine":
                coffee_machine.turn_off()


def open_window(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        windows = get_room_actuators(home, room_name)
        for window in windows:
            if window.actuator_type == "Window":
                window.turn_on()


def close_window(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        windows = get_room_actuators(home, room_name)
        for window in windows:
            if window.actuator_type == "Window":
                window.turn_off()


def open_curtain(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        curtains = get_room_actuators(home, room_name)
        for curtain in curtains:
            if curtain.actuator_type == "Curtain":
                curtain.turn_on()


def close_curtain(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        curtains = get_room_actuators(home, room_name)
        for curtain in curtains:
            if curtain.actuator_type == "Curtain":
                curtain.turn_off()


def play_music(home, room_name, playlist):
    room = get_room(home, room_name)
    if room is not None:
        music_players = get_room_actuators(home, room_name)
        for music_player in music_players:
            if music_player.actuator_type == "MusicPlayer":
                music_player.turn_on()
                music_player.play_music(playlist)


def stop_music(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        music_players = get_room_actuators(home, room_name)
        for music_player in music_players:
            if music_player.actuator_type == "MusicPlayer":
                music_player.turn_off()


def start_cleaning_robot(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        cleaning_robots = get_room_actuators(home, room_name)
        for cleaning_robot in cleaning_robots:
            if cleaning_robot.actuator_type == "CleaningRobot":
                cleaning_robot.turn_on()
                cleaning_robot.daily_routine()


def stop_cleaning_robot(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        cleaning_robots = get_room_actuators(home, room_name)
        for cleaning_robot in cleaning_robots:
            if cleaning_robot.actuator_type == "CleaningRobot":
                cleaning_robot.turn_off()


def send_notification(home, room_name, message):
    room = get_room(home, room_name)
    if room is not None:
        notification_senders = get_room_actuators(home, room_name)
        for notification_sender in notification_senders:
            if notification_sender.actuator_type == "NotificationSender":
                notification_sender.notification_sender(message)


def play_tv_channel(home, room_name, channel_name):
    room = get_room(home, room_name)
    if room is not None:
        smart_tvs = get_room_actuators(home, room_name)
        for smart_tv in smart_tvs:
            if smart_tv.actuator_type == "SmartTV":
                smart_tv.turn_on()
                smart_tv.play_channel(channel_name)


def turn_off_tv(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        smart_tvs = get_room_actuators(home, room_name)
        for smart_tv in smart_tvs:
            if smart_tv.actuator_type == "SmartTV":
                smart_tv.turn_off()


def turn_on_smart_socket(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        smart_sockets = get_room_actuators(home, room_name)
        for smart_socket in smart_sockets:
            if smart_socket.actuator_type == "SmartSocket":
                smart_socket.turn_on()


def turn_off_smart_socket(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        smart_sockets = get_room_actuators(home, room_name)
        for smart_socket in smart_sockets:
            if smart_socket.actuator_type == "SmartSocket":
                smart_socket.turn_off()


def open_door(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        doors = get_room_actuators(home, room_name)
        for door in doors:
            if door.actuator_type == "Door":
                door.unlock()


def close_door(home, room_name):
    room = get_room(home, room_name)
    if room is not None:
        doors = get_room_actuators(home, room_name)
        for door in doors:
            if door.actuator_type == "Door":
                door.lock()


def main():
    home = home_plan()
    print_home_plan(home)

    while True:
        # Example usage:
        # turn_on_light(home, "LivingRoom", "high")
        # turn_off_light(home, "LivingRoom")
        # adjust_temperature(home, "LivingRoom")
        # adjust_humidity(home, "LivingRoom")
        # adjust_light_intensity(home, "LivingRoom")
        # turn_on_coffee_machine(home, "Kitchen", "Espresso")
        # turn_off_coffee_machine(home, "Kitchen")
        # open_window(home, "LivingRoom")
        # close_window(home, "LivingRoom")
        # open_curtain(home, "LivingRoom")
        # close_curtain(home, "LivingRoom")
        # play_music(home, "LivingRoom", "Pop")
        # stop_music(home, "LivingRoom")
        # start_cleaning_robot(home, "LivingRoom")
        # stop_cleaning_robot(home, "LivingRoom")
        # send_notification(home, "LivingRoom", "It's time to go home!")
        # play_tv_channel(home, "LivingRoom", "CNN")
        # turn_off_tv(home, "LivingRoom")
        # turn_on_smart_socket(home, "LivingRoom")
        # turn_off_smart_socket(home, "LivingRoom")
        # open_door(home, "LivingRoom")
        # close_door(home, "LivingRoom")

        # Simulation of sensor readings and actuator actions:
        # Indoor Temperature Sensor
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        for sensor in indoor_temp_sensors:
            current_temp = sensor.get_reading()
            if current_temp is not None:
                room_name = sensor.room_name
                if current_temp < TEMP_LOW:
                    heaters = get_room_actuators(home, room_name)
                    for heater in heaters:
                        if heater.actuator_type == "Heater":
                            heater.turn_on()
                            logger.info(f"Heater in {room_name} is turned ON.")
                            time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                elif current_temp > TEMP_HIGH:
                    acs = get_room_actuators(home, room_name)
                    for ac in acs:
                        if ac.actuator_type == "AC":
                            ac.turn_on()
                            logger.info(f"AC in {room_name} is turned ON.")
                            time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                else:
                    heaters = get_room_actuators(home, room_name)
                    for heater in heaters:
                        if heater.actuator_type == "Heater":
                            heater.turn_off()
                            logger.info(f"Heater in {room_name} is turned OFF.")
                    acs = get_room_actuators(home, room_name)
                    for ac in acs:
                        if ac.actuator_type == "AC":
                            ac.turn_off()
                            logger.info(f"AC in {room_name} is turned OFF.")

        # Humidity Sensor
        humidity_sensors = get_all_sensors(home, "Humidity")
        for sensor in humidity_sensors:
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                room_name = sensor.room_name
                if current_humidity < HUMIDITY_LOW:
                    humidifiers = get_room_actuators(home, room_name)
                    for humidifier in humidifiers:
                        if humidifier.actuator_type == "Humidifier":
                            humidifier.increase_humidity()
                            logger.info(f"Humidifier in {room_name} is increasing humidity.")
                elif current_humidity > HUMIDITY_HIGH:
                    humidifiers = get_room_actuators(home, room_name)
                    for humidifier in humidifiers:
                        if humidifier.actuator_type == "Humidifier":
                            humidifier.decrease_humidity()
                            logger.info(f"Humidifier in {room_name} is decreasing humidity.")

        # Light Intensity Sensor
        light_intensity_sensors = get_all_sensors(home, "LightIntensive")
        for sensor in light_intensity_sensors:
            current_intensity = sensor.get_reading()
            if current_intensity is not None:
                room_name = sensor.room_name
                if current_intensity < LIGHT_INTENSITY_LOW:
                    lights = get_room_actuators(home, room_name)
                    for light in lights:
                        if light.actuator_type == "Light":
                            light.turn_on()
                            light.set_brightness_level("high")
                            logger.info(f"Light in {room_name} is turned ON with high brightness.")
                elif current_intensity > LIGHT_INTENSITY_HIGH:
                    lights = get_room_actuators(home, room_name)
                    for light in lights:
                        if light.actuator_type == "Light":
                            light.turn_off()
                            logger.info(f"Light in {room_name} is turned OFF.")

        # Smoke Sensor
        smoke_sensors = get_all_sensors(home, "Smoke")
        for sensor in smoke_sensors:
            current_reading = sensor.get_reading()
            if current_reading is not None:
                room_name = sensor.room_name
                if current_reading > 50:  # Arbitrary threshold for smoke detection
                    notification_senders = get_room_actuators(home, room_name)
                    for notification_sender in notification_senders:
                        if notification_sender.actuator_type == "NotificationSender":
                            notification_sender.notification_sender(f"Smoke detected in {room_name}!")
                            logger.warning(f"Smoke detected in {room_name}!")

        # Cleaning Robot
        cleaning_robots = get_all_actuators(home, "CleaningRobot")
        for robot in cleaning_robots:
            if robot.status == "off" and random.random() < 0.2:  # 20% chance of starting cleaning routine
                robot.turn_on()
                robot.daily_routine()

        time.sleep(1)  # Simulate time passing


if __name__ == "__main__":
    main()

# **Explanation of `function.py`:**

# 1. **Imports:**
#    - Imports necessary modules from `home` package: `home_plan`, `sensor`, `actuator`, `config`, and `logger_config`.
#    - Imports `time` and `random` for simulation purposes.

# 2. **Functions:**
#    - `turn_on_light()`: Turns on the light in a specified room and sets the brightness level.
#    - `turn_off_light()`: Turns off the light in a specified room.
#    - `adjust_temperature()`: Adjusts the temperature in a room based on the current temperature and target temperature set on the heater/AC.
#    - `adjust_humidity()`: Adjusts the humidity in a room based on the current humidity and thresholds.
#    - `adjust_light_intensity()`: Adjusts the light intensity in a room based on the current light intensity and thresholds.
#    - `turn_on_coffee_machine()`: Turns on the coffee machine in a specified room and makes coffee.
#    - `turn_off_coffee_machine()`: Turns off the coffee machine in a specified room.
#    - `open_window()`: Opens the window in a specified room.
#    - `close_window()`: Closes the window in a specified room.
#    - `open_curtain()`: Opens the curtain in a specified room.
#    - `close_curtain()`: Closes the curtain in a specified room.
#    - `play_music()`: Plays music on the music player in a specified room.
#    - `stop_music()`: Stops the music on the music player in a specified room.
#    - `start_cleaning_robot()`: Starts the daily cleaning routine of the cleaning robot in a specified room.
#    - `stop_cleaning_robot()`: Stops the cleaning robot in a specified room.
#    - `send_notification()`: Sends a notification message using the notification sender in a specified room.
#    - `play_tv_channel()`: Plays a specified channel on the SmartTV in a specified room.
#    - `turn_off_tv()`: Turns off the SmartTV in a specified room.
#    - `turn_on_smart_socket()`: Turns on the smart socket in a specified room.
#    - `turn_off_smart_socket()`: Turns off the smart socket in a specified room.
#    - `open_door()`: Opens the door in a specified room.
#    - `close_door()`: Closes the door in a specified room.

# 3. **`main()` Function:**
#    - Creates the home plan using `home_plan()`.
#    - Prints the home plan using `print_home_plan()`.
#    - Enters an infinite loop (`while True`) to simulate the smart home functionality:
#      - **Sensor Readings:**
#        - Simulates sensor readings for IndoorTemperature, Humidity, LightIntensive, and Smoke sensors.
#        - Based on the readings, it triggers appropriate actuator actions (e.g., turning on/off heaters, ACs, humidifiers, lights, sending smoke notifications).
#      - **Cleaning Robot:**
#        - Simulates a random chance of the cleaning robot starting its daily routine.
#      - **Time Delay:**
#        - Uses `time.sleep(1)` to simulate the passage of time.

# **How to Use `function.py`:**

# 1. **Import:** Import `function.py` into your main script.
# 2. **Create Home Plan:** Create the home plan using `home = home_plan()`.
# 3. **Call Functions:** Call the functions in `function.py` to interact with the smart home components (e.g., `turn_on_light(home, "LivingRoom", "high")`).

# **Remember to adapt the code and function calls to match your specific smart home project and functionalities.**
