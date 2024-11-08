# Based on the functional description and provided source code, I will create a `function.py` file in the `functions` folder. This file will contain the main function to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light, MusicPlayer, SmartTV, Door, NotificationSender, CleaningRobot


def morning_plan(home):
    print("Executing MORNING PLAN")
    # Find the actuators in the required rooms
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Turn on lights in the bedroom
    for actuator in bedroom_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()

    # Turn on coffee machine in the kitchen
    for actuator in kitchen_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")

    # Turn on music player in the living room
    for actuator in living_room_actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")


def leave_home_plan(home):
    print("Executing LEAVE HOME PLAN")
    # Find the actuators in the required rooms
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    kitchen_actuators = get_room_actuators(home, "Kitchen")

    # Turn off all lights and lock doors
    for room_actuators in [living_room_actuators, bedroom_actuators, kitchen_actuators]:
        for actuator in room_actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
            if isinstance(actuator, Door):
                actuator.lock()

    # Send notification
    for actuator in living_room_actuators:
        if isinstance(actuator, NotificationSender):
            actuator.turn_on()
            actuator.notification_sender("The house is locked and secured. All lights are off.")

    # Start cleaning robot in the living room
    for actuator in living_room_actuators:
        if isinstance(actuator, CleaningRobot):
            actuator.turn_on()
            actuator.daily_routine()


def movie_plan(home):
    print("Executing MOVIE PLAN")
    # Find the actuators in the required rooms
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Turn on TV and turn off lights
    for actuator in living_room_actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Movie Channel")
        if isinstance(actuator, Light):
            actuator.turn_off()


def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()