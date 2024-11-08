import time
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import Heater, AC, CoffeeMachine, Light, Curtain, MusicPlayer, SmartTV, CleaningRobot, NotificationSender, \
    SmartSocket, Humidifier
from home.logger_config import logger


def turn_on_light(home, room_name):
    room = get_room(home, room_name)
    lights = get_room_actuators(home, room_name)
    if lights:
        for light in lights:
            if light.actuator_type == 'Light':
                if light.status == "off":
                    light.turn_on()
                    print(f"Turn on light in {room_name}!")
                    logger.info(f"Turn on light in {room_name}!")
                    return True
                else:
                    print(f"Light in {room_name} is already on!")
                    logger.info(f"Light in {room_name} is already on!")
                    return False
    else:
        print(f"No light found in {room_name}!")
        logger.warning(f"No light found in {room_name}!")
        return False


def turn_off_light(home, room_name):
    room = get_room(home, room_name)
    lights = get_room_actuators(home, room_name)
    if lights:
        for light in lights:
            if light.actuator_type == 'Light':
                if light.status == "on":
                    light.turn_off()
                    print(f"Turn off light in {room_name}!")
                    logger.info(f"Turn off light in {room_name}!")
                    return True
                else:
                    print(f"Light in {room_name} is already off!")
                    logger.info(f"Light in {room_name} is already off!")
                    return False
    else:
        print(f"No light found in {room_name}!")
        logger.warning(f"No light found in {room_name}!")
        return False


def set_light_brightness(home, room_name, brightness_level):
    room = get_room(home, room_name)
    lights = get_room_actuators(home, room_name)
    if lights:
        for light in lights:
            if light.actuator_type == 'Light':
                light.set_brightness_level(brightness_level)
                print(f"Set brightness level of the light in {room_name} to {brightness_level}!")
                logger.info(f"Set brightness level of the light in {room_name} to {brightness_level}!")
                return True
    else:
        print(f"No light found in {room_name}!")
        logger.warning(f"No light found in {room_name}!")
        return False


def turn_on_ac(home, room_name):
    room = get_room(home, room_name)
    acs = get_room_actuators(home, room_name)
    if acs:
        for ac in acs:
            if ac.actuator_type == 'AC':
                if ac.status == "off":
                    ac.turn_on()
                    print(f"Turn on AC in {room_name}!")
                    logger.info(f"Turn on AC in {room_name}!")
                    return True
                else:
                    print(f"AC in {room_name} is already on!")
                    logger.info(f"AC in {room_name} is already on!")
                    return False
    else:
        print(f"No AC found in {room_name}!")
        logger.warning(f"No AC found in {room_name}!")
        return False


def turn_off_ac(home, room_name):
    room = get_room(home, room_name)
    acs = get_room_actuators(home, room_name)
    if acs:
        for ac in acs:
            if ac.actuator_type == 'AC':
                if ac.status == "on":
                    ac.turn_off()
                    print(f"Turn off AC in {room_name}!")
                    logger.info(f"Turn off AC in {room_name}!")
                    return True
                else:
                    print(f"AC in {room_name} is already off!")
                    logger.info(f"AC in {room_name} is already off!")
                    return False
    else:
        print(f"No AC found in {room_name}!")
        logger.warning(f"No AC found in {room_name}!")
        return False


def set_ac_temperature(home, room_name, target_temperature):
    room = get_room(home, room_name)
    acs = get_room_actuators(home, room_name)
    if acs:
        for ac in acs:
            if ac.actuator_type == 'AC':
                ac.set_target_temperature(target_temperature)
                print(f"Set AC target temperature in {room_name} to {target_temperature} degrees!")
                logger.info(f"Set AC target temperature in {room_name} to {target_temperature} degrees!")
                return True
    else:
        print(f"No AC found in {room_name}!")
        logger.warning(f"No AC found in {room_name}!")
        return False


