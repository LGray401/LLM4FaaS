from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, \
    LIGHT_INTENSITY_LOW, TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
import time


def sleeping_mode(home):
    # turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # close all windows
    windows = get_all_actuators(home, "Window")
    for window in windows:
        window.turn_off()

    # close all curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()

    # set AC to 22 degrees
    acs = get_all_actuators(home, "AC")
    for ac in acs:
        ac.set_target_temperature(22)
        ac.turn_on()

    # turn off music player
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.turn_off()

    # turn off coffee machine
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_machines:
        coffee_machine.turn_off()

    # turn off cleaning robot
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for cleaning_robot in cleaning_robots:
        cleaning_robot.turn_off()

    # turn off smart tv
    smart_tvs = get_all_actuators(home, "SmartTV")
    for smart_tv in smart_tvs:
        smart_tv.turn_off()

    # send notification
    notification_senders = get_all_actuators(home, "NotificationSender")
    for notification_sender in notification_senders:
        notification_sender.notification_sender("Good night! Sleep well!")


def wake_up_mode(home):
    # turn on all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()

    # open curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # set AC to 25 degrees
    acs = get_all_actuators(home, "AC")
    for ac in acs:
        ac.set_target_temperature(25)
        ac.turn_on()

    # turn on music player
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.play_music("Morning playlist")

    # make coffee
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_machines:
        coffee_machine.make_coffee("Espresso")

    # send notification
    notification_senders = get_all_actuators(home, "NotificationSender")
    for notification_sender in notification_senders:
        notification_sender.notification_sender("Good morning! Have a great day!")


def turn_off_lights_mode(home):
    # turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()


def close_windows_mode(home):
    # close all windows
    windows = get_all_actuators(home, "Window")
    for window in windows:
        window.turn_off()


if __name__ == "__main__":
    # Initialize the home
    home = home_plan()

    # Example usage of functions
    sleeping_mode(home)
    time.sleep(5)
    wake_up_mode(home)
    time.sleep(5)
    turn_off_lights_mode(home)
    time.sleep(5)
    close_windows_mode(home)