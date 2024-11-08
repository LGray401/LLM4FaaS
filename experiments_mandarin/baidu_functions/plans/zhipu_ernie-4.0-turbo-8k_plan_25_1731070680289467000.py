# Based on your functional description and the provided source code, here is the `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN:

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, MusicPlayer, CoffeeMachine, Door, SmartSocket
import home.config as config

def morning_plan(home):
    # Get the bedroom
    bedroom = get_room(home, "Bedroom")
    if not bedroom:
        return

    # Get light sensor in the bedroom
    light_sensors = get_all_sensors(home, "LightIntensive")
    light_intensity = sum([sensor.get_reading() for sensor in light_sensors if sensor.room_name == "Bedroom"]) / len(light_sensors)
    
    # Execute the morning plan if light intensity is high enough
    if light_intensity >= config.LIGHT_INTENSITY_HIGH:
        # Open curtains
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            if curtain.room_name == "Bedroom":
                curtain.turn_on()  # Assuming turn_on() opens the curtains

        # Turn off bedroom lights
        lights = get_all_actuators(home, "Light")
        for light in lights:
            if light.room_name == "Bedroom":
                light.turn_off()

        # Turn on music player
        music_players = get_all_actuators(home, "MusicPlayer")
        for music_player in music_players:
            if music_player.room_name == "Bedroom":
                music_player.turn_on()
                music_player.play_music("Morning Playlist")

        # Start coffee machine
        coffee_machines = get_all_actuators(home, "CoffeeMachine")
        for coffee_machine in coffee_machines:
            if coffee_machine.room_name == "Kitchen":
                coffee_machine.turn_on()
                coffee_machine.make_coffee("Espresso")

def leave_home_plan(home):
    # Get the main door
    doors = get_all_actuators(home, "Door")
    for door in doors:
        if door.room_name == "LivingRoom" or door.room_name == "MainEntrance":  # Assuming main door is in LivingRoom or MainEntrance
            door.lock()

    # Get all curtains and close them
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()  # Assuming turn_off() closes the curtains

    # Turn off all indoor lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # Turn off all sockets
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

def movie_plan(home):
    # Turn on the TV
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        if tv.room_name == "LivingRoom":
            tv.turn_on()
            tv.play_channel("Movie Channel")

    # Close the curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        if curtain.room_name == "LivingRoom":
            curtain.turn_off()  # Assuming turn_off() closes the curtains

    # Dim the lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        if light.room_name == "LivingRoom":
            light.set_brightness_level("low")

# Main function to execute plans based on input
def main():
    home = home_plan()
    
    # Example usage:
    # Uncomment the following lines to test the plans
    
    # morning_plan(home)
    # leave_home_plan(home)
    # movie_plan(home)

if __name__ == "__main__":
    main()