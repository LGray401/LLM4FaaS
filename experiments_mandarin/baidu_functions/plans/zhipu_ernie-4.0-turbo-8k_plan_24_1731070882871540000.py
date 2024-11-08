# Based on the functional description and the provided source code, here is the `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door, Window

def morning_plan(home):
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Get relevant sensors and actuators
    light_sensors = get_all_sensors(home, "LightIntensive")
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    music_players = get_all_actuators(home, "MusicPlayer")

    # Open curtains
    for curtain in curtains:
        curtain.turn_on()  # Assuming turn_on opens the curtains

    # Check if it's cloudy (low light intensity)
    is_cloudy = False
    for sensor in light_sensors:
        if sensor.room_name == "LivingRoom" and sensor.get_reading() < 300:  # Assuming 300 is the threshold for cloudy
            is_cloudy = True
            break

    # Turn on lights if it's cloudy
    if is_cloudy:
        for light in lights:
            if light.room_name == "LivingRoom":
                light.turn_on()

    # Make coffee
    for coffee_machine in coffee_machines:
        if coffee_machine.room_name == "Kitchen":
            coffee_machine.turn_on()  # Assuming the coffee machine starts making coffee when turned on
            coffee_machine.make_coffee("Espresso")  # Or any other type of coffee

    # Play music after coffee is made (assuming instantly for simplicity)
    for music_player in music_players:
        if music_player.room_name == "LivingRoom":
            music_player.turn_on()
            music_player.play_music("Morning Playlist")

def leave_home_plan(home):
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Get relevant sensors and actuators
    light_sensors = get_all_sensors(home, "LightIntensive")
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")
    sockets = get_all_actuators(home, "SmartSocket")
    doors = get_all_actuators(home, "Door")

    # Check if it's sunny (high light intensity)
    is_sunny = False
    for sensor in light_sensors:
        if sensor.room_name == "LivingRoom" and sensor.get_reading() >= 900:  # Assuming 900 is the threshold for sunny
            is_sunny = True
            break

    # Open curtains if it's sunny
    if is_sunny:
        for curtain in curtains:
            curtain.turn_on()  # Assuming turn_on opens the curtains

    # Turn off lights
    for light in lights:
        light.turn_off()

    # Turn off sockets
    for socket in sockets:
        socket.turn_off()

    # Lock doors
    for door in doors:
        door.lock()

def movie_plan(home):
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Get relevant actuators
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")

    # Close curtains
    for curtain in curtains:
        curtain.turn_off()  # Assuming turn_off closes the curtains

    # Turn off lights
    for light in lights:
        if light.room_name == "LivingRoom":
            light.turn_off()

if __name__ == "__main__":
    # Initialize home plan
    home = home_plan()

    # Execute morning plan
    morning_plan(home)

    # Execute leave home plan (as an example, this would typically be triggered by a different event)
    # leave_home_plan(home)

    # Execute movie plan (as an example, this would typically be triggered by a different event)
    # movie_plan(home)