# Here is the `function.py` file based on your functional description and the provided source code. This file will implement the main function that executes the specified plans for your smart home project.

# function.py
from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Light, SmartTV, Door

def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Open curtains
        curtains = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Curtain)]
        for curtain in curtains:
            curtain.turn_on()  # Assume turn_on opens the curtain

        # Start music player
        music_players = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, MusicPlayer)]
        for music_player in music_players:
            music_player.turn_on()
            music_player.play_music("morning playlist")

        # Make coffee
        coffee_machine = [actuator for actuator in get_room_actuators(home, "Kitchen") if isinstance(actuator, CoffeeMachine)]
        if coffee_machine:
            coffee_machine[0].turn_on()
            coffee_machine[0].make_coffee("espresso")  # Specify coffee type

def leave_home_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Close lights
        lights = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Light)]
        for light in lights:
            light.turn_off()
        
        # Lock the door
        door = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Door)]
        if door:
            door[0].lock()

        # Turn off all sockets except fridge (assuming we have a smart fridge actuator)
        smart_sockets = [actuator for actuator in get_room_actuators(home, "Kitchen") if isinstance(actuator, SmartSocket)]
        for socket in smart_sockets:
            socket.turn_off()

def movie_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Close curtains
        curtains = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Curtain)]
        for curtain in curtains:
            curtain.turn_off()  # Assume turn_off closes the curtain

        # Dim lights
        lights = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Light)]
        for light in lights:
            light.set_brightness_level("low")  # Set brightness to low

        # Start the TV
        smart_tv = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, SmartTV)]
        if smart_tv:
            smart_tv[0].turn_on()
            smart_tv[0].play_channel("favorite show")

def main():
    home = home_plan()
    
    # Execute the plans
    print("Executing Morning Plan...")
    morning_plan(home)

    print("\nExecuting Leave Home Plan...")
    leave_home_plan(home)

    print("\nExecuting Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()