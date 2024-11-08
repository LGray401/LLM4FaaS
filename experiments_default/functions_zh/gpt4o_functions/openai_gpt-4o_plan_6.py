# Based on your provided functional description and source code, I'll create the `function.py` file in the 'functions' folder. This file will include the main function that orchestrates the "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN".
# 
# Here's the `function.py` file:
from home.actuator import Light, MusicPlayer, Curtain, CoffeeMachine, Door, Window, CleaningRobot, SmartTV
# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW
import time

def morning_plan(home):
    print("Executing Morning Plan:")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    kitchen_actuators = get_room_actuators(home, "Kitchen")

    if bedroom_actuators:
        for actuator in bedroom_actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("medium")
            elif isinstance(actuator, MusicPlayer):
                actuator.turn_on()
                actuator.play_music("Morning Playlist")
            elif isinstance(actuator, Curtain):
                actuator.turn_on()
    
    if kitchen_actuators:
        for actuator in kitchen_actuators:
            if isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("Espresso")

def leave_home_plan(home):
    print("Executing Leave Home Plan:")
    all_rooms = home

    for room in all_rooms:
        for actuator in room.actuators:
            if isinstance(actuator, Light) or isinstance(actuator, MusicPlayer):
                actuator.turn_off()
            elif isinstance(actuator, Door):
                actuator.lock()
            elif isinstance(actuator, Window):
                actuator.turn_off()
            elif isinstance(actuator, CleaningRobot):
                actuator.turn_on()
                actuator.daily_routine()

def movie_plan(home):
    print("Executing Movie Plan:")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    if living_room_actuators:
        for actuator in living_room_actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")
            elif isinstance(actuator, Curtain):
                actuator.turn_on()
            elif isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Movie Channel")
            elif isinstance(actuator, MusicPlayer):
                actuator.turn_off()

def main():
    home = home_plan()
    morning_plan(home)
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Simulate waiting time
    leave_home_plan(home)
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Simulate waiting time
    movie_plan(home)

if __name__ == "__main__":
    main()