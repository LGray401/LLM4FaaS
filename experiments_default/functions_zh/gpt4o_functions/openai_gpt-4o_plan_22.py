# Based on the functional description and the provided source code, here is your `function.py` file. This file contains the main function to execute the specified plans.
# 
# ### Function.py

from home.home_plan import home_plan, get_room_actuators
from home.logger_config import logger

def morning_plan(home):
    bedroom = get_room_actuators(home, "Bedroom")
    kitchen = get_room_actuators(home, "Kitchen")
    
    for actuator in bedroom:
        if actuator.actuator_type == "Light":
            actuator.turn_on()
        elif actuator.actuator_type == "Curtain":
            actuator.turn_on()

    for actuator in kitchen:
        if actuator.actuator_type == "CoffeeMachine":
            actuator.turn_on()
            actuator.make_coffee("Espresso")

    for actuator in bedroom:
        if actuator.actuator_type == "MusicPlayer":
            actuator.turn_on()
            actuator.play_music("Morning Playlist")

def leave_home_plan(home):
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
            elif actuator.actuator_type == "SmartSocket":
                actuator.turn_off()
            elif actuator.actuator_type == "Door":
                actuator.lock()

def movie_plan(home):
    living_room = get_room_actuators(home, "LivingRoom")

    for actuator in living_room:
        if actuator.actuator_type == "Curtain":
            actuator.turn_off()  # Close the curtain
        elif actuator.actuator_type == "Light":
            actuator.turn_on()
            actuator.set_brightness_level("low")
        elif actuator.actuator_type == "SmartTV":
            actuator.turn_on()
            actuator.play_channel("Movie Channel")

def main():
    home = home_plan()
    
    print("\nExecuting Morning Plan:")
    logger.info("Executing Morning Plan")
    morning_plan(home)
    
    print("\nExecuting Leave Home Plan:")
    logger.info("Executing Leave Home Plan")
    leave_home_plan(home)
    
    print("\nExecuting Movie Plan:")
    logger.info("Executing Movie Plan")
    movie_plan(home)

if __name__ == "__main__":
    main()