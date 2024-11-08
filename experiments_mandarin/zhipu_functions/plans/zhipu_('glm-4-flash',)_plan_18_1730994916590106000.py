# Based on your functional description and provided source code, I will create a `function.py` file that contains the main function to execute the specified plans (Morning Plan, Leave Home Plan, and Movie Plan). This file will utilize the classes and functions from `sensor.py`, `actuator.py`, and `home_plan.py`.
# 
# Here is the `function.py` file:

# function.py
from home.home_plan import home_plan, get_room, get_room_actuators
from home.sensor import Sensor
from home.actuator import Actuator

# Function to execute Morning Plan
def morning_plan():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    music_player = next((act for act in get_room_actuators(living_room, "MusicPlayer") if isinstance(act, Actuator)), None)
    if music_player:
        music_player.play_music("Morning Playlist")

# Function to execute Leave Home Plan
def leave_home_plan():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    door = next((act for act in get_room_actuators(living_room, "Door") if isinstance(act, Actuator)), None)
    if door:
        door.lock()

# Function to execute Movie Plan
def movie_plan():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    curtain = next((act for act in get_room_actuators(living_room, "Curtain") if isinstance(act, Actuator)), None)
    if curtain:
        curtain.turn_on()

# Main function
def main():
    # Execute the Morning Plan
    morning_plan()
    
    # Execute the Leave Home Plan
    leave_home_plan()
    
    # Execute the Movie Plan
    movie_plan()

if __name__ == "__main__":
    main()