from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Window
from home.logger_config import logger

def main():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    if living_room:
        windows = get_room_actuators(living_room, "Window")
        if windows:
            for window in windows:
                window.turn_on()
                logger.info(f"Window {window.id} is opened")
                print(f"Window {window.id} is opened")
        else:
            logger.warning(f"No window found in LivingRoom")
            print(f"No window found in LivingRoom")
    else:
        logger.warning(f"LivingRoom not found in the home plan")
        print(f"LivingRoom not found in the home plan")

if __name__ == "__main__":
    main()