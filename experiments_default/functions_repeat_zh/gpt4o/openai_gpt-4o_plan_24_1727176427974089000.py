# Based on the provided functional description and source code, I will create a `function.py` file to implement the specified plans: Morning Plan, Leave Home Plan, and Movie Plan.
# 
# Here's the `function.py` file:

# functions/function.py

from home.sensor import LightIntensiveSensor, OutdoorTemperatureSensor
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door, SmartSocket, Window
from home.home_plan import home_plan, get_room, get_room_actuators

def morning_plan(home):
    print("Executing Morning Plan")
    living_room = get_room(home, "LivingRoom")
    
    # Open curtain
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
    
    # Check outdoor light intensity
    outdoor_light_sensor = next(sensor for sensor in get_room(home, "Balcony").sensors if isinstance(sensor, OutdoorTemperatureSensor))
    outdoor_light_sensor.turn_on()
    outdoor_light_intensity = outdoor_light_sensor.get_reading()
    
    if outdoor_light_intensity and outdoor_light_intensity < 900:  # Assuming 900 as the threshold
        for actuator in living_room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
    
    # Make coffee
    kitchen = get_room(home, "Kitchen")
    coffee_machine = next(actuator for actuator in kitchen.actuators if isinstance(actuator, CoffeeMachine))
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")
    
    # Play music
    if coffee_machine.status == "on":
        living_room_music_player = next(actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer))
        living_room_music_player.turn_on()
        living_room_music_player.play_music("Morning Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan")
    living_room = get_room(home, "LivingRoom")
    
    # Check outdoor weather
    outdoor_light_sensor = next(sensor for sensor in get_room(home, "Balcony").sensors if isinstance(sensor, OutdoorTemperatureSensor))
    outdoor_light_sensor.turn_on()
    outdoor_light_intensity = outdoor_light_sensor.get_reading()
    
    if outdoor_light_intensity and outdoor_light_intensity > 900:  # Assuming 900 as the threshold for sunny day
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()
    
    # Turn off lights
    for actuator in get_all_actuators(home, "Light"):
        actuator.turn_off()
    
    # Turn off sockets
    for actuator in get_all_actuators(home, "SmartSocket"):
        actuator.turn_off()
    
    # Lock doors
    for actuator in get_all_actuators(home, "Door"):
        actuator.lock()

def movie_plan(home):
    print("Executing Movie Plan")
    living_room = get_room(home, "LivingRoom")
    
    # Close curtains
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()
    
    # Turn off lights
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

def main():
    home = home_plan()
    
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()