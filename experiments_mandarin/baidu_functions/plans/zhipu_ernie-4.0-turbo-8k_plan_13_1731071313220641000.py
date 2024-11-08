# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. These functions will utilize the classes and methods defined in the `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Actuator
from home.logger_config import logger

def execute_morning_plan(home):
    # Get the Living Room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Open curtains
    for actuator in living_room.actuators:
        if actuator.actuator_type == "Curtain":
            actuator.turn_on()  # Assuming turn_on opens the curtains

    # Set light brightness to medium
    for actuator in living_room.actuators:
        if actuator.actuator_type == "Light":
            actuator.set_brightness_level("medium")

    # Start coffee machine
    for actuator in living_room.actuators:
        if actuator.actuator_type == "CoffeeMachine":
            actuator.turn_on()
            actuator.make_coffee("regular")  # Assuming 'regular' is a type of coffee

    # Play music
    for actuator in living_room.actuators:
        if actuator.actuator_type == "MusicPlayer":
            actuator.turn_on()
            actuator.play_music("morning_playlist")  # Assuming 'morning_playlist' is defined

def execute_leave_home_plan(home):
    # Iterate through all rooms to turn off lights, open windows (if any), turn off sockets, and lock doors
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
            elif actuator.actuator_type == "Window":
                actuator.turn_on()  # Assuming turn_on opens the window (for ventilation purposes)
            elif actuator.actuator_type == "SmartSocket":
                actuator.turn_off()
            elif actuator.actuator_type == "Door":
                actuator.lock()

def execute_movie_plan(home):
    # Get the Living Room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Close the sheer curtains (assuming sheer curtains are a type of Window actuator)
    # and dim the lights
    for actuator in living_room.actuators:
        if actuator.actuator_type == "Window" and "sheer" in actuator.id:  # Assuming sheer curtains have 'sheer' in their ID
            actuator.turn_off()  # Assuming turn_off closes the curtains
        elif actuator.actuator_type == "Light":
            actuator.set_brightness_level("low")

    # Smart TV control
    for actuator in living_room.actuators:
        if actuator.actuator_type == "SmartTV":
            actuator.turn_on()
            actuator.play_channel("movie_channel")  # Assuming 'movie_channel' is defined

# Main function to execute plans based on input
def main(plan_name):
    home = home_plan()
    
    if plan_name == "MORNING_PLAN":
        execute_morning_plan(home)
    elif plan_name == "LEAVE_HOME_PLAN":
        execute_leave_home_plan(home)
    elif plan_name == "MOVIE_PLAN":
        execute_movie_plan(home)
    else:
        print("Invalid plan name")
        logger.error("Invalid plan name")

if __name__ == "__main__":
    # Example usage:
    # main("MORNING_PLAN")
    # main("LEAVE_HOME_PLAN")
    # main("MOVIE_PLAN")
    pass