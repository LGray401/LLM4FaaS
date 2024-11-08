from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Light, AC, Heater, CleaningRobot, SmartSocket, MusicPlayer, Curtain, SmartTV, Humidifier, \
    NotificationSender
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, \
    LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION, TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger


def energy_saving_mode(home):
    """
    Implements the energy saving mode for the smart home.
    """

    logger.info("Entering energy saving mode...")
    print("Entering energy saving mode...")

    # Turn off all lights
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()
        light.set_brightness_level("low")

    # Close all curtains
    all_curtains = get_all_actuators(home, "Curtain")
    for curtain in all_curtains:
        curtain.turn_off()

    # Turn off unused smart sockets
    all_smart_sockets = get_all_actuators(home, "SmartSocket")
    for smart_socket in all_smart_sockets:
        smart_socket.turn_off()

    # Stop humidifier
    all_humidifiers = get_all_actuators(home, "Humidifier")
    for humidifier in all_humidifiers:
        humidifier.turn_off()

    # Return cleaning robot to its base
    all_cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for cleaning_robot in all_cleaning_robots:
        cleaning_robot.turn_off()

    # Turn off music player
    all_music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in all_music_players:
        music_player.turn_off()

    # Set TV to energy saving mode
    all_smart_tvs = get_all_actuators(home, "SmartTV")
    for smart_tv in all_smart_tvs:
        smart_tv.turn_off()

    # Adjust temperature
    all_heaters = get_all_actuators(home, "Heater")
    for heater in all_heaters:
        heater.turn_off()
    all_acs = get_all_actuators(home, "AC")
    for ac in all_acs:
        ac.turn_off()

    logger.info("Energy saving mode activated successfully!")
    print("Energy saving mode activated successfully!")


def main():
    """
    Main function to test energy saving mode.
    """
    home = home_plan()

    # Example: Simulate some initial conditions
    living_room = get_room(home, "LivingRoom")
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Simulate the living room light being on and at high brightness
    living_room_light = living_room_actuators[0]
    living_room_light.turn_on()
    living_room_light.set_brightness_level("high")

    # Simulate the living room AC being on
    living_room_ac = living_room_actuators[10]
    living_room_ac.turn_on()

    # Simulate the living room cleaning robot being on
    living_room_cleaning_robot = living_room_actuators[9]
    living_room_cleaning_robot.turn_on()

    # Simulate the living room smart socket being on
    living_room_smart_socket = living_room_actuators[7]
    living_room_smart_socket.turn_on()

    # Simulate the living room music player being on
    living_room_music_player = living_room_actuators[6]
    living_room_music_player.turn_on()

    # Simulate the living room curtain being open
    living_room_curtain = living_room_actuators[5]
    living_room_curtain.turn_on()

    # Simulate the living room smart TV being on
    living_room_smart_tv = living_room_actuators[11]
    living_room_smart_tv.turn_on()

    # Simulate the living room humidifier being on
    living_room_humidifier = living_room_actuators[12]
    living_room_humidifier.turn_on()

    # Simulate the living room temperature sensor reading
    living_room_temperature_sensor = living_room_sensors[1]
    living_room_temperature_sensor.turn_on()
    living_room_temperature = living_room_temperature_sensor.get_reading()
    print(f"Living room temperature: {living_room_temperature}")
    logger.info(f"Living room temperature: {living_room_temperature}")

    # Simulate the living room humidity sensor reading
    living_room_humidity_sensor = living_room_sensors[2]
    living_room_humidity_sensor.turn_on()
    living_room_humidity = living_room_humidity_sensor.get_reading()
    print(f"Living room humidity: {living_room_humidity}")
    logger.info(f"Living room humidity: {living_room_humidity}")

    # Simulate the living room light intensity sensor reading
    living_room_light_intensity_sensor = living_room_sensors[0]
    living_room_light_intensity_sensor.turn_on()
    living_room_light_intensity = living_room_light_intensity_sensor.get_reading()
    print(f"Living room light intensity: {living_room_light_intensity}")
    logger.info(f"Living room light intensity: {living_room_light_intensity}")

    # Activate energy saving mode
    energy_saving_mode(home)

    # Print home plan with current status
    print_home_plan(home)
    print("Energy saving mode activated, you can check the home plan")
    logger.info(
        "Energy saving mode activated, please check the home plan to confirm if the devices are turned off")


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** The code imports necessary modules and classes from your other files:
#     - `home.home_plan`: For home plan functions like creating rooms and getting devices.
#     - `home.sensor`: For sensor classes like `IndoorTemperatureSensor` and `HumiditySensor`.
#     - `home.actuator`: For actuator classes like `Light`, `AC`, and `CleaningRobot`.
#     - `home.config`: For configuration variables like temperature thresholds and duration.
#     - `home.logger_config`: To log messages.

# 2. **`energy_saving_mode` Function:**
#     - This function implements the core logic for energy saving mode.
#     - It iterates through all devices of each type in the home and performs the desired actions:
#         - **Lights:** Turn off and set to low brightness.
#         - **Curtains:** Close.
#         - **Smart Sockets:** Turn off.
#         - **Humidifier:** Turn off.
#         - **Cleaning Robot:** Turn off.
#         - **Music Player:** Turn off.
#         - **Smart TV:** Turn off.
#         - **Heater/AC:** Turn off.

# 3. **`main` Function:**
#     - This function is an example demonstrating how to use the `energy_saving_mode` function.
#     - It simulates some initial conditions for a living room (lights on, AC on, etc.).
#     - It then calls `energy_saving_mode` to activate energy saving mode.
#     - Finally, it prints the updated home plan to show the changes.

# **Key Improvements:**

# - **Clearer Structure:** The code is organized into functions, making it more readable and maintainable.
# - **Function-Based Approach:**  The `energy_saving_mode` function encapsulates the core logic, making it reusable and easier to test.
# - **Better Error Handling:** The code uses a logger to record messages, helping with debugging and understanding the system's behavior.

# **How to Use:**

# 1. **Integrate with Your Project:** Replace the example simulation in the `main` function with your actual sensor and actuator data.
# 2. **Call `energy_saving_mode`:** Call the function when you want to activate energy saving mode in your smart home application.

# This code provides a robust framework for implementing an energy saving mode in your smart home project. You can easily customize it to fit your specific requirements.