def turn_on_heater(home, room_name):
    room = get_room(home, room_name)
    heaters = get_room_actuators(home, room_name)
    if heaters:
        for heater in heaters:
            if heater.actuator_type == 'Heater':
                if heater.status == "off":
                    heater.turn_on()
                    print(f"Turn on heater in {room_name}!")
                    logger.info(f"Turn on heater in {room_name}!")
                    return True
                else:
                    print(f"Heater in {room_name} is already on!")
                    logger.info(f"Heater in {room_name} is already on!")
                    return False
    else:
        print(f"No heater found in {room_name}!")
        logger.warning(f"No heater found in {room_name}!")
        return False


def turn_off_heater(home, room_name):
    room = get_room(home, room_name)
    heaters = get_room_actuators(home, room_name)
    if heaters:
        for heater in heaters:
            if heater.actuator_type == 'Heater':
                if heater.status == "on":
                    heater.turn_off()
                    print(f"Turn off heater in {room_name}!")
                    logger.info(f"Turn off heater in {room_name}!")
                    return True
                else:
                    print(f"Heater in {room_name} is already off!")
                    logger.info(f"Heater in {room_name} is already off!")
                    return False
    else:
        print(f"No heater found in {room_name}!")
        logger.warning(f"No heater found in {room_name}!")
        return False


def set_heater_temperature(home, room_name, target_temperature):
    room = get_room(home, room_name)
    heaters = get_room_actuators(home, room_name)
    if heaters:
        for heater in heaters:
            if heater.actuator_type == 'Heater':
                heater.set_target_temperature(target_temperature)
                print(f"Set heater target temperature in {room_name} to {target_temperature} degrees!")
                logger.info(f"Set heater target temperature in {room_name} to {target_temperature} degrees!")
                return True
    else:
        print(f"No heater found in {room_name}!")
        logger.warning(f"No heater found in {room_name}!")
        return False


def turn_on_coffee_machine(home, room_name):
    room = get_room(home, room_name)
    coffee_machines = get_room_actuators(home, room_name)
    if coffee_machines:
        for coffee_machine in coffee_machines:
            if coffee_machine.actuator_type == 'CoffeeMachine':
                if coffee_machine.status == "off":
                    coffee_machine.turn_on()
                    print(f"Turn on coffee machine in {room_name}!")
                    logger.info(f"Turn on coffee machine in {room_name}!")
                    return True
                else:
                    print(f"Coffee machine in {room_name} is already on!")
                    logger.info(f"Coffee machine in {room_name} is already on!")
                    return False
    else:
        print(f"No coffee machine found in {room_name}!")
        logger.warning(f"No coffee machine found in {room_name}!")
        return False


def turn_off_coffee_machine(home, room_name):
    room = get_room(home, room_name)
    coffee_machines = get_room_actuators(home, room_name)
    if coffee_machines:
        for coffee_machine in coffee_machines:
            if coffee_machine.actuator_type == 'CoffeeMachine':
                if coffee_machine.status == "on":
                    coffee_machine.turn_off()
                    print(f"Turn off coffee machine in {room_name}!")
                    logger.info(f"Turn off coffee machine in {room_name}!")
                    return True
                else:
                    print(f"Coffee machine in {room_name} is already off!")
                    logger.info(f"Coffee machine in {room_name} is already off!")
                    return False
    else:
        print(f"No coffee machine found in {room_name}!")
        logger.warning(f"No coffee machine found in {room_name}!")
        return False


def make_coffee(home, room_name, coffee_type):
    room = get_room(home, room_name)
    coffee_machines = get_room_actuators(home, room_name)
    if coffee_machines:
        for coffee_machine in coffee_machines:
            if coffee_machine.actuator_type == 'CoffeeMachine':
                coffee_machine.make_coffee(coffee_type)
                print(f"Making {coffee_type} coffee in {room_name}!")
                logger.info(f"Making {coffee_type} coffee in {room_name}!")
                return True
    else:
        print(f"No coffee machine found in {room_name}!")
        logger.warning(f"No coffee machine found in {room_name}!")
        return False


def turn_on_music_player(home, room_name):
    room = get_room(home, room_name)
    music_players = get_room_actuators(home, room_name)
    if music_players:
        for music_player in music_players:
            if music_player.actuator_type == 'MusicPlayer':
                if music_player.status == "off":
                    music_player.turn_on()
                    print(f"Turn on music player in {room_name}!")
                    logger.info(f"Turn on music player in {room_name}!")
                    return True
                else:
                    print(f"Music player in {room_name} is already on!")
                    logger.info(f"Music player in {room_name} is already on!")
                    return False
    else:
        print(f"No music player found in {room_name}!")
        logger.warning(f"No music player found in {room_name}!")
        return False


