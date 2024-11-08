# Based on your functional description and the provided source code, here is the `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Light, SmartSocket, Door
from home.logger_config import logger

def execute_morning_plan(home):
    # Get the Living Room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Open the curtains
    curtains = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Curtain)]
    for curtain in curtains:
        curtain.turn_on()  # Assuming turn_on opens the curtain

    # Start music player
    music_players = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, MusicPlayer)]
    if music_players:
        music_players[0].turn_on()
        music_players[0].play_music("Morning Playlist")

    # Make coffee
    coffee_machines = [actuator for actuator in get_room_actuators(home, "Kitchen") if isinstance(actuator, CoffeeMachine)]
    if coffee_machines:
        coffee_machines[0].turn_on()
        coffee_machines[0].make_coffee("Espresso")

    logger.info("Morning Plan Executed")


def execute_leave_home_plan(home):
    # Iterate through all rooms to turn off lights and close doors
    for room in home:
        # Turn off lights
        lights = [actuator for actuator in get_room_actuators(home, room.name) if isinstance(actuator, Light)]
        for light in lights:
            light.turn_off()

        # Close doors
        doors = [actuator for actuator in get_room_actuators(home, room.name) if isinstance(actuator, Door)]
        for door in doors:
            door.lock()  # Assuming lock() closes the door

        # Turn off sockets except for refrigerators (assuming refrigerator is not in the SmartSocket list)
        sockets = [actuator for actuator in get_room_actuators(home, room.name) if isinstance(actuator, SmartSocket)]
        for socket in sockets:
            # You might want to add logic to exclude refrigerators if they are SmartSockets
            socket.turn_off()

    logger.info("Leave Home Plan Executed")


def execute_movie_plan(home):
    # Get the Living Room
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # Close the curtains
    curtains = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Curtain)]
    for curtain in curtains:
        curtain.turn_off()  # Assuming turn_off closes the curtain

    # Dim the lights
    lights = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Light)]
    for light in lights:
        light.set_brightness_level("low")

    # Turn on the TV
    tvs = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, SmartTV)]
    if tvs:
        tvs[0].turn_on()
        tvs[0].play_channel("Favorite Channel")

    logger.info("Movie Plan Executed")


if __name__ == "__main__":
    # Create the home plan
    home = home_plan()

    # Execute plans
    execute_morning_plan(home)
    # execute_leave_home_plan(home)
    # execute_movie_plan(home)