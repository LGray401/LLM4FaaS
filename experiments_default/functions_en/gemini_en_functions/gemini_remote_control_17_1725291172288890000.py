from home.home_plan import get_room, get_room_actuators
from home.logger_config import logger


def main():
    home = get_room(get_room_actuators, "LivingRoom")
    if home is not None:
        for actuator in home:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
                logger.info(f"Turn off the living room lights")
                print(f"Turn off the living room lights")
    else:
        print(f"Error: Cannot find living room.")
        logger.error(f"Error: Cannot find living room.")

if __name__ == "__main__":
    main()