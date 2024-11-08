# Based on the functional description and the provided source code, here is the `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN:

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, MusicPlayer, Door, Light

def morning_plan(home):
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Get light intensity sensor
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        if sensor.room_name == "LivingRoom":
            sensor.turn_on()
            light_intensity = sensor.get_reading()
            if light_intensity >= 900:  # Assuming 900 is the threshold for "increased light intensity"
                # Open curtains
                curtains = get_all_actuators(living_room.actuators, "Curtain")
                for curtain in curtains:
                    curtain.turn_on()  # Assuming turn_on() opens the curtains

                # Play music
                music_players = get_all_actuators(living_room.actuators, "MusicPlayer")
                for music_player in music_players:
                    music_player.turn_on()
                    music_player.play_music("Morning Playlist")  # Assuming a default playlist
                break

def leave_home_plan(home):
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Close the entry door
    doors = get_all_actuators(living_room.actuators, "Door")
    for door in doors:
        door.turn_off()  # Assuming turn_off() closes and/or locks the door
        door.lock()

    # Open curtains
    curtains = get_all_actuators(living_room.actuators, "Curtain")
    for curtain in curtains:
        curtain.turn_on()  # Assuming turn_on() opens the curtains

    # Turn off lights
    lights = get_all_actuators(living_room.actuators, "Light")
    for light in lights:
        light.turn_off()

def movie_plan(home):
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Close curtains
    curtains = get_all_actuators(living_room.actuators, "Curtain")
    for curtain in curtains:
        curtain.turn_off()  # Assuming turn_off() closes the curtains

    # Dim lights
    lights = get_all_actuators(living_room.actuators, "Light")
    for light in lights:
        light.set_brightness_level("low")  # Set to low brightness

# Helper function to get actuators from a room's actuator list by type
def get_all_actuators(actuators, actuator_type):
    return [actuator for actuator in actuators if actuator.actuator_type == actuator_type]

if __name__ == "__main__":
    home = home_plan()
    
    # Test the plans
    morning_plan(home)
    # leave_home_plan(home)
    # movie_plan(home)