# Here is the 'function.py' file based on the provided functional description and the given code files:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def start_cleaning_robot(room_name):
    home = home_plan()
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    cleaning_robot = None
    for actuator in actuators:
        if actuator.actuator_type == "CleaningRobot":
            cleaning_robot = actuator
            break

    if cleaning_robot is None:
        print("Cleaning Robot is not available in the specified room.")
        return

    cleaning_robot.turn_on()
    cleaning_robot.daily_routine()

def play_music(room_name, playlist):
    home = home_plan()
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    music_player = None
    for actuator in actuators:
        if actuator.actuator_type == "MusicPlayer":
            music_player = actuator
            break

    if music_player is None:
        print("Music Player is not available in the specified room.")
        return

    music_player.turn_on()
    music_player.play_music(playlist)

def change_tv_channel(room_name, channel_name):
    home = home_plan()
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    smart_tv = None
    for actuator in actuators:
        if actuator.actuator_type == "SmartTV":
            smart_tv = actuator
            break

    if smart_tv is None:
        print("Smart TV is not available in the specified room.")
        return

    smart_tv.turn_on()
    smart_tv.play_channel(channel_name)

def adjust_brightness_level(room_name, brightness_level):
    home = home_plan()
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    light = None
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            light = actuator
            break

    if light is None:
        print("Light is not available in the specified room.")
        return

    light.turn_on()
    light.set_brightness_level(brightness_level)

def smart_home(project):
    if project == "start_cleaning_robot":
        room_name = input("Enter the room name where the Cleaning Robot is located: ")
        start_cleaning_robot(room_name)
    elif project == "play_music":
        room_name = input("Enter the room name where the Music Player is located: ")
        playlist = input("Enter the playlist you want to listen to: ")
        play_music(room_name, playlist)
    elif project == "change_tv_channel":
        room_name = input("Enter the room name where the Smart TV is located: ")
        channel_name = input("Enter the TV channel you want to watch: ")
        change_tv_channel(room_name, channel_name)
    elif project == "adjust_brightness_level":
        room_name = input("Enter the room name where the Light is located: ")
        brightness_level = input("Enter the brightness level you want to set (low, medium, high): ")
        adjust_brightness_level(room_name, brightness_level)
    else:
        print("Invalid project.")

if __name__ == "__main__":
    project = input("Enter the name of the project you want to execute: ")
    smart_home(project)