def turn_off_music_player(home, room_name):
    room = get_room(home, room_name)
    music_players = get_room_actuators(home, room_name)
    if music_players:
        for music_player in music_players:
            if music_player.actuator_type == 'MusicPlayer':
                if music_player.status == "on":
                    music_player.turn_off()
                    print(f"Turn off music player in {room_name}!")
                    logger.info(f"Turn off music player in {room_name}!")
                    return True
                else:
                    print(f"Music player in {room_name} is already off!")
                    logger.info(f"Music player in {room_name} is already off!")
                    return False
    else:
        print(f"No music player found in {room_name}!")
        logger.warning(f"No music player found in {room_name}!")
        return False


def play_music(home, room_name, playlist):
    room = get_room(home, room_name)
    music_players = get_room_actuators(home, room_name)
    if music_players:
        for music_player in music_players:
            if music_player.actuator_type == 'MusicPlayer':
                music_player.play_music(playlist)
                print(f"Playing {playlist} on music player in {room_name}!")
                logger.info(f"Playing {playlist} on music player in {room_name}!")
                return True
    else:
        print(f"No music player found in {room_name}!")
        logger.warning(f"No music player found in {room_name}!")
        return False


def turn_on_tv(home, room_name):
    room = get_room(home, room_name)
    tvs = get_room_actuators(home, room_name)
    if tvs:
        for tv in tvs:
            if tv.actuator_type == 'SmartTV':
                if tv.status == "off":
                    tv.turn_on()
                    print(f"Turn on TV in {room_name}!")
                    logger.info(f"Turn on TV in {room_name}!")
                    return True
                else:
                    print(f"TV in {room_name} is already on!")
                    logger.info(f"TV in {room_name} is already on!")
                    return False
    else:
        print(f"No TV found in {room_name}!")
        logger.warning(f"No TV found in {room_name}!")
        return False


def turn_off_tv(home, room_name):
    room = get_room(home, room_name)
    tvs = get_room_actuators(home, room_name)
    if tvs:
        for tv in tvs:
            if tv.actuator_type == 'SmartTV':
                if tv.status == "on":
                    tv.turn_off()
                    print(f"Turn off TV in {room_name}!")
                    logger.info(f"Turn off TV in {room_name}!")
                    return True
                else:
                    print(f"TV in {room_name} is already off!")
                    logger.info(f"TV in {room_name} is already off!")
                    return False
    else:
        print(f"No TV found in {room_name}!")
        logger.warning(f"No TV found in {room_name}!")
        return False


def play_channel(home, room_name, channel_name):
    room = get_room(home, room_name)
    tvs = get_room_actuators(home, room_name)
    if tvs:
        for tv in tvs:
            if tv.actuator_type == 'SmartTV':
                tv.play_channel(channel_name)
                print(f"Playing {channel_name} on TV in {room_name}!")
                logger.info(f"Playing {channel_name} on TV in {room_name}!")
                return True
    else:
        print(f"No TV found in {room_name}!")
        logger.warning(f"No TV found in {room_name}!")
        return False


def turn_on_cleaning_robot(home, room_name):
    room = get_room(home, room_name)
    cleaning_robots = get_room_actuators(home, room_name)
    if cleaning_robots:
        for cleaning_robot in cleaning_robots:
            if cleaning_robot.actuator_type == 'CleaningRobot':
                if cleaning_robot.status == "off":
                    cleaning_robot.turn_on()
                    print(f"Turn on cleaning robot in {room_name}!")
                    logger.info(f"Turn on cleaning robot in {room_name}!")
                    return True
                else:
                    print(f"Cleaning robot in {room_name} is already on!")
                    logger.info(f"Cleaning robot in {room_name} is already on!")
                    return False
    else:
        print(f"No cleaning robot found in {room_name}!")
        logger.warning(f"No cleaning robot found in {room_name}!")
        return False


