# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to execute the morning plan, leave home plan, and movie plan. This file will be placed in the `functions` folder.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light, Curtain, MusicPlayer, CoffeeMachine, Door, SmartSocket, SmartTV
from home.config import DAILY_ROUTINE_DURATION

def execute_morning_plan(home):
    bedroom = get_room_actuators(home, "Bedroom")
    for actuator in bedroom:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("medium")
        elif isinstance(actuator, Curtain):
            actuator.turn_on()
        elif isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")
        elif isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Latte")

def execute_leave_home_plan(home):
    all_rooms = ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"]
    for room_name in all_rooms:
        room_actuators = get_room_actuctors(home, room_name)
        for actuator in room_actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
            elif isinstance(actuator, Door):
                actuator.lock()
            elif isinstance(actuator, SmartSocket):
                actuator.turn_off()

def execute_movie_plan(home):
    living_room = get_room_actuators(home, "LivingRoom")
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
        elif isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")
        elif isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Movie Channel")

def main():
    home = home_plan()
    
    # Uncomment the following lines to test the plans
    # execute_morning_plan(home)
    # execute_leave_home_plan(home)
    # execute_movie_plan(home)

if __name__ == "__main__":
    main()