# Here is the 'function.py' file that you requested:

from home.home_plan import home_plan, get_room_sensors, get_all_actuators
from home.sensor import Sensor

def main():
    home = home_plan()

    # Morning Plan
    # morning_plan(home)

    # Leave Home Plan
    # leave_home_plan(home)
    #
    # # Movie Plan
    movie_plan(home)


def morning_plan(home):
    print("\nMORNING PLAN")
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")
    coffee_machine = get_all_actuators(home, "CoffeeMachine")
    music_player = get_all_actuators(home, "MusicPlayer")

    for curtain in curtains:
        curtain.turn_on()

    for light in lights:
        light.set_brightness_level("medium")

    for coffee_machine in coffee_machine:
        coffee_machine.turn_on()

    for music_player in music_player:
        music_player.play_music("morning playlist")


def leave_home_plan(home):
    print("\nLEAVE HOME PLAN")
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")
    smart_sockets = get_all_actuators(home, "SmartSocket")
    doors = get_all_actuators(home, "Door")

    for light in lights:
        light.turn_off()

    for curtain in curtains:
        curtain.turn_on()

    for smart_socket in smart_sockets:
        smart_socket.turn_off()

    for door in doors:
        door.lock()


def movie_plan(home):
    print("\nMOVIE PLAN")
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")
    smart_tv = get_all_actuators(home, "SmartTV")
    windows = get_all_actuators(home, "Window")

    for curtain in curtains:
        curtain.turn_on()

    for light in lights:
        light.set_brightness_level("low")

    for window in windows:
        window.turn_on()

    for smart_tv in smart_tv:
        smart_tv.play_channel("movie channel")


if __name__ == "__main__":
    main()