def turn_off_cleaning_robot(home, room_name):
    room = get_room(home, room_name)
    cleaning_robots = get_room_actuators(home, room_name)
    if cleaning_robots:
        for cleaning_robot in cleaning_robots:
            if cleaning_robot.actuator_type == 'CleaningRobot':
                if cleaning_robot.status == "on":
                    cleaning_robot.turn_off()
                    print(f"Turn off cleaning robot in {room_name}!")
                    logger.info(f"Turn off cleaning robot in {room_name}!")
                    return True
                else:
                    print(f"Cleaning robot in {room_name} is already off!")
                    logger.info(f"Cleaning robot in {room_name} is already off!")
                    return False
    else:
        print(f"No cleaning robot found in {room_name}!")
        logger.warning(f"No cleaning robot found in {room_name}!")
        return False


def start_daily_cleaning_routine(home, room_name):
    room = get_room(home, room_name)
    cleaning_robots = get_room_actuators(home, room_name)
    if cleaning_robots:
        for cleaning_robot in cleaning_robots:
            if cleaning_robot.actuator_type == 'CleaningRobot':
                cleaning_robot.daily_routine()
                print(f"Start daily cleaning routine in {room_name}!")
                logger.info(f"Start daily cleaning routine in {room_name}!")
                return True
    else:
        print(f"No cleaning robot found in {room_name}!")
        logger.warning(f"No cleaning robot found in {room_name}!")
        return False


def turn_on_notification_sender(home, room_name):
    room = get_room(home, room_name)
    notification_senders = get_room_actuators(home, room_name)
    if notification_senders:
        for notification_sender in notification_senders:
            if notification_sender.actuator_type == 'NotificationSender':
                if notification_sender.status == "off":
                    notification_sender.turn_on()
                    print(f"Turn on notification sender in {room_name}!")
                    logger.info(f"Turn on notification sender in {room_name}!")
                    return True
                else:
                    print(f"Notification sender in {room_name} is already on!")
                    logger.info(f"Notification sender in {room_name} is already on!")
                    return False
    else:
        print(f"No notification sender found in {room_name}!")
        logger.warning(f"No notification sender found in {room_name}!")
        return False


def turn_off_notification_sender(home, room_name):
    room = get_room(home, room_name)
    notification_senders = get_room_actuators(home, room_name)
    if notification_senders:
        for notification_sender in notification_senders:
            if notification_sender.actuator_type == 'NotificationSender':
                if notification_sender.status == "on":
                    notification_sender.turn_off()
                    print(f"Turn off notification sender in {room_name}!")
                    logger.info(f"Turn off notification sender in {room_name}!")
                    return True
                else:
                    print(f"Notification sender in {room_name} is already off!")
                    logger.info(f"Notification sender in {room_name} is already off!")
                    return False
    else:
        print(f"No notification sender found in {room_name}!")
        logger.warning(f"No notification sender found in {room_name}!")
        return False


def send_notification(home, room_name, message):
    room = get_room(home, room_name)
    notification_senders = get_room_actuators(home, room_name)
    if notification_senders:
        for notification_sender in notification_senders:
            if notification_sender.actuator_type == 'NotificationSender':
                notification_sender.notification_sender(message)
                print(f"Sent notification: {message} from {room_name}!")
                logger.info(f"Sent notification: {message} from {room_name}!")
                return True
    else:
        print(f"No notification sender found in {room_name}!")
        logger.warning(f"No notification sender found in {room_name}!")
        return False


def turn_on_curtain(home, room_name):
    room = get_room(home, room_name)
    curtains = get_room_actuators(home, room_name)
    if curtains:
        for curtain in curtains:
            if curtain.actuator_type == 'Curtain':
                if curtain.status == "off":
                    curtain.turn_on()
                    print(f"Turn on curtain in {room_name}!")
                    logger.info(f"Turn on curtain in {room_name}!")
                    return True
                else:
                    print(f"Curtain in {room_name} is already on!")
                    logger.info(f"Curtain in {room_name} is already on!")
                    return False
    else:
        print(f"No curtain found in {room_name}!")
        logger.warning(f"No curtain found in {room_name}!")
        return False


