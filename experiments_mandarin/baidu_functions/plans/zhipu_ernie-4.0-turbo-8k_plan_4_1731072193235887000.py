# Based on the functional description and the provided source code, I will create a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. These functions will interact with the sensors and actuators defined in the other modules.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_actuators
from home.actuator import Curtain, Light

def morning_plan(home):
    # Open curtains in the bedroom
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        for actuator in bedroom.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Assuming turn_on opens the curtain

def leave_home_plan(home):
    # Turn off all lights in the house
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

def movie_plan(home, room_name="LivingRoom", brightness_level="low"):
    # Adjust light brightness in the specified room (default is LivingRoom)
    room = get_room(home, room_name)
    if room:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.set_brightness_level(brightness_level)

if __name__ == "__main__":
    # Initialize the home plan
    home = home_plan()
    
    # Execute the morning plan
    morning_plan(home)
    
    # Execute the leave home plan
    leave_home_plan(home)
    
    # Execute the movie plan
    movie_plan(home)