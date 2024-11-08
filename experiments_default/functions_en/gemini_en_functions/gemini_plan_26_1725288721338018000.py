from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_actuators, \
    get_all_sensors, print_home_plan
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, CoffeeMachine, Curtain, MusicPlayer, Heater, AC, Door, CleaningRobot
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger
import time

def morning_plan(home):
    """Executes the morning plan."""
    print("Good Morning! Here's your Morning Plan:")
    logger.info("Starting the Morning Plan")

    # Turn on lights
    living_room = get_room(home, "LivingRoom")
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if light.actuator_type == "Light":
            light.turn_on()
    print("Turning on lights in the Living Room.")
    logger.info("Turning on lights in the Living Room.")

    # Adjust light brightness based on indoor sunlight
    light_sensor = get_room_sensors(home, "LivingRoom")[0]
    if light_sensor.sensor_type == "LightIntensive":
        light_sensor.turn_on()
        light_intensity = light_sensor.get_reading()
        light_sensor.turn_off()

        if light_intensity < LIGHT_INTENSITY_LOW:
            print("Sunlight is low, setting lights to high brightness.")
            logger.info("Sunlight is low, setting lights to high brightness.")
            for light in living_room_lights:
                if light.actuator_type == "Light":
                    light.set_brightness_level("high")
        else:
            print("Sunlight is sufficient, setting lights to medium brightness.")
            logger.info("Sunlight is sufficient, setting lights to medium brightness.")
            for light in living_room_lights:
                if light.actuator_type == "Light":
                    light.set_brightness_level("medium")

    # Make cappuccino
    kitchen = get_room(home, "Kitchen")
    coffee_machine = get_room_actuators(home, "Kitchen")[0]
    if coffee_machine.actuator_type == "CoffeeMachine":
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Cappuccino")
    print("Making a cup of cappuccino in the Kitchen.")
    logger.info("Making a cup of cappuccino in the Kitchen.")

    # Open curtains
    living_room_curtains = get_room_actuators(home, "LivingRoom")
    for curtain in living_room_curtains:
        if curtain.actuator_type == "Curtain":
            curtain.turn_on()
    print("Opening the curtains in the Living Room.")
    logger.info("Opening the curtains in the Living Room.")

    # Play relaxing music
    living_room_music_player = get_room_actuators(home, "LivingRoom")
    for music_player in living_room_music_player:
        if music_player.actuator_type == "MusicPlayer":
            music_player.turn_on()
            music_player.play_music("Relaxing")
    print("Playing relaxing music in the Living Room.")
    logger.info("Playing relaxing music in the Living Room.")

    # Adjust temperature in Living Room
    living_room_temperature_sensor = get_room_sensors(home, "LivingRoom")[0]
    living_room_heater = get_room_actuators(home, "LivingRoom")
    for heater in living_room_heater:
        if heater.actuator_type == "Heater":
            if living_room_temperature_sensor.sensor_type == "IndoorTemperature":
                living_room_temperature_sensor.turn_on()
                current_temperature = living_room_temperature_sensor.get_reading()
                living_room_temperature_sensor.turn_off()

                if current_temperature < TEMP_LOW:
                    print("It's cold, turning on the heater in the Living Room.")
                    logger.info("It's cold, turning on the heater in the Living Room.")
                    heater.turn_on()
                    heater.set_target_temperature(TEMP_HIGH)
                elif current_temperature > TEMP_HIGH:
                    print("It's warm, turning off the heater in the Living Room.")
                    logger.info("It's warm, turning off the heater in the Living Room.")
                    heater.turn_off()

    # Adjust temperature in Bedroom
    bedroom_temperature_sensor = get_room_sensors(home, "Bedroom")[0]
    bedroom_heater = get_room_actuators(home, "Bedroom")
    for heater in bedroom_heater:
        if heater.actuator_type == "Heater":
            if bedroom_temperature_sensor.sensor_type == "IndoorTemperature":
                bedroom_temperature_sensor.turn_on()
                current_temperature = bedroom_temperature_sensor.get_reading()
                bedroom_temperature_sensor.turn_off()

                if current_temperature < TEMP_LOW:
                    print("It's cold, turning on the heater in the Bedroom.")
                    logger.info("It's cold, turning on the heater in the Bedroom.")
                    heater.turn_on()
                    heater.set_target_temperature(TEMP_HIGH)
                elif current_temperature > TEMP_HIGH:
                    print("It's warm, turning off the heater in the Bedroom.")
                    logger.info("It's warm, turning off the heater in the Bedroom.")
                    heater.turn_off()

    print("Morning plan completed!")
    logger.info("Morning plan completed!")


def leave_home_plan(home):
    """Executes the leave home plan."""
    print("Leaving Home Now!")
    logger.info("Starting the leave home plan.")

    # Close the door
    living_room = get_room(home, "LivingRoom")
    living_room_door = get_room_actuators(home, "LivingRoom")
    for door in living_room_door:
        if door.actuator_type == "Door":
            door.lock()
    print("Locking the door in the Living Room.")
    logger.info("Locking the door in the Living Room.")

    # Turn off all lights
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()
    print("Turning off all lights.")
    logger.info("Turning off all lights.")

    # Disconnect power sockets
    all_smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in all_smart_sockets:
        socket.turn_off()
    print("Disconnecting all power sockets.")
    logger.info("Disconnecting all power sockets.")

    print("Leave home plan completed!")
    logger.info("Leave home plan completed!")


def movie_plan(home):
    """Executes the movie plan."""
    print("Movie time!")
    logger.info("Starting the movie plan.")

    # Draw curtains
    living_room = get_room(home, "LivingRoom")
    living_room_curtains = get_room_actuators(home, "LivingRoom")
    for curtain in living_room_curtains:
        if curtain.actuator_type == "Curtain":
            curtain.turn_on()
    print("Drawing the curtains in the Living Room.")
    logger.info("Drawing the curtains in the Living Room.")

    # Dim the lights
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if light.actuator_type == "Light":
            light.set_brightness_level("low")
    print("Dimming the lights in the Living Room.")
    logger.info("Dimming the lights in the Living Room.")

    print("Movie plan completed!")
    logger.info("Movie plan completed!")


if __name__ == "__main__":
    home = home_plan()
    # print_home_plan(home)

    morning_plan(home)
    time.sleep(5)
    leave_home_plan(home)
    time.sleep(5)
    movie_plan(home)