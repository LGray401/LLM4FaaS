# Based on your functional description and the provided source code, here is a `function.py` file that encapsulates the morning plan, leave home plan, and movie plan functionalities. This file will utilize the classes and methods defined in your existing code. 
# 
# You need to ensure that the `functions` directory exists alongside your `home` directory for this to work.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door
from home.sensor import LightIntensiveSensor
from home.logger_config import logger

def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    
    # Open curtains in the bedroom
    bedroom_curtain = next((actuator for actuator in get_room_actuators(home, "Bedroom") if isinstance(actuator, Curtain)), None)
    if bedroom_curtain:
        bedroom_curtain.turn_on()  # Open curtains

    # Check if it is cloudy using the light intensity sensor
    light_sensor = next((sensor for sensor in get_room_sensors(home, "LivingRoom") if isinstance(sensor, LightIntensiveSensor)), None)
    if light_sensor:
        light_sensor.turn_on()  # Turn on the light sensor to get readings
        light_reading = light_sensor.get_reading()
        if light_reading is not None and light_reading < 300:  # Assuming 300 lux is cloudy
            living_room_light = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Light)), None)
            if living_room_light:
                living_room_light.turn_on()  # Turn on lights if cloudy

    # Make coffee
    coffee_machine = next((actuator for actuator in get_room_actuators(home, "Kitchen") if isinstance(actuator, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.turn_on()  # Turn on coffee machine
        coffee_machine.make_coffee("Your favorite coffee")  # Replace with actual coffee type

    # Play music
    music_player = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, MusicPlayer)), None)
    if music_player:
        music_player.turn_on()  # Turn on music player
        music_player.play_music("Morning Playlist")  # Replace with actual playlist

def leave_home_plan(home):
    living_room = get_room(home, "LivingRoom")
    
    # Open curtains in living room
    living_room_curtain = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Curtain)), None)
    if living_room_curtain:
        living_room_curtain.turn_on()  # Open curtains

    # Turn off lights if it's sunny
    light_sensor = next((sensor for sensor in get_room_sensors(home, "LivingRoom") if isinstance(sensor, LightIntensiveSensor)), None)
    if light_sensor:
        light_sensor.turn_on()  # Turn on the light sensor to get readings
        light_reading = light_sensor.get_reading()
        if light_reading is not None and light_reading >= 300:  # Assuming 300 lux is sunny
            living_room_light = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Light)), None)
            if living_room_light:
                living_room_light.turn_off()  # Turn off lights if sunny

    # Turn off sockets
    smart_sockets = get_room_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()  # Turn off all smart sockets

    # Lock the door
    door = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Door)), None)
    if door:
        door.lock()  # Lock the door

def movie_plan(home):
    living_room = get_room(home, "LivingRoom")
    
    # Close curtains in living room
    living_room_curtain = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Curtain)), None)
    if living_room_curtain:
        living_room_curtain.turn_off()  # Close curtains

    # Turn off lights
    living_room_light = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Light)), None)
    if living_room_light:
        living_room_light.turn_off()  # Turn off lights

def main():
    home = home_plan()  # Initialize home plan

    # Execute the plans
    print("Executing morning plan...")
    morning_plan(home)

    print("Executing leave home plan...")
    leave_home_plan(home)

    print("Executing movie plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()