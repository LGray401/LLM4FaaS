# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to implement the morning, leave home, and movie plans. This file will be placed in the `functions` folder.
# 
# ### `function.py`

from home.home_plan import home_plan, get_room_actuators, get_all_actuators
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Light, Door, SmartSocket, SmartTV

def execute_morning_plan(home):
    print("Executing Morning Plan...")
    
    # Get actuators for the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Open curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
            print(f"Opened {actuator.id}")
    
    # Start playing music
    for actuator in living_room_actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")
            print(f"Playing 'Morning Playlist' on {actuator.id}")
    
    # Make coffee
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    for actuator in kitchen_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Latte")
            print(f"Making Latte with {actuator.id}")

def execute_leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    # Turn off lights
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()
        print(f"Turned off {light.id}")
    
    # Close doors
    all_doors = get_all_actuators(home, "Door")
    for door in all_doors:
        door.turn_off()
        print(f"Closed {door.id}")
    
    # Turn off smart sockets (except for the refrigerator)
    all_sockets = get_all_actuators(home, "SmartSocket")
    for socket in all_sockets:
        if "refrigerator" not in socket.id:  # Assuming the refrigerator is connected to a specific socket
            socket.turn_off()
            print(f"Turned off {socket.id}")

def execute_movie_plan(home):
    print("Executing Movie Plan...")
    
    # Close curtains
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()
            print(f"Closed {actuator.id}")
    
    # Dim the lights
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")
            print(f"Set brightness level to LOW for {actuator.id}")
    
    # Start playing movie on Smart TV
    for actuator in living_room_actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Favorite Movie Channel")
            print(f"Playing 'Favorite Movie Channel' on {actuator.id}")

def main():
    home = home_plan()
    
    # Uncomment the plan you want to execute
    # execute_morning_plan(home)
    # execute_leave_home_plan(home)
    # execute_movie_plan(home)

if __name__ == "__main__":
    main()