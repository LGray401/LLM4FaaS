# Based on your functional description and the provided source code, here's a `function.py` file that implements the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Curtain, Light, MusicPlayer, CoffeeMachine, Door, SmartTV
from home.logger_config import logger

def execute_morning_plan(home):
    # Get the LivingRoom
    room = get_room(home, "LivingRoom")
    if not room:
        return

    # Get actuators in the LivingRoom
    actuators = get_room_actuators(home, "LivingRoom")
    if not actuators:
        return

    # Open curtains
    for actuator in actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()  # Assuming turn_on opens the curtains

    # Turn on lights
    for actuator in actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("high")  # Optional: set to a specific brightness level

    # Play soothing music
    for actuator in actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("soothing_playlist")  # Assuming a predefined playlist name

    # Make coffee
    for actuator in actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("espresso")  # Assuming a type of coffee

    logger.info("Morning plan executed in LivingRoom.")

def execute_leave_home_plan(home):
    # Get the LivingRoom (or specify another room if needed)
    room = get_room(home, "LivingRoom")
    if not room:
        return

    # Get actuators in the LivingRoom
    actuators = get_room_actuators(home, "LivingRoom")
    if not actuators:
        return

    # Close the main door
    for actuator in actuators:
        if isinstance(actuator, Door):
            actuator.turn_off()  # Assuming turn_off closes the door
            actuator.lock()  # Lock the door

    # Turn off lights
    for actuator in actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

    logger.info("Leave home plan executed in LivingRoom.")

def execute_movie_plan(home):
    # Get the LivingRoom
    room = get_room(home, "LivingRoom")
    if not room:
        return

    # Get actuators in the LivingRoom
    actuators = get_room_actuators(home, "LivingRoom")
    if not actuators:
        return

    # Turn on the TV
    for actuator in actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("movie_channel")  # Assuming a movie channel name

    # Close curtains
    for actuator in actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()  # Assuming turn_off closes the curtains

    # Dim lights
    for actuator in actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")  # Dim the lights

    logger.info("Movie plan executed in LivingRoom.")

if __name__ == "__main__":
    # Initialize home plan
    home = home_plan()

    # Execute plans
    execute_morning_plan(home)
    # execute_leave_home_plan(home)
    # execute_movie_plan(home)