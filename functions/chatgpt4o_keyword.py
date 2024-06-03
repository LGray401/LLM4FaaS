import time
from home.home_plan import home_plan, get_all_actuators, get_room

def morning_routine(home):
    print("Starting morning routine...")
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")

    if living_room:
        # Open the curtain
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Curtain":
                actuator.turn_on()

        # Turn on the light if it's too dark
        light_sensor = next((sensor for sensor in living_room.sensors if sensor.sensor_type == "LightIntensive"), None)
        if light_sensor and light_sensor.get_reading() < 950:
            light = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "Light"), None)
            if light:
                light.turn_on()

        # Play daily news
        music_player = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "MusicPlayer"), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("daily news")

    if kitchen:
        # Make a cup of coffee
        coffee_machine = next((actuator for actuator in kitchen.actuators if actuator.actuator_type == "CoffeeMachine"), None)
        if coffee_machine:
            coffee_machine.turn_on()
            print("Making a cup of coffee...")

def evening_routine(home):
    print("Starting evening routine...")
    bedroom = get_room(home, "Bedroom")

    if bedroom:
        # Close the curtain
        for actuator in bedroom.actuators:
            if actuator.actuator_type == "Curtain":
                actuator.turn_off()

        # Play bedtime music
        music_player = next((actuator for actuator in bedroom.actuators if actuator.actuator_type == "MusicPlayer"), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("bedtime music")

        # Turn the light to medium level, then off after 30 minutes
        light = next((actuator for actuator in bedroom.actuators if actuator.actuator_type == "Light"), None)
        if light:
            light.turn_on()
            light.set_brightness_level("medium")
            # time.sleep(1800)  # Wait for 30 minutes
            time.sleep(5)   # delete later
            light.turn_off()

def home_plan_routine(home):
    print("Starting home plan routine...")
    living_room = get_room(home, "LivingRoom")

    if living_room:
        # Turn on the light
        light = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "Light"), None)
        if light:
            light.turn_on()

        # Close the curtain
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Curtain":
                actuator.turn_off()

        # Turn on all sockets
        for actuator in living_room.actuators:
            if actuator.actuator_type == "SmartSocket":
                actuator.turn_on()

def away_plan_routine(home):
    print("Starting away plan routine...")
    # Turn off all lights
    for light in get_all_actuators(home, "Light"):
        light.turn_off()

    # Close all windows
    for window in get_all_actuators(home, "Window"):
        window.turn_off()

    # Lock the home door
    main_door = next((actuator for actuator in get_all_actuators(home, "Door") if actuator.room_name == "MainDoor"), None)
    if main_door:
        main_door.turn_on()

    # Start the cleaning robot
    for robot in get_all_actuators(home, "CleaningRobot"):
        robot.daily_routine()

    # Turn off all sockets except for the kitchen ones
    for socket in get_all_actuators(home, "SmartSocket"):
        if socket.room_name != "Kitchen":
            socket.turn_off()

def movie_plan_routine(home):
    print("Starting movie plan routine...")
    # Turn off all lights except in the living room
    for light in get_all_actuators(home, "Light"):
        if light.room_name != "LivingRoom":
            light.turn_off()

    # Set the light in the living room to medium level
    living_room = get_room(home, "LivingRoom")
    if living_room:
        light = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "Light"), None)
        if light:
            light.turn_on()
            light.set_brightness_level("medium")

        # Close the curtain
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Curtain":
                actuator.turn_off()

        # Turn on the TV
        tv = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "SmartTV"), None)
        if tv:
            tv.turn_on()

if __name__ == "__main__":
    home = home_plan()

    # Test routines
    # morning_routine(home)
    # evening_routine(home)
    # home_plan_routine(home)
    # away_plan_routine(home)
    # movie_plan_routine(home)