def turn_off_curtain(home, room_name):
    room = get_room(home, room_name)
    curtains = get_room_actuators(home, room_name)
    if curtains:
        for curtain in curtains:
            if curtain.actuator_type == 'Curtain':
                if curtain.status == "on":
                    curtain.turn_off()
                    print(f"Turn off curtain in {room_name}!")
                    logger.info(f"Turn off curtain in {room_name}!")
                    return True
                else:
                    print(f"Curtain in {room_name} is already off!")
                    logger.info(f"Curtain in {room_name} is already off!")
                    return False
    else:
        print(f"No curtain found in {room_name}!")
        logger.warning(f"No curtain found in {room_name}!")
        return False


def turn_on_window(home, room_name):
    room = get_room(home, room_name)
    windows = get_room_actuators(home, room_name)
    if windows:
        for window in windows:
            if window.actuator_type == 'Window':
                if window.status == "off":
                    window.turn_on()
                    print(f"Turn on window in {room_name}!")
                    logger.info(f"Turn on window in {room_name}!")
                    return True
                else:
                    print(f"Window in {room_name} is already on!")
                    logger.info(f"Window in {room_name} is already on!")
                    return False
    else:
        print(f"No window found in {room_name}!")
        logger.warning(f"No window found in {room_name}!")
        return False


def turn_off_window(home, room_name):
    room = get_room(home, room_name)
    windows = get_room_actuators(home, room_name)
    if windows:
        for window in windows:
            if window.actuator_type == 'Window':
                if window.status == "on":
                    window.turn_off()
                    print(f"Turn off window in {room_name}!")
                    logger.info(f"Turn off window in {room_name}!")
                    return True
                else:
                    print(f"Window in {room_name} is already off!")
                    logger.info(f"Window in {room_name} is already off!")
                    return False
    else:
        print(f"No window found in {room_name}!")
        logger.warning(f"No window found in {room_name}!")
        return False


def turn_on_door(home, room_name):
    room = get_room(home, room_name)
    doors = get_room_actuators(home, room_name)
    if doors:
        for door in doors:
            if door.actuator_type == 'Door':
                if door.status == "off":
                    door.turn_on()
                    print(f"Turn on door in {room_name}!")
                    logger.info(f"Turn on door in {room_name}!")
                    return True
                else:
                    print(f"Door in {room_name} is already on!")
                    logger.info(f"Door in {room_name} is already on!")
                    return False
    else:
        print(f"No door found in {room_name}!")
        logger.warning(f"No door found in {room_name}!")
        return False


def turn_off_door(home, room_name):
    room = get_room(home, room_name)
    doors = get_room_actuators(home, room_name)
    if doors:
        for door in doors:
            if door.actuator_type == 'Door':
                if door.status == "on":
                    door.turn_off()
                    print(f"Turn off door in {room_name}!")
                    logger.info(f"Turn off door in {room_name}!")
                    return True
                else:
                    print(f"Door in {room_name} is already off!")
                    logger.info(f"Door in {room_name} is already off!")
                    return False
    else:
        print(f"No door found in {room_name}!")
        logger.warning(f"No door found in {room_name}!")
        return False


def lock_door(home, room_name):
    room = get_room(home, room_name)
    doors = get_room_actuators(home, room_name)
    if doors:
        for door in doors:
            if door.actuator_type == 'Door':
                door.lock()
                print(f"Lock door in {room_name}!")
                logger.info(f"Lock door in {room_name}!")
                return True
    else:
        print(f"No door found in {room_name}!")
        logger.warning(f"No door found in {room_name}!")
        return False


def unlock_door(home, room_name):
    room = get_room(home, room_name)
    doors = get_room_actuators(home, room_name)
    if doors:
        for door in doors:
            if door.actuator_type == 'Door':
                door.unlock()
                print(f"Unlock door in {room_name}!")
                logger.info(f"Unlock door in {room_name}!")
                return True
    else:
        print(f"No door found in {room_name}!")
        logger.warning(f"No door found in {room_name}!")
        return False


