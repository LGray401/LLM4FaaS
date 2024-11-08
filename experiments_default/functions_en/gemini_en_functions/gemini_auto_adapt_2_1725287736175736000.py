from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import AC, Heater, Humidifier, Light, Window, Curtain, MusicPlayer, CleaningRobot, NotificationSender
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, \
    LIGHT_INTENSITY_LOW, TEMP_CHANGE_DURATION_WINDOW
import time
from home.logger_config import logger


def check_temperature(home):
    """
    Check indoor temperature in each room. If temperature exceeds 25 degrees, turn on the AC and close windows.
    """
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        temp_reading = sensor.get_reading()
        if temp_reading is not None:
            room_name = sensor.room_name
            room = get_room(home, room_name)

            # Get AC and windows in the room
            acs = get_room_actuators(room, "AC")
            windows = get_room_actuators(room, "Window")

            if temp_reading > TEMP_HIGH:
                # Turn on AC
                for ac in acs:
                    if ac.status == "off":
                        ac.turn_on()
                        logger.info(f"AC in {room_name} turned ON due to high temperature ({temp_reading}°C)")
                        print(f"AC in {room_name} turned ON due to high temperature ({temp_reading}°C)")

                # Close windows
                for window in windows:
                    if window.status == "on":
                        window.turn_off()
                        logger.info(f"Window in {room_name} closed due to high temperature ({temp_reading}°C)")
                        print(f"Window in {room_name} closed due to high temperature ({temp_reading}°C)")
            elif temp_reading < TEMP_LOW:
                # Turn on Heater
                heaters = get_room_actuators(room, "Heater")
                for heater in heaters:
                    if heater.status == "off":
                        heater.turn_on()
                        logger.info(f"Heater in {room_name} turned ON due to low temperature ({temp_reading}°C)")
                        print(f"Heater in {room_name} turned ON due to low temperature ({temp_reading}°C)")

                # Open windows
                for window in windows:
                    if window.status == "off":
                        window.turn_on()
                        logger.info(f"Window in {room_name} opened due to low temperature ({temp_reading}°C)")
                        print(f"Window in {room_name} opened due to low temperature ({temp_reading}°C)")

            # Wait before next temperature check
            time.sleep(TEMP_CHANGE_DURATION_WINDOW)


def check_humidity(home):
    """
    Check indoor humidity in each room. If humidity is too low, turn on the humidifier.
    """
    humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in humidity_sensors:
        humidity_reading = sensor.get_reading()
        if humidity_reading is not None:
            room_name = sensor.room_name
            room = get_room(home, room_name)

            # Get humidifier in the room
            humidifiers = get_room_actuators(room, "Humidifier")

            if humidity_reading < HUMIDITY_LOW:
                for humidifier in humidifiers:
                    if humidifier.status == "off":
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                        logger.info(
                            f"Humidifier in {room_name} turned ON due to low humidity ({humidity_reading}%)")
                        print(f"Humidifier in {room_name} turned ON due to low humidity ({humidity_reading}%)")


def check_light_intensity(home):
    """
    Check light intensity in each room and adjust lighting accordingly.
    """
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_intensity_sensors:
        light_intensity_reading = sensor.get_reading()
        if light_intensity_reading is not None:
            room_name = sensor.room_name
            room = get_room(home, room_name)

            # Get lights in the room
            lights = get_room_actuators(room, "Light")

            if light_intensity_reading > LIGHT_INTENSITY_HIGH:
                for light in lights:
                    if light.status == "on":
                        light.set_brightness_level("low")
                        logger.info(
                            f"Light in {room_name} brightness set to low due to high light intensity ({light_intensity_reading} lux)")
                        print(
                            f"Light in {room_name} brightness set to low due to high light intensity ({light_intensity_reading} lux)")

            elif light_intensity_reading < LIGHT_INTENSITY_LOW:
                for light in lights:
                    if light.status == "on":
                        light.set_brightness_level("high")
                        logger.info(
                            f"Light in {room_name} brightness set to high due to low light intensity ({light_intensity_reading} lux)")
                        print(
                            f"Light in {room_name} brightness set to high due to low light intensity ({light_intensity_reading} lux)")

            else:
                for light in lights:
                    if light.status == "on":
                        light.set_brightness_level("medium")
                        logger.info(
                            f"Light in {room_name} brightness set to medium due to moderate light intensity ({light_intensity_reading} lux)")
                        print(
                            f"Light in {room_name} brightness set to medium due to moderate light intensity ({light_intensity_reading} lux)")


def check_smoke(home):
    """
    Check smoke sensor readings and trigger appropriate actions.
    """
    smoke_sensors = get_all_sensors(home, "Smoke")
    for sensor in smoke_sensors:
        smoke_reading = sensor.get_reading()
        if smoke_reading is not None:
            room_name = sensor.room_name
            room = get_room(home, room_name)

            # Get notification sender in the room
            notification_senders = get_room_actuators(room, "NotificationSender")

            if smoke_reading > 50:
                for notification_sender in notification_senders:
                    if notification_sender.status == "on":
                        notification_sender.notification_sender(f"Smoke detected in {room_name}!")
                        logger.warning(f"Smoke detected in {room_name}! Notification sent.")
                        print(f"Smoke detected in {room_name}! Notification sent.")


def main():
    """
    Main function to run the smart home automation.
    """
    home = home_plan()

    # Turn on all sensors
    for sensor_type in [IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor]:
        sensors = get_all_sensors(home, sensor_type.sensor_type)
        for sensor in sensors:
            sensor.turn_on()

    # Turn on all actuators
    for actuator_type in [AC, Heater, Humidifier, Light, Window, Curtain, MusicPlayer, CleaningRobot,
                          NotificationSender]:
        actuators = get_all_actuators(home, actuator_type.actuator_type)
        for actuator in actuators:
            actuator.turn_on()

    # Run automation loop
    while True:
        check_temperature(home)
        check_humidity(home)
        check_light_intensity(home)
        check_smoke(home)


if __name__ == "__main__":
    main()
