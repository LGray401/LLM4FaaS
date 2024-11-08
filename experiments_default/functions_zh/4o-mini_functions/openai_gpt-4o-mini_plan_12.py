# Based on the provided functional description and source code, here is the `function.py` file that implements the three plans: Morning Plan, Leave Home Plan, and Movie Plan. This file will also include a main function that you can run to execute these plans.
# 
# ### functions/function.py

from home.home_plan import home_plan, get_room
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Door, Light, SmartTV

def morning_plan(home):
    print("\n--- Morning Plan ---")
    
    living_room = get_room(home, "LivingRoom")
    if living_room:
        curtains = [actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)]
        music_player = [actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)]
        coffee_machine = [actuator for actuator in living_room.actuators if isinstance(actuator, CoffeeMachine)]

        if curtains:
            curtains[0].turn_on()  # Open curtains
        if music_player:
            music_player[0].turn_on()  # Start music
            music_player[0].play_music("Morning Playlist")  # Play specific playlist
        if coffee_machine:
            coffee_machine[0].turn_on()  # Start coffee machine
            coffee_machine[0].make_coffee("Espresso")  # Make a specific type of coffee

def leave_home_plan(home):
    print("\n--- Leave Home Plan ---")
    
    main_entrance = get_room(home, "Entrance")
    if main_entrance:
        door = [actuator for actuator in main_entrance.actuators if isinstance(actuator, Door)]
        lights = [actuator for actuator in main_entrance.actuators if isinstance(actuator, Light)]
        
        if door:
            door[0].turn_off()  # Close the door
        if lights:
            lights[0].turn_off()  # Turn off the lights

def movie_plan(home):
    print("\n--- Movie Plan ---")
    
    living_room = get_room(home, "LivingRoom")
    if living_room:
        curtains = [actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)]
        tv = [actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)]

        if curtains:
            curtains[0].turn_off()  # Close curtains
        if tv:
            tv[0].turn_on()  # Turn on the TV
            tv[0].play_channel("Movie Channel")  # Play a specific channel

def main():
    home = home_plan()  # Initialize the home plan
    morning_plan(home)  # Execute the morning plan
    leave_home_plan(home)  # Execute the leave home plan
    movie_plan(home)  # Execute the movie plan

if __name__ == "__main__":
    main()