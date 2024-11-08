# Based on your functional description and the provided source code, here is the `function.py` file that implements the required functionality for your smart home project.
# 
# ### `function.py`

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light, Curtain, MusicPlayer, Door

def morning_plan(home):
    print("Executing Morning Plan...")
    living_room = get_room_actuators(home, "LivingRoom")
    
    for actuator in living_room:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("high")
        elif isinstance(actuator, Curtain):
            actuator.turn_on()
            print("Curtains are now opening...")
        elif isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    living_room = get_room_actuators(home, "LivingRoom")
    
    for actuator in living_room:
        if isinstance(actuator, Door):
            actuator.lock()
        elif isinstance(actuator, Curtain):
            actuator.turn_off()
            print("Curtains are now closing...")
        elif isinstance(actuator, Light):
            actuator.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room_actuators(home, "LivingRoom")
    
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
            print("Curtains are now closing...")
        elif isinstance(actuator, Light):
            actuator.set_brightness_level("low")

def main():
    home = home_plan()
    
    # Example invocation of plans
    morning_plan(home)  # Execute morning plan
    leave_home_plan(home)  # Execute leave home plan
    movie_plan(home)  # Execute movie plan

if __name__ == "__main__":
    main()