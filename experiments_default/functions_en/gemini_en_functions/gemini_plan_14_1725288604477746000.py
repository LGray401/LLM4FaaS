from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION
import time


def morning_plan(home):
    print("Start Morning Plan")
    # Open curtains in Bedroom and Living Room
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    living_room_curtains = get_room_actuators(living_room, "Curtain")
    bedroom_curtains = get_room_actuators(bedroom, "Curtain")
    for curtain in living_room_curtains:
        curtain.turn_on()
    for curtain in bedroom_curtains:
        curtain.turn_on()

    # Turn on lights in Living Room and Kitchen
    living_room_lights = get_room_actuators(living_room, "Light")
    kitchen = get_room(home, "Kitchen")
    kitchen_lights = get_room_actuators(kitchen, "Light")
    for light in living_room_lights:
        light.turn_on()
    for light in kitchen_lights:
        light.turn_on()

    # Turn on Coffee Machine in Kitchen
    kitchen_coffee_machine = get_room_actuators(kitchen, "CoffeeMachine")
    for coffee_machine in kitchen_coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # Adjust Temperature in Living Room and Bedroom
    living_room_heater = get_room_actuators(living_room, "Heater")
    living_room_ac = get_room_actuators(living_room, "AC")
    bedroom_heater = get_room_actuators(bedroom, "Heater")
    bedroom_ac = get_room_actuators(bedroom, "AC")
    for heater in living_room_heater:
        heater.set_target_temperature(22)
    for ac in living_room_ac:
        ac.set_target_temperature(22)
    for heater in bedroom_heater:
        heater.set_target_temperature(20)
    for ac in bedroom_ac:
        ac.set_target_temperature(20)

    # Turn on Music Player in Living Room
    living_room_music_player = get_room_actuators(living_room, "MusicPlayer")
    for music_player in living_room_music_player:
        music_player.turn_on()
        music_player.play_music("Morning playlist")

    # Play TV in Living Room
    living_room_tv = get_room_actuators(living_room, "SmartTV")
    for tv in living_room_tv:
        tv.turn_on()
        tv.play_channel("News Channel")

    print("Morning Plan finished.")


def leave_home_plan(home):
    print("Start Leave Home Plan")

    # Turn off all lights
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()

    # Turn off all music players
    all_music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in all_music_players:
        music_player.turn_off()

    # Turn off all TVs
    all_tvs = get_all_actuators(home, "SmartTV")
    for tv in all_tvs:
        tv.turn_off()

    # Close all windows and curtains
    all_windows = get_all_actuators(home, "Window")
    all_curtains = get_all_actuators(home, "Curtain")
    for window in all_windows:
        window.turn_off()
    for curtain in all_curtains:
        curtain.turn_off()

    # Lock all doors
    all_doors = get_all_actuators(home, "Door")
    for door in all_doors:
        door.lock()

    # Turn off all smart sockets
    all_smart_sockets = get_all_actuators(home, "SmartSocket")
    for smart_socket in all_smart_sockets:
        smart_socket.turn_off()

    # Turn off all cleaning robots
    all_cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for cleaning_robot in all_cleaning_robots:
        cleaning_robot.turn_off()

    print("Leave Home Plan finished.")


def movie_plan(home):
    print("Start Movie Plan")

    # Turn on lights in Living Room and set them to low brightness
    living_room = get_room(home, "LivingRoom")
    living_room_lights = get_room_actuators(living_room, "Light")
    for light in living_room_lights:
        light.turn_on()
        light.set_brightness_level("low")

    # Close curtains in Living Room
    living_room_curtains = get_room_actuators(living_room, "Curtain")
    for curtain in living_room_curtains:
        curtain.turn_on()

    # Turn on TV in Living Room and play a movie
    living_room_tv = get_room_actuators(living_room, "SmartTV")
    for tv in living_room_tv:
        tv.turn_on()
        tv.play_channel("Netflix")

    # Turn on Music Player in Living Room and play some relaxing music
    living_room_music_player = get_room_actuators(living_room, "MusicPlayer")
    for music_player in living_room_music_player:
        music_player.turn_on()
        music_player.play_music("Relaxing playlist")

    print("Movie Plan finished.")


def temperature_control(home):
    print("Start Temperature Control")

    # Get all indoor temperature sensors
    all_indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    # Get all heaters and ACs
    all_heaters = get_all_actuators(home, "Heater")
    all_acs = get_all_actuators(home, "AC")

    # Adjust temperature based on sensor readings
    for sensor in all_indoor_temp_sensors:
        current_temperature = sensor.get_reading()
        room_name = sensor.room_name

        # Find the heater/AC in the same room
        room_heaters = [heater for heater in all_heaters if heater.room_name == room_name]
        room_acs = [ac for ac in all_acs if ac.room_name == room_name]

        for heater in room_heaters:
            heater.adjust_temperature(current_temperature)
        for ac in room_acs:
            ac.adjust_temperature(current_temperature)

    print("Temperature Control finished.")


