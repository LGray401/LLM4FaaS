# Based on your provided source code and functional description, I will create the `function.py` file to handle the three plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here is the `function.py` file:
# 
# ### functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light, Curtain, MusicPlayer, Door

def morning_plan(home):
    print("\n--- Executing Morning Plan ---")
    living_room = get_room_actuators(home, "LivingRoom")
    bedroom = get_room_actuators(home, "Bedroom")

    # Increase light intensity
    for actuator in living_room + bedroom:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("high")

    # Open curtains
    for actuator in living_room + bedroom:
        if isinstance(actuator, Curtain):
            actuator.turn_on()

    # Play music
    for actuator in living_room + bedroom:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("morning_playlist")

def leave_home_plan(home):
    print("\n--- Executing Leave Home Plan ---")
    living_room = get_room_actuators(home, "LivingRoom")
    bedroom = get_room_actuators(home, "Bedroom")
    kitchen = get_room_actuators(home, "Kitchen")
    bathroom = get_room_actuators(home, "Bathroom")
    balcony = get_room_actuators(home, "Balcony")

    home_actuators = living_room + bedroom + kitchen + bathroom + balcony

    # Close the door
    for actuator in home_actuators:
        if isinstance(actuator, Door):
            actuator.turn_off()
            actuator.lock()

    # Open the curtains
    for actuator in home_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()

    # Turn off the lights
    for actuator in home_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

def movie_plan(home):
    print("\n--- Executing Movie Plan ---")
    living_room = get_room_actuators(home, "LivingRoom")

    # Close the curtains
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            actuator.turn_off()

    # Dim the lights
    for actuator in living_room:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")

if __name__ == "__main__":
    home = home_plan()
    print("Home plan created. Available plans: [morning_plan, leave_home_plan, movie_plan]")
    
    # Example of executing plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)