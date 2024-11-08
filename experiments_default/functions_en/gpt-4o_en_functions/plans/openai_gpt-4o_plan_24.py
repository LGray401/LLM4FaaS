# Sure! Based on your functional description and the provided source codes, I've created the `function.py` file with the main function to implement the required plans: `MORNING PLAN`, `LEAVE HOME PLAN`, and `MOVIE PLAN`.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door, SmartSocket
from home.home_plan import home_plan, get_all_sensors, get_all_actuators

def morning_plan(home):
    # Open the curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # Check if it is cloudy
    light_sensors = get_all_sensors(home, "LightIntensive")
    is_cloudy = any(sensor.get_reading() and sensor.get_reading() < 900 for sensor in light_sensors)

    # Turn on the lights if it is cloudy
    if is_cloudy:
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_on()

    # Make coffee and play music when coffee is ready
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Regular")
        # Simulate coffee making process
        coffee_machine.turn_off()

    # Play music after coffee is ready
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Morning Playlist")
        music_player.turn_off()

def leave_home_plan(home):
    # Check if it is sunny
    light_sensors = get_all_sensors(home, "LightIntensive")
    is_sunny = any(sensor.get_reading() and sensor.get_reading() >= 900 for sensor in light_sensors)

    # Open the curtains if it is sunny
    if is_sunny:
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_on()

    # Turn off lights and sockets
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

    # Lock the door
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.turn_on()
        door.lock()
        door.turn_off()

def movie_plan(home):
    # Close the curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()

    # Turn off the lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def main():
    home = home_plan()
    print("Executing Morning Plan...")
    morning_plan(home)
    print("Executing Leave Home Plan...")
    leave_home_plan(home)
    print("Executing Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()