# Based on the provided functional description and the source code for your smart home project, I will create a `function.py` file that implements the three plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. The `function.py` will contain a main function that invokes these plans based on specific conditions. 
# 
# Here's the implementation of `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door
from home.sensor import LightIntensiveSensor, OutdoorTemperatureSensor
import random

def morning_plan(home):
    print("Executing Morning Plan...")
    
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")
    
    # Open curtains
    curtains = get_room_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # Check light intensity for lighting condition
    light_sensor = get_all_sensors(home, "LightIntensive")
    if light_sensor:
        light_reading = light_sensor[0].get_reading()
        if light_reading and light_reading < 300:  # Assuming < 300 lux is considered 'cloudy'
            lights = get_room_actuators(home, "Light")
            for light in lights:
                light.turn_on()

    # Make coffee
    coffee_machine = get_all_actuators(home, "CoffeeMachine")
    if coffee_machine:
        coffee_machine[0].turn_on()
        coffee_machine[0].make_coffee("Espresso")  # Example coffee type

    # Play music
    music_player = get_all_actuators(home, "MusicPlayer")
    if music_player:
        music_player[0].turn_on()
        music_player[0].play_music("Morning Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    outdoor_sensor = get_all_sensors(home, "OutdoorTemperature")
    if outdoor_sensor:
        outdoor_reading = outdoor_sensor[0].get_reading()
        if outdoor_reading and outdoor_reading >= 25:  # Assuming >= 25 degrees is sunny
            curtains = get_all_actuators(home, "Curtain")
            for curtain in curtains:
                curtain.turn_off()
        
    # Turn off lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # Turn off sockets
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

    # Lock door
    door = get_all_actuators(home, "Door")
    if door:
        door[0].lock()

def movie_plan(home):
    print("Executing Movie Plan...")
    
    living_room = get_room(home, "LivingRoom")
    
    # Close curtains
    curtains = get_room_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()
    
    # Turn off lights
    lights = get_room_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def main():
    home = home_plan()

    # Example use case: Execute each plan based on random selection for demonstration
    plans = [morning_plan, leave_home_plan, movie_plan]
    selected_plan = random.choice(plans)

    selected_plan(home)

if __name__ == "__main__":
    main()