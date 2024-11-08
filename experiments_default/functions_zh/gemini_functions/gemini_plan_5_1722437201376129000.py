from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_sensors, get_all_actuators
from home.actuator import Light, CleaningRobot, CoffeeMachine, Curtain, MusicPlayer
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def morning_plan(home):
    """
    Morning plan function
    :param home: The home object
    :return: None
    """
    # Turn on lights in the LivingRoom and Bedroom
    living_room = get_room(home, "LivingRoom")
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if light.actuator_type == "Light":
            light.turn_on()

    bedroom = get_room(home, "Bedroom")
    bedroom_lights = get_room_actuators(home, "Bedroom")
    for light in bedroom_lights:
        if light.actuator_type == "Light":
            light.turn_on()

    # Make coffee in the Kitchen
    kitchen = get_room(home, "Kitchen")
    kitchen_coffee_machine = get_room_actuators(home, "Kitchen")
    for coffee_machine in kitchen_coffee_machine:
        if coffee_machine.actuator_type == "CoffeeMachine":
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")

    # Start cleaning robot in the LivingRoom
    living_room_cleaning_robot = get_room_actuators(home, "LivingRoom")
    for robot in living_room_cleaning_robot:
        if robot.actuator_type == "CleaningRobot":
            robot.turn_on()
            robot.daily_routine()

    # Play music in the LivingRoom
    living_room_music_player = get_room_actuators(home, "LivingRoom")
    for music_player in living_room_music_player:
        if music_player.actuator_type == "MusicPlayer":
            music_player.turn_on()
            music_player.play_music("Morning playlist")

    logger.info(format("Morning plan completed."))
    print("Morning plan completed.")


def leave_home_plan(home):
    """
    Leave home plan function
    :param home: The home object
    :return: None
    """
    # Turn off all lights in the house
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()

    # Close all windows and curtains
    all_windows = get_all_actuators(home, "Window")
    for window in all_windows:
        window.turn_off()

    all_curtains = get_all_actuators(home, "Curtain")
    for curtain in all_curtains:
        curtain.turn_off()

    # Turn off music player
    all_music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in all_music_players:
        music_player.turn_off()

    logger.info(format("Leave home plan completed."))
    print("Leave home plan completed.")


def movie_plan(home):
    """
    Movie plan function
    :param home: The home object
    :return: None
    """
    # Turn on lights in the LivingRoom to a low brightness level
    living_room = get_room(home, "LivingRoom")
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if light.actuator_type == "Light":
            light.turn_on()
            light.set_brightness_level("low")

    # Close curtains in the LivingRoom
    living_room_curtains = get_room_actuators(home, "LivingRoom")
    for curtain in living_room_curtains:
        if curtain.actuator_type == "Curtain":
            curtain.turn_on()

    # Turn on SmartTV in the LivingRoom and play Netflix
    living_room_smart_tv = get_room_actuators(home, "LivingRoom")
    for smart_tv in living_room_smart_tv:
        if smart_tv.actuator_type == "SmartTV":
            smart_tv.turn_on()
            smart_tv.play_channel("Netflix")

    logger.info(format("Movie plan completed."))
    print("Movie plan completed.")


def temperature_control(home):
    """
    Temperature control function
    :param home: The home object
    :return: None
    """
    # Get all indoor temperature sensors
    all_indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in all_indoor_temp_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            current_temperature = sensor.get_reading()
            if current_temperature is not None:
                # Get all heaters and ACs in the same room
                room_actuators = get_room_actuators(home, sensor.room_name)
                for actuator in room_actuators:
                    if actuator.actuator_type == "Heater":
                        actuator.adjust_temperature(current_temperature)
                    elif actuator.actuator_type == "AC":
                        actuator.adjust_temperature(current_temperature)

    logger.info(format("Temperature control completed."))
    print("Temperature control completed.")


def humidity_control(home):
    """
    Humidity control function
    :param home: The home object
    :return: None
    """
    # Get all humidity sensors
    all_humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in all_humidity_sensors:
        if isinstance(sensor, HumiditySensor):
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                # Get all humidifiers in the same room
                room_actuators = get_room_actuators(home, sensor.room_name)
                for actuator in room_actuators:
                    if actuator.actuator_type == "Humidifier":
                        if current_humidity < HUMIDITY_LOW:
                            actuator.increase_humidity()
                        elif current_humidity > HUMIDITY_HIGH:
                            actuator.decrease_humidity()

    logger.info(format("Humidity control completed."))
    print("Humidity control completed.")


def light_intensity_control(home):
    """
    Light intensity control function
    :param home: The home object
    :return: None
    """
    # Get all light intensive sensors
    all_light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in all_light_intensive_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            current_light_intensity = sensor.get_reading()
            if current_light_intensity is not None:
                # Get all lights in the same room
                room_actuators = get_room_actuators(home, sensor.room_name)
                for actuator in room_actuators:
                    if actuator.actuator_type == "Light":
                        if current_light_intensity < LIGHT_INTENSITY_LOW:
                            actuator.turn_on()
                        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                            actuator.turn_off()

    logger.info(format("Light intensity control completed."))
    print("Light intensity control completed.")


if __name__ == "__main__":
    # Example usage:
    home = home_plan()
    # morning_plan(home)
    # leave_home_plan(home)
    movie_plan(home)
    # temperature_control(home)
    # humidity_control(home)
    # light_intensity_control(home)