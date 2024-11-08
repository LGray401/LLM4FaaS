from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Heater, AC, Light, Window, Curtain, MusicPlayer, CoffeeMachine, NotificationSender, CleaningRobot
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger
import time


def adjust_temperature(home, room_name, desired_temperature):
    room = get_room(home, room_name)
    if room is None:
        return

    temp_sensors = get_room_sensors(home, room_name)
    if temp_sensors is None:
        return

    temp_sensor = [sensor for sensor in temp_sensors if isinstance(sensor, IndoorTemperatureSensor)][0]
    current_temperature = temp_sensor.get_reading()

    heaters = get_room_actuators(home, room_name)
    if heaters is None:
        return

    heaters = [heater for heater in heaters if isinstance(heater, Heater)]
    acs = get_room_actuators(home, room_name)
    if acs is None:
        return

    acs = [ac for ac in acs if isinstance(ac, AC)]

    if current_temperature < desired_temperature:
        for heater in heaters:
            heater.turn_on()
            heater.set_target_temperature(desired_temperature)
        for ac in acs:
            ac.turn_off()
    elif current_temperature > desired_temperature:
        for ac in acs:
            ac.turn_on()
            ac.set_target_temperature(desired_temperature)
        for heater in heaters:
            heater.turn_off()
    else:
        for ac in acs:
            ac.turn_off()
        for heater in heaters:
            heater.turn_off()

    logger.info(
        f"Adjusted temperature in {room_name} to {desired_temperature}°C. Current temperature is {current_temperature}°C.")
    print(
        f"Adjusted temperature in {room_name} to {desired_temperature}°C. Current temperature is {current_temperature}°C.")


def adjust_humidity(home, room_name, desired_humidity):
    room = get_room(home, room_name)
    if room is None:
        return

    humidity_sensors = get_room_sensors(home, room_name)
    if humidity_sensors is None:
        return

    humidity_sensor = [sensor for sensor in humidity_sensors if isinstance(sensor, HumiditySensor)][0]
    current_humidity = humidity_sensor.get_reading()

    humidifiers = get_room_actuators(home, room_name)
    if humidifiers is None:
        return

    humidifiers = [humidifier for humidifier in humidifiers if isinstance(humidifier, Humidifier)]

    if current_humidity < desired_humidity:
        for humidifier in humidifiers:
            humidifier.increase_humidity()
    elif current_humidity > desired_humidity:
        for humidifier in humidifiers:
            humidifier.decrease_humidity()
    else:
        pass  # Already at desired humidity

    logger.info(
        f"Adjusted humidity in {room_name} to {desired_humidity}%. Current humidity is {current_humidity}%.")
    print(
        f"Adjusted humidity in {room_name} to {desired_humidity}%. Current humidity is {current_humidity}%.")


def adjust_light_intensity(home, room_name, desired_intensity, desired_brightness_level):
    room = get_room(home, room_name)
    if room is None:
        return

    light_intensity_sensors = get_room_sensors(home, room_name)
    if light_intensity_sensors is None:
        return

    light_intensity_sensor = [sensor for sensor in light_intensity_sensors if isinstance(sensor, LightIntensiveSensor)][0]
    current_intensity = light_intensity_sensor.get_reading()

    lights = get_room_actuators(home, room_name)
    if lights is None:
        return

    lights = [light for light in lights if isinstance(light, Light)]

    if current_intensity < desired_intensity:
        for light in lights:
            light.turn_on()
            light.set_brightness_level(desired_brightness_level)
    elif current_intensity > desired_intensity:
        for light in lights:
            light.turn_off()
    else:
        pass  # Already at desired light intensity

    logger.info(
        f"Adjusted light intensity in {room_name} to {desired_intensity} lux. Current light intensity is {current_intensity} lux.")
    print(
        f"Adjusted light intensity in {room_name} to {desired_intensity} lux. Current light intensity is {current_intensity} lux.")


def adjust_light_brightness(home, room_name, desired_brightness_level):
    room = get_room(home, room_name)
    if room is None:
        return

    lights = get_room_actuators(home, room_name)
    if lights is None:
        return

    lights = [light for light in lights if isinstance(light, Light)]

    for light in lights:
        light.set_brightness_level(desired_brightness_level)

    logger.info(f"Set the brightness level of the lights in {room_name} to {desired_brightness_level}.")
    print(f"Set the brightness level of the lights in {room_name} to {desired_brightness_level}.")


