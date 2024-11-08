from home.home_plan import get_room, get_room_actuators
from home.actuator import Light
from home.logger_config import logger

def main():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_lights = get_room_actuators(home, "LivingRoom", "Light")
        if living_room_lights:
            for light in living_room_lights:
                light.turn_on()
                logger.info(f"Turned on the light in the living room.")
                print("Turned on the light in the living room.")
        else:
            print("No lights found in the living room.")
            logger.warning("No lights found in the living room.")
    else:
        print("Living room not found.")
        logger.warning("Living room not found.")

if __name__ == "__main__":
    main()