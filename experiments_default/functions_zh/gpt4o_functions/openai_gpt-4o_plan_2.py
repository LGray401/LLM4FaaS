# Based on the provided files and functional description, I will create a `function.py` file that will implement the required plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here is the `function.py` file:

# function.py

from home.home_plan import home_plan, get_room, get_all_actuators
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Light, Door, SmartSocket, SmartTV


def morning_plan(home):
    print("\nExecuting Morning Plan:")
    living_room = get_room(home, "LivingRoom")

    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()
                print("Curtains are opened.")
            elif isinstance(actuator, MusicPlayer):
                actuator.turn_on()
                actuator.play_music("Morning Playlist")
                print("Music player started playing the morning playlist.")
            elif isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("Latte")
                print("Coffee machine started making coffee.")


def leave_home_plan(home):
    print("\nExecuting Leave Home Plan:")
    all_lights = get_all_actuators(home, "Light")
    all_doors = get_all_actuators(home, "Door")
    all_sockets = get_all_actuators(home, "SmartSocket")

    for light in all_lights:
        light.turn_off()
        print(f"{light.id} is turned off.")

    for door in all_doors:
        door.lock()
        print(f"{door.id} is locked.")

    for socket in all_sockets:
        if "Refrigerator" not in socket.id:
            socket.turn_off()
            print(f"{socket.id} is turned off (except for refrigerator).")


def movie_plan(home):
    print("\nExecuting Movie Plan:")
    living_room = get_room(home, "LivingRoom")

    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_off()
                print("Curtains are closed.")
            elif isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")
                print("Lights are dimmed.")
            elif isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Favorite Movie Channel")
                print("TV started playing favorite movie channel.")


def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()