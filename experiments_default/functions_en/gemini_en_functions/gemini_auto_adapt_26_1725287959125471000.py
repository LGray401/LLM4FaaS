from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger


def control_temperature(home, room_name, target_temperature, sensor_type="IndoorTemperature"):
    """
    Controls the temperature of a room by turning on/off the heater or AC as needed.

    Args:
        home: The home plan object.
        room_name: The name of the room to control.
        target_temperature: The desired temperature in Celsius.
        sensor_type: The type of temperature sensor to use. Default is "IndoorTemperature".

    Returns:
        None
    """
    sensors = get_room_sensors(home, room_name)
    # print(sensors)
    for sensor in sensors:
        if sensor.sensor_type == sensor_type:
            current_temperature = sensor.get_reading()
            # print(f"current temperature is: {current_temperature}")
            if current_temperature is not None:
                actuators = get_room_actuators(home, room_name)
                # print(actuators)
                for actuator in actuators:
                    if actuator.actuator_type == "Heater":
                        actuator.set_target_temperature(target_temperature)
                        actuator.adjust_temperature(current_temperature)
                    elif actuator.actuator_type == "AC":
                        actuator.set_target_temperature(target_temperature)
                        actuator.adjust_temperature(current_temperature)
    logger.info(f"Successfully set target temperature in {room_name} to {target_temperature}")


def control_humidity(home, room_name, target_humidity):
    """
    Controls the humidity of a room by turning on/off the humidifier as needed.

    Args:
        home: The home plan object.
        room_name: The name of the room to control.
        target_humidity: The desired humidity percentage.

    Returns:
        None
    """
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == "Humidity":
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                actuators = get_room_actuators(home, room_name)
                for actuator in actuators:
                    if actuator.actuator_type == "Humidifier":
                        if current_humidity < target_humidity:
                            actuator.increase_humidity()
                        elif current_humidity > target_humidity:
                            actuator.decrease_humidity()
    logger.info(f"Successfully set target humidity in {room_name} to {target_humidity}%")


def control_light(home, room_name, light_level):
    """
    Controls the light intensity of a room.

    Args:
        home: The home plan object.
        room_name: The name of the room to control.
        light_level: The desired light intensity level ("low", "medium", or "high").

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            actuator.set_brightness_level(light_level)
    logger.info(f"Successfully set light level in {room_name} to {light_level.upper()}")


def keep_temperature_stable(home, room_name, target_temperature, sensor_type="IndoorTemperature"):
    """
    Keeps the temperature of a room stable by repeatedly checking and adjusting the temperature.

    Args:
        home: The home plan object.
        room_name: The name of the room to control.
        target_temperature: The desired temperature in Celsius.
        sensor_type: The type of temperature sensor to use. Default is "IndoorTemperature".

    Returns:
        None
    """
    while True:
        control_temperature(home, room_name, target_temperature, sensor_type)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait before checking again


def keep_humidity_stable(home, room_name, target_humidity):
    """
    Keeps the humidity of a room stable by repeatedly checking and adjusting the humidity.

    Args:
        home: The home plan object.
        room_name: The name of the room to control.
        target_humidity: The desired humidity percentage.

    Returns:
        None
    """
    while True:
        control_humidity(home, room_name, target_humidity)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait before checking again


def turn_on_off_light(home, room_name, status):
    """
    Turns on/off the lights in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room to control.
        status: "on" or "off".

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            if status == "on":
                actuator.turn_on()
                logger.info(f"Turned on the lights in {room_name}")
            elif status == "off":
                actuator.turn_off()
                logger.info(f"Turned off the lights in {room_name}")


def get_sensor_reading(home, room_name, sensor_type):
    """
    Gets the reading from a specific sensor in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        sensor_type: The type of sensor.

    Returns:
        The sensor reading, or None if the sensor is not found or is off.
    """
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == sensor_type:
            return sensor.get_reading()

    logger.warning(f"Sensor type {sensor_type} not found in {room_name}")
    return None


def set_music_playlist(home, room_name, playlist):
    """
    Sets the music playlist for the music player in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        playlist: The name of the playlist.

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "MusicPlayer":
            actuator.play_music(playlist)
    logger.info(f"Playing {playlist} on the music player in {room_name}")


def send_notification(home, room_name, message):
    """
    Sends a notification to the notification sender in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        message: The message to send.

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "NotificationSender":
            actuator.notification_sender(message)
    logger.info(f"Sent notification to {room_name}: {message}")


def turn_on_cleaning_robot(home, room_name):
    """
    Turns on the cleaning robot in a room and starts its daily routine.

    Args:
        home: The home plan object.
        room_name: The name of the room.

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "CleaningRobot":
            actuator.turn_on()
            actuator.daily_routine()
    logger.info(f"Started daily cleaning routine for the cleaning robot in {room_name}")


def get_outdoor_temperature(home, sensor_type="OutdoorTemperature"):
    """
    Gets the current outdoor temperature.

    Args:
        home: The home plan object.
        sensor_type: The type of outdoor temperature sensor to use. Default is "OutdoorTemperature".

    Returns:
        The outdoor temperature reading, or None if the sensor is not found or is off.
    """
    all_sensors = get_all_sensors(home, sensor_type)
    for sensor in all_sensors:
        return sensor.get_reading()

    logger.warning(f"Outdoor temperature sensor ({sensor_type}) not found.")
    return None


def play_channel_on_tv(home, room_name, channel_name):
    """
    Plays a specific channel on the TV in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        channel_name: The name of the channel to play.

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "SmartTV":
            actuator.play_channel(channel_name)
    logger.info(f"Playing {channel_name} on the TV in {room_name}")


