from home.home_plan import home_plan, get_room, get_room_actuators, get_all_actuators
from home.logger_config import logger

def turn_on_lights(home, room_names):
    """Turn on lights in the specified rooms."""
    for room_name in room_names:
        room = get_room(home, room_name)
        if room:
            lights = get_room_actuators(home, room_name, "Light")
            if lights:
                for light in lights:
                    light.turn_on()
                    logger.info(f"Turned on the light in {room_name}")
                    print(f"Turned on the light in {room_name}")
            else:
                logger.warning(f"No lights found in {room_name}")
                print(f"No lights found in {room_name}")
        else:
            logger.warning(f"Room {room_name} not found.")
            print(f"Room {room_name} not found.")


def turn_on_ac(home, room_names):
    """Turn on AC in the specified rooms."""
    for room_name in room_names:
        room = get_room(home, room_name)
        if room:
            acs = get_room_actuators(home, room_name, "AC")
            if acs:
                for ac in acs:
                    ac.turn_on()
                    logger.info(f"Turned on the AC in {room_name}")
                    print(f"Turned on the AC in {room_name}")
            else:
                logger.warning(f"No AC found in {room_name}")
                print(f"No AC found in {room_name}")
        else:
            logger.warning(f"Room {room_name} not found.")
            print(f"Room {room_name} not found.")


def turn_on_heater(home, room_names):
    """Turn on heater in the specified rooms."""
    for room_name in room_names:
        room = get_room(home, room_name)
        if room:
            heaters = get_room_actuators(home, room_name, "Heater")
            if heaters:
                for heater in heaters:
                    heater.turn_on()
                    logger.info(f"Turned on the heater in {room_name}")
                    print(f"Turned on the heater in {room_name}")
            else:
                logger.warning(f"No heater found in {room_name}")
                print(f"No heater found in {room_name}")
        else:
            logger.warning(f"Room {room_name} not found.")
            print(f"Room {room_name} not found.")


def turn_on_tv(home, room_name, channel_name):
    """Turn on TV in the specified room and play the specified channel."""
    room = get_room(home, room_name)
    if room:
        tvs = get_room_actuators(home, room_name, "SmartTV")
        if tvs:
            for tv in tvs:
                tv.turn_on()
                tv.play_channel(channel_name)
                logger.info(f"Turned on the TV in {room_name} and playing {channel_name}")
                print(f"Turned on the TV in {room_name} and playing {channel_name}")
        else:
            logger.warning(f"No TV found in {room_name}")
            print(f"No TV found in {room_name}")
    else:
        logger.warning(f"Room {room_name} not found.")
        print(f"Room {room_name} not found.")


def main():
    """Main function to execute the smart home functions."""
    home = home_plan()

    # Execute the desired functions
    turn_on_lights(home, ["LivingRoom", "Bedroom", "Bathroom"])
    turn_on_ac(home, ["LivingRoom", "Bedroom"])
    turn_on_heater(home, ["Bathroom"])
    turn_on_tv(home, "LivingRoom", "CCTV News")

    logger.info("Smart home functions executed successfully.")
    print("Smart home functions executed successfully.")


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - Import necessary modules from `home` package: `home_plan`, `get_room`, `get_room_actuators`, `get_all_actuators`.
#    - Import `logger` from `home.logger_config` to log messages.

# 2. **Functions:**
#    - **`turn_on_lights(home, room_names)`:**
#      - Iterates through each room in `room_names`.
#      - Gets the room using `get_room`.
#      - Finds the `Light` actuators in the room using `get_room_actuators`.
#      - Turns on each `Light` actuator using `turn_on()`.
#      - Logs and prints messages for successful actions and warnings for errors.
#    - **`turn_on_ac(home, room_names)`:**
#      - Same logic as `turn_on_lights` but for `AC` actuators.
#    - **`turn_on_heater(home, room_names)`:**
#      - Same logic as `turn_on_lights` but for `Heater` actuators.
#    - **`turn_on_tv(home, room_name, channel_name)`:**
#      - Gets the room using `get_room`.
#      - Finds the `SmartTV` actuator in the room.
#      - Turns on the `SmartTV` using `turn_on()`.
#      - Plays the specified `channel_name` on the TV using `play_channel()`.
#      - Logs and prints messages.

# 3. **`main()` Function:**
#    - Calls `home_plan()` to get the `home` object.
#    - Executes the functions to turn on the lights, AC, heater, and TV.
#    - Logs and prints a success message.

# 4. **`if __name__ == "__main__":` Block:**
#    - Calls the `main()` function if the script is run directly.

# **Integration with other files:**

# - **`home_plan.py`:** Provides the `home_plan()` function to create the smart home structure and `get_room`, `get_room_actuators`, `get_all_actuators` functions to access specific components.
# - **`actuator.py`:** Defines the `Light`, `AC`, `Heater`, and `SmartTV` actuator classes with `turn_on()` and other methods.
# - **`config.py`:** May contain configurations for devices, settings, or other relevant data.

# **To use the code:**

# 1. Make sure the files are in the correct folder structure (`home` folder for `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`, and `functions` folder for `function.py`).
# 2. Run the `function.py` script.

# This structure and implementation will execute the specified commands in the functional description, turning on the lights, AC, heater, and TV in the specified rooms and playing the desired channel on the TV.
