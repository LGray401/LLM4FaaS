# Based on the provided functional description of your smart home project, I will create a `function.py` file that contains the main function to handle the three specified plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here is the code for `function.py`:

# function.py
from home.home_plan import home_plan, get_room_actuators
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Light, Door, SmartSocket, SmartTV

def morning_plan(home):
    print("\n--- MORNING PLAN ---")
    
    living_room = get_room_actuators(home, "LivingRoom")
    bedroom = get_room_actuators(home, "Bedroom")
    
    # Draw curtains
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
            print("Curtains drawn in the Living Room.")
    
    # Start music player
    for actuator in living_room:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")
    
    # Make coffee
    for actuator in bedroom:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")
    
def leave_home_plan(home):
    print("\n--- LEAVE HOME PLAN ---")
    
    living_room = get_room_actuators(home, "LivingRoom")
    
    # Turn off lights and close door
    for actuator in living_room:
        if isinstance(actuator, Light):
            actuator.turn_off()
    
    for actuator in living_room:
        if isinstance(actuator, Door):
            actuator.lock()
    
    # Disconnect sockets except for refrigerator
    for actuator in living_room:
        if isinstance(actuator, SmartSocket):
            actuator.turn_off()
    
def movie_plan(home):
    print("\n--- MOVIE PLAN ---")
    
    living_room = get_room_actuators(home, "LivingRoom")
    
    # Close curtains
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
            print("Curtains closed in the Living Room.")
    
    # Dim lights
    for actuator in living_room:
        if isinstance(actuator, Light):
            actuator.set_brightness_level("low")
    
    # Turn on TV and play favorite show
    for actuator in living_room:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Favorite Show")

def main():
    home = home_plan()
    
    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()