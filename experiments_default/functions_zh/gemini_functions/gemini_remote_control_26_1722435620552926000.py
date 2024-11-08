from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_actuators, \
    get_all_sensors
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import Heater, AC, CoffeeMachine, Light, SmartTV, CleaningRobot, NotificationSender, MusicPlayer, \
    Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

# Create the home plan
home = home_plan()


def main():
    while True:
        command = input("Enter a command (e.g., 'turn on light in LivingRoom'): ")
        words = command.split()

        if len(words) < 3:
            print("Invalid command. Please try again.")
            continue

        action = words[0].lower()
        device_type = words[1].lower()
        room_name = words[2]

        # Check if room exists
        room = get_room(home, room_name)
        if room is None:
            continue

        # Handle turning on/off devices
        if action == "turn" and (words[1] == "on" or words[1] == "off"):
            if words[1] == "on":
                turn_on_device(room, device_type)
            else:
                turn_off_device(room, device_type)
        # Handle brightness level
        elif action == "set" and device_type == "light":
            brightness_level = words[3].lower()
            set_brightness_level(room, brightness_level)
        # Handle temperature control
        elif action == "set" and (device_type == "heater" or device_type == "ac"):
            target_temperature = float(words[3])
            set_target_temperature(room, device_type, target_temperature)
        # Handle coffee machine
        elif action == "make" and device_type == "coffee":
            coffee_type = words[3].lower()
            make_coffee(room, coffee_type)
        # Handle music player
        elif action == "play" and device_type == "music":
            playlist = words[3].lower()
            play_music(room, playlist)
        # Handle TV
        elif action == "play" and device_type == "tv":
            channel = words[3]
            play_channel(room, channel)
        # Handle cleaning robot
        elif action == "clean" and device_type == "robot":
            start_daily_cleaning(room)
        # Handle notification
        elif action == "send" and device_type == "notification":
            message = " ".join(words[3:])
            send_notification(room, message)
        # Handle humidifier
        elif action == "increase" and device_type == "humidity":
            increase_humidity(room)
        elif action == "decrease" and device_type == "humidity":
            decrease_humidity(room)
        # Handle other commands
        else:
            print("Invalid command. Please try again.")

        # Automatically handle sensor readings
        handle_sensor_readings(room)


def turn_on_device(room, device_type):
    if device_type == "light":
        for light in get_room_actuators(room, "Light"):
            light.turn_on()
    elif device_type == "heater":
        for heater in get_room_actuators(room, "Heater"):
            heater.turn_on()
    elif device_type == "ac":
        for ac in get_room_actuators(room, "AC"):
            ac.turn_on()
    elif device_type == "coffee":
        for coffee_machine in get_room_actuators(room, "CoffeeMachine"):
            coffee_machine.turn_on()
    elif device_type == "music":
        for music_player in get_room_actuators(room, "MusicPlayer"):
            music_player.turn_on()
    elif device_type == "tv":
        for tv in get_room_actuators(room, "SmartTV"):
            tv.turn_on()
    elif device_type == "robot":
        for cleaning_robot in get_room_actuators(room, "CleaningRobot"):
            cleaning_robot.turn_on()
    elif device_type == "notification":
        for notification_sender in get_room_actuators(room, "NotificationSender"):
            notification_sender.turn_on()
    elif device_type == "humidity":
        for humidifier in get_room_actuators(room, "Humidifier"):
            humidifier.turn_on()
    else:
        print(f"Invalid device type: {device_type}")
        logger.error(f"Invalid device type: {device_type}")


def turn_off_device(room, device_type):
    if device_type == "light":
        for light in get_room_actuators(room, "Light"):
            light.turn_off()
    elif device_type == "heater":
        for heater in get_room_actuators(room, "Heater"):
            heater.turn_off()
    elif device_type == "ac":
        for ac in get_room_actuators(room, "AC"):
            ac.turn_off()
    elif device_type == "coffee":
        for coffee_machine in get_room_actuators(room, "CoffeeMachine"):
            coffee_machine.turn_off()
    elif device_type == "music":
        for music_player in get_room_actuators(room, "MusicPlayer"):
            music_player.turn_off()
    elif device_type == "tv":
        for tv in get_room_actuators(room, "SmartTV"):
            tv.turn_off()
    elif device_type == "robot":
        for cleaning_robot in get_room_actuators(room, "CleaningRobot"):
            cleaning_robot.turn_off()
    elif device_type == "notification":
        for notification_sender in get_room_actuators(room, "NotificationSender"):
            notification_sender.turn_off()
    elif device_type == "humidity":
        for humidifier in get_room_actuators(room, "Humidifier"):
            humidifier.turn_off()
    else:
        print(f"Invalid device type: {device_type}")
        logger.error(f"Invalid device type: {device_type}")


