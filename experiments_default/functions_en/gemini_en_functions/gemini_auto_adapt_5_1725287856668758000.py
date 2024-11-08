from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, \
    LIGHT_INTENSITY_LOW, TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger

import time


def main():
    home = home_plan()
    print_home_plan(home)

    # # Example: Turn on the light in the living room
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     living_room_lights = get_room_actuators(home, "LivingRoom")
    #     if living_room_lights:
    #         for light in living_room_lights:
    #             if light.actuator_type == "Light":
    #                 light.turn_on()

    # # Example: Get the temperature reading from the bedroom
    # bedroom = get_room(home, "Bedroom")
    # if bedroom:
    #     bedroom_sensors = get_room_sensors(home, "Bedroom")
    #     if bedroom_sensors:
    #         for sensor in bedroom_sensors:
    #             if sensor.sensor_type == "IndoorTemperature":
    #                 temperature_reading = sensor.get_reading()
    #                 print(f"The temperature in the bedroom is {temperature_reading}°C.")

    # Example: Adjust temperature in rooms
    while True:
        # Get all indoor temperature sensors
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        # Get all heaters
        heaters = get_all_actuators(home, "Heater")
        # Get all ACs
        acs = get_all_actuators(home, "AC")

        for sensor in indoor_temp_sensors:
            current_temp = sensor.get_reading()
            # print(f"Sensor {sensor.id} current temp is {current_temp}.")
            room_name = sensor.room_name

            # Adjust heater
            for heater in heaters:
                if heater.room_name == room_name:
                    heater.adjust_temperature(current_temp)
                    # print(f"heater {heater.id} status: {heater.get_status()}")
                    if heater.status == "on":
                        # print("heater is on")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait before checking again

            # Adjust AC
            for ac in acs:
                if ac.room_name == room_name:
                    ac.adjust_temperature(current_temp)
                    # print(f"ac {ac.id} status: {ac.get_status()}")
                    if ac.status == "on":
                        # print("ac is on")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait before checking again

        # Get all humidity sensors
        humidity_sensors = get_all_sensors(home, "Humidity")
        # Get all humidifiers
        humidifiers = get_all_actuators(home, "Humidifier")

        for sensor in humidity_sensors:
            current_humidity = sensor.get_reading()
            # print(f"Sensor {sensor.id} current humidity is {current_humidity}.")
            room_name = sensor.room_name

            # Adjust humidifier
            for humidifier in humidifiers:
                if humidifier.room_name == room_name:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif current_humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

        # Get all light intensive sensors
        light_intensive_sensors = get_all_sensors(home, "LightIntensive")
        # Get all lights
        lights = get_all_actuators(home, "Light")

        for sensor in light_intensive_sensors:
            current_light_intensity = sensor.get_reading()
            room_name = sensor.room_name
            for light in lights:
                if light.room_name == room_name:
                    if current_light_intensity < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                    elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                        light.turn_off()

        # Get all cleaning robots and start their daily routine
        cleaning_robots = get_all_actuators(home, "CleaningRobot")
        for robot in cleaning_robots:
            if robot.status == "off":
                robot.turn_on()
            robot.daily_routine()

        # Get all smoke sensors
        smoke_sensors = get_all_sensors(home, "Smoke")
        for sensor in smoke_sensors:
            smoke_level = sensor.get_reading()
            if smoke_level > 50:
                # Trigger smoke alarm
                notification_sender = get_all_actuators(home, "NotificationSender")
                if notification_sender:
                    notification_sender[0].notification_sender(
                        f"Smoke detected in {sensor.room_name}, please evacuate.")
                # Other actions (e.g., open windows, activate sprinklers)

        time.sleep(5)  # Check sensor readings every 5 seconds

    # Example: Play music in the living room
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     living_room_music_player = get_room_actuators(home, "LivingRoom")
    #     if living_room_music_player:
    #         for music_player in living_room_music_player:
    #             if music_player.actuator_type == "MusicPlayer":
    #                 music_player.turn_on()
    #                 music_player.play_music("Jazz")

    # Example: Turn on the TV in the living room
    # living_room = get_room(home, "LivingRoom")
    # if living_room:
    #     living_room_tv = get_room_actuators(home, "LivingRoom")
    #     if living_room_tv:
    #         for tv in living_room_tv:
    #             if tv.actuator_type == "SmartTV":
    #                 tv.turn_on()
    #                 tv.play_channel("BBC News")

    # Example: Make coffee in the kitchen
    # kitchen = get_room(home, "Kitchen")
    # if kitchen:
    #     kitchen_coffee_machine = get_room_actuators(home, "Kitchen")
    #     if kitchen_coffee_machine:
    #         for coffee_machine in kitchen_coffee_machine:
    #             if coffee_machine.actuator_type == "CoffeeMachine":
    #                 coffee_machine.turn_on()
    #                 coffee_machine.make_coffee("Espresso")


if __name__ == "__main__":
    main()