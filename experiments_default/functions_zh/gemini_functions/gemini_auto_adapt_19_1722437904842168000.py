from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW
from home.logger_config import logger
import time
import random


def check_temperature(home, room_name, sensor_type="IndoorTemperature", target_temp=None):
    """
    Check the temperature of the specified room and adjust the heater/AC if necessary.
    :param home: The home plan.
    :param room_name: The name of the room.
    :param sensor_type: The type of temperature sensor to use.
    :param target_temp: The target temperature.
    """
    room = get_room(home, room_name)
    if room is None:
        return

    sensors = get_room_sensors(home, room_name)
    if sensors is None:
        return

    for sensor in sensors:
        if sensor.sensor_type == sensor_type:
            current_temp = sensor.get_reading()
            if current_temp is not None:
                print(f"Current temperature in {room_name}: {current_temp}°C")
                logger.info(f"Current temperature in {room_name}: {current_temp}°C")
                # Adjust heater/AC based on target temperature or thresholds
                if target_temp is not None:
                    # Adjust based on target temperature
                    print(f"Target temperature in {room_name}: {target_temp}°C")
                    logger.info(f"Target temperature in {room_name}: {target_temp}°C")
                    for actuator in room.actuators:
                        if isinstance(actuator, Heater) or isinstance(actuator, AC):
                            actuator.set_target_temperature(target_temp)
                            actuator.adjust_temperature(current_temp)
                else:
                    # Adjust based on temperature thresholds
                    if current_temp < TEMP_LOW:
                        # Turn on heater
                        print(f"Turning on heater in {room_name}")
                        logger.info(f"Turning on heater in {room_name}")
                        for actuator in room.actuators:
                            if isinstance(actuator, Heater):
                                actuator.turn_on()
                                break
                    elif current_temp > TEMP_HIGH:
                        # Turn on AC
                        print(f"Turning on AC in {room_name}")
                        logger.info(f"Turning on AC in {room_name}")
                        for actuator in room.actuators:
                            if isinstance(actuator, AC):
                                actuator.turn_on()
                                break
                    else:
                        # Turn off heater/AC
                        print(f"Turning off heater/AC in {room_name}")
                        logger.info(f"Turning off heater/AC in {room_name}")
                        for actuator in room.actuators:
                            if isinstance(actuator, Heater) or isinstance(actuator, AC):
                                actuator.turn_off()
                                break
                time.sleep(1)  # Wait for a short period before checking again
                break  # Only check one temperature sensor per room


def check_humidity(home, room_name):
    """
    Check the humidity of the specified room and adjust the humidifier if necessary.
    :param home: The home plan.
    :param room_name: The name of the room.
    """
    room = get_room(home, room_name)
    if room is None:
        return

    sensors = get_room_sensors(home, room_name)
    if sensors is None:
        return

    for sensor in sensors:
        if sensor.sensor_type == "Humidity":
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                print(f"Current humidity in {room_name}: {current_humidity}%")
                logger.info(f"Current humidity in {room_name}: {current_humidity}%")
                # Adjust humidifier based on humidity thresholds
                if current_humidity < HUMIDITY_LOW:
                    # Turn on humidifier
                    print(f"Turning on humidifier in {room_name}")
                    logger.info(f"Turning on humidifier in {room_name}")
                    for actuator in room.actuators:
                        if isinstance(actuator, Humidifier):
                            actuator.increase_humidity()
                            break
                elif current_humidity > HUMIDITY_HIGH:
                    # Turn on dehumidifier (not implemented yet)
                    print(f"Turning on dehumidifier in {room_name}")
                    logger.info(f"Turning on dehumidifier in {room_name}")
                    # ... (Implement dehumidifier logic)
                    break
                else:
                    # Turn off humidifier
                    print(f"Turning off humidifier in {room_name}")
                    logger.info(f"Turning off humidifier in {room_name}")
                    for actuator in room.actuators:
                        if isinstance(actuator, Humidifier):
                            actuator.decrease_humidity()
                            break
                time.sleep(1)  # Wait for a short period before checking again
                break  # Only check one humidity sensor per room


