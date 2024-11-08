# Here is the `function.py` file for your smart home project based on the functional description you provided. This file contains a main function that executes the morning plan, leave home plan, and movie plan.

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Curtain, Door, Light, MusicPlayer
from home.sensor import LightIntensiveSensor

def morning_plan(home):
    print("Executing MORNING PLAN...")
    living_room = next(room for room in home if room.name == "LivingRoom")
    
    # Light intensity sensor to check if it's morning
    light_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "LightIntensive")
    light_sensor.turn_on()  # Simulate turning on the light sensor to get readings
    light_reading = light_sensor.get_reading()  # Get the current light intensity
    
    if light_reading and light_reading > 900:  # Check if the light intensity is high
        # Open curtains and play music
        curtain = next(actuator for actuator in living_room.actuators if isinstance(actuator, Curtain))
        music_player = next(actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer))

        curtain.turn_on()  # Open curtains
        music_player.turn_on()  # Turn on music player
        music_player.play_music("Morning Playlist")  # Play music
    else:
        print("It's not bright enough to execute the morning plan.")

def leave_home_plan(home):
    print("Executing LEAVE HOME PLAN...")
    living_room = next(room for room in home if room.name == "LivingRoom")
    
    # Lock the door, open curtains and turn off lights
    door = next(actuator for actuator in living_room.actuators if isinstance(actuator, Door))
    curtain = next(actuator for actuator in living_room.actuators if isinstance(actuator, Curtain))
    light = next(actuator for actuator in living_room.actuators if isinstance(actuator, Light))

    door.lock()  # Lock the door
    curtain.turn_on()  # Open curtains
    light.turn_off()  # Turn off lights

def movie_plan(home):
    print("Executing MOVIE PLAN...")
    living_room = next(room for room in home if room.name == "LivingRoom")
    
    # Close curtains and dim lights
    curtain = next(actuator for actuator in living_room.actuators if isinstance(actuator, Curtain))
    light = next(actuator for actuator in living_room.actuators if isinstance(actuator, Light))

    curtain.turn_off()  # Close curtains
    light.set_brightness_level("low")  # Dim lights

def main():
    home = home_plan()
    
    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()