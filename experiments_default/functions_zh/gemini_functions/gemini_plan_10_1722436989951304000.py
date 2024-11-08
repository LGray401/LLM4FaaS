from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_actuators, get_all_sensors
from home.actuator import Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, Door, CleaningRobot, SmartTV
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def morning_plan(home):
    """
    Execute the morning plan.

    Args:
        home: The home plan object.

    Returns:
        None
    """
    # Get actuators
    living_room = get_room(home, "LivingRoom")
    curtain = [actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)][0]
    curtain.turn_on()
    print(f"Turned on the curtain in the LivingRoom")
    logger.info(f"Turned on the curtain in the LivingRoom")
    print(f"Morning plan completed.")
    logger.info(f"Morning plan completed.")


def leave_home_plan(home):
    """
    Execute the leave home plan.

    Args:
        home: The home plan object.

    Returns:
        None
    """
    # Get actuators
    living_room = get_room(home, "LivingRoom")
    light = [actuator for actuator in living_room.actuators if isinstance(actuator, Light)][0]
    window = [actuator for actuator in living_room.actuators if isinstance(actuator, Window)][0]

    # Turn off the light and window
    light.turn_off()
    window.turn_off()
    print(f"Turned off the light and window in the LivingRoom")
    logger.info(f"Turned off the light and window in the LivingRoom")

    # Get the door in LivingRoom
    door = [actuator for actuator in living_room.actuators if isinstance(actuator, Door)][0]
    door.lock()
    print(f"Locked the door in the LivingRoom")
    logger.info(f"Locked the door in the LivingRoom")

    # Turn off the light and window in Bedroom
    bedroom = get_room(home, "Bedroom")
    light = [actuator for actuator in bedroom.actuators if isinstance(actuator, Light)][0]
    window = [actuator for actuator in bedroom.actuators if isinstance(actuator, Window)][0]
    light.turn_off()
    window.turn_off()
    print(f"Turned off the light and window in the Bedroom")
    logger.info(f"Turned off the light and window in the Bedroom")

    # Lock the door in Bedroom
    door = [actuator for actuator in bedroom.actuators if isinstance(actuator, Door)][0]
    door.lock()
    print(f"Locked the door in the Bedroom")
    logger.info(f"Locked the door in the Bedroom")

    # Turn off the light and window in Kitchen
    kitchen = get_room(home, "Kitchen")
    light = [actuator for actuator in kitchen.actuators if isinstance(actuator, Light)][0]
    window = [actuator for actuator in kitchen.actuators if isinstance(actuator, Window)][0]
    light.turn_off()
    window.turn_off()
    print(f"Turned off the light and window in the Kitchen")
    logger.info(f"Turned off the light and window in the Kitchen")

    # Lock the door in Kitchen
    door = [actuator for actuator in kitchen.actuators if isinstance(actuator, Door)][0]
    door.lock()
    print(f"Locked the door in the Kitchen")
    logger.info(f"Locked the door in the Kitchen")

    # Turn off the light and window in Bathroom
    bathroom = get_room(home, "Bathroom")
    light = [actuator for actuator in bathroom.actuators if isinstance(actuator, Light)][0]
    window = [actuator for actuator in bathroom.actuators if isinstance(actuator, Window)][0]
    light.turn_off()
    window.turn_off()
    print(f"Turned off the light and window in the Bathroom")
    logger.info(f"Turned off the light and window in the Bathroom")

    # Lock the door in Bathroom
    door = [actuator for actuator in bathroom.actuators if isinstance(actuator, Door)][0]
    door.lock()
    print(f"Locked the door in the Bathroom")
    logger.info(f"Locked the door in the Bathroom")

    print(f"Leave home plan completed.")
    logger.info(f"Leave home plan completed.")


def movie_plan(home):
    """
    Execute the movie plan.

    Args:
        home: The home plan object.

    Returns:
        None
    """
    # Get actuators
    living_room = get_room(home, "LivingRoom")
    tv = [actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)][0]

    # Turn on the TV and play channel
    tv.turn_on()
    tv.play_channel("Netflix")
    print(f"Turned on the TV and play Netflix in the LivingRoom")
    logger.info(f"Turned on the TV and play Netflix in the LivingRoom")

    print(f"Movie plan completed.")
    logger.info(f"Movie plan completed.")


def main():
    """
    Main function to demonstrate smart home functionalities.
    """
    home = home_plan()

    # Example: Execute morning plan
    morning_plan(home)

    # Example: Execute leave home plan
    leave_home_plan(home)

    # Example: Execute movie plan
    movie_plan(home)


if __name__ == "__main__":
    main()