from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light
from home.logger_config import logger

def main():
    """
    This function demonstrates how to use the home plan and actuator functions.
    """
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_lights = get_room_actuators(home, "LivingRoom")
        if living_room_lights:
            for light in living_room_lights:
                if isinstance(light, Light):
                    light.turn_on()
                    logger.info(f"Turned on the light in the Living Room.")
                    print(f"Turned on the light in the Living Room.")
                    break
    else:
        logger.error(f"Unable to find the Living Room.")

if __name__ == "__main__":
    main()