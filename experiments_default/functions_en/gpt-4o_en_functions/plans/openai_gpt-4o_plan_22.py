# Based on the provided functional description and source code, here is the `function.py` file for your smart home project. This file contains the main function to execute the specified plans (MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN).

# function.py
from home.home_plan import home_plan, get_room_actuators

def morning_plan(home):
    bedroom = get_room_actuators(home, "Bedroom")
    living_room = get_room_actuators(home, "LivingRoom")
    kitchen = get_room_actuators(home, "Kitchen")
    
    # Turn on the bedroom light
    for actuator in bedroom:
        if actuator.actuator_type == "Light":
            actuator.turn_on()
            
    # Open the curtains
    for actuator in bedroom:
        if actuator.actuator_type == "Curtain":
            actuator.turn_on()
    
    # Set the music player for 6am
    for actuator in bedroom:
        if actuator.actuator_type == "MusicPlayer":
            actuator.turn_on()
            actuator.play_music("Morning Playlist")
    
    # Start the coffee machine to make coffee
    for actuator in kitchen:
        if actuator.actuator_type == "CoffeeMachine":
            actuator.turn_on()
            actuator.make_coffee("Espresso")

def leave_home_plan(home):
    # Turn off all lights in the house
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()
    
    # Lock the front door
    for door in get_all_actuators(home, "Door"):
        door.lock()
    
    # Close the sockets
    all_sockets = get_all_actuators(home, "SmartSocket")
    for socket in all_sockets:
        socket.turn_off()

def movie_plan(home):
    living_room = get_room_actuators(home, "LivingRoom")
    
    # Close the curtains
    for actuator in living_room:
        if actuator.actuator_type == "Curtain":
            actuator.turn_off()
    
    # Dim the lights
    for actuator in living_room:
        if actuator.actuator_type == "Light":
            actuator.turn_on()
            actuator.set_brightness_level("low")
    
    # Turn on the TV and set the program
    for actuator in living_room:
        if actuator.actuator_type == "SmartTV":
            actuator.turn_on()
            actuator.play_channel("Movie Channel")

def main():
    home = home_plan()
    
    # Execute the plans
    print("Executing Morning Plan...")
    morning_plan(home)

    print("Executing Leave Home Plan...")
    leave_home_plan(home)

    print("Executing Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()