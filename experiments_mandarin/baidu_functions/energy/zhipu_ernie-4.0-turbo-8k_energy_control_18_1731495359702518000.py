# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to open a window. The main function will utilize the classes and methods defined in the `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Window
from home.logger_config import logger

def open_window(room_name):
    # Get the home plan
    home = home_plan()
    
    # Get the specified room
    room = get_room(home, room_name)
    if room is None:
        return
    
    # Get the actuators in the room
    actuators = get_room_actuators(home, room_name)
    if actuators is None:
        return
    
    # Find the window actuator and open it
    for actuator in actuators:
        if isinstance(actuator, Window):
            if actuator.status == "off":
                actuator.turn_on()
                logger.info(f"Opened window in {room_name}.")
                print(f"Opened window in {room_name}.")
            else:
                logger.info(f"Window in {room_name} is already open.")
                print(f"Window in {room_name} is already open.")
            break
    else:
        logger.warning(f"No window found in {room_name}.")
        print(f"No window found in {room_name}.")

if __name__ == "__main__":
    # Example usage: open the window in the LivingRoom
    open_window("LivingRoom")