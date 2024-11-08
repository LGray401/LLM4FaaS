from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time

def morning_plan(home):
    """
    Executes the morning plan:
        - Open curtains
        - Turn on music
        - Start the coffee machine
    """
    print("Starting Morning Plan...")
    logger.info(format("Starting Morning Plan."))

    living_room = get_room(home, "LivingRoom")
    if living_room:
        curtains = get_room_actuators(home, "LivingRoom")
        if curtains:
            for curtain in curtains:
                if curtain.actuator_type == "Curtain":
                    curtain.turn_on()
                    print(f"Opened curtain in {living_room.name}.")
                    logger.info(f"Opened curtain in {living_room.name}.")
                    time.sleep(1)

        music_player = get_room_actuators(home, "LivingRoom")
        if music_player:
            for player in music_player:
                if player.actuator_type == "MusicPlayer":
                    player.play_music("Morning playlist")
                    print(f"Playing music in {living_room.name}.")
                    logger.info(f"Playing music in {living_room.name}.")

        coffee_machine = get_room_actuators(home, "Kitchen")
        if coffee_machine:
            for machine in coffee_machine:
                if machine.actuator_type == "CoffeeMachine":
                    machine.turn_on()
                    machine.make_coffee("Espresso")
                    print(f"Making coffee in Kitchen.")
                    logger.info(f"Making coffee in Kitchen.")
                    time.sleep(2)
    else:
        print("Living Room not found!")
        logger.warning("Living Room not found!")

def leave_home_plan(home):
    """
    Executes the leave home plan:
        - Close the door
        - Turn off lights
    """
    print("Starting Leave Home Plan...")
    logger.info(format("Starting Leave Home Plan."))

    living_room = get_room(home, "LivingRoom")
    if living_room:
        door = get_room_actuators(home, "LivingRoom")
        if door:
            for d in door:
                if d.actuator_type == "Door":
                    d.lock()
                    print(f"Closed and locked the door in {living_room.name}.")
                    logger.info(f"Closed and locked the door in {living_room.name}.")
                    time.sleep(1)

        lights = get_room_actuators(home, "LivingRoom")
        if lights:
            for light in lights:
                if light.actuator_type == "Light":
                    light.turn_off()
                    print(f"Turned off the lights in {living_room.name}.")
                    logger.info(f"Turned off the lights in {living_room.name}.")
                    time.sleep(1)

    else:
        print("Living Room not found!")
        logger.warning("Living Room not found!")


def movie_plan(home):
    """
    Executes the movie plan:
        - Close curtains
        - Turn on TV
    """
    print("Starting Movie Plan...")
    logger.info(format("Starting Movie Plan."))

    living_room = get_room(home, "LivingRoom")
    if living_room:
        curtains = get_room_actuators(home, "LivingRoom")
        if curtains:
            for curtain in curtains:
                if curtain.actuator_type == "Curtain":
                    curtain.turn_off()
                    print(f"Closed the curtains in {living_room.name}.")
                    logger.info(f"Closed the curtains in {living_room.name}.")
                    time.sleep(1)

        tv = get_room_actuators(home, "LivingRoom")
        if tv:
            for t in tv:
                if t.actuator_type == "SmartTV":
                    t.turn_on()
                    t.play_channel("Netflix")
                    print(f"Turned on TV and started Netflix in {living_room.name}.")
                    logger.info(f"Turned on TV and started Netflix in {living_room.name}.")

    else:
        print("Living Room not found!")
        logger.warning("Living Room not found!")


