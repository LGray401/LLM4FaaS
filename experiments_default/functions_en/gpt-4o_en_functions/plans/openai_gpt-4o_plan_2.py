# Based on the provided functional description and the source code of the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files, I'll create a new `function.py` file that includes the main functions for the "Morning Plan", "Leave Home Plan", and "Movie Plan".
# 
# Here is the `function.py` file:

# function.py

from home.home_plan import home_plan, get_room_actuators

def morning_plan(home):
    # Draw the curtains, start the music player, and make coffee
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    kitchen_actuators = get_room_actuators(home, "Kitchen")

    for actuator in living_room_actuators + bedroom_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
        elif isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")

    for actuator in kitchen_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")

def leave_home_plan(home):
    # Close lights, lock doors, disconnect sockets except for the refrigerator
    all_actuators = [actuator for room in home for actuator in room.actuators]

    for actuator in all_actuators:
        if isinstance(actuator, Light) or isinstance(actuator, Door) or isinstance(actuator, SmartSocket):
            actuator.turn_off()
        if isinstance(actuator, Door):
            actuator.lock()
        if isinstance(actuator, SmartSocket) and "refrigerator" not in actuator.id.lower():
            actuator.turn_off()

def movie_plan(home):
    # Close the curtains, dim the lights, and turn on the TV to play a favorite show
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
        elif isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")
        elif isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Favorite Show")

def main():
    home = home_plan()

    # Execute the plans
    print("Executing Morning Plan...")
    morning_plan(home)

    print("\nExecuting Leave Home Plan...")
    leave_home_plan(home)

    print("\nExecuting Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()