def get_temperature(home, room_name):
    room = get_room(home, room_name)
    sensors = get_room_sensors(home, room_name)
    if sensors:
        for sensor in sensors:
            if sensor.sensor_type == 'IndoorTemperature':
                temperature = sensor.get_reading()
                print(f"Temperature in {room_name}: {temperature} degrees!")
                logger.info(f"Temperature in {room_name}: {temperature} degrees!")
                return temperature
    else:
        print(f"No temperature sensor found in {room_name}!")
        logger.warning(f"No temperature sensor found in {room_name}!")
        return None


def get_humidity(home, room_name):
    room = get_room(home, room_name)
    sensors = get_room_sensors(home, room_name)
    if sensors:
        for sensor in sensors:
            if sensor.sensor_type == 'Humidity':
                humidity = sensor.get_reading()
                print(f"Humidity in {room_name}: {humidity} %!")
                logger.info(f"Humidity in {room_name}: {humidity} %!")
                return humidity
    else:
        print(f"No humidity sensor found in {room_name}!")
        logger.warning(f"No humidity sensor found in {room_name}!")
        return None


def get_light_intensity(home, room_name):
    room = get_room(home, room_name)
    sensors = get_room_sensors(home, room_name)
    if sensors:
        for sensor in sensors:
            if sensor.sensor_type == 'LightIntensive':
                light_intensity = sensor.get_reading()
                print(f"Light intensity in {room_name}: {light_intensity} lux!")
                logger.info(f"Light intensity in {room_name}: {light_intensity} lux!")
                return light_intensity
    else:
        print(f"No light intensity sensor found in {room_name}!")
        logger.warning(f"No light intensity sensor found in {room_name}!")
        return None


def get_outdoor_temperature(home, room_name):
    room = get_room(home, room_name)
    sensors = get_room_sensors(home, room_name)
    if sensors:
        for sensor in sensors:
            if sensor.sensor_type == 'OutdoorTemperature':
                outdoor_temperature = sensor.get_reading()
                print(f"Outdoor temperature in {room_name}: {outdoor_temperature} degrees!")
                logger.info(f"Outdoor temperature in {room_name}: {outdoor_temperature} degrees!")
                return outdoor_temperature
    else:
        print(f"No outdoor temperature sensor found in {room_name}!")
        logger.warning(f"No outdoor temperature sensor found in {room_name}!")
        return None


def get_smoke_level(home, room_name):
    room = get_room(home, room_name)
    sensors = get_room_sensors(home, room_name)
    if sensors:
        for sensor in sensors:
            if sensor.sensor_type == 'Smoke':
                smoke_level = sensor.get_reading()
                print(f"Smoke level in {room_name}: {smoke_level} %!")
                logger.info(f"Smoke level in {room_name}: {smoke_level} %!")
                return smoke_level
    else:
        print(f"No smoke sensor found in {room_name}!")
        logger.warning(f"No smoke sensor found in {room_name}!")
        return None


def adjust_temperature(home, room_name):
    room = get_room(home, room_name)
    temperature = get_temperature(home, room_name)
    if temperature is not None:
        heaters = get_room_actuators(home, room_name)
        if heaters:
            for heater in heaters:
                if heater.actuator_type == 'Heater':
                    heater.adjust_temperature(temperature)
        acs = get_room_actuators(home, room_name)
        if acs:
            for ac in acs:
                if ac.actuator_type == 'AC':
                    ac.adjust_temperature(temperature)
    else:
        print(f"No temperature sensor found in {room_name}!")
        logger.warning(f"No temperature sensor found in {room_name}!")


def adjust_humidity(home, room_name):
    room = get_room(home, room_name)
    humidity = get_humidity(home, room_name)
    if humidity is not None:
        humidifiers = get_room_actuators(home, room_name)
        if humidifiers:
            for humidifier in humidifiers:
                if humidifier.actuator_type == 'Humidifier':
                    if humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()
    else:
        print(f"No humidity sensor found in {room_name}!")
        logger.warning(f"No humidity sensor found in {room_name}!")


def adjust_light_intensity(home, room_name):
    room = get_room(home, room_name)
    light_intensity = get_light_intensity(home, room_name)
    if light_intensity is not None:
        lights = get_room_actuators(home, room_name)
        if lights:
            for light in lights:
                if light.actuator_type == 'Light':
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level('high