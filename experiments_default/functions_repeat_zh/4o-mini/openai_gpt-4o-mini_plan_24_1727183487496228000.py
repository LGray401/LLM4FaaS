# Based on the functional description and the provided source code for your smart home project, I will create the `function.py` file that implements the three plans: Morning Plan, Leave Home Plan, and Movie Plan. This file will manage the interaction between sensors and actuators to execute the specified actions.
# 
# Here is the `function.py` file content:

# function.py
from home.home_plan import home_plan, get_room, get_room_actuators, get_all_sensors
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door
import random

def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    
    # Open curtains in the living room
    for actuator in get_room_actuators(home, "LivingRoom"):
        if isinstance(actuator, Curtain):
            actuator.turn_on()  # Open curtains

    # Check the light intensity in the living room
    light_sensor = get_all_sensors(home, "LightIntensive")
    if light_sensor:
        light_reading = light_sensor[0].get_reading()
        if light_reading < 300:  # Assuming 300 lux is the threshold for turning on lights
            for actuator in get_room_actuators(home, "LivingRoom"):
                if isinstance(actuator, Light):
                    actuator.turn_on()  # Turn on lights

    # Make coffee
    coffee_machine = get_all_sensors(home, "CoffeeMachine")
    if coffee_machine:
        coffee_machine[0].turn_on()  # Turn on coffee machine
        coffee_machine[0].make_coffee("Espresso")  # Assuming we make espresso

    # Play music after coffee is ready
    music_player = get_all_sensors(home, "MusicPlayer")
    if music_player:
        music_player[0].turn_on()  # Turn on music player
        music_player[0].play_music("Morning Playlist")  # Play morning playlist

def leave_home_plan(home):
    living_room = get_room(home, "LivingRoom")
    outdoor_sensor = get_all_sensors(home, "OutdoorTemperature")

    # Open curtains in the living room if the weather is sunny
    if outdoor_sensor and outdoor_sensor[0].get_reading() > 20:  # Assuming 20°C is sunny
        for actuator in get_room_actuators(home, "LivingRoom"):
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Open curtains

    # Turn off lights and smart sockets
    for actuator in get_room_actuators(home, "LivingRoom"):
        if isinstance(actuator, Light) or isinstance(actuator, SmartSocket):
            actuator.turn_off()  # Turn off lights and sockets

    # Lock the door
    door = get_all_sensors(home, "Door")
    if door:
        door[0].lock()  # Lock the door

def movie_plan(home):
    living_room = get_room(home, "LivingRoom")

    # Close curtains
    for actuator in get_room_actuators(home, "LivingRoom"):
        if isinstance(actuator, Curtain):
            actuator.turn_off()  # Close curtains

    # Turn off lights
    for actuator in get_room_actuators(home, "LivingRoom"):
        if isinstance(actuator, Light):
            actuator.turn_off()  # Turn off lights

def main():
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()