def turn_off_device(home, room_name, device_type):
    """
    Turns off a specific device in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        device_type: The type of device to turn off.

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == device_type:
            actuator.turn_off()
    logger.info(f"Turned off the {device_type} in {room_name}")


def make_coffee(home, room_name, coffee_type="Espresso"):
    """
    Makes a cup of coffee using the coffee machine in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        coffee_type: The type of coffee to make. Default is "Espresso".

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "CoffeeMachine":
            actuator.make_coffee(coffee_type)
    logger.info(f"Making a cup of {coffee_type} in {room_name}")


def turn_on_device(home, room_name, device_type):
    """
    Turns on a specific device in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        device_type: The type of device to turn on.

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == device_type:
            actuator.turn_on()
    logger.info(f"Turned on the {device_type} in {room_name}")


def open_close_window(home, room_name, status):
    """
    Opens or closes a window in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        status: "open" or "close".

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "Window":
            if status == "open":
                actuator.turn_on()  # Assuming "turn_on" represents opening the window
                logger.info(f"Opened the window in {room_name}")
            elif status == "close":
                actuator.turn_off()  # Assuming "turn_off" represents closing the window
                logger.info(f"Closed the window in {room_name}")


def open_close_curtain(home, room_name, status):
    """
    Opens or closes a curtain in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        status: "open" or "close".

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "Curtain":
            if status == "open":
                actuator.turn_on()  # Assuming "turn_on" represents opening the curtain
                logger.info(f"Opened the curtain in {room_name}")
            elif status == "close":
                actuator.turn_off()  # Assuming "turn_off" represents closing the curtain
                logger.info(f"Closed the curtain in {room_name}")


def lock_unlock_door(home, room_name, status):
    """
    Locks or unlocks the door in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        status: "lock" or "unlock".

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == "Door":
            if status == "lock":
                actuator.lock()
                logger.info(f"Locked the door in {room_name}")
            elif status == "unlock":
                actuator.unlock()
                logger.info(f"Unlocked the door in {room_name}")


def turn_on_off_device(home, room_name, device_type, status):
    """
    Turns on or off a specific device in a room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        device_type: The type of device.
        status: "on" or "off".

    Returns:
        None
    """
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == device_type:
            if status == "on":
                actuator.turn_on()
                logger.info(f"Turned on the {device_type} in {room_name}")
            elif status == "off":
                actuator.turn_off()
                logger.info(f"Turned off the {device_type} in {room_name}")


def get_average_temperature(home, sensor_type="IndoorTemperature"):
    """
    Calculates the average temperature across all rooms in the home.

    Args:
        home: The home plan object.
        sensor_type: The type of temperature sensor to use. Default is "IndoorTemperature".

    Returns:
        The average temperature, or None if no sensors of the given type are found.
    """
    all_sensors = get_all_sensors(home, sensor_type)
    if all_sensors:
        temperatures = [sensor.get_reading() for sensor in all_sensors if sensor.get_reading() is not None]
        if temperatures:
            return sum(temperatures) / len(temperatures)
    logger.warning(f"No {sensor_type} sensors found or readings are unavailable.")
    return None


if __name__ == "__main__":
    home = home_plan()

    # Example usage:
    # control_temperature(home, "LivingRoom", 26)
    # control_humidity(home, "LivingRoom", 60)
    # control_light(home, "LivingRoom", "medium")

    # # Example of turning on/off the light
    # turn_on_off_light(home, "LivingRoom", "on")
    # turn_on_off_light(home, "LivingRoom", "off")
    #
    # # Example of sending a notification
    # send_notification(home, "LivingRoom", "It's time for dinner!")
    #
    # # Example of turning on the cleaning robot
    # turn_on_cleaning_robot(home, "LivingRoom")
    #
    # # Example of playing a channel on TV
    # play_channel_on_tv(home, "LivingRoom", "BBC News")
    #
    # # Example of turning off a device
    # turn_off_device(home, "LivingRoom", "Light")
    #
    # # Example of making coffee
    # make_coffee(home, "Kitchen", "Latte")
    #
    # # Example of opening and closing a window
    # open_close_window(home, "LivingRoom", "open")
    # open_close_window(home, "LivingRoom", "close")
    #
    # # Example of locking and unlocking a door
    # lock_unlock_door(home, "LivingRoom", "lock")
    # lock_unlock_door(home, "LivingRoom", "unlock")
    #
    # # Example of turning on/off a device using a generic function
    # turn_on_off_device(home, "LivingRoom", "Light", "on")
    # turn_on_off_device(home, "LivingRoom", "Light", "off")
    #
    # # Example of getting the average temperature
    # average_temp = get_average_temperature(home)
    # print(f"Average temperature: {average_temp}")
