# Based on your functional description and the provided source code, I will create a `function.py` file that includes the main function to execute the morning plan, leave home plan, and movie plan. This script will be placed in the `functions` folder and will interact with the sensors and actuators as defined in your `sensor.py` and `actuator.py` files.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Door, Light, SmartTV

def execute_morning_plan(home):
    print("Executing Morning Plan...")
    
    # Get actuators for the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Open curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
    
    # Play music
    for actuator in living_room_actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")
    
    # Start coffee machine
    for actuator in living_room_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")

def execute_leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    # Get actuators for the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Close the door
    for actuator in living_room_actuators:
        if isinstance(actuator, Door):
            actuator.lock()
    
    # Turn off lights
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

def execute_movie_plan(home):
    print("Executing Movie Plan...")
    
    # Get actuators for the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Close curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()
    
    # Turn on TV
    for actuator in living_room_actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Movie Channel")

def main():
    # Create the home plan
    home = home_plan()
    
    # Execute the plans
    execute_morning_plan(home)
    execute_leave_home_plan(home)
    execute_movie_plan(home)

if __name__ == "__main__":
    main()