def set_brightness_level(room, brightness_level):
    for light in get_room_actuators(room, "Light"):
        light.set_brightness_level(brightness_level)


def set_target_temperature(room, device_type, target_temperature):
    if device_type == "heater":
        for heater in get_room_actuators(room, "Heater"):
            heater.set_target_temperature(target_temperature)
    elif device_type == "ac":
        for ac in get_room_actuators(room, "AC"):
            ac.set_target_temperature(target_temperature)
    else:
        print(f"Invalid device type: {device_type}")
        logger.error(f"Invalid device type: {device_type}")


def make_coffee(room, coffee_type):
    for coffee_machine in get_room_actuators(room, "CoffeeMachine"):
        coffee_machine.make_coffee(coffee_type)


def play_music(room, playlist):
    for music_player in get_room_actuators(room, "MusicPlayer"):
        music_player.play_music(playlist)


def play_channel(room, channel):
    for tv in get_room_actuators(room, "SmartTV"):
        tv.play_channel(channel)


def start_daily_cleaning(room):
    for cleaning_robot in get_room_actuators(room, "CleaningRobot"):
        cleaning_robot.daily_routine()


def send_notification(room, message):
    for notification_sender in get_room_actuators(room, "NotificationSender"):
        notification_sender.notification_sender(message)


def increase_humidity(room):
    for humidifier in get_room_actuators(room, "Humidifier"):
        humidifier.increase_humidity()


def decrease_humidity(room):
    for humidifier in get_room_actuators(room, "Humidifier"):
        humidifier.decrease_humidity()


def handle_sensor_readings(room):
    # Handle temperature sensor readings
    for temp_sensor in get_room_sensors(room, "IndoorTemperature"):
        current_temperature = temp_sensor.get_reading()
        if current_temperature is not None:
            for heater in get_room_actuators(room, "Heater"):
                heater.adjust_temperature(current_temperature)
            for ac in get_room_actuators(room, "AC"):
                ac.adjust_temperature(current_temperature)

    # Handle humidity sensor readings
    for humidity_sensor in get_room_sensors(room, "Humidity"):
        current_humidity = humidity_sensor.get_reading()
        if current_humidity is not None:
            if current_humidity < HUMIDITY_LOW:
                for humidifier in get_room_actuators(room, "Humidifier"):
                    humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                for humidifier in get_room_actuators(room, "Humidifier"):
                    humidifier.decrease_humidity()

    # Handle light intensity sensor readings
    for light_sensor in get_room_sensors(room, "LightIntensive"):
        current_light_intensity = light_sensor.get_reading()
        if current_light_intensity is not None:
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                for light in get_room_actuators(room, "Light"):
                    light.turn_on()
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                for light in get_room_actuators(room, "Light"):
                    light.turn_off()

    # Handle smoke sensor readings
    for smoke_sensor in get_room_sensors(room, "Smoke"):
        current_smoke_level = smoke_sensor.get_reading()
        if current_smoke_level is not None and current_smoke_level > 50:
            for notification_sender in get_all_actuators(home, "NotificationSender"):
                notification_sender.notification_sender(
                    f"Smoke detected in {room.name}! Please check the area immediately.")

    # Handle outdoor temperature sensor readings
    for outdoor_temp_sensor in get_all_sensors(home, "OutdoorTemperature"):
        current_outdoor_temperature = outdoor_temp_sensor.get_reading()
        if current_outdoor_temperature is not None and current_outdoor_temperature < TEMP_LOW:
            for heater in get_all_actuators(home, "Heater"):
                heater.turn_on()
        elif current_outdoor_temperature is not None and current_outdoor_temperature > TEMP_HIGH:
            for ac in get_all_actuators(home, "AC"):
                ac.turn_on()

# Start the main function
if __name__ == "__main__":
    main()