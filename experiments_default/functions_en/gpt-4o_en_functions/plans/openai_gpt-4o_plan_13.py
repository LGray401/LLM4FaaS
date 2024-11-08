# Based on the functional description and the provided source code files, we will create a `function.py` file located in the `functions` folder. This file will contain a main function to execute the different home plans (MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN).
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room
from home.actuator import Light, Curtain, CoffeeMachine, MusicPlayer, Door, SmartSocket, SmartTV


def execute_morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")

    if living_room:
        # Open Curtains
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()

        # Dim Lights
        for actuator in living_room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")

        # Play Music
        for actuator in living_room.actuators:
            if isinstance(actuator, MusicPlayer):
                actuator.turn_on()
                actuator.play_music("Morning Playlist")

    if kitchen:
        # Start Coffee Machine
        for actuator in kitchen.actuators:
            if isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("Espresso")


def execute_leave_home_plan(home):
    for room in home:
        # Turn off Lights
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

        # Draw Curtains
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_off()

        # Turn off Sockets
        for actuator in room.actuators:
            if isinstance(actuator, SmartSocket):
                actuator.turn_off()

        # Lock Entrance Door
        if room.name == "LivingRoom":
            for actuator in room.actuators:
                if isinstance(actuator, Door):
                    actuator.lock()


def execute_movie_plan(home):
    living_room = get_room(home, "LivingRoom")

    if living_room:
        # Draw Gauze Curtains
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()

        # Dim Lights
        for actuator in living_room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")

        # Watch TV
        for actuator in living_room.actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Movie Channel")


def main():
    home = home_plan()

    # Execute different plans
    execute_morning_plan(home)
    execute_leave_home_plan(home)
    execute_movie_plan(home)


if __name__ == "__main__":
    main()