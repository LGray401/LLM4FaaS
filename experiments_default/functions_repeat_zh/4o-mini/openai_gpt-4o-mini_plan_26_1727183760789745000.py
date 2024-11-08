# Based on your functional description and the provided source code, I've created a `function.py` file that implements the required functionalities for your smart home project. The code will handle the "MORNING PLAN," "LEAVE HOME PLAN," and "MOVIE PLAN" as specified.
# 
# Here is the content for the `function.py` file:

# function.py

from datetime import datetime
import time
from home.home_plan import home_plan
from home.actuator import Light, CoffeeMachine, Curtain, MusicPlayer, Door, SmartSocket

def morning_plan(home):
    current_time = datetime.now()
    if current_time.hour == 7 and current_time.minute == 0:
        print("Executing morning plan...")

        for room in home:
            # Turn on Lights and adjust brightness
            lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
            for light in lights:
                light.turn_on()
                sunlight_intensity = get_sunlight_intensity(room)  # Assuming we have a function to get this
                if sunlight_intensity < 300:  # Example threshold for adjusting brightness
                    light.set_brightness_level('high')
                elif sunlight_intensity < 600:
                    light.set_brightness_level('medium')
                else:
                    light.set_brightness_level('low')

            # Make coffee
            coffee_machine = [actuator for actuator in room.actuators if isinstance(actuator, CoffeeMachine)]
            if coffee_machine:
                coffee_machine[0].turn_on()
                coffee_machine[0].make_coffee("Cappuccino")

            # Open curtains
            curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
            for curtain in curtains:
                curtain.turn_on()

            # Play relaxing music
            music_player = [actuator for actuator in room.actuators if isinstance(actuator, MusicPlayer)]
            if music_player:
                music_player[0].turn_on()
                music_player[0].play_music("Relaxing Playlist")
        
def leave_home_plan(home):
    print("Executing leave home plan...")
    for room in home:
        # Close the door
        doors = [actuator for actuator in room.actuators if isinstance(actuator, Door)]
        for door in doors:
            door.turn_off()  # Assuming turning off closes the door

        # Turn off all lights
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        for light in lights:
            light.turn_off()

        # Turn off all smart sockets
        smart_sockets = [actuator for actuator in room.actuators if isinstance(actuator, SmartSocket)]
        for socket in smart_sockets:
            socket.turn_off()

def movie_plan(home):
    print("Executing movie plan...")
    for room in home:
        # Close curtains
        curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
        for curtain in curtains:
            curtain.turn_on()

        # Dim lights
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        for light in lights:
            light.set_brightness_level('low')

def get_sunlight_intensity(room):
    # This function should return the sunlight intensity based on the sensors in the room
    # For now, we will return a mock value
    return 500  # Example mock value; replace with actual sensor reading logic

def main():
    home = home_plan()

    # Run plans based on time and conditions
    while True:
        morning_plan(home)
        leave_home_plan(home)
        movie_plan(home)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()