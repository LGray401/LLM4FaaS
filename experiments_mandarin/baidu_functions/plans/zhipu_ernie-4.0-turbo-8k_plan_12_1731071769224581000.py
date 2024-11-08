# Based on your functional description and the provided source code, here's a `function.py` file that implements the `MORNING PLAN`, `LEAVE HOME PLAN`, and `MOVIE PLAN` functionalities. This file will be located in the `functions` folder and will utilize the classes and methods defined in the `sensor.py`, `actuator.py`, and `home_plan.py` files.

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Door, Light, SmartTV
from home.logger_config import logger

def morning_plan(home):
    # Open curtains
    living_room = get_room(home, "LivingRoom")
    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Assuming turn_on opens the curtain

    # Play music
    for actuator in living_room.actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")

    # Start coffee machine
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        for actuator in kitchen.actuators:
            if isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("Espresso")

    logger.info("Morning Plan Executed")

def leave_home_plan(home):
    # Close main door
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Door) and "Main" in room.name:  # Assuming main door has "Main" in its name
                actuator.turn_off()  # Assuming turn_off closes the door
                actuator.lock()

    # Turn off lights
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

    logger.info("Leave Home Plan Executed")

def movie_plan(home):
    # Close curtains
    living_room = get_room(home, "LivingRoom")
    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_off()  # Assuming turn_off closes the curtain

    # Turn on TV
    for actuator in living_room.actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Movie Channel")

    logger.info("Movie Plan Executed")

def main():
    # Initialize home plan
    home = home_plan()

    # Execute morning plan
    morning_plan(home)

    # Execute leave home plan (for demonstration purposes, you may not want to execute this immediately after morning plan)
    # leave_home_plan(home)

    # Execute movie plan (for demonstration purposes, you may not want to execute this immediately after leave home plan)
    # movie_plan(home)

if __name__ == "__main__":
    main()