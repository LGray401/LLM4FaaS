# Based on the provided functional description and source code, I will create a `function.py` file that includes the main function to execute the plans (MORNING PLAN, LEAVE HOME PLAN, MOVIE PLAN) using the actuators and sensors defined in your project. This script will be placed in the `functions` folder.
# 
# ### `function.py`

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Curtain, Light, MusicPlayer, CoffeeMachine, Door, SmartTV

def morning_plan(home):
    # Get the LivingRoom actuators
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Open curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
            print(f"Opened {actuator.id} in LivingRoom.")
    
    # Turn on lights
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("high")
            print(f"Turned on {actuator.id} in LivingRoom with high brightness.")
    
    # Play soothing music
    for actuator in living_room_actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Soothing Music")
            print(f"Playing soothing music on {actuator.id} in LivingRoom.")
    
    # Make coffee
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    for actuator in kitchen_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Latte")
            print(f"Making Latte with {actuator.id} in Kitchen.")

def leave_home_plan(home):
    # Get the LivingRoom actuators
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Close the door
    for actuator in living_room_actuators:
        if isinstance(actuator, Door):
            actuator.lock()
            print(f"Locked {actuator.id} in LivingRoom.")
    
    # Turn off lights
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()
            print(f"Turned off {actuator.id} in LivingRoom.")

def movie_plan(home):
    # Get the LivingRoom actuators
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Turn on TV
    for actuator in living_room_actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Movie Channel")
            print(f"Playing Movie Channel on {actuator.id} in LivingRoom.")
    
    # Close curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()
            print(f"Closed {actuator.id} in LivingRoom.")
    
    # Dim the lights
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")
            print(f"Dimmed {actuator.id} in LivingRoom to low brightness.")

def main():
    # Create the home plan
    home = home_plan()
    
    # Execute the plans
    print("\n--- MORNING PLAN ---")
    morning_plan(home)
    
    print("\n--- LEAVE HOME PLAN ---")
    leave_home_plan(home)
    
    print("\n--- MOVIE PLAN ---")
    movie_plan(home)

if __name__ == "__main__":
    main()