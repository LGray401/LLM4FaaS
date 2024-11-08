# Based on your functional description and the provided source code files, here is the `function.py` file that implements the three plans: `MORNING PLAN`, `LEAVE HOME PLAN`, and `MOVIE PLAN`. This file will utilize the classes defined in your other modules to carry out the specified actions.
# 
# ### `function.py`

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light, Curtain, CoffeeMachine, MusicPlayer, Door, SmartTV, Window

def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Open curtains
        curtains = get_room_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_on()
        
        # Set light brightness to medium
        lights = get_room_actuators(home, "Light")
        for light in lights:
            light.turn_on()
            light.set_brightness_level("medium")
        
        # Start coffee machine
        coffee_machine = next((actuator for actuator in living_room.actuators if isinstance(actuator, CoffeeMachine)), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")
        
        # Play music
        music_player = next((actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("Morning Playlist")

def leave_home_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Turn off lights
        lights = get_room_actuators(home, "Light")
        for light in lights:
            light.turn_off()

        # Close curtains
        curtains = get_room_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_off()

        # Turn off smart sockets
        smart_sockets = get_room_actuators(home, "SmartSocket")
        for socket in smart_sockets:
            socket.turn_off()

        # Lock the door
        door = next((actuator for actuator in living_room.actuators if isinstance(actuator, Door)), None)
        if door:
            door.lock()

def movie_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Close windows
        windows = get_room_actuators(home, "Window")
        for window in windows:
            window.turn_off()  # Assuming turning off closes the window

        # Dim lights
        lights = get_room_actuators(home, "Light")
        for light in lights:
            light.turn_on()
            light.set_brightness_level("low")

        # Play TV channel
        tv = next((actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)), None)
        if tv:
            tv.turn_on()
            tv.play_channel("Movie Channel")

def main():
    home = home_plan()
    
    # Run the morning plan
    print("Executing MORNING PLAN...")
    morning_plan(home)
    
    # Run the leave home plan
    print("\nExecuting LEAVE HOME PLAN...")
    leave_home_plan(home)
    
    # Run the movie plan
    print("\nExecuting MOVIE PLAN...")
    movie_plan(home)

if __name__ == "__main__":
    main()