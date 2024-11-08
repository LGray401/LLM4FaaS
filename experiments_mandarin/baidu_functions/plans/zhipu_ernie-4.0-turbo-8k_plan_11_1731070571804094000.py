# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. These functions will interact with the sensors and actuators defined in your `home_plan.py`, `sensor.py`, and `actuator.py` files.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light, Curtain, SmartTV
from home.logger_config import logger

def morning_plan():
    home = home_plan()
    room = get_room(home, "Bedroom")
    
    if room:
        actuators = get_room_actuators(home, "Bedroom")
        for actuator in actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                logger.info(f"Turned on light in {room.name} for Morning Plan.")

def leave_home_plan():
    home = home_plan()
    room = get_room(home, "LivingRoom")
    
    if room:
        actuators = get_room_actuators(home, "LivingRoom")
        for actuator in actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Assuming turn_on() opens the curtains
                logger.info(f"Opened curtains in {room.name} for Leave Home Plan.")

def movie_plan():
    home = home_plan()
    room = get_room(home, "LivingRoom")
    
    if room:
        actuators = get_room_actuators(home, "LivingRoom")
        for actuator in actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_on()
                logger.info(f"Turned on SmartTV in {room.name} for Movie Plan.")

if __name__ == "__main__":
    # Test the functions
    morning_plan()
    leave_home_plan()
    movie_plan()