from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

import time


def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")

    # Turn on the lights
    for light in get_room_actuators(home, "LivingRoom"):
        if light.actuator_type == "Light":
            light.turn_on()
            light.set_brightness_level("medium")

    # Turn on the music
    for music_player in get_room_actuators(home, "LivingRoom"):
        if music_player.actuator_type == "MusicPlayer":
            music_player.turn_on()
            music_player.play_music("Morning playlist")

    # Open the curtains
    for curtain in get_room_actuators(home, "LivingRoom"):
        if curtain.actuator_type == "Curtain":
            curtain.turn_on()

    # Start the coffee machine
    for coffee_machine in get_room_actuators(home, "Kitchen"):
        if coffee_machine.actuator_type == "CoffeeMachine":
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")

    # Adjust the temperature in the living room
    for ac in get_room_actuators(home, "LivingRoom"):
        if ac.actuator_type == "AC":
            ac.set_target_temperature(22)
            ac.adjust_temperature(get_room_sensors(home, "LivingRoom")[0].get_reading())

    # Adjust the temperature in the bedroom
    for heater in get_room_actuators(home, "Bedroom"):
        if heater.actuator_type == "Heater":
            heater.set_target_temperature(20)
            heater.adjust_temperature(get_room_sensors(home, "Bedroom")[0].get_reading())

    time.sleep(10)


def leave_home_plan(home):
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")
    bedroom = get_room(home, "Bedroom")

    # Close the front door
    for door in get_room_actuators(home, "LivingRoom"):
        if door.actuator_type == "Door":
            door.lock()

    # Turn off all lights
    for light in get_all_actuators(home, "Light"):
        light.turn_off()

    # Turn off the music
    for music_player in get_all_actuators(home, "MusicPlayer"):
        music_player.turn_off()

    # Close the curtains
    for curtain in get_all_actuators(home, "Curtain"):
        curtain.turn_off()

    # Turn off the coffee machine
    for coffee_machine in get_room_actuators(home, "Kitchen"):
        if coffee_machine.actuator_type == "CoffeeMachine":
            coffee_machine.turn_off()

    # Turn off the AC/Heater
    for ac in get_all_actuators(home, "AC"):
        ac.turn_off()
    for heater in get_all_actuators(home, "Heater"):
        heater.turn_off()

    # Start the cleaning robot
    for cleaning_robot in get_all_actuators(home, "CleaningRobot"):
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()


def movie_plan(home):
    living_room = get_room(home, "LivingRoom")

    # Close the curtains
    for curtain in get_room_actuators(home, "LivingRoom"):
        if curtain.actuator_type == "Curtain":
            curtain.turn_off()

    # Turn on the TV
    for smart_tv in get_room_actuators(home, "LivingRoom"):
        if smart_tv.actuator_type == "SmartTV":
            smart_tv.turn_on()
            smart_tv.play_channel("Netflix")

    # Turn on the lights
    for light in get_room_actuators(home, "LivingRoom"):
        if light.actuator_type == "Light":
            light.turn_on()
            light.set_brightness_level("low")

    # Adjust the temperature
    for ac in get_room_actuators(home, "LivingRoom"):
        if ac.actuator_type == "AC":
            ac.set_target_temperature(22)
            ac.adjust_temperature(get_room_sensors(home, "LivingRoom")[0].get_reading())

    time.sleep(10)


def main():
    home = home_plan()
    # print_home_plan(home)

    # morning_plan(home)
    # leave_home_plan(home)
    movie_plan(home)


if __name__ == '__main__':
    main()
