# Based on your functional description and the provided source code, I'll create a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. These functions will utilize the classes and methods defined in the `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Curtain, Light, SmartTV

def morning_plan(home):
    # Open curtains in all rooms
    for room in home:
        actuators = get_room_actuators(home, room.name)
        for actuator in actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Open the curtain

def leave_home_plan(home):
    # Turn off lights and windows in all rooms
    for room in home:
        actuators = get_room_actuators(home, room.name)
        for actuator in actuators:
            if isinstance(actuator, Light) or isinstance(actuator, Window):
                actuator.turn_off()  # Turn off lights and close windows

def movie_plan(home):
    # Turn on the TV in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        actuators = get_room_actuators(home, living_room.name)
        for actuator in actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_on()  # Turn on the TV
                actuator.play_channel("Movie Channel")  # Assuming a movie channel

if __name__ == "__main__":
    # Create the home plan
    home = home_plan()
    
    # Execute the morning plan
    morning_plan(home)
    
    # Execute the leave home plan
    # leave_home_plan(home)
    
    # Execute the movie plan
    # movie_plan(home)