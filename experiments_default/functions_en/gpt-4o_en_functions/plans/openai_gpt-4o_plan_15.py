# Based on the provided functional description and source code, I will create a `function.py` file that defines the main function to execute the specified home plans (MORNING PLAN, LEAVE HOME PLAN, MOVIE PLAN). This main function will utilize the components defined in your `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 
# Here is the `function.py` file content:

# functions/function.py

from home.home_plan import home_plan, get_room, get_all_actuators, get_all_sensors
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def morning_plan(home):
    print("Executing Morning Plan...")
    
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")
    bedroom = get_room(home, "Bedroom")

    # Turn on the coffee machine in the kitchen
    coffee_machines = [actuator for actuator in kitchen.actuators if actuator.actuator_type == "CoffeeMachine"]
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")
    
    # Open the curtains in the living room and bedroom
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # Turn on the lights in the living room and bedroom
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("high")
    
    # Turn on the music player in the living room
    music_players = [actuator for actuator in living_room.actuators if actuator.actuator_type == "MusicPlayer"]
    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Morning Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    # Turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # Lock all doors
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()

    # Turn off all music players and TVs
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.turn_off()

    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        tv.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    
    living_room = get_room(home, "LivingRoom")

    # Turn off all lights except in the living room
    lights = get_all_actuators(home, "Light")
    for light in lights:
        if light.room_name != "LivingRoom":
            light.turn_off()

    # Set living room light to low brightness
    living_room_lights = [light for light in lights if light.room_name == "LivingRoom"]
    for light in living_room_lights:
        light.turn_on()
        light.set_brightness_level("low")

    # Close the curtains in the living room
    curtains = [actuator for actuator in living_room.actuators if actuator.actuator_type == "Curtain"]
    for curtain in curtains:
        curtain.turn_off()

    # Turn on the TV in the living room
    tvs = [actuator for actuator in living_room.actuators if actuator.actuator_type == "SmartTV"]
    for tv in tvs:
        tv.turn_on()
        tv.play_channel("Netflix")

def main():
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()