def humidity_control(home):
    print("Start Humidity Control")

    # Get all humidity sensors
    all_humidity_sensors = get_all_sensors(home, "Humidity")
    # Get all humidifiers
    all_humidifiers = get_all_actuators(home, "Humidifier")

    # Adjust humidity based on sensor readings
    for sensor in all_humidity_sensors:
        current_humidity = sensor.get_reading()
        room_name = sensor.room_name

        # Find the humidifier in the same room
        room_humidifiers = [humidifier for humidifier in all_humidifiers if humidifier.room_name == room_name]

        for humidifier in room_humidifiers:
            if current_humidity < HUMIDITY_LOW:
                humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                humidifier.decrease_humidity()

    print("Humidity Control finished.")


def light_intensity_control(home):
    print("Start Light Intensity Control")

    # Get all light intensity sensors
    all_light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    # Get all lights
    all_lights = get_all_actuators(home, "Light")

    # Adjust light intensity based on sensor readings
    for sensor in all_light_intensity_sensors:
        current_light_intensity = sensor.get_reading()
        room_name = sensor.room_name

        # Find the lights in the same room
        room_lights = [light for light in all_lights if light.room_name == room_name]

        for light in room_lights:
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                light.turn_on()
                light.set_brightness_level("high")
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                light.set_brightness_level("low")

    print("Light Intensity Control finished.")


def smoke_detection(home):
    print("Start Smoke Detection")

    # Get all smoke sensors
    all_smoke_sensors = get_all_sensors(home, "Smoke")
    # Get all notification senders
    all_notification_senders = get_all_actuators(home, "NotificationSender")

    # Check smoke levels and send notifications
    for sensor in all_smoke_sensors:
        smoke_level = sensor.get_reading()
        room_name = sensor.room_name

        # Find the notification sender in the same room
        room_notification_senders = [
            notification_sender for notification_sender in all_notification_senders
            if notification_sender.room_name == room_name
        ]

        for notification_sender in room_notification_senders:
            if smoke_level > 50:
                notification_sender.notification_sender(
                    f"Smoke detected in {room_name}! Please check the area."
                )

    print("Smoke Detection finished.")


def daily_cleaning_routine(home):
    print("Start Daily Cleaning Routine")

    # Get all cleaning robots
    all_cleaning_robots = get_all_actuators(home, "CleaningRobot")

    # Start the daily cleaning routine for each robot
    for cleaning_robot in all_cleaning_robots:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

    print("Daily Cleaning Routine finished.")


def main():
    # Initialize the home plan
    home = home_plan()
    print_home_plan(home)

    # Run the morning plan
    morning_plan(home)
    time.sleep(5)

    # Run the leave home plan
    leave_home_plan(home)
    time.sleep(5)

    # Run the movie plan
    movie_plan(home)
    time.sleep(5)

    # Run temperature control every 1 second
    while True:
        temperature_control(home)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    # Run humidity control every 1 second
    # while True:
    #     humidity_control(home)
    #     time.sleep(1)

    # Run light intensity control every 1 second
    # while True:
    #     light_intensity_control(home)
    #     time.sleep(1)

    # Run smoke detection every 1 second
    # while True:
    #     smoke_detection(home)
    #     time.sleep(1)

    # Run daily cleaning routine every 5 seconds
    # while True:
    #     daily_cleaning_routine(home)
    #     time.sleep(DAILY_ROUTINE_DURATION)


if __name__ == "__main__":
    main()

# This file implements the main functions for your smart home project based on your functional descriptions. It uses the classes defined in your other files to interact with sensors and actuators and create different plans.

# Here's a breakdown of the code:

# * **Import necessary modules:** Imports classes from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# * **Define functions for each plan:**
#     * **`morning_plan(home)`:** Executes the morning routine by turning on lights, coffee machine, music player, opening curtains, and adjusting temperatures.
#     * **`leave_home_plan(home)`:** Turns off lights, music players, TVs, closes windows and curtains, locks doors, turns off smart sockets and cleaning robots.
#     * **`movie_plan(home)`:** Prepares the living room for a movie night by turning on lights at low brightness, closing curtains, playing a movie on TV, and playing relaxing music.
# * **Define functions for automatic control:**
#     * **`temperature_control(home)`:** Reads indoor temperature sensors and adjusts heaters or ACs accordingly.
#     * **`humidity_control(home)`:** Reads humidity sensors and adjusts humidifiers to maintain desired humidity levels.
#     * **`light_intensity_control(home)`:** Reads light intensity sensors and adjusts lights to maintain desired brightness levels.
#     * **`smoke_detection(home)`:** Reads smoke sensors and sends notifications if smoke levels exceed a threshold.
#     * **`daily_cleaning_routine(home)`:** Activates cleaning robots for a daily cleaning routine.
# * **`main()` function:** Initializes the home plan, calls the plan functions, and sets up loops for automatic control based on the defined intervals.

# To use this code:

# 1. Place `function.py` in the `functions` folder.
# 2. Run `function.py` to start the smart home system.

# Remember to configure the thresholds and intervals in `config.py` to suit your needs.
