# Sure, based on your functional description and the provided source code, here is the `function.py` file that implements the main function to handle your smart home plans:

import time
from home.home_plan import home_plan, get_room_actuators, get_all_actuators
from home.config import LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def morning_plan(home):
    rooms = ["LivingRoom", "Bedroom", "Kitchen"]

    # Turn on lights and adjust brightness based on sunlight intensity
    for room_name in rooms:
        lights = [actuator for actuator in get_room_actuators(home, room_name) if actuator.actuator_type == "Light"]
        for light in lights:
            light.turn_on()
        
        light_sensors = [sensor for sensor in get_room_actuators(home, room_name) if sensor.sensor_type == "LightIntensive"]
        for sensor in light_sensors:
            light_intensity = sensor.get_reading()
            if light_intensity < LIGHT_INTENSITY_LOW:
                for light in lights:
                    light.set_brightness_level("high")
            elif light_intensity > LIGHT_INTENSITY_HIGH:
                for light in lights:
                    light.set_brightness_level("low")
            else:
                for light in lights:
                    light.set_brightness_level("medium")

    # Make coffee
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    coffee_machines = [actuator for actuator in kitchen_actuators if actuator.actuator_type == "CoffeeMachine"]
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Cappuccino")

    # Open curtains
    for room_name in rooms:
        curtains = [actuator for actuator in get_room_actuators(home, room_name) if actuator.actuator_type == "Curtain"]
        for curtain in curtains:
            curtain.turn_on()

    # Play relaxing music
    for room_name in rooms:
        music_players = [actuator for actuator in get_room_actuators(home, room_name) if actuator.actuator_type == "MusicPlayer"]
        for music_player in music_players:
            music_player.turn_on()
            music_player.play_music("Relaxing Playlist")


def leave_home_plan(home):
    # Close door
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.turn_on()
        door.lock()

    # Turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
    
    # Turn off all smart sockets
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()


def movie_plan(home):
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Close curtains
    curtains = [actuator for actuator in living_room_actuators if actuator.actuator_type == "Curtain"]
    for curtain in curtains:
        curtain.turn_on()

    # Dim lights
    lights = [actuator for actuator in living_room_actuators if actuator.actuator_type == "Light"]
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")


def main():
    home = home_plan()
    
    # Assuming you want to run the morning plan at 7 AM
    current_hour = time.localtime().tm_hour
    if current_hour == 7:
        morning_plan(home)
    
    # You can add triggers for leave_home_plan and movie_plan as needed
    # For example:
    # leave_home_plan(home) when leaving home
    # movie_plan(home) when starting to watch a movie

if __name__ == "__main__":
    main()