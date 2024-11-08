from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time

def main():
    home = home_plan()
    print("Smart Home System is online! Please enter your command.")
    while True:
        command = input("\nPlease enter your command (e.g., 'get temperature LivingRoom', 'turn on light Kitchen'): ")
        # print(command.split())
        # Process the command
        try:
            command_words = command.split()

            if command_words[0].lower() == 'get':
                if command_words[1].lower() == 'temperature':
                    room_name = command_words[2]
                    sensors = get_room_sensors(home, room_name)
                    if sensors:
                        for sensor in sensors:
                            if sensor.sensor_type == "IndoorTemperature":
                                print(f"The current temperature in {room_name} is {sensor.get_reading()}°C.")
                                logger.info(
                                    f"The current temperature in {room_name} is {sensor.get_reading()}°C.")
                                break

                elif command_words[1].lower() == 'humidity':
                    room_name = command_words[2]
                    sensors = get_room_sensors(home, room_name)
                    if sensors:
                        for sensor in sensors:
                            if sensor.sensor_type == "Humidity":
                                print(f"The current humidity in {room_name} is {sensor.get_reading()}%")
                                logger.info(
                                    f"The current humidity in {room_name} is {sensor.get_reading()}%")
                                break

                elif command_words[1].lower() == 'light':
                    room_name = command_words[2]
                    sensors = get_room_sensors(home, room_name)
                    if sensors:
                        for sensor in sensors:
                            if sensor.sensor_type == "LightIntensive":
                                print(
                                    f"The current light intensity in {room_name} is {sensor.get_reading()}lux.")
                                logger.info(
                                    f"The current light intensity in {room_name} is {sensor.get_reading()}lux.")
                                break

            elif command_words[0].lower() == 'turn':
                if command_words[1].lower() == 'on':
                    device_type = command_words[2].lower()
                    room_name = command_words[3]
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if actuator.actuator_type == device_type:
                                actuator.turn_on()
                                break

                elif command_words[1].lower() == 'off':
                    device_type = command_words[2].lower()
                    room_name = command_words[3]
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if actuator.actuator_type == device_type:
                                actuator.turn_off()
                                break

            elif command_words[0].lower() == 'set':
                if command_words[1].lower() == 'temperature':
                    room_name = command_words[2]
                    target_temp = float(command_words[3])
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if isinstance(actuator, (Heater, AC)):
                                actuator.set_target_temperature(target_temp)
                                break

                elif command_words[1].lower() == 'brightness':
                    room_name = command_words[2]
                    brightness_level = command_words[3].lower()
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if isinstance(actuator, Light):
                                actuator.set_brightness_level(brightness_level)
                                break

            elif command_words[0].lower() == 'start':
                if command_words[1].lower() == 'cleaning':
                    room_name = command_words[2]
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if isinstance(actuator, CleaningRobot):
                                actuator.daily_routine()
                                break

            elif command_words[0].lower() == 'make':
                if command_words[1].lower() == 'coffee':
                    room_name = command_words[2]
                    coffee_type = command_words[3]
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if isinstance(actuator, CoffeeMachine):
                                actuator.make_coffee(coffee_type)
                                break

            elif command_words[0].lower() == 'play':
                if command_words[1].lower() == 'music':
                    room_name = command_words[2]
                    playlist = command_words[3]
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if isinstance(actuator, MusicPlayer):
                                actuator.play_music(playlist)
                                break

                elif command_words[1].lower() == 'channel':
                    room_name = command_words[2]
                    channel_name = command_words[3]
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if isinstance(actuator, SmartTV):
                                actuator.play_channel(channel_name)
                                break

            elif command_words[0].lower() == 'send':
                if command_words[1].lower() == 'notification':
                    room_name = command_words[2]
                    message = " ".join(command_words[3:])
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if isinstance(actuator, NotificationSender):
                                actuator.notification_sender(message)
                                break

            elif command_words[0].lower() == 'lock':
                if command_words[1].lower() == 'door':
                    room_name = command_words[2]
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if isinstance(actuator, Door):
                                actuator.lock()
                                break

            elif command_words[0].lower() == 'unlock':
                if command_words[1].lower() == 'door':
                    room_name = command_words[2]
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if isinstance(actuator, Door):
                                actuator.unlock()
                                break

            elif command_words[0].lower() == 'increase':
                if command_words[1].lower() == 'humidity':
                    room_name = command_words[2]
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if isinstance(actuator, Humidifier):
                                actuator.increase_humidity()
                                break

            elif command_words[0].lower() == 'decrease':
                if command_words[1].lower() == 'humidity':
                    room_name = command_words[2]
                    actuators = get_room_actuators(home, room_name)
                    if actuators:
                        for actuator in actuators:
                            if isinstance(actuator, Humidifier):
                                actuator.decrease_humidity()
                                break

            else:
                print(f"Invalid command: {command}.")
                logger.warning(f"Invalid command: {command}.")

        except Exception as e:
            print(f"Error: {e}")
            logger.error(f"Error: {e}")
            continue

        # Check sensor readings and trigger automatic actions
        check_sensor_readings(home)

        # Check for automatic actions
        check_automatic_actions(home)