def check_light_intensity(home, room_name):
    """
    Check the light intensity of the specified room and adjust the lights if necessary.
    :param home: The home plan.
    :param room_name: The name of the room.
    """
    room = get_room(home, room_name)
    if room is None:
        return

    sensors = get_room_sensors(home, room_name)
    if sensors is None:
        return

    for sensor in sensors:
        if sensor.sensor_type == "LightIntensive":
            current_intensity = sensor.get_reading()
            if current_intensity is not None:
                print(f"Current light intensity in {room_name}: {current_intensity} lux")
                logger.info(f"Current light intensity in {room_name}: {current_intensity} lux")
                # Adjust lights based on light intensity thresholds
                if current_intensity < LIGHT_INTENSITY_LOW:
                    # Turn on lights
                    print(f"Turning on lights in {room_name}")
                    logger.info(f"Turning on lights in {room_name}")
                    for actuator in room.actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_on()
                            break
                elif current_intensity > LIGHT_INTENSITY_HIGH:
                    # Turn off lights
                    print(f"Turning off lights in {room_name}")
                    logger.info(f"Turning off lights in {room_name}")
                    for actuator in room.actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_off()
                            break
                else:
                    # Adjust brightness based on intensity (not implemented yet)
                    print(f"Adjusting brightness in {room_name}")
                    logger.info(f"Adjusting brightness in {room_name}")
                    # ... (Implement brightness adjustment logic)
                    break
                time.sleep(1)  # Wait for a short period before checking again
                break  # Only check one light sensor per room


def check_smoke(home, room_name):
    """
    Check the smoke level in the specified room and send a notification if necessary.
    :param home: The home plan.
    :param room_name: The name of the room.
    """
    room = get_room(home, room_name)
    if room is None:
        return

    sensors = get_room_sensors(home, room_name)
    if sensors is None:
        return

    for sensor in sensors:
        if sensor.sensor_type == "Smoke":
            smoke_level = sensor.get_reading()
            if smoke_level is not None:
                print(f"Current smoke level in {room_name}: {smoke_level}%")
                logger.info(f"Current smoke level in {room_name}: {smoke_level}%")
                # Send notification if smoke level is high
                if smoke_level > 50:
                    print(f"Sending smoke alarm notification for {room_name}")
                    logger.warning(f"Sending smoke alarm notification for {room_name}")
                    for actuator in room.actuators:
                        if isinstance(actuator, NotificationSender):
                            actuator.notification_sender(
                                f"Smoke alarm triggered in {room_name}. Please evacuate immediately!")
                            break
                time.sleep(1)  # Wait for a short period before checking again
                break  # Only check one smoke sensor per room


def check_outdoor_temperature(home):
    """
    Check the outdoor temperature and send a notification if it's too hot or too cold.
    :param home: The home plan.
    """
    all_sensors = get_all_sensors(home, "OutdoorTemperature")
    if all_sensors is not None:
        for sensor in all_sensors:
            outdoor_temp = sensor.get_reading()
            if outdoor_temp is not None:
                print(f"Current outdoor temperature: {outdoor_temp}°C")
                logger.info(f"Current outdoor temperature: {outdoor_temp}°C")
                # Send notification if temperature is too hot or too cold
                if outdoor_temp > 35:
                    print(f"Sending hot weather notification")
                    logger.info(f"Sending hot weather notification")
                    for actuator in sensor.room.actuators:
                        if isinstance(actuator, NotificationSender):
                            actuator.notification_sender(f"It's very hot outside! Stay hydrated!")
                            break
                elif outdoor_temp < 0:
                    print(f"Sending cold weather notification")
                    logger.info(f"Sending cold weather notification")
                    for actuator in sensor.room.actuators:
                        if isinstance(actuator, NotificationSender):
                            actuator.notification_sender(f"It's very cold outside! Dress warmly!")
                            break
                time.sleep(1)  # Wait for a short period before checking again
                break  # Only check one outdoor temperature sensor


def main():
    """
    The main function of the smart home system.
    """
    home = home_plan()

    while True:
        # Check temperature in each room
        check_temperature(home, "LivingRoom")
        check_temperature(home, "Bedroom")
        check_temperature(home, "Kitchen")
        check_temperature(home, "Bathroom")

        # Check humidity in each room
        check_humidity(home, "LivingRoom")
        check_humidity(home, "Bedroom")
        check_humidity(home, "Kitchen")
        check_humidity(home, "Bathroom")

        # Check light intensity in each room
        check_light_intensity(home, "LivingRoom")
        check_light_intensity(home, "Bedroom")
        check_light_intensity(home, "Kitchen")
        check_light_intensity(home, "Bathroom")

        # Check smoke level in the kitchen
        check_smoke(home, "Kitchen")

        # Check outdoor temperature
        check_outdoor_temperature(home)

        # Example of controlling actuators based on conditions
        # ... (Add your own logic here)

        # Wait for a while before checking again
        time.sleep(random.randint(1, 5))  # Adjust the sleep time as needed


if __name__ == "__main__":
    main()