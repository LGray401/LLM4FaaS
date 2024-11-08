from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.actuator import Light, Heater, AC, Humidifier, CleaningRobot, MusicPlayer, SmartTV
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, \
    LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def adjust_light_brightness(home, room_name, brightness_level):
    """Adjust the brightness of the light in a given room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        brightness_level: The desired brightness level ("low", "medium", "high").
    """
    room = get_room(home, room_name)
    if room:
        for light in get_room_actuators(home, room_name):
            if isinstance(light, Light):
                light.set_brightness_level(brightness_level)
                return True
    return False


def adjust_indoor_temperature(home, room_name, target_temperature):
    """Adjust the indoor temperature in a given room using heater or AC.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        target_temperature: The desired temperature in Celsius.
    """
    room = get_room(home, room_name)
    if room:
        for sensor in get_room_sensors(home, room_name):
            if isinstance(sensor, IndoorTemperatureSensor):
                current_temperature = sensor.get_reading()
                if current_temperature:
                    for heater in get_room_actuators(home, room_name):
                        if isinstance(heater, Heater):
                            heater.set_target_temperature(target_temperature)
                            heater.adjust_temperature(current_temperature)
                            return True
                    for ac in get_room_actuators(home, room_name):
                        if isinstance(ac, AC):
                            ac.set_target_temperature(target_temperature)
                            ac.adjust_temperature(current_temperature)
                            return True
    return False


def adjust_curtain_switch(home, room_name, action):
    """Adjust the curtain switch in a given room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        action: "open" or "close".
    """
    room = get_room(home, room_name)
    if room:
        for curtain in get_room_actuators(home, room_name):
            if isinstance(curtain, Curtain):
                if action == "open":
                    curtain.turn_on()
                    return True
                elif action == "close":
                    curtain.turn_off()
                    return True
    return False


def adjust_room_humidity(home, room_name, action):
    """Adjust the humidity in a given room.

    Args:
        home: The home plan object.
        room_name: The name of the room.
        action: "increase" or "decrease".
    """
    room = get_room(home, room_name)
    if room:
        for sensor in get_room_sensors(home, room_name):
            if isinstance(sensor, HumiditySensor):
                current_humidity = sensor.get_reading()
                if current_humidity:
                    for humidifier in get_room_actuators(home, room_name):
                        if isinstance(humidifier, Humidifier):
                            if action == "increase":
                                if current_humidity < HUMIDITY_LOW:
                                    humidifier.increase_humidity()
                                    return True
                            elif action == "decrease":
                                if current_humidity > HUMIDITY_HIGH:
                                    humidifier.decrease_humidity()
                                    return True
    return False


def main():
    """Main function to test the functions."""
    home = home_plan()

    # Adjust light brightness
    adjust_light_brightness(home, "LivingRoom", "high")

    # Adjust indoor temperature
    adjust_indoor_temperature(home, "LivingRoom", 22)

    # Adjust curtain switch
    adjust_curtain_switch(home, "LivingRoom", "open")

    # Adjust room humidity
    adjust_room_humidity(home, "LivingRoom", "increase")
    #
    # # Example using cleaning robot
    # for robot in get_all_actuators(home, "CleaningRobot"):
    #     if isinstance(robot, CleaningRobot):
    #         robot.daily_routine()
    #
    # # Example using music player
    # for music_player in get_all_actuators(home, "MusicPlayer"):
    #     if isinstance(music_player, MusicPlayer):
    #         music_player.play_music("Jazz")
    #
    # # Example using Smart TV
    # for tv in get_all_actuators(home, "SmartTV"):
    #     if isinstance(tv, SmartTV):
    #         tv.play_channel("Discovery")


if __name__ == "__main__":
    main()

# This code defines five functions corresponding to the functional descriptions you provided:

# * **adjust_light_brightness:** Adjusts the light brightness in a given room.
# * **adjust_indoor_temperature:** Adjusts the indoor temperature in a given room using a heater or AC.
# * **adjust_curtain_switch:** Adjusts the curtain switch in a given room.
# * **adjust_room_humidity:** Adjusts the humidity in a given room.
# * **main:** A function to demonstrate how to use the functions. 

# These functions leverage the existing classes from `sensor.py`, `actuator.py`, and `home_plan.py` to interact with the smart home components. The `config.py` file provides constants used for threshold values and other settings.

# This code provides a basic framework for implementing smart home functionality. You can expand on this by adding more features, such as:

# * Adding support for more sensor types and actuator types.
# * Implementing more complex logic for controlling devices based on sensor readings.
# * Integrating with a user interface or voice assistant for easier interaction.
# * Adding error handling and logging for better stability and debugging.

# Let me know if you have any other questions or require additional modifications. 
