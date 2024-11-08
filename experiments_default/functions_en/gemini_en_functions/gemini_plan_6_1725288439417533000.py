from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time
import random

def morning_plan(home):
    """
    Morning Plan:
    - Turn on lights in the LivingRoom to medium brightness.
    - Turn on coffee machine in Kitchen.
    - Turn on the music in LivingRoom.
    - If the temperature in Bedroom is below 20°C, turn on the heater to 22°C.
    - If the temperature in LivingRoom is above 25°C, turn on the AC to 23°C.
    """
    # Get rooms and their components
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")
    bedroom = get_room(home, "Bedroom")

    # Turn on lights in the LivingRoom to medium brightness
    for light in get_room_actuators(home, "LivingRoom"):
        if light.actuator_type == "Light":
            light.turn_on()
            light.set_brightness_level("medium")
    print(f"Turn on the light in LivingRoom to medium brightness")
    logger.info(f"Turn on the light in LivingRoom to medium brightness")

    # Turn on coffee machine in Kitchen
    for coffee_machine in get_room_actuators(home, "Kitchen"):
        if coffee_machine.actuator_type == "CoffeeMachine":
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")
    print(f"Turn on the coffee machine in Kitchen")
    logger.info(f"Turn on the coffee machine in Kitchen")

    # Turn on the music in LivingRoom
    for music_player in get_room_actuators(home, "LivingRoom"):
        if music_player.actuator_type == "MusicPlayer":
            music_player.turn_on()
            music_player.play_music("Morning playlist")
    print(f"Turn on the music in LivingRoom")
    logger.info(f"Turn on the music in LivingRoom")

    # Adjust temperature in Bedroom
    for heater in get_room_actuators(home, "Bedroom"):
        if heater.actuator_type == "Heater":
            for temp_sensor in get_room_sensors(home, "Bedroom"):
                if temp_sensor.sensor_type == "IndoorTemperature":
                    current_temperature = temp_sensor.get_reading()
                    if current_temperature < TEMP_LOW:
                        heater.set_target_temperature(22)
                        heater.adjust_temperature(current_temperature)
                        print(f"Turn on the heater in Bedroom to 22°C")
                        logger.info(f"Turn on the heater in Bedroom to 22°C")
                    else:
                        print(f"The temperature in Bedroom is {current_temperature}°C, no need to turn on the heater")
                        logger.info(f"The temperature in Bedroom is {current_temperature}°C, no need to turn on the heater")
    
    # Adjust temperature in LivingRoom
    for ac in get_room_actuators(home, "LivingRoom"):
        if ac.actuator_type == "AC":
            for temp_sensor in get_room_sensors(home, "LivingRoom"):
                if temp_sensor.sensor_type == "IndoorTemperature":
                    current_temperature = temp_sensor.get_reading()
                    if current_temperature > TEMP_HIGH:
                        ac.set_target_temperature(23)
                        ac.adjust_temperature(current_temperature)
                        print(f"Turn on the AC in LivingRoom to 23°C")
                        logger.info(f"Turn on the AC in LivingRoom to 23°C")
                    else:
                        print(f"The temperature in LivingRoom is {current_temperature}°C, no need to turn on the AC")
                        logger.info(f"The temperature in LivingRoom is {current_temperature}°C, no need to turn on the AC")

    time.sleep(10)

def leave_home_plan(home):
    """
    Leave Home Plan:
    - Turn off all lights in the house.
    - Turn off the music player in LivingRoom.
    - Lock all doors in the house.
    - Turn on the cleaning robot in LivingRoom.
    - Send a notification to the user's phone with the message "Leaving home now".
    """
    # Get rooms and their components
    living_room = get_room(home, "LivingRoom")

    # Turn off all lights in the house
    for light in get_all_actuators(home, "Light"):
        light.turn_off()
    print(f"Turn off all lights in the house")
    logger.info(f"Turn off all lights in the house")

    # Turn off the music player in LivingRoom
    for music_player in get_room_actuators(home, "LivingRoom"):
        if music_player.actuator_type == "MusicPlayer":
            music_player.turn_off()
    print(f"Turn off the music player in LivingRoom")
    logger.info(f"Turn off the music player in LivingRoom")

    # Lock all doors in the house
    for door in get_all_actuators(home, "Door"):
        door.lock()
    print(f"Lock all doors in the house")
    logger.info(f"Lock all doors in the house")

    # Turn on the cleaning robot in LivingRoom
    for cleaning_robot in get_room_actuators(home, "LivingRoom"):
        if cleaning_robot.actuator_type == "CleaningRobot":
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()
    print(f"Turn on the cleaning robot in LivingRoom")
    logger.info(f"Turn on the cleaning robot in LivingRoom")

    # Send a notification to the user's phone with the message "Leaving home now"
    for notification_sender in get_all_actuators(home, "NotificationSender"):
        notification_sender.turn_on()
        notification_sender.notification_sender("Leaving home now")
    print(f"Send a notification to the user's phone with the message \"Leaving home now\"")
    logger.info(f"Send a notification to the user's phone with the message \"Leaving home now\"")

    time.sleep(10)

def movie_plan(home):
    """
    Movie Plan:
    - Turn off all lights in the LivingRoom except for the TV light.
    - Turn on the SmartTV in LivingRoom and play Netflix.
    - Adjust the temperature in LivingRoom to 22°C.
    - Close the curtains in LivingRoom.
    """
    # Get rooms and their components
    living_room = get_room(home, "LivingRoom")

    # Turn off all lights in the LivingRoom except for the TV light
    for light in get_room_actuators(home, "LivingRoom"):
        if light.actuator_type == "Light":
            light.turn_off()
    print(f"Turn off all lights in the LivingRoom except for the TV light")
    logger.info(f"Turn off all lights in the LivingRoom except for the TV light")

    # Turn on the SmartTV in LivingRoom and play Netflix
    for smart_tv in get_room_actuators(home, "LivingRoom"):
        if smart_tv.actuator_type == "SmartTV":
            smart_tv.turn_on()
            smart_tv.play_channel("Netflix")
    print(f"Turn on the SmartTV in LivingRoom and play Netflix")
    logger.info(f"Turn on the SmartTV in LivingRoom and play Netflix")

    # Adjust the temperature in LivingRoom to 22°C
    for ac in get_room_actuators(home, "LivingRoom"):
        if ac.actuator_type == "AC":
            for temp_sensor in get_room_sensors(home, "LivingRoom"):
                if temp_sensor.sensor_type == "IndoorTemperature":
                    current_temperature = temp_sensor.get_reading()
                    ac.set_target_temperature(22)
                    ac.adjust_temperature(current_temperature)
                    print(f"Adjust the temperature in LivingRoom to 22°C")
                    logger.info(f"Adjust the temperature in LivingRoom to 22°C")

    # Close the curtains in LivingRoom
    for curtain in get_room_actuators(home, "LivingRoom"):
        if curtain.actuator_type == "Curtain":
            curtain.turn_on()
    print(f"Close the curtains in LivingRoom")
    logger.info(f"Close the curtains in LivingRoom")

    time.sleep(10)


def main():
    """
    Main function to test the smart home functions.
    """
    # Initialize home plan
    home = home_plan()
    print_home_plan(home)

    # Run morning plan
    print("\n---Running Morning Plan---")
    morning_plan(home)

    # Run leave home plan
    print("\n---Running Leave Home Plan---")
    leave_home_plan(home)

    # Run movie plan
    print("\n---Running Movie Plan---")
    movie_plan(home)

if __name__ == "__main__":
    main()
