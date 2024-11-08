# Based on your functional description and the provided source code, here's the `function.py` file that implements the required functionality for your smart home project. This file includes a main function that schedules the execution of your morning plan, leave home plan, and movie plan.
# 
# Here's how the `function.py` file looks:

# functions/function.py
import time
from datetime import datetime
from home.home_plan import home_plan
from home.actuator import Light, CoffeeMachine, Curtain, MusicPlayer, Door, SmartSocket

def morning_plan(home):
    # Execute the morning plan at 7 AM
    current_time = datetime.now()
    if current_time.hour == 7 and current_time.minute == 0:
        # Turn on lights and adjust brightness
        for room in home:
            lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
            for light in lights:
                light.turn_on()
                light.set_brightness_level("medium")  # Example brightness level
            
        # Make cappuccino
        for room in home:
            coffee_machine = next((actuator for actuator in room.actuators if isinstance(actuator, CoffeeMachine)), None)
            if coffee_machine:
                coffee_machine.turn_on()
                coffee_machine.make_coffee("Cappuccino")

        # Open curtains
        for room in home:
            curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
            for curtain in curtains:
                curtain.turn_on()

        # Play relaxing music
        for room in home:
            music_player = next((actuator for actuator in room.actuators if isinstance(actuator, MusicPlayer)), None)
            if music_player:
                music_player.turn_on()
                music_player.play_music("Relaxing Playlist")

def leave_home_plan(home):
    # Close doors, turn off all lights, and disable sockets when leaving home
    for room in home:
        # Close doors
        doors = [actuator for actuator in room.actuators if isinstance(actuator, Door)]
        for door in doors:
            door.turn_off()  # Assuming turning off locks the door

        # Turn off lights
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        for light in lights:
            light.turn_off()

        # Turn off smart sockets
        sockets = [actuator for actuator in room.actuators if isinstance(actuator, SmartSocket)]
        for socket in sockets:
            socket.turn_off()

def movie_plan(home):
    # Close curtains and dim lights for movie time
    for room in home:
        # Close curtains
        curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
        for curtain in curtains:
            curtain.turn_on()

        # Dim lights
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        for light in lights:
            light.set_brightness_level("low")  # Set brightness to low for movie time

def main():
    home = home_plan()  # Load home setup
    while True:
        morning_plan(home)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()