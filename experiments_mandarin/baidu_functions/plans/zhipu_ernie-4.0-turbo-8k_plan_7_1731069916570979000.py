# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. These functions will utilize the classes and methods defined in the `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_actuators
from home.actuator import MusicPlayer, CoffeeMachine, Door, Light, Curtain
import time
from datetime import datetime, timedelta

# Function to execute the Morning Plan
def morning_plan(home):
    # Wake me up at 7:00
    wake_up_time = datetime.now().replace(hour=7, minute=0, second=0, microsecond=0)
    while datetime.now() < wake_up_time:
        time.sleep(1)
    
    # Assuming there's a way to play an alarm sound or notification, for simplicity we'll just print a message
    print("Wake up! It's 7:00 AM.")

    # Turn on music at 7:05
    music_time = wake_up_time + timedelta(minutes=5)
    while datetime.now() < music_time:
        time.sleep(1)
    
    music_players = get_all_actuators(home, "MusicPlayer")
    for player in music_players:
        player.turn_on()
        player.play_music("周杰伦歌单")  # Assuming this is the playlist name

    # Make coffee at 7:20
    coffee_time = wake_up_time + timedelta(minutes=20)
    while datetime.now() < coffee_time:
        time.sleep(1)
    
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for machine in coffee_machines:
        machine.turn_on()
        machine.make_coffee("Your preferred coffee type")  # Specify your coffee type

# Function to execute the Leave Home Plan
def leave_home_plan(home):
    # Wait until 7:30 to execute the plan
    leave_home_time = datetime.now().replace(hour=7, minute=30, second=0, microsecond=0)
    while datetime.now() < leave_home_time:
        time.sleep(1)
    
    # Lock the doors
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()

    # Turn off lights and sockets
    lights_and_sockets = get_all_actuators(home, "Light") + get_all_actuators(home, "SmartSocket")
    for device in lights_and_sockets:
        device.turn_off()

# Function to execute the Movie Plan
def movie_plan(home):
    # For simplicity, we'll assume this function is called when the movie starts
    # Close curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()  # Assuming turn_off() means close for curtains

    # Dim the lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.set_brightness_level("low")

# Main function to run the plans
def main():
    # Initialize the home plan
    home = home_plan()

    # Execute the morning plan
    morning_plan(home)

    # Execute the leave home plan (this will happen automatically at the specified time)
    # You might want to run this in a separate thread or process if you don't want to block the main function
    # For simplicity, we'll just call it here and it will block until the plan is executed
    leave_home_plan(home)

    # The movie plan should be called when needed, not automatically
    # For example, you could have a separate function or event listener that calls movie_plan() when a movie starts

if __name__ == "__main__":
    main()