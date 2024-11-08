# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. Since the functional description only mentions "灯" (which means "lights" in Chinese), I'll assume that the plans involve controlling the lights in different rooms.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light

def morning_plan():
    # Get the home plan
    home = home_plan()
    
    # Turn on lights in the bedroom and living room
    rooms_to_illuminate = ["Bedroom", "LivingRoom"]
    for room_name in rooms_to_illuminate:
        room = get_room(home, room_name)
        if room:
            actuators = get_room_actuators(home, room_name)
            for actuator in actuators:
                if isinstance(actuator, Light) and actuator.status == "off":
                    actuator.turn_on()

def leave_home_plan():
    # Get the home plan
    home = home_plan()
    
    # Turn off all lights
    for room in home:
        actuators = get_room_actuators(home, room.name)
        for actuator in actuators:
            if isinstance(actuator, Light) and actuator.status == "on":
                actuator.turn_off()

def movie_plan():
    # Get the home plan
    home = home_plan()
    
    # Turn off lights in the living room (assuming movie is being watched in the living room)
    # and turn them on at a low brightness level
    room_name = "LivingRoom"
    room = get_room(home, room_name)
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, Light) and actuator.status == "on":
                actuator.set_brightness_level("low")
            elif isinstance(actuator, Light) and actuator.status == "off":
                actuator.turn_on()
                actuator.set_brightness_level("low")

if __name__ == "__main__":
    # Test the plans
    morning_plan()
    # leave_home_plan()
    # movie_plan()