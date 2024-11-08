from home.home_plan import get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators, get_room
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    DAILY_ROUTINE_DURATION
from home.sensor import LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import Light, AC, Heater, CoffeeMachine, CleaningRobot, SmartTV, MusicPlayer, Door, NotificationSender
from home.logger_config import logger


def morning_plan(home):
    """
    Implements the "MORNING PLAN" for the smart home.
    Turns on lights in the living room and bedroom, starts playing music in the living room,
    and makes coffee in the kitchen.
    """
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")

    # Turn on lights
    for light in get_room_actuators(home, "LivingRoom"):
        if light.actuator_type == "Light":
            light.turn_on()
    for light in get_room_actuators(home, "Bedroom"):
        if light.actuator_type == "Light":
            light.turn_on()

    # Start music
    for music_player in get_room_actuators(home, "LivingRoom"):
        if music_player.actuator_type == "MusicPlayer":
            music_player.play_music("Morning playlist")

    # Make coffee
    for coffee_machine in get_room_actuators(home, "Kitchen"):
        if coffee_machine.actuator_type == "CoffeeMachine":
            coffee_machine.make_coffee("Espresso")

    logger.info("Morning plan completed.")
    print("Morning plan completed.")


def leave_home_plan(home):
    """
    Implements the "LEAVE HOME PLAN" for the smart home.
    Turns off lights in all rooms, closes all windows, locks the door and sends a notification to the user
    """
    # Turn off lights in all rooms
    for light in get_all_actuators(home, "Light"):
        light.turn_off()

    # Close all windows
    for window in get_all_actuators(home, "Window"):
        window.turn_off()

    # Lock the door
    for door in get_all_actuators(home, "Door"):
        door.lock()

    # Send a notification
    for notification_sender in get_all_actuators(home, "NotificationSender"):
        notification_sender.notification_sender(
            "Leaving home, all lights are off, windows are closed, and the door is locked. Have a great day!")

    logger.info("Leave home plan completed.")
    print("Leave home plan completed.")


def movie_plan(home):
    """
    Implements the "MOVIE PLAN" for the smart home.
    Turns off lights in the living room, sets the AC to a comfortable temperature,
    starts playing a movie on the TV, and sets the brightness level of the lights to "low".
    """
    living_room = get_room(home, "LivingRoom")
    for light in get_room_actuators(home, "LivingRoom"):
        if light.actuator_type == "Light":
            light.turn_off()
    for ac in get_room_actuators(home, "LivingRoom"):
        if ac.actuator_type == "AC":
            ac.set_target_temperature(22)
            ac.turn_on()
    for tv in get_room_actuators(home, "LivingRoom"):
        if tv.actuator_type == "SmartTV":
            tv.play_channel("Netflix")
    for light in get_room_actuators(home, "LivingRoom"):
        if light.actuator_type == "Light":
            light.set_brightness_level("low")

    logger.info("Movie plan completed.")
    print("Movie plan completed.")


def daily_routine_plan(home):
    """
    Implements the "DAILY ROUTINE PLAN" for the smart home.
    Starts the cleaning robot in the living room, bedroom, and kitchen
    Adjusts the AC/Heater based on the temperature and humidity
    """
    # Starts cleaning robot
    for cleaning_robot in get_all_actuators(home, "CleaningRobot"):
        cleaning_robot.daily_routine()

    # Adjust temperature and humidity in each room
    for room in home:
        # Adjust AC/Heater
        for ac in get_room_actuators(home, room.name):
            if ac.actuator_type == "AC":
                for temp_sensor in get_room_sensors(home, room.name):
                    if temp_sensor.sensor_type == "IndoorTemperature":
                        current_temperature = temp_sensor.get_reading()
                        ac.adjust_temperature(current_temperature)
        for heater in get_room_actuators(home, room.name):
            if heater.actuator_type == "Heater":
                for temp_sensor in get_room_sensors(home, room.name):
                    if temp_sensor.sensor_type == "IndoorTemperature":
                        current_temperature = temp_sensor.get_reading()
                        heater.adjust_temperature(current_temperature)

    logger.info("Daily routine plan completed.")
    print("Daily routine plan completed.")


def main():
    """
    Main function that sets up the smart home and runs the plans.
    """
    home = home_plan()
    morning_plan(home)
    daily_routine_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** The necessary modules from `home` folder are imported, including sensor types, actuator types, configuration values, and the `logger_config` for logging.

# 2. **Plan Functions:**
#    - `morning_plan()`, `leave_home_plan()`, `movie_plan()`, and `daily_routine_plan()` implement the respective plans by:
#      - Accessing specific rooms and actuators using functions like `get_room()`, `get_room_actuators()`, `get_all_actuators()`.
#      - Manipulating actuator states using methods like `turn_on()`, `turn_off()`, `set_target_temperature()`, `play_music()`, etc.
#      - Reading sensor values using `get_reading()`.
#      - Logging actions using the `logger` object.

# 3. **`main()` function:**
#    - Creates the `home` using `home_plan()`.
#    - Calls the plan functions in sequence, demonstrating how they interact with the smart home.

# 4. **Conditionals and Loops:** 
#    - Loops are used to iterate through rooms or actuators. 
#    - Conditionals are used to select specific actuator types within a room.

# **To use this file:**

# 1. Save it as `function.py` in the `functions` folder.
# 2. Make sure the `home` folder is in the same directory.
# 3. Run `function.py` to execute the smart home plans.

# **Note:**

# - This code assumes the `home` folder contains the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files you provided.
# - The code provides a basic example. You can expand it further by adding more plan functions, sensor types, actuator types, and complex logic based on your smart home requirements.
