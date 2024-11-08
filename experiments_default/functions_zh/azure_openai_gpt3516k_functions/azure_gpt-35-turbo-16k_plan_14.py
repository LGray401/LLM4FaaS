# Sure, here is the 'function.py' file based on the given functional description and the provided source code:

from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.logger_config import logger

def main():
    home = home_plan()

    # MORNING PLAN
    print("MORNING PLAN:")
    logger.info("MORNING PLAN:")
    morning_room = get_room_actuators(home, "Bedroom")
    if morning_room is not None:
        for actuator in morning_room:
            if actuator.actuator_type == "Light":
                actuator.turn_on()
            elif actuator.actuator_type == "Curtain":
                actuator.turn_on()

    # LEAVE HOME PLAN
    print("\nLEAVE HOME PLAN:")
    logger.info("LEAVE HOME PLAN:")
    leave_home_room = get_room_actuators(home, "LivingRoom")
    if leave_home_room is not None:
        for actuator in leave_home_room:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
            elif actuator.actuator_type == "Window":
                actuator.turn_off()

    # MOVIE PLAN
    print("\nMOVIE PLAN:")
    logger.info("MOVIE PLAN:")
    movie_room = get_room_actuators(home, "LivingRoom")
    if movie_room is not None:
        for actuator in movie_room:
            if actuator.actuator_type == "Light":
                actuator.set_brightness_level("low")
            elif actuator.actuator_type == "Curtain":
                actuator.turn_off()
            elif actuator.actuator_type == "MusicPlayer":
                actuator.play_music("Movie Soundtrack")

if __name__ == "__main__":
    main()