from datetime import datetime

from functions_without_room_info.actuator_without_room_name import SmartSocket, SmartDoorLock, Heater, MusicPlayer, Light
# todo: Maybe also setup some sensor triggered plan?
# we should know which lights should be turned off ✅


def scheduler(keyword):
    current_time = datetime.now().strftime("%H:%M")
    print(f"current time is {current_time}")
    if current_time == "07:00" or keyword.lower() == "morning":
        morning_plan()
    elif current_time >= "20:00" or current_time < "07:00" or keyword.lower() == "night":
        night_plan()
    elif keyword.lower() == "leave":
        leave_home_plan()
    elif keyword.lower() == "back":
        back_home_plan()
    elif keyword.lower() == "movie":
        movie_plan()
    else:
        print("Invalid keyword. Please input a valid keyword.")


def leave_home_plan():
    print("Starting Leave Home Plan Now")
    # Turn off lights
    light_1 = Light()
    if light_1.status == "on":
        light_1.turn_off()

    # Turn off some sockets except for fridge
    smart_socket = SmartSocket()
    smart_socket.turn_off_except(exceptions=["fridge"])

    # Lock all doors and windows
    smart_lock = SmartDoorLock()
    smart_lock.lock_all()

    # Turn off heater
    heater = Heater()
    heater.turn_off()


def back_home_plan():
    print("Starting Back Home Plan Now")
    # Turn on lights
    light = Light()
    light.turn_on()

    # Turn on some devices as needed


def morning_plan():
    print("Starting Morning Plan Now")
    # Turn on lights
    light = Light()
    light.turn_on()
    light.set_brightness_level("medium")

    # Turn on heater if needed
    heater = Heater()
    heater.turn_on()
    heater.temp_increment(init_temp=20, curr_level=3)


def night_plan():
    print("Starting Night Plan Now")
    # Turn off unnecessary devices
    # Close curtains, etc.


def movie_plan():
    print("Starting Movie Plan Now")
    # Dim lights
    light = Light()
    light.turn_on()
    light.set_brightness_level("low")

    # Turn on music player
    music_player = MusicPlayer()
    music_player.turn_on()
    music_player.music_player(playlist="Movie Soundtrack")



# invocation
# scheduler("morning")
