# Based on the functional description you've provided for your smart home project, I'll create a `function.py` file that implements the morning plan, leave home plan, and movie plan. This file will include a main function to manage the various activities and automate the tasks as described.
# 
# Here's the `function.py` file:

# function.py
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import Light, CoffeeMachine, Curtain, MusicPlayer, Door, SmartSocket
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import datetime
import time

def morning_plan(home):
    now = datetime.datetime.now()
    if now.hour == 7 and now.minute == 0:  # Check if it's 7:00 AM
        print("Executing Morning Plan...")
        
        living_room = get_room(home, "LivingRoom")
        bedroom = get_room(home, "Bedroom")
        
        # Turn on the lights in the living room and bedroom
        for light in get_room_actuators(home, "Light"):
            light.turn_on()
            # Adjust brightness based on light intensity sensor reading
            light_sensor = get_room_sensors(home, "LivingRoom")[0]  # Assuming first sensor is LightIntensive
            light_intensity = light_sensor.get_reading()
            if light_intensity is not None:
                if light_intensity < LIGHT_INTENSITY_LOW:
                    light.set_brightness_level("high")
                elif LIGHT_INTENSITY_LOW <= light_intensity <= LIGHT_INTENSITY_HIGH:
                    light.set_brightness_level("medium")
                else:  # light_intensity > LIGHT_INTENSITY_HIGH
                    light.set_brightness_level("low")
        
        # Make cappuccino
        coffee_machine = get_room_actuators(home, "CoffeeMachine")[0]
        coffee_machine.turn_on()
        coffee_machine.make_coffee("cappuccino")
        
        # Open curtains
        for curtain in get_room_actuators(home, "Curtain"):
            curtain.turn_on()  # Assuming this means to open
        
        # Play relaxing light music
        music_player = get_room_actuators(home, "MusicPlayer")[0]
        music_player.turn_on()
        music_player.play_music("Relaxing Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    # Close the door
    door = get_room_actuators(home, "Door")[0]
    door.lock()
    
    # Turn off all lights
    for light in get_all_actuators(home, "Light"):
        light.turn_off()
    
    # Disconnect power sockets (assuming SmartSocket means disconnecting)
    for smart_socket in get_all_actuators(home, "SmartSocket"):
        smart_socket.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    # Draw the curtains
    for curtain in get_all_actuators(home, "Curtain"):
        curtain.turn_on()  # Assuming this means to close
    
    # Dim the lights
    for light in get_all_actuators(home, "Light"):
        light.set_brightness_level("low")

def main():
    home = home_plan()
    
    # Execute plans based on the time or triggers
    while True:
        morning_plan(home)
        time.sleep(60)  # Check every minute for the morning plan

        # Check for leave home plan, replace with actual condition to leave
        if input("Type 'leave' to execute Leave Home Plan: ").strip().lower() == 'leave':
            leave_home_plan(home)

        # Check for movie plan, replace with actual condition to start movie
        if input("Type 'movie' to execute Movie Plan: ").strip().lower() == 'movie':
            movie_plan(home)

if __name__ == "__main__":
    main()