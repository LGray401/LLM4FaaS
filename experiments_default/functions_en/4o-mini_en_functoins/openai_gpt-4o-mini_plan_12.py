# Based on the functional description and the provided source code, here is the `function.py` file that implements the specified plans for your smart home project. This file will contain a main function that executes the morning, leave home, and movie plans by interacting with the actuators defined in your existing code.

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Door, Light, SmartTV

def execute_morning_plan(home):
    print("Executing Morning Plan...")
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Open curtains
        curtains = [actor for actor in living_room.actuators if isinstance(actor, Curtain)]
        for curtain in curtains:
            curtain.turn_on()

        # Play music
        music_player = [actor for actor in living_room.actuators if isinstance(actor, MusicPlayer)]
        if music_player:
            music_player[0].turn_on()
            music_player[0].play_music("Morning Playlist")

        # Start coffee machine
        coffee_machine = [actor for actor in living_room.actuators if isinstance(actor, CoffeeMachine)]
        if coffee_machine:
            coffee_machine[0].turn_on()
            coffee_machine[0].make_coffee("Espresso")

def execute_leave_home_plan(home):
    print("Executing Leave Home Plan...")
    door = get_room_actuators(home, "Door")
    if door:
        door[0].turn_off()  # Close Door
    lights = get_room_actuators(home, "Light")
    for light in lights:
        light.turn_off()  # Turn off lights

def execute_movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Close curtains
        curtains = [actor for actor in living_room.actuators if isinstance(actor, Curtain)]
        for curtain in curtains:
            curtain.turn_off()

        # Turn on TV
        smart_tv = [actor for actor in living_room.actuators if isinstance(actor, SmartTV)]
        if smart_tv:
            smart_tv[0].turn_on()
            smart_tv[0].play_channel("Movie Channel")

def main():
    home = home_plan()

    # Execute plans
    execute_morning_plan(home)
    execute_leave_home_plan(home)
    execute_movie_plan(home)

if __name__ == "__main__":
    main()