from home.home_plan import get_room, get_room_actuators, get_all_actuators
from home.logger_config import logger

def turn_off_lights_in_living_room(home):
    """Turns off all lights in the living room.

    Args:
        home: A list of Room objects representing the home.
    """
    living_room = get_room(home, "LivingRoom")
    if living_room:
        lights = get_room_actuators(home, "LivingRoom", "Light")
        if lights:
            for light in lights:
                light.turn_off()
                logger.info(f"Turned off light: {light.id}")
        else:
            logger.warning("No lights found in the Living Room.")
    else:
        logger.warning("Living Room not found in home plan.")

def main():
    """Main function to run the script."""
    home = home_plan()
    turn_off_lights_in_living_room(home)

if __name__ == "__main__":
    main()