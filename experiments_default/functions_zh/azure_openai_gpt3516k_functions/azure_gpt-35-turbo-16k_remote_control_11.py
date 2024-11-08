# Sure, here is the 'function.py' file based on the functional description and the provided code files:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators, print_home_plan

def sleep_mode(home):
    print("Entering sleep mode...")
    print("Turning off lights...")
    light_sensors = get_room_sensors(home, "Bedroom")
    for sensor in light_sensors:
        if sensor.sensor_type == "LightIntensive":
            sensor.turn_off()

    print("Closing curtains...")
    curtains = get_room_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    print("Locking doors...")
    doors = get_room_actuators(home, "Door")
    for door in doors:
        door.lock()

    print("Turning off music player...")
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.turn_off()

def wake_up_mode(home):
    print("Entering wake up mode...")
    print("Turning on lights...")
    light_sensors = get_room_sensors(home, "Bedroom")
    for sensor in light_sensors:
        if sensor.sensor_type == "LightIntensive":
            sensor.turn_on()

    print("Opening curtains...")
    curtains = get_room_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()

    print("Unlocking doors...")
    doors = get_room_actuators(home, "Door")
    for door in doors:
        door.unlock()

    print("Playing morning playlist...")
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.play_music("morning_playlist")

def turn_off_lights_mode(home):
    print("Entering turn off lights mode...")
    print("Turning off lights...")
    light_sensors = get_room_sensors(home, "LivingRoom")
    for sensor in light_sensors:
        if sensor.sensor_type == "LightIntensive":
            sensor.turn_off()