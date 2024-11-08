# Based on your functional description and the provided source code, I'll create a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. These functions will utilize the classes and methods defined in the `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light, Curtain

def morning_plan(home):
    # Open curtains in the LivingRoom and Bedroom
    rooms_to_open_curtains = ["LivingRoom", "Bedroom"]
    for room_name in rooms_to_open_curtains:
        room = get_room(home, room_name)
        if room:
            actuators = get_room_actuators(home, room_name)
            for actuator in actuators:
                if isinstance(actuator, Curtain):
                    actuator.turn_on()  # Assuming turn_on() opens the curtains

def leave_home_plan(home):
    # Turn off lights in all rooms
    for room in home:
        actuators = get_room_actuators(home, room.name)
        for actuator in actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

def movie_plan(home, room_name="LivingRoom", brightness_level="low"):
    # Adjust light brightness in the specified room (default is LivingRoom)
    room = get_room(home, room_name)
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, Light):
                actuator.set_brightness_level(brightness_level)

if __name__ == "__main__":
    # Create the home plan
    home = home_plan()
    
    # Execute the morning plan
    morning_plan(home)
    
    # Execute the leave home plan
    # leave_home_plan(home)
    
    # Execute the movie plan
    # movie_plan(home, room_name="LivingRoom", brightness_level="medium")