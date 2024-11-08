# Based on the provided functional description and the source code, we'll create the `function.py` file within the `functions` folder. This file will contain the main functions to implement the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here is the `function.py` file:

# function.py
from home.home_plan import home_plan, get_room
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door, SmartSocket, Window, SmartTV

def morning_plan(home):
    print("Executing MORNING PLAN...")
    living_room = get_room(home, "LivingRoom")
    
    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Open curtains
            elif isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("medium")  # Set light to medium
            elif isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("espresso")  # Start coffee machine
            elif isinstance(actuator, MusicPlayer):
                actuator.turn_on()
                actuator.play_music("morning_playlist")  # Play music to adjust mood

def leave_home_plan(home):
    print("Executing LEAVE HOME PLAN...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()  # Turn off lights
            elif isinstance(actuator, Curtain):
                actuator.turn_off()  # Close curtains
            elif isinstance(actuator, SmartSocket):
                actuator.turn_off()  # Turn off smart sockets
            elif isinstance(actuator, Door):
                actuator.lock()  # Lock doors

def movie_plan(home):
    print("Executing MOVIE PLAN...")
    living_room = get_room(home, "LivingRoom")
    
    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, Window):
                actuator.turn_on()  # Close windows
            elif isinstance(actuator, Curtain):
                actuator.turn_on()  # Close curtains
            elif isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")  # Set light to low
            elif isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("movie_channel")  # Start TV to movie channel

def main():
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()