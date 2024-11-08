# Based on your provided functional description and source code, I will create a `function.py` file with a main function to implement the "MORNING PLAN," "LEAVE HOME PLAN," and "MOVIE PLAN" functionalities. 
# 
# I'll assume some typical actions for each plan:
# 1. **MORNING PLAN**: Turn on the light, make coffee, and play some morning music in the living room.
# 2. **LEAVE HOME PLAN**: Turn off all lights, lock all doors, and turn off all actuators.
# 3. **MOVIE PLAN**: Dim the lights, close the curtains, and turn on the TV to a specific channel in the living room.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_actuators
from home.actuator import CoffeeMachine, Light, MusicPlayer, Curtain, SmartTV, Door

def morning_plan(home):
    print("\nExecuting MORNING PLAN:")
    living_room = get_room(home, "LivingRoom")

    if living_room:
        # Turn on the light
        for actuator in living_room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("high")

        # Make coffee
        for actuator in living_room.actuators:
            if isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("Espresso")

        # Play morning music
        for actuator in living_room.actuators:
            if isinstance(actuator, MusicPlayer):
                actuator.turn_on()
                actuator.play_music("Morning Playlist")


def leave_home_plan(home):
    print("\nExecuting LEAVE HOME PLAN:")
    # Turn off all lights and actuators, and lock all doors
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
            elif isinstance(actuator, Door):
                actuator.lock()
            else:
                actuator.turn_off()


def movie_plan(home):
    print("\nExecuting MOVIE PLAN:")
    living_room = get_room(home, "LivingRoom")

    if living_room:
        # Dim the lights
        for actuator in living_room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")

        # Close the curtains
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()

        # Turn on the TV to a specific channel
        for actuator in living_room.actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Movie Channel")


def main():
    home = home_plan()

    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()