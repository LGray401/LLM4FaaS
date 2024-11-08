from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW

import time


def turn_on_light_in_room(home, room_name):
    """
    Turns on all lights in a specified room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
    """
    lights = get_room_actuators(home, room_name)
    for light in lights:
        if light.actuator_type == "Light":
            light.turn_on()


def turn_off_light_in_room(home, room_name):
    """
    Turns off all lights in a specified room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
    """
    lights = get_room_actuators(home, room_name)
    for light in lights:
        if light.actuator_type == "Light":
            light.turn_off()


def adjust_temperature(home, room_name, target_temperature):
    """
    Adjusts the temperature in a specified room using heaters or AC units.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        target_temperature: The desired temperature in Celsius.
    """
    room = get_room(home, room_name)
    if room is not None:
        sensors = get_room_sensors(home, room_name)
        for sensor in sensors:
            if sensor.sensor_type == "IndoorTemperature":
                current_temperature = sensor.get_reading()
                if current_temperature is not None:
                    actuators = get_room_actuators(home, room_name)
                    for actuator in actuators:
                        if actuator.actuator_type == "Heater":
                            actuator.set_target_temperature(target_temperature)
                            actuator.adjust_temperature(current_temperature)
                        elif actuator.actuator_type == "AC":
                            actuator.set_target_temperature(target_temperature)
                            actuator.adjust_temperature(current_temperature)
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait for a while to allow temperature adjustment


def adjust_humidity(home, room_name, target_humidity):
    """
    Adjusts the humidity in a specified room using humidifiers.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        target_humidity: The desired humidity percentage.
    """
    room = get_room(home, room_name)
    if room is not None:
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


def play_music(home, room_name, playlist_name):
    """
    Plays music in a specified room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        playlist_name: The name of the playlist.
    """
    room = get_room(home, room_name)
    if room is not None:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if actuator.actuator_type == "MusicPlayer":
                actuator.play_music(playlist_name)


def send_notification(home, message):
    """
    Sends a notification to all notification senders in the home.

    Args:
        home: The home plan object.
        message: The notification message.
    """
    notification_senders = get_all_actuators(home, "NotificationSender")
    for sender in notification_senders:
        sender.notification_sender(message)


def main():
    """
    Main function to demonstrate the smart home functions.
    """
    home = home_plan()

    # Example usage:

    # Turn on lights in the LivingRoom
    turn_on_light_in_room(home, "LivingRoom")
    print("\nLights turned on in the LivingRoom!")

    # Adjust temperature in the Bedroom to 20°C
    adjust_temperature(home, "Bedroom", 20)
    print("\nTemperature adjusted to 20°C in the Bedroom!")

    # Play music in the LivingRoom
    play_music(home, "LivingRoom", "Rock Classics")
    print("\nPlaying Rock Classics in the LivingRoom!")

    # Send a notification
    send_notification(home, "Reminder: It's time for dinner!")
    print("\nNotification sent!")

    # Turn off lights in the LivingRoom
    turn_off_light_in_room(home, "LivingRoom")
    print("\nLights turned off in the LivingRoom!")

    # Adjust humidity in the Bathroom to 40%
    adjust_humidity(home, "Bathroom", 40)
    print("\nHumidity adjusted to 40% in the Bathroom!")


if __name__ == "__main__":
    main()