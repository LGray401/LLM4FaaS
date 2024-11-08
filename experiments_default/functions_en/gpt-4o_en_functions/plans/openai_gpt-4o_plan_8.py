# Absolutely, I can help create the `function.py` file for your smart home project based on the functional description and the given source code. Below is the code for the `function.py` file which will reside in the 'functions' folder and contain the main function to handle the different plans:
# 
# ### `functions/function.py`

import time
from home.home_plan import home_plan, get_room_actuators
from home.config import DAILY_ROUTINE_DURATION

def morning_plan(home):
    print("Executing Morning Plan...")
    living_room = get_room_actuators(home, "LivingRoom")
    bedroom = get_room_actuators(home, "Bedroom")
    kitchen = get_room_actuators(home, "Kitchen")

    # Turn on lights, heater, coffee machine, and play music
    for actuator in living_room + bedroom + kitchen:
        if isinstance(actuator, Light) or isinstance(actuator, Heater):
            actuator.turn_on()
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("espresso")
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("morning_playlist")

    # Start cleaning routine
    for actuator in living_room + bedroom + kitchen:
        if isinstance(actuator, CleaningRobot):
            actuator.turn_on()
            actuator.daily_routine()

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Door):
                actuator.lock()
            elif isinstance(actuator, Light) or isinstance(actuator, Heater) or isinstance(actuator, AC):
                actuator.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room_actuators(home, "LivingRoom")

    for actuator in living_room:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Movie Channel")
        elif isinstance(actuator, Light):
            actuator.turn_off()

def main():
    home = home_plan()

    # Example of executing plans
    morning_plan(home)
    time.sleep(DAILY_ROUTINE_DURATION)  # Simulating wait time for routine completion
    leave_home_plan(home)
    time.sleep(DAILY_ROUTINE_DURATION)
    movie_plan(home)

if __name__ == "__main__":
    main()