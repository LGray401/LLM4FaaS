# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to implement the morning plan, leave home plan, and movie plan. This file will be located in the `functions` folder.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door, SmartSocket, SmartTV
from home.config import DAILY_ROUTINE_DURATION

def execute_morning_plan(home):
    print("Executing Morning Plan...")
    
    # Get actuators for the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Open curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
    
    # Set light brightness to medium
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("medium")
    
    # Start coffee machine
    for actuator in living_room_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")
    
    # Play music
    for actuator in living_room_actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")

def execute_leave_home_plan(home):
    print("Executing Leave Home Plan...")

    # Get actuators for the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Turn off lights
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()
    
    # Open curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
    
    # Turn off smart sockets
    for actuator in living_room_actuators:
        if isinstance(actuator, SmartSocket):
            actuator.turn_off()
    
    # Lock the door
    for actuator in living_room_actuators:
        if isinstance(actuator, Door):
            actuator.lock()

def execute_movie_plan(home):
    print("Executing Movie Plan...")

    # Get actuators for the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Close sheer curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()
    
    # Set light brightness to low
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")
    
    # Start playing movie on Smart TV
    for actuator in living_room_actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Movie Channel")

def main():
    home = home_plan()
    
    # Uncomment the plan you want to execute
    execute_morning_plan(home)
    execute_leave_home_plan(home)
    execute_movie_plan(home)

if __name__ == "__main__":
    main()