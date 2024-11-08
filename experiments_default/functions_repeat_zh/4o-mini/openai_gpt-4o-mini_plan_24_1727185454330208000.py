# Based on the functional description you provided, I will create a `function.py` file that contains a main function to execute the specified plans for your smart home project. The `function.py` will be located in the `functions` folder.
# 
# Here's the `function.py`:

# function.py

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door
from home.sensor import LightIntensiveSensor
import random

def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Open curtains
        curtains = get_all_actuators(living_room, Curtain)
        for curtain in curtains:
            curtain.turn_on()
        
        # Check light intensity and turn on light if it's a cloudy day
        light_sensor = get_all_sensors(living_room, LightIntensiveSensor)
        if light_sensor:
            sensor_reading = light_sensor[0].get_reading()  # Only take one reading for this example
            if sensor_reading and sensor_reading < 400:  # Assuming 400 lux is the threshold for cloudy
                lights = get_all_actuators(living_room, Light)
                for light in lights:
                    light.turn_on()
        
        # Make coffee
        coffee_machine = get_all_actuators(living_room, CoffeeMachine)
        if coffee_machine:
            coffee_machine[0].turn_on()  # Turn on the coffee machine
            coffee_machine[0].make_coffee("Espresso")  # Prepare coffee
        
        # Play music
        music_player = get_all_actuators(living_room, MusicPlayer)
        if music_player:
            music_player[0].turn_on()
            music_player[0].play_music("Morning Playlist")

def leave_home_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Open curtains
        curtains = get_all_actuators(living_room, Curtain)
        for curtain in curtains:
            curtain.turn_on()
        
        # Check light intensity and turn off lights if it's sunny
        light_sensor = get_all_sensors(living_room, LightIntensiveSensor)
        if light_sensor:
            sensor_reading = light_sensor[0].get_reading()
            if sensor_reading and sensor_reading >= 400:  # Assuming 400 lux is the threshold for sunny
                lights = get_all_actuators(living_room, Light)
                for light in lights:
                    light.turn_off()
        
        # Turn off sockets and lock the door
        sockets = get_all_actuators(living_room, "SmartSocket")
        for socket in sockets:
            socket.turn_off()
        
        door = get_all_actuators(living_room, Door)
        if door:
            door[0].lock()

def movie_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Close curtains
        curtains = get_all_actuators(living_room, Curtain)
        for curtain in curtains:
            curtain.turn_off()
        
        # Turn off lights
        lights = get_all_actuators(living_room, Light)
        for light in lights:
            light.turn_off()

def main():
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()