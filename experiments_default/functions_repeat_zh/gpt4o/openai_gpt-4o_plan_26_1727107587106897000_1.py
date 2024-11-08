# Certainly, I'll create a `function.py` file for your smart home project based on the functional description you provided. The main function will orchestrate the various actions for the three different plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here is the `function.py` file:

from home.sensor import LightIntensiveSensor
from home.actuator import CoffeeMachine, Curtain, MusicPlayer, Light, Door, SmartSocket
from home.home_plan import home_plan, get_room, get_all_actuators

def morning_plan(home):
    print("Executing Morning Plan...")
    # Turn on lights and adjust brightness based on indoor sunlight
    living_room = get_room(home, "LivingRoom")
    lights = [actuator for actuator in living_room.actuators if isinstance(actuator, Light)]
    for light in lights:
        light.turn_on()
        light.set_brightness_level("medium")

    # Make a cup of cappuccino
    kitchen = get_room(home, "Kitchen")
    coffee_machines = [actuator for actuator in kitchen.actuators if isinstance(actuator, CoffeeMachine)]
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Cappuccino")
    
    # Open curtains
    curtains = [actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)]
    for curtain in curtains:
        curtain.turn_on()
    
    # Play relaxing music
    music_players = [actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)]
    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Relaxing Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    # Close doors
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.turn_on()
        door.lock()
    
    # Turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
    
    # Turn off all smart sockets
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    # Close curtains
    living_room = get_room(home, "LivingRoom")
    curtains = [actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)]
    for curtain in curtains:
        curtain.turn_off()
    
    # Dim lights
    lights = [actuator for actuator in living_room.actuators if isinstance(actuator, Light)]
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

def main():
    home = home_plan()
    
    # Execute plans based on the current time or user command
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()