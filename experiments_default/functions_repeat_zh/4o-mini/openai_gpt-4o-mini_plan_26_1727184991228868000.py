# Based on your functional description and the provided source code, here is a `function.py` file that implements the morning plan, leave home plan, and movie plan. This file will utilize the classes from `sensor.py`, `actuator.py`, and `home_plan.py`. 
# 
# The main function will execute the routines as specified in your functional description.
# 
# ### function.py

import schedule
import time
from datetime import datetime
from home.home_plan import home_plan
from home.actuator import Light, Curtain, MusicPlayer, CoffeeMachine, Door, SmartSocket

# Initialize the home plan
home = home_plan()

def morning_plan():
    print("Executing Morning Plan...")
    # Turn on lights and adjust brightness based on light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    
    for sensor in light_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            for light in lights:
                light.turn_on()
                if light_intensity < 500:  # Adjust brightness based on reading
                    light.set_brightness_level("high")
                else:
                    light.set_brightness_level("low")

    # Make a cappuccino
    coffee_machine = get_all_actuators(home, "CoffeeMachine")
    for machine in coffee_machine:
        machine.turn_on()
        machine.make_coffee("Cappuccino")

    # Open curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # Play relaxing music
    music_players = get_all_actuators(home, "MusicPlayer")
    for player in music_players:
        player.turn_on()
        player.play_music("Relaxing Playlist")

def leave_home_plan():
    print("Executing Leave Home Plan...")
    # Lock the door, turn off lights and sockets
    doors = get_all_actuators(home, "Door")
    lights = get_all_actuators(home, "Light")
    sockets = get_all_actuators(home, "SmartSocket")

    for door in doors:
        door.lock()
    
    for light in lights:
        light.turn_off()

    for socket in sockets:
        socket.turn_off()

def movie_plan():
    print("Executing Movie Plan...")
    # Close curtains and dim lights
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")

    for curtain in curtains:
        curtain.turn_off()  # Assuming turn_off means closing the curtain
    
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

def main():
    # Schedule the morning plan
    schedule.every().day.at("07:00").do(morning_plan)

    # Example scheduling for leave home plan and movie plan
    # schedule.every().day.at("17:00").do(leave_home_plan)  # For when you leave home
    # schedule.every().day.at("20:00").do(movie_plan)  # For when you want to watch a movie

    print("Scheduler started...")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()