from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import Light, Heater, AC, CoffeeMachine, MusicPlayer, CleaningRobot, SmartTV, NotificationSender, \
    Humidifier, Window, Curtain
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time

def sleep_mode(home):
    """
    Turns off all lights, closes windows, and sets the temperature to a comfortable sleeping temperature.
    """

    # Turn off all lights
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()

    # Close all windows
    all_windows = get_all_actuators(home, "Window")
    for window in all_windows:
        window.turn_off()

    # Set the temperature to a comfortable sleeping temperature
    all_heaters = get_all_actuators(home, "Heater")
    for heater in all_heaters:
        heater.set_target_temperature(20)
    all_acs = get_all_actuators(home, "AC")
    for ac in all_acs:
        ac.set_target_temperature(20)

    # Play relaxing music
    living_room = get_room(home, "LivingRoom")
    if living_room:
        music_player = get_room_actuators(home, "LivingRoom")[0]
        if music_player:
            music_player.play_music("relaxing_music")

    print("Sleep mode activated.")
    logger.info("Sleep mode activated.")

def wake_up_mode(home):
    """
    Turns on lights, opens windows, and sets the temperature to a comfortable waking temperature.
    """

    # Turn on lights
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_on()

    # Open windows
    all_windows = get_all_actuators(home, "Window")
    for window in all_windows:
        window.turn_on()

    # Set the temperature to a comfortable waking temperature
    all_heaters = get_all_actuators(home, "Heater")
    for heater in all_heaters:
        heater.set_target_temperature(22)
    all_acs = get_all_actuators(home, "AC")
    for ac in all_acs:
        ac.set_target_temperature(22)

    # Play upbeat music
    living_room = get_room(home, "LivingRoom")
    if living_room:
        music_player = get_room_actuators(home, "LivingRoom")[0]
        if music_player:
            music_player.play_music("upbeat_music")

    print("Wake up mode activated.")
    logger.info("Wake up mode activated.")

def lights_off_mode(home):
    """
    Turns off all lights.
    """

    # Turn off all lights
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()

    print("Lights off mode activated.")
    logger.info("Lights off mode activated.")

def window_closing_mode(home):
    """
    Closes all windows.
    """

    # Close all windows
    all_windows = get_all_actuators(home, "Window")
    for window in all_windows:
        window.turn_off()

    print("Window closing mode activated.")
    logger.info("Window closing mode activated.")

def main():
    home = home_plan()

    # Example usage:
    sleep_mode(home)
    time.sleep(3)
    wake_up_mode(home)
    time.sleep(3)
    lights_off_mode(home)
    time.sleep(3)
    window_closing_mode(home)


if __name__ == '__main__':
    main()

# This Python file defines several functions for different smart home modes:

# - **`sleep_mode(home)`**: Turns off lights, closes windows, and sets the temperature to 20°C.
# - **`wake_up_mode(home)`**: Turns on lights, opens windows, and sets the temperature to 22°C.
# - **`lights_off_mode(home)`**: Turns off all lights.
# - **`window_closing_mode(home)`**: Closes all windows.

# The `main()` function provides an example of how to use these functions. It first creates a home plan using `home_plan()` and then calls the different modes in sequence.

# This code is based on the provided sensor.py, actuator.py, home_plan.py, and config.py files. Make sure to have these files in the same directory as `functions.py` for the code to work.
