# Here is the `function.py` file based on your functional description and provided source code files. The code utilizes the classes and methods defined in the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.

from home_plan import home_plan, get_room, get_all_actuators, get_all_sensors
from config import LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def morning_plan(home):
    print("Starting Morning Plan...")
    
    # Define default settings
    light_level = "medium"
    coffee_type = "Cappuccino"
    playlist = "Relaxing Music"
    
    # Get all rooms
    rooms = home_plan()
    
    # Turn on lights in all rooms and adjust brightness
    all_lights = get_all_actuators(rooms, "Light")
    for light in all_lights:
        light.turn_on()
        light.set_brightness_level(light_level)
    
    # Make coffee in the kitchen
    kitchen = get_room(rooms, "Kitchen")
    if kitchen:
        for actuator in kitchen.actuators:
            if actuator.actuator_type == "CoffeeMachine":
                actuator.turn_on()
                actuator.make_coffee(coffee_type)
    
    # Open curtains in all rooms
    all_curtains = get_all_actuators(rooms, "Curtain")
    for curtain in all_curtains:
        curtain.turn_on()
        
    # Play relaxing music in all rooms
    all_music_players = get_all_actuators(rooms, "MusicPlayer")
    for music_player in all_music_players:
        music_player.turn_on()
        music_player.play_music(playlist)
    
    print("Morning Plan Completed.")

def leave_home_plan(home):
    print("Starting Leave Home Plan...")
    
    # Get all rooms
    rooms = home_plan()
    
    # Turn off all lights
    all_lights = get_all_actuators(rooms, "Light")
    for light in all_lights:
        light.turn_off()
    
    # Turn off all sockets
    all_sockets = get_all_actuators(rooms, "SmartSocket")
    for socket in all_sockets:
        socket.turn_off()
    
    # Lock all doors
    all_doors = get_all_actuators(rooms, "Door")
    for door in all_doors:
        door.turn_on()
        door.lock()
    
    print("Leave Home Plan Completed.")

def movie_plan(home):
    print("Starting Movie Plan...")
    
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        print("Living room not found!")
        return
    
    # Close curtains in the living room
    for actuator in living_room.actuators:
        if actuator.actuator_type == "Curtain":
            actuator.turn_on()
    
    # Dim lights in the living room
    for actuator in living_room.actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_on()
            actuator.set_brightness_level("low")
    
    print("Movie Plan Completed.")

def main():
    # Get home plan
    home = home_plan()
    
    # Morning plan at 7 AM
    morning_plan(home)
    time.sleep(1)  # Sleep for demonstration purposes
    
    # Leave home plan
    leave_home_plan(home)
    time.sleep(1)  # Sleep for demonstration purposes
    
    # Movie plan
    movie_plan(home)

if __name__ == "__main__":
    main()