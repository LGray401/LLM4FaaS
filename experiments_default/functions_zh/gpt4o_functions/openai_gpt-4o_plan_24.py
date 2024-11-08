# Based on your requirements and the provided code, I will create the `function.py` file to handle the main functions for the smart home project. This file will include the core logic to execute the Morning Plan, Leave Home Plan, and Movie Plan.
# 
# Here's the `function.py` file:

# functions/function.py

from home.sensor import LightIntensiveSensor, OutdoorTemperatureSensor
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door, SmartSocket
from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators

def morning_plan(home):
    print("Executing Morning Plan...")
    
    # Open curtains in all rooms
    for curtain in get_all_actuators(home, "Curtain"):
        curtain.turn_on()
    
    # Check if it's cloudy, if so, turn on lights
    outdoor_temp_sensor = get_all_sensors(home, "OutdoorTemperature")[0]
    outdoor_temp_sensor.turn_on()
    if outdoor_temp_sensor.get_reading() < 20:  # Assuming < 20 as cloudy
        for light in get_all_actuators(home, "Light"):
            light.turn_on()
    
    # Make coffee
    coffee_machine = get_all_actuators(home, "CoffeeMachine")[0]
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")
    
    # Play music after coffee is made
    music_player = get_all_actuators(home, "MusicPlayer")[0]
    music_player.turn_on()
    music_player.play_music("Morning Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    # Open curtains if it's sunny
    outdoor_temp_sensor = get_all_sensors(home, "OutdoorTemperature")[0]
    outdoor_temp_sensor.turn_on()
    if outdoor_temp_sensor.get_reading() > 20:  # Assuming > 20 as sunny
        for curtain in get_all_actuators(home, "Curtain"):
            curtain.turn_on()
    
    # Turn off lights and smart sockets
    for light in get_all_actuators(home, "Light"):
        light.turn_off()
    for socket in get_all_actuators(home, "SmartSocket"):
        socket.turn_off()
    
    # Lock the doors
    for door in get_all_actuators(home, "Door"):
        door.turn_off()
        door.lock()

def movie_plan(home):
    print("Executing Movie Plan...")
    
    # Close curtains
    for curtain in get_all_actuators(home, "Curtain"):
        curtain.turn_off()
    
    # Turn off lights
    for light in get_all_actuators(home, "Light"):
        light.turn_off()

def main():
    # Initialize home and get the plan
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()