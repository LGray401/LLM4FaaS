# Based on the functional description you've provided, I'll create the `function.py` file for your smart home project. This file will implement the required morning plan, leave home plan, and movie plan functionality. 
# 
# Here's the implementation of `function.py`:

# functions/function.py

import time
from home.home_plan import home_plan
from home.actuator import Light, CoffeeMachine, Curtain, MusicPlayer, Door, SmartSocket

def morning_plan(home):
    current_time = time.localtime()
    if current_time.tm_hour == 7 and current_time.tm_min == 0:
        for room in home:
            # Turn on lights and adjust brightness based on the light intensity
            light_actuators = get_room_actuators(home, room.name)
            for light in light_actuators:
                light.turn_on()
                # Here we would adjust the brightness based on the light intensity sensor readings
                light.set_brightness_level('medium')  # Replace with actual sensor reading logic
            
            # Make coffee
            coffee_machine = next((act for act in room.actuators if isinstance(act, CoffeeMachine)), None)
            if coffee_machine:
                coffee_machine.turn_on()
                coffee_machine.make_coffee("Cappuccino")
            
            # Open curtains
            curtain_actuators = get_room_actuators(home, room.name)
            for curtain in curtain_actuators:
                if isinstance(curtain, Curtain):
                    curtain.turn_on()  # Assuming turning on opens the curtain
            
            # Play relaxing music
            music_player = next((act for act in room.actuators if isinstance(act, MusicPlayer)), None)
            if music_player:
                music_player.turn_on()
                music_player.play_music("Relaxing Playlist")

def leave_home_plan(home):
    for room in home:
        # Close door
        door_actuator = next((act for act in room.actuators if isinstance(act, Door)), None)
        if door_actuator:
            door_actuator.turn_off()  # Assuming turn off locks the door
        
        # Turn off all lights
        light_actuators = get_room_actuators(home, room.name)
        for light in light_actuators:
            light.turn_off()
        
        # Turn off all smart sockets
        smart_sockets = get_all_actuators(home, "SmartSocket")
        for socket in smart_sockets:
            socket.turn_off()

def movie_plan(home):
    # Assuming you are in the living room for watching a movie
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Close curtains
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_on()  # Assuming turning on closes the curtain
        
        # Dim lights
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.set_brightness_level('low')  # Dim lights for movie

def get_room_actuators(home, room_name):
    for room in home:
        if room.name == room_name:
            return room.actuators
    return []

def get_all_actuators(home, actuator_type):
    all_actuators = []
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == actuator_type:
                all_actuators.append(actuator)
    return all_actuators

def main():
    home = home_plan()
    
    # Execute plans based on conditions
    while True:
        morning_plan(home)
        leave_home_plan(home)
        movie_plan(home)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()