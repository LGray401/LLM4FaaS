from home.home_plan import get_room, get_room_actuators, get_all_actuators
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH


def open_windows(home, room_name):
    """Opens all the windows in the specified room.

    Args:
        home: A list of Room objects representing the home.
        room_name: The name of the room to open the windows in.
    """

    room = get_room(home, room_name)
    if room:
        actuators = get_room_actuators(home, room_name)
        if actuators:
            for actuator in actuators:
                if actuator.actuator_type == "Window":
                    actuator.turn_on()
                    logger.info(f"Opened window {actuator.id} in {room_name}")
        else:
            logger.warning(f"No actuators found in {room_name}")
    else:
        logger.warning(f"Room '{room_name}' not found in home plan.")


def open_all_windows(home):
    """Opens all windows in the house.

    Args:
        home: A list of Room objects representing the home.
    """

    windows = get_all_actuators(home, "Window")
    if windows:
        for window in windows:
            window.turn_on()
            logger.info(f"Opened window {window.id}")
    else:
        logger.warning(f"No windows found in the home plan.")


def main():
    # Load the home plan
    home = home_plan()  # Replace with your actual home plan creation

    # Open the windows in the LivingRoom
    open_windows(home, "LivingRoom")

    # Open all windows in the house
    open_all_windows(home)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - `get_room`, `get_room_actuators`, `get_all_actuators`: These functions are imported from `home.home_plan` to access the home plan data.
#    - `logger`: The logger from `home.logger_config` is imported for logging messages.
#    - `TEMP_LOW`, `TEMP_HIGH`: These constants are imported from `home.config` for temperature thresholds (you can customize these as needed).

# 2. **`open_windows` Function:**
#    - Takes `home` (the list of rooms) and `room_name` as input.
#    - Calls `get_room` to find the specified room.
#    - If the room is found, it gets the actuators of that room using `get_room_actuators`.
#    - Iterates through the actuators and finds all "Window" actuators.
#    - Calls `turn_on()` on each window actuator to open the window and logs the action.

# 3. **`open_all_windows` Function:**
#    - Takes `home` as input.
#    - Calls `get_all_actuators` to find all window actuators in the entire home.
#    - Iterates through the windows and calls `turn_on()` on each one.
#    - Logs the action.

# 4. **`main` Function:**
#    - Calls `home_plan()` to get the home plan data.
#    - Calls `open_windows` to open the windows in the "LivingRoom".
#    - Calls `open_all_windows` to open all windows in the home.

# 5. **`if __name__ == "__main__":` Block:**
#    - Executes the `main` function when the file is run directly.

# **How to Use:**

# 1. **Replace `home_plan()`:** In the `main` function, replace `home_plan()` with your actual code to load your home plan data from your `home_plan.py` file.
# 2. **Run the File:** Save the code as `function.py` in the `functions` folder of your project and run it. This will open the windows based on your home plan and the defined functions.

# Remember to customize the `TEMP_LOW`, `TEMP_HIGH`, and other constants in `config.py` according to your specific needs.
