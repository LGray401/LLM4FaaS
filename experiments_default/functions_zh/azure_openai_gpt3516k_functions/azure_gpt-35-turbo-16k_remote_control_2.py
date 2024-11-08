# Here is the 'function.py' file based on the given functional description and the provided source code:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.logger_config import logger


def adjust_lighting(home, room_name, brightness_level):
    room_sensors = get_room_sensors(home, room_name)
    room_actuators = get_room_actuators(home, room_name)

    if room_sensors is not None and room_actuators is not None:
        light_sensor = None
        light_actuator = None

        # Find light sensor and actuator in the room
        for sensor in room_sensors:
            if sensor.sensor_type == "LightIntensive":
                light_sensor = sensor
                break

        for actuator in room_actuators:
            if actuator.actuator_type == "Light":
                light_actuator = actuator
                break

        if light_sensor is not None and light_actuator is not None:
            current_reading = light_sensor.get_reading()
            status = light_actuator.get_status()

            if current_reading is not None and status == "on":
                if current_reading < brightness_level:
                    light_actuator.set_brightness_level("high")
                else:
                    light_actuator.set_brightness_level("low")
            else:
                logger.warning("Failed to adjust lighting. Light sensor is off or in error status.")
        else:
            logger.warning(f"No light sensor or actuator found in {room_name}.")
    else:
        logger.warning(f"No room called {room_name} found in the home.")


def adjust_temperature(home, room_name, target_temperature):
    room_sensors = get_room_sensors(home, room_name)
    room_actuators = get_room_actuators(home, room_name)

    if room_sensors is not None and room_actuators is not None:
        indoor_temp_sensor = None
        heater_actuator = None
        ac_actuator = None

        # Find indoor temperature sensor, heater actuator, and AC actuator in the room
        for sensor in room_sensors:
            if sensor.sensor_type == "IndoorTemperature":
                indoor_temp_sensor = sensor
                break

        for actuator in room_actuators:
            if actuator.actuator_type == "Heater":
                heater_actuator = actuator
            elif actuator.actuator_type == "AC":
                ac_actuator = actuator

        if indoor_temp_sensor is not None and heater_actuator is not None and ac_actuator is not None:
            current_reading = indoor_temp_sensor.get_reading()
            heater_status = heater_actuator.get_status()
            ac_status = ac_actuator.get_status()

            if current_reading is not None and heater_status == "on" and ac_status == "on":
                if current_reading < target_temperature:
                    heater_actuator.turn_on()
                    ac_actuator.turn_off()
                else:
                    heater_actuator.turn_off()
                    ac_actuator.turn_on()
            else:
                logger.warning("Failed to adjust temperature. Indoor temperature sensor, Heater, or AC is off or in error status.")
        else:
            logger.warning(f"No indoor temperature sensor, Heater, or AC found in {room_name}.")
    else:
        logger.warning(f"No room called {room_name} found in the home.")


def open_window(home, room_name):
    room_actuators = get_room_actuators(home, room_name)

    if room_actuators is not None:
        window_actuator = None

        # Find window actuator in the room
        for actuator in room_actuators:
            if actuator.actuator_type == "Window":
                window_actuator = actuator
                break

        if window_actuator is not None:
            window_status = window_actuator.get_status()

            if window_status == "off":
                window_actuator.turn_on()
            else:
                logger.warning(f"Window in {room_name} is already open.")
        else:
            logger.warning(f"No window actuator found in {room_name}.")
    else:
        logger.warning(f"No room called {room_name} found in the home.")


def play_music(home, room_name, playlist):
    room_actuators = get_room_actuators(home, room_name)

    if room_actuators is not None:
        music_player_actuator = None

        # Find music player actuator in the room
        for actuator in room_actuators:
            if actuator.actuator_type == "MusicPlayer":
                music_player_actuator = actuator
                break

        if music_player_actuator is not None:
            music_player_status = music_player_actuator.get_status()

            if music_player_status == "off":
                logger.warning(f"Music player in {room_name} is off. Turn it on before playing music.")
            else:
                music_player_actuator.play_music(playlist)
        else:
            logger.warning(f"No music player actuator found in {room_name}.")
    else:
        logger.warning(f"No room called {room_name} found in the home.")


if __name__ == "__main__":
    # Example usage
    home = home_plan()

    adjust_lighting(home, "LivingRoom", 80)
    adjust_temperature(home, "Bedroom", 20)
    open_window(home, "Kitchen")
    play_music(home, "LivingRoom", "pop")