def check_sensor_readings(home):
    # Check temperature sensors
    for sensor in get_all_sensors(home, "IndoorTemperature"):
        temperature = sensor.get_reading()
        room_name = sensor.room_name
        if temperature is not None:
            if temperature < TEMP_LOW:
                print(f"The temperature in {room_name} is too low. Turning on the heater.")
                logger.info(f"The temperature in {room_name} is too low. Turning on the heater.")
                actuators = get_room_actuators(home, room_name)
                for actuator in actuators:
                    if isinstance(actuator, Heater):
                        actuator.turn_on()
                        break
            elif temperature > TEMP_HIGH:
                print(f"The temperature in {room_name} is too high. Turning on the AC.")
                logger.info(f"The temperature in {room_name} is too high. Turning on the AC.")
                actuators = get_room_actuators(home, room_name)
                for actuator in actuators:
                    if isinstance(actuator, AC):
                        actuator.turn_on()
                        break

    # Check humidity sensors
    for sensor in get_all_sensors(home, "Humidity"):
        humidity = sensor.get_reading()
        room_name = sensor.room_name
        if humidity is not None:
            if humidity < HUMIDITY_LOW:
                print(f"The humidity in {room_name} is too low. Turning on the humidifier.")
                logger.info(f"The humidity in {room_name} is too low. Turning on the humidifier.")
                actuators = get_room_actuators(home, room_name)
                for actuator in actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.increase_humidity()
                        break
            elif humidity > HUMIDITY_HIGH:
                print(f"The humidity in {room_name} is too high. Turning on the dehumidifier.")
                logger.info(f"The humidity in {room_name} is too high. Turning on the dehumidifier.")
                actuators = get_room_actuators(home, room_name)
                for actuator in actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.decrease_humidity()
                        break

    # Check light intensity sensors
    for sensor in get_all_sensors(home, "LightIntensive"):
        light_intensity = sensor.get_reading()
        room_name = sensor.room_name
        if light_intensity is not None:
            if light_intensity < LIGHT_INTENSITY_LOW:
                print(f"The light intensity in {room_name} is too low. Turning on the lights.")
                logger.info(f"The light intensity in {room_name} is too low. Turning on the lights.")
                actuators = get_room_actuators(home, room_name)
                for actuator in actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_on()
                        break
            elif light_intensity > LIGHT_INTENSITY_HIGH:
                print(f"The light intensity in {room_name} is too high. Turning off the lights.")
                logger.info(f"The light intensity in {room_name} is too high. Turning off the lights.")
                actuators = get_room_actuators(home, room_name)
                for actuator in actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_off()
                        break

def check_automatic_actions(home):
    # Check if the cleaning robot needs to start its daily routine
    for cleaning_robot in get_all_actuators(home, "CleaningRobot"):
        if cleaning_robot.status == "off":
            print(f"{cleaning_robot.id} is ready to start daily cleaning routine")
            logger.info(f"{cleaning_robot.id} is ready to start daily cleaning routine")
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

    # Check if the windows need to be opened or closed based on temperature
    for room in home:
        temperature_sensors = [sensor for sensor in room.sensors if isinstance(sensor, Sensor) and sensor.sensor_type == "IndoorTemperature"]
        if temperature_sensors:
            temperature = temperature_sensors[0].get_reading()
            if temperature is not None:
                windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
                for window in windows:
                    if temperature < TEMP_LOW:
                        print(f"The temperature in {room.name} is too low. Closing the windows.")
                        logger.info(f"The temperature in {room.name} is too low. Closing the windows.")
                        window.turn_off()
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                    elif temperature > TEMP_HIGH:
                        print(f"The temperature in {room.name} is too high. Opening the windows.")
                        logger.info(f"The temperature in {room.name} is too high. Opening the windows.")
                        window.turn_on()
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    # Check if the curtains need to be opened or closed based on light intensity
    for room in home:
        light_intensity_sensors = [sensor for sensor in room.sensors if isinstance(sensor, Sensor) and sensor.sensor_type == "LightIntensive"]
        if light_intensity_sensors:
            light_intensity = light_intensity_sensors[0].get_reading()
            if light_intensity is not None:
                curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
                for curtain in curtains:
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        print(f"The light intensity in {room.name} is too low. Opening the curtains.")
                        logger.info(f"The light intensity in {room.name} is too low. Opening the curtains.")
                        curtain.turn_on()
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                        print(f"The light intensity in {room.name} is too high. Closing the curtains.")
                        logger.info(f"The light intensity in {room.name} is too high. Closing the curtains.")
                        curtain.turn_off()
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()