from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Window, Door
from home.logger_config import logger

def open_window(room_name):
    """Opens a window in the specified room."""

    home = home_plan()
    room = get_room(home, room_name)

    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, Window):
                actuator.turn_on()
                logger.info(f"Window in {room_name} is opened.")
                print(f"Window in {room_name} is opened.")
                return

        print(f"No window found in {room_name}.")
        logger.warning(f"No window found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")

def main():
    """Main function for testing."""
    open_window("LivingRoom")

if __name__ == "__main__":
    main()