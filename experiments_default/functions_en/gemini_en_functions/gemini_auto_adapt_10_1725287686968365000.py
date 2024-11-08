from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time


def main():
    home = home_plan()
    # print_home_plan(home)
    # living_room = get_room(home, "LivingRoom")
    # # print(living_room.sensors)
    # # print(living_room.actuators)
    # living_room_sensors = get_room_sensors(home, "LivingRoom")
    # for sensor in living_room_sensors:
    #     if sensor.sensor_type == "IndoorTemperature":
    #         sensor.turn_on()
    #         print(sensor.get_reading())
    #         sensor.turn_off()
    #         print(sensor.get_reading())

    # living_room_actuators = get_room_actuators(home, "LivingRoom")
    # for actuator in living_room_actuators:
    #     if actuator.actuator_type == "Light":
    #         actuator.turn_on()
    #         time.sleep(1)
    #         actuator.turn_off()

    # all_indoor_temps = get_all_sensors(home, "IndoorTemperature")
    # for sensor in all_indoor_temps:
    #     if sensor.status == "off":
    #         sensor.turn_on()
    #     print(sensor.get_reading())
    #     sensor.turn_off()

    # all_lights = get_all_actuators(home, "Light")
    # for light in all_lights:
    #     light.turn_on()
    #     time.sleep(1)
    #     light.turn_off()

    # for sensor in all_indoor_temps:
    #     sensor.turn_on()
    #     time.sleep(0.5)
    #     print(sensor.get_reading())
    #     sensor.turn_off()
    #     time.sleep(0.5)

    # all_music_players = get_all_actuators(home, "MusicPlayer")
    # for music_player in all_music_players:
    #     music_player.turn_on()
    #     music_player.play_music("jazz")
    #     time.sleep(1)
    #     music_player.turn_off()

    # all_cleaning_robots = get_all_actuators(home, "CleaningRobot")
    # for robot in all_cleaning_robots:
    #     robot.turn_on()
    #     robot.daily_routine()
    #     time.sleep(1)

    # all_notification_senders = get_all_actuators(home, "NotificationSender")
    # for sender in all_notification_senders:
    #     sender.turn_on()
    #     sender.notification_sender("test")
    #     sender.turn_off()

    # all_smart_tvs = get_all_actuators(home, "SmartTV")
    # for tv in all_smart_tvs:
    #     tv.turn_on()
    #     tv.play_channel("CCTV5")
    #     time.sleep(1)
    #     tv.turn_off()

    # all_heaters = get_all_actuators(home, "Heater")
    # for heater in all_heaters:
    #     heater.turn_on()
    #     heater.set_target_temperature(TEMP_HIGH)
    #     time.sleep(1)
    #     heater.turn_off()

    # all_acs = get_all_actuators(home, "AC")
    # for ac in all_acs:
    #     ac.turn_on()
    #     ac.set_target_temperature(TEMP_LOW)
    #     time.sleep(1)
    #     ac.turn_off()

    # all_coffee_machines = get_all_actuators(home, "CoffeeMachine")
    # for coffee_machine in all_coffee_machines:
    #     coffee_machine.turn_on()
    #     coffee_machine.make_coffee("Espresso")
    #     time.sleep(1)
    #     coffee_machine.turn_off()

    # all_doors = get_all_actuators(home, "Door")
    # for door in all_doors:
    #     door.unlock()
    #     time.sleep(1)
    #     door.lock()

    # all_curtains = get_all_actuators(home, "Curtain")
    # for curtain in all_curtains:
    #     curtain.turn_on()
    #     time.sleep(1)
    #     curtain.turn_off()

    # all_windows = get_all_actuators(home, "Window")
    # for window in all_windows:
    #     window.turn_on()
    #     time.sleep(1)
    #     window.turn_off()

    # all_smart_sockets = get_all_actuators(home, "SmartSocket")
    # for socket in all_smart_sockets:
    #     socket.turn_on()
    #     time.sleep(1)
    #     socket.turn_off()

    # all_humidifiers = get_all_actuators(home, "Humidifier")
    # for humidifier in all_humidifiers:
    #     humidifier.turn_on()
    #     humidifier.increase_humidity()
    #     time.sleep(1)
    #     humidifier.decrease_humidity()
    #     time.sleep(1)
    #     humidifier.turn_off()

    # all_lights = get_all_actuators(home, "Light")
    # for light in all_lights:
    #     light.turn_on()
    #     light.set_brightness_level("high")
    #     time.sleep(1)
    #     light.set_brightness_level("medium")
    #     time.sleep(1)
    #     light.set_brightness_level("low")
    #     time.sleep(1)
    #     light.turn_off()

    # all_indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    # all_heaters = get_all_actuators(home, "Heater")
    # all_acs = get_all_actuators(home, "AC")
    # for indoor_temp_sensor in all_indoor_temp_sensors:
    #     indoor_temp_sensor.turn_on()
    # for heater in all_heaters:
    #     heater.turn_on()
    #     heater.set_target_temperature(TEMP_HIGH)
    # for ac in all_acs:
    #     ac.turn_on()
    #     ac.set_target_temperature(TEMP_LOW)
    # while True:
    #     for indoor_temp_sensor in all_indoor_temp_sensors:
    #         current_temp = indoor_temp_sensor.get_reading()
    #         for heater in all_heaters:
    #             heater.adjust_temperature(current_temp)
    #         for ac in all_acs:
    #             ac.adjust_temperature(current_temp)
    #     time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    all_indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    all_humidity_sensors = get_all_sensors(home, "Humidity")
    all_light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    all_heaters = get_all_actuators(home, "Heater")
    all_acs = get_all_actuators(home, "AC")
    all_lights = get_all_actuators(home, "Light")
    all_curtains = get_all_actuators(home, "Curtain")
    all_cleaning_robots = get_all_actuators(home, "CleaningRobot")

    for sensor in all_indoor_temp_sensors:
        sensor.turn_on()
    for sensor in all_humidity_sensors:
        sensor.turn_on()
    for sensor in all_light_intensive_sensors:
        sensor.turn_on()
    for heater in all_heaters:
        heater.turn_on()
        heater.set_target_temperature(TEMP_HIGH)
    for ac in all_acs:
        ac.turn_on()
        ac.set_target_temperature(TEMP_LOW)
    for light in all_lights:
        light.turn_on()
    for cleaning_robot in all_cleaning_robots:
        cleaning_robot.turn_on()

    while True:
        for indoor_temp_sensor in all_indoor_temp_sensors:
            current_temp = indoor_temp_sensor.get_reading()
            for heater in all_heaters:
                heater.adjust_temperature(current_temp)
            for ac in all_acs:
                ac.adjust_temperature(current_temp)
        for humidity_sensor in all_humidity_sensors:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity < HUMIDITY_LOW:
                logger.info(f"Humidity in {humidity_sensor.room_name} is low. Increasing humidity.")
                print(f"Humidity in {humidity_sensor.room_name} is low. Increasing humidity.")
                for humidifier in all_humidifiers:
                    humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                logger.info(f"Humidity in {humidity_sensor.room_name} is high. Decreasing humidity.")
                print(f"Humidity in {humidity_sensor.room_name} is high. Decreasing humidity.")
                for humidifier in all_humidifiers:
                    humidifier.decrease_humidity()
        for light_intensive_sensor in all_light_intensive_sensors:
            current_light_intensity = light_intensive_sensor.get_reading()
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                logger.info(f"Light intensity in {light_intensive_sensor.room_name} is low. Turning on lights.")
                print(f"Light intensity in {light_intensive_sensor.room_name} is low. Turning on lights.")
                for light in all_lights:
                    light.turn_on()
                for curtain in all_curtains:
                    curtain.turn_on()
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                logger.info(f"Light intensity in {light_intensive_sensor.room_name} is high. Turning off lights.")
                print(f"Light intensity in {light_intensive_sensor.room_name} is high. Turning off lights.")
                for light in all_lights:
                    light.turn_off()
                for curtain in all_curtains:
                    curtain.turn_off()

        for cleaning_robot in all_cleaning_robots:
            if time.localtime().tm_hour == 8:
                cleaning_robot.daily_routine()

        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


if __name__ == "__main__":
    main()