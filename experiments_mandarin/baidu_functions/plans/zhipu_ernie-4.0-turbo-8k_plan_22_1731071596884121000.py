# Based on the provided functional description and source code, here is the `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light, Curtain, MusicPlayer, CoffeeMachine, Door, SmartSocket

def execute_morning_plan(home):
    # Get the bedroom
    bedroom = get_room(home, "Bedroom")
    if not bedroom:
        return

    # Get bedroom actuators
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    if not bedroom_actuators:
        return

    # Turn on the bedroom lights
    for actuator in bedroom_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()

    # Open the curtains
    for actuator in bedroom_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()  # Assuming turn_on() opens the curtains

    # Set the music player to play at 6 AM (this functionality is not implemented in the provided code)
    # You would need to implement a scheduler or use an existing one to trigger this at the specified time
    # For simplicity, we'll just turn on the music player here
    for actuator in bedroom_actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()  # You can add more logic to set a specific playlist or time

    # Start the coffee machine
    for actuator in bedroom_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Your Preferred Coffee Type")  # Specify the coffee type

def execute_leave_home_plan(home):
    # Iterate through all rooms to turn off lights and lock doors
    for room in home:
        room_actuators = get_room_actuators(home, room.name)
        if not room_actuators:
            continue

        # Turn off all lights
        for actuator in room_actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

        # Lock all doors
        for actuator in room_actuators:
            if isinstance(actuator, Door):
                actuator.lock()

        # Turn off all sockets
        for actuator in room_actuators:
            if isinstance(actuator, SmartSocket):
                actuator.turn_off()

def execute_movie_plan(home):
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Get living room actuators
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    if not living_room_actuators:
        return

    # Close the curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()  # Assuming turn_off() closes the curtains

    # Dim the lights
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.set_brightness_level("low")

    # Turn on the TV
    for actuator in living_room_actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Your Preferred Channel")  # Specify the channel name

# Main function to execute the plans
def main():
    home = home_plan()
    
    # Execute the morning plan
    print("Executing Morning Plan...")
    execute_morning_plan(home)
    
    # Execute the leave home plan
    # This is usually executed when leaving the home, so you might want to call this function at the appropriate time
    # For demonstration, we'll just call it here
    print("Executing Leave Home Plan...")
    execute_leave_home_plan(home)
    
    # Execute the movie plan
    # This is usually executed when you want to watch a movie, so you might want to call this function when needed
    # For demonstration, we'll just call it here
    print("Executing Movie Plan...")
    execute_movie_plan(home)

if __name__ == "__main__":
    main()