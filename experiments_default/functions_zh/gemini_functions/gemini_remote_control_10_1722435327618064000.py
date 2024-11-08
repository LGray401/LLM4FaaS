from home.home_plan import home_plan, get_room, get_room_actuators, get_all_actuators
from home.logger_config import logger

def open_window(room_name):
    """Opens a window in the specified room.

    Args:
        room_name (str): The name of the room containing the window.
    """
    home = home_plan()
    room = get_room(home, room_name)

    if room is not None:
        actuators = get_room_actuators(home, room_name)
        windows = get_all_actuators(home, "Window")
        # if windows:
        #     print(f"Found window(s) in {room_name}: {windows}")
        for window in windows:
            if window.room_name == room_name:
                if window.status == "off":
                    window.turn_on()
                    print(f"Window in {room_name} is now open.")
                    logger.info(f"Window in {room_name} is now open.")
                else:
                    print(f"Window in {room_name} is already open.")
                    logger.info(f"Window in {room_name} is already open.")
        # else:
        #     print(f"No window found in {room_name}.")
        #     logger.warning(f"No window found in {room_name}.")
    else:
        print(f"No room found with name {room_name}.")
        logger.warning(f"No room found with name {room_name}.")


if __name__ == "__main__":
    open_window("LivingRoom")