def play_music(home, room_name, playlist):
    room = get_room(home, room_name)
    if room is None:
        return

    music_players = get_room_actuators(home, room_name)
    if music_players is None:
        return

    music_players = [music_player for music_player in music_players if isinstance(music_player, MusicPlayer)]

    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music(playlist)

    logger.info(f"Playing {playlist} in {room_name}.")
    print(f"Playing {playlist} in {room_name}.")


def make_coffee(home, room_name, coffee_type):
    room = get_room(home, room_name)
    if room is None:
        return

    coffee_machines = get_room_actuators(home, room_name)
    if coffee_machines is None:
        return

    coffee_machines = [coffee_machine for coffee_machine in coffee_machines if isinstance(coffee_machine, CoffeeMachine)]

    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee(coffee_type)

    logger.info(f"Making {coffee_type} coffee in {room_name}.")
    print(f"Making {coffee_type} coffee in {room_name}.")


def send_notification(home, room_name, message):
    room = get_room(home, room_name)
    if room is None:
        return

    notification_senders = get_room_actuators(home, room_name)
    if notification_senders is None:
        return

    notification_senders = [
        notification_sender for notification_sender in notification_senders if isinstance(notification_sender, NotificationSender)
    ]

    for notification_sender in notification_senders:
        notification_sender.turn_on()
        notification_sender.notification_sender(message)

    logger.info(f"Sending notification: {message} in {room_name}.")
    print(f"Sending notification: {message} in {room_name}.")


def run_cleaning_robot(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    cleaning_robots = get_room_actuators(home, room_name)
    if cleaning_robots is None:
        return

    cleaning_robots = [
        cleaning_robot for cleaning_robot in cleaning_robots if isinstance(cleaning_robot, CleaningRobot)
    ]

    for cleaning_robot in cleaning_robots:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

    logger.info(f"Running cleaning robot in {room_name}.")
    print(f"Running cleaning robot in {room_name}.")


def open_window(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    windows = get_room_actuators(home, room_name)
    if windows is None:
        return

    windows = [window for window in windows if isinstance(window, Window)]

    for window in windows:
        window.turn_on()

    logger.info(f"Opening window in {room_name}.")
    print(f"Opening window in {room_name}.")


def close_window(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    windows = get_room_actuators(home, room_name)
    if windows is None:
        return

    windows = [window for window in windows if isinstance(window, Window)]

    for window in windows:
        window.turn_off()

    logger.info(f"Closing window in {room_name}.")
    print(f"Closing window in {room_name}.")


def open_curtain(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    curtains = get_room_actuators(home, room_name)
    if curtains is None:
        return

    curtains = [curtain for curtain in curtains if isinstance(curtain, Curtain)]

    for curtain in curtains:
        curtain.turn_on()

    logger.info(f"Opening curtain in {room_name}.")
    print(f"Opening curtain in {room_name}.")


def close_curtain(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    curtains = get_room_actuators(home, room_name)
    if curtains is None:
        return

    curtains = [curtain for curtain in curtains if isinstance(curtain, Curtain)]

    for curtain in curtains:
        curtain.turn_off()

    logger.info(f"Closing curtain in {room_name}.")
    print(f"Closing curtain in {room_name}.")


def main():
    home = home_plan()

    while True:
        # Example usage:
        adjust_temperature(home, "LivingRoom", 22)
        adjust_humidity(home, "LivingRoom", 45)
        adjust_light_intensity(home, "LivingRoom", 600, "medium")
        adjust_light_brightness(home, "LivingRoom", "high")
        play_music(home, "LivingRoom", "Jazz")
        make_coffee(home, "Kitchen", "Espresso")
        send_notification(home, "LivingRoom", "Dinner is ready!")
        run_cleaning_robot(home, "LivingRoom")
        open_window(home, "LivingRoom")
        close_window(home, "LivingRoom")
        open_curtain(home, "LivingRoom")
        close_curtain(home, "LivingRoom")

        time.sleep(5)  # Wait for 5 seconds before checking again


if __name__ == "__main__":
    main()