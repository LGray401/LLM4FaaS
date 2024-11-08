# Here's a `function.py` file for your smart home project, which includes the main function to implement the three plans described in your functional description. The code will handle the execution of the morning, leave home, and movie plans by controlling the respective actuators and sensors.
# 
# ### function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import CoffeeMachine, Curtain, Light, MusicPlayer, Door, SmartTV
from home.logger_config import logger

def execute_morning_plan(home):
    room = get_room(home, "LivingRoom")

    # Open the curtains
    curtains = get_room_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()  # Assuming turning on opens the curtains

    # Turn on the lights
    lights = get_room_actuators(home, "Light")
    for light in lights:
        light.turn_on()

    # Play soothing music
    music_players = get_room_actuators(home, "MusicPlayer")
    for player in music_players:
        player.turn_on()
        player.play_music("Soothing Music Playlist")

    # Make coffee
    coffee_machine = next((act for act in get_room_actuators(home, "CoffeeMachine")), None)
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

def execute_leave_home_plan(home):
    room = get_room(home, "LivingRoom")

    # Close the door
    door = next((act for act in get_room_actuators(home, "Door")), None)
    if door:
        door.lock()
    
    # Turn off the lights
    lights = get_room_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def execute_movie_plan(home):
    room = get_room(home, "LivingRoom")

    # Turn on the TV
    tv = next((act for act in get_room_actuators(home, "SmartTV")), None)
    if tv:
        tv.turn_on()
        tv.play_channel("Your Favorite Movie Channel")

    # Close the curtains
    curtains = get_room_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()  # Assuming turning off closes the curtains

    # Dim the lights
    lights = get_room_actuators(home, "Light")
    for light in lights:
        light.set_brightness_level("low")

def main():
    home = home_plan()
    
    # Execute plans based on your needs
    print("Executing Morning Plan...")
    execute_morning_plan(home)
    
    print("Executing Leave Home Plan...")
    execute_leave_home_plan(home)

    print("Executing Movie Plan...")
    execute_movie_plan(home)

if __name__ == "__main__":
    main()