def temperature_control(home):
    """
    Controls the temperature in the house:
        - Turn on heater if temperature is below 15 degrees Celsius
        - Turn on AC if temperature is above 25 degrees Celsius
    """
    print("Starting Temperature Control...")
    logger.info(format("Starting Temperature Control."))

    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temperature_sensors:
        current_temperature = sensor.get_reading()
        if current_temperature:
            room_name = sensor.room_name
            room = get_room(home, room_name)
            if room:
                heaters = get_room_actuators(home, room_name)
                acs = get_room_actuators(home, room_name)
                if heaters:
                    for heater in heaters:
                        if heater.actuator_type == "Heater":
                            heater.adjust_temperature(current_temperature)
                            if heater.status == "on":
                                print(
                                    f"Turning ON the heater in {room_name} as the temperature is {current_temperature}°C.")
                                logger.info(
                                    f"Turning ON the heater in {room_name} as the temperature is {current_temperature}°C.")
                            else:
                                print(
                                    f"Turning OFF the heater in {room_name} as the temperature is {current_temperature}°C.")
                                logger.info(
                                    f"Turning OFF the heater in {room_name} as the temperature is {current_temperature}°C.")

                if acs:
                    for ac in acs:
                        if ac.actuator_type == "AC":
                            ac.adjust_temperature(current_temperature)
                            if ac.status == "on":
                                print(
                                    f"Turning ON the AC in {room_name} as the temperature is {current_temperature}°C.")
                                logger.info(
                                    f"Turning ON the AC in {room_name} as the temperature is {current_temperature}°C.")
                            else:
                                print(
                                    f"Turning OFF the AC in {room_name} as the temperature is {current_temperature}°C.")
                                logger.info(
                                    f"Turning OFF the AC in {room_name} as the temperature is {current_temperature}°C.")

    time.sleep(TEMP_CHANGE_DURATION_WINDOW)


def humidity_control(home):
    """
    Controls the humidity in the house:
        - Turn on humidifier if humidity is below 30%
        - Open windows if humidity is above 50%
    """
    print("Starting Humidity Control...")
    logger.info(format("Starting Humidity Control."))

    humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in humidity_sensors:
        current_humidity = sensor.get_reading()
        if current_humidity:
            room_name = sensor.room_name
            room = get_room(home, room_name)
            if room:
                humidifiers = get_room_actuators(home, room_name)
                windows = get_room_actuators(home, room_name)

                if humidifiers:
                    for humidifier in humidifiers:
                        if humidifier.actuator_type == "Humidifier":
                            if current_humidity < HUMIDITY_LOW:
                                humidifier.increase_humidity()
                                print(f"Turning ON humidifier in {room_name} as humidity is {current_humidity}%.")
                                logger.info(f"Turning ON humidifier in {room_name} as humidity is {current_humidity}%.")
                            elif current_humidity > HUMIDITY_HIGH:
                                humidifier.decrease_humidity()
                                print(f"Turning OFF humidifier in {room_name} as humidity is {current_humidity}%.")
                                logger.info(f"Turning OFF humidifier in {room_name} as humidity is {current_humidity}%.")
                if windows:
                    for window in windows:
                        if window.actuator_type == "Window":
                            if current_humidity > HUMIDITY_HIGH:
                                window.turn_on()
                                print(f"Opening windows in {room_name} as humidity is {current_humidity}%.")
                                logger.info(f"Opening windows in {room_name} as humidity is {current_humidity}%.")
                            elif current_humidity < HUMIDITY_LOW:
                                window.turn_off()
                                print(f"Closing windows in {room_name} as humidity is {current_humidity}%.")
                                logger.info(f"Closing windows in {room_name} as humidity is {current_humidity}%.")


def light_control(home):
    """
    Controls the light in the house:
        - Turn on lights if light intensity is below 300 lux
        - Turn off lights if light intensity is above 900 lux
    """
    print("Starting Light Control...")
    logger.info(format("Starting Light Control."))

    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_intensity_sensors:
        current_light_intensity = sensor.get_reading()
        if current_light_intensity:
            room_name = sensor.room_name
            room = get_room(home, room_name)
            if room:
                lights = get_room_actuators(home, room_name)
                if lights:
                    for light in lights:
                        if light.actuator_type == "Light":
                            if current_light_intensity < LIGHT_INTENSITY_LOW:
                                light.turn_on()
                                print(f"Turning ON lights in {room_name} as light intensity is {current_light_intensity} lux.")
                                logger.info(
                                    f"Turning ON lights in {room_name} as light intensity is {current_light_intensity} lux.")
                            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                                light.turn_off()
                                print(f"Turning OFF lights in {room_name} as light intensity is {current_light_intensity} lux.")
                                logger.info(
                                    f"Turning OFF lights in {room_name} as light intensity is {current_light_intensity} lux.")


def smoke_detection(home):
    """
    Detects smoke in the house:
        - Send a notification if smoke is detected
    """
    print("Starting Smoke Detection...")
    logger.info(format("Starting Smoke Detection."))

    smoke_sensors = get_all_sensors(home, "Smoke")
    for sensor in smoke_sensors:
        current_smoke_level = sensor.get_reading()
        if current_smoke_level:
            room_name = sensor.room_name
            room = get_room(home, room_name)
            if room:
                notification_sender = get_room_actuators(home, room_name)
                if notification_sender:
                    for sender in notification_sender:
                        if sender.actuator_type == "NotificationSender":
                            sender.notification_sender(f"Smoke detected in {room_name}!")
                            print(f"Sending notification: Smoke detected in {room_name}!")
                            logger.warning(f"Smoke detected in {room_name}!")

def daily_cleaning_routine(home):
    """
    Executes the daily cleaning routine:
        - Starts the cleaning robot in the living room
    """
    print("Starting Daily Cleaning Routine...")
    logger.info(format("Starting Daily Cleaning Routine."))

    living_room = get_room(home, "LivingRoom")
    if living_room:
        cleaning_robot = get_room_actuators(home, "LivingRoom")
        if cleaning_robot:
            for robot in cleaning_robot:
                if robot.actuator_type == "CleaningRobot":
                    robot.turn_on()
                    robot.daily_routine()
                    print(f"Cleaning Robot started in {living_room.name}.")
                    logger.info(f"Cleaning Robot started in {living_room.name}.")
        else:
            print(f"No Cleaning Robot found in {living_room.name}.")
            logger.warning(f"No Cleaning Robot found in {living_room.name}.")
    else:
        print("Living Room not found!")
        logger.warning("Living Room not found!")


def main():
    """
    Main function of the smart home system.
    """
    home = home_plan()

    while True:
        morning_plan(home)
        leave_home_plan(home)
        movie_plan(home)
        temperature_control(home)
        humidity_control(home)
        light_control(home)
        smoke_detection(home)
        daily_cleaning_routine(home)

        # Add more plans and functions here

        # Sleep for a short time before checking again
        time.sleep(5)

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:** 
#    - Imports functions from `home_plan.py`, `sensor.py`, `actuator.py`, `config.py`, and `logger_config.py`.
#    - Uses `time` for sleep functions.

# 2. **Define plan functions:**
#    - **`morning_plan(home)`:**
#      - Opens curtains, plays music, and starts the coffee machine in the Living Room.
#    - **`leave_home_plan(home)`:**
#      - Locks the door and turns off lights in the Living Room.
#    - **`movie_plan(home)`:**
#      - Closes curtains and turns on the TV in the Living Room.
#    - **`temperature_control(home)`:**
#      - Adjusts heaters and AC based on temperature readings from indoor temperature sensors.
#    - **`humidity_control(home)`:**
#      - Adjusts humidifiers and opens/closes windows based on humidity readings.
#    - **`light_control(home)`:**
#      - Turns on/off lights based on light intensity readings.
#    - **`smoke_detection(home)`:**
#      - Sends a notification if any smoke sensor detects smoke.
#    - **`daily_cleaning_routine(home)`:**
#      - Starts the cleaning robot in the Living Room.

# 3. **Define `main()` function:**
#    - Creates a `home` object using `home_plan()`.
#    - Enters a loop:
#      - Calls each plan function in sequence.
#      - Sleeps for 5 seconds before checking again.

# 4. **Call `main()` if the script is run directly:**
#    - Executes the main function if the script is run as `python function.py`.

# **How to use:**

# 1. **Run the script:**
#    - Navigate to the `functions` folder in your project.
#    - Execute the script using `python function.py`.

# 2. **Check logs:**
#    - The logs will be saved in the `logs` folder as `smart_home.log`.

# **Further Development:**

# - Add more plans and functions for other tasks.
# - Implement more complex logic for controlling actuators based on sensor readings.
# - Integrate with external systems like voice assistants or home automation platforms.
# - Improve logging and error handling.