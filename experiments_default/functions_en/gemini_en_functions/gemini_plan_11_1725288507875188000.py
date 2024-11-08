from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.actuator import Light, SmartTV, CleaningRobot, NotificationSender
from home.sensor import OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.logger_config import logger
import time


def morning_plan(home):
    """
    Executes the morning plan.

    Args:
        home: A list of Room objects representing the home layout.
    """

    # Turn on the light in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        lights = get_room_actuators(home, "LivingRoom")
        if lights is not None:
            for light in lights:
                if light.actuator_type == "Light":
                    print(f"Turning on the light in the Living Room...")
                    logger.info("Turning on the light in the Living Room...")
                    light.turn_on()
                    time.sleep(1)


def leave_home_plan(home):
    """
    Executes the leave home plan.

    Args:
        home: A list of Room objects representing the home layout.
    """

    # Check if it's raining
    outdoor_sensors = get_all_sensors(home, "OutdoorTemperature")
    if outdoor_sensors is not None:
        for outdoor_sensor in outdoor_sensors:
            if outdoor_sensor.sensor_type == "OutdoorTemperature":
                print("Checking the weather...")
                logger.info("Checking the weather...")
                current_temperature = outdoor_sensor.get_reading()
                if current_temperature is not None:
                    # Open the curtains if it's raining
                    if current_temperature < 10:  # You might want to adjust this temperature threshold
                        print("It's raining! Opening the curtains...")
                        logger.info("It's raining! Opening the curtains...")
                        living_room = get_room(home, "LivingRoom")
                        if living_room is not None:
                            curtains = get_room_actuators(home, "LivingRoom")
                            if curtains is not None:
                                for curtain in curtains:
                                    if curtain.actuator_type == "Curtain":
                                        curtain.turn_on()
                                        time.sleep(1)


def movie_plan(home):
    """
    Executes the movie plan.

    Args:
        home: A list of Room objects representing the home layout.
    """

    # Turn on the TV in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        tvs = get_room_actuators(home, "LivingRoom")
        if tvs is not None:
            for tv in tvs:
                if tv.actuator_type == "SmartTV":
                    print("Turning on the TV in the Living Room...")
                    logger.info("Turning on the TV in the Living Room...")
                    tv.turn_on()
                    time.sleep(1)
                    print("Playing Netflix...")
                    logger.info("Playing Netflix...")
                    tv.play_channel("Netflix")
                    time.sleep(1)


def main():
    """
    Main function for the smart home system.
    """

    # Initialize home layout
    home = home_plan()

    # Run the plans based on user input or pre-programmed schedules
    # Example usage:
    morning_plan(home)  # Execute morning plan
    leave_home_plan(home)  # Execute leave home plan
    movie_plan(home)  # Execute movie plan

    # Example of automation:
    # Check temperature and humidity levels
    # living_room = get_room(home, "LivingRoom")
    # if living_room is not None:
    #     living_room_temperature_sensor = get_room_sensors(home, "LivingRoom")[0]
    #     current_temperature = living_room_temperature_sensor.get_reading()
    #     if current_temperature < TEMP_LOW:
    #         # Turn on heater
    #         living_room_heater = get_room_actuators(home, "LivingRoom")[0]
    #         living_room_heater.turn_on()
    #         print("Turning on the heater in the Living Room...")
    #         logger.info("Turning on the heater in the Living Room...")

    # # Turn off the heater after a while
    # time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    # living_room_heater.turn_off()
    # print("Turning off the heater in the Living Room...")
    # logger.info("Turning off the heater in the Living Room...")

    # # Check humidity levels in Living Room
    # living_room_humidity_sensor = get_room_sensors(home, "LivingRoom")[1]
    # current_humidity = living_room_humidity_sensor.get_reading()
    # if current_humidity < HUMIDITY_LOW:
    #     # Turn on humidifier
    #     living_room_humidifier = get_room_actuators(home, "LivingRoom")[3]
    #     living_room_humidifier.increase_humidity()
    #     print("Turning on the humidifier in the Living Room...")
    #     logger.info("Turning on the humidifier in the Living Room...")

    # # Turn off the humidifier after a while
    # time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    # living_room_humidifier.decrease_humidity()
    # print("Turning off the humidifier in the Living Room...")
    # logger.info("Turning off the humidifier in the Living Room...")

    # # Check light intensity in Living Room
    # living_room_light_sensor = get_room_sensors(home, "LivingRoom")[2]
    # current_light_intensity = living_room_light_sensor.get_reading()
    # if current_light_intensity < LIGHT_INTENSITY_LOW:
    #     # Turn on light
    #     living_room_light = get_room_actuators(home, "LivingRoom")[0]
    #     living_room_light.turn_on()
    #     print("Turning on the light in the Living Room...")
    #     logger.info("Turning on the light in the Living Room...")

    # # Turn off the light after a while
    # time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    # living_room_light.turn_off()
    # print("Turning off the light in the Living Room...")
    # logger.info("Turning off the light in the Living Room...")

    # # Start cleaning robot in Living Room
    # living_room_cleaning_robot = get_room_actuators(home, "LivingRoom")[5]
    # living_room_cleaning_robot.daily_routine()
    # print("Starting daily cleaning routine in the Living Room...")
    # logger.info("Starting daily cleaning routine in the Living Room...")

    # # Send a notification to user
    # living_room_notification_sender = get_room_actuators(home, "LivingRoom")[4]
    # living_room_notification_sender.notification_sender("The cleaning robot is done.")
    # print("Sending a notification to user...")
    # logger.info("Sending a notification to user...")


if __name__ == "__main__":
    main()

# **Explanation:**

# - **Import necessary modules:** This imports the relevant modules from your `home` package and other necessary modules.
# - **Define plan functions:**
#     - `morning_plan(home)`: Turns on the lights in the Living Room.
#     - `leave_home_plan(home)`: Opens the curtains in the Living Room if it's raining.
#     - `movie_plan(home)`: Turns on the TV in the Living Room and plays Netflix.
# - **`main()` function:**
#     - Initializes the `home` layout using `home_plan()`.
#     - Executes the plans based on user input or pre-programmed schedules (example usage provided).
#     - Demonstrates how to interact with sensors and actuators to implement automation.

# **Remember:**

# - This code assumes you have implemented the classes and functions defined in the provided source code files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`).
# - You can modify and extend these functions to implement more complex plans and automation based on your needs.
# - Replace the example plan calls in `main()` with your actual desired behavior.
# - You'll need to adapt the weather check logic and the threshold values to fit your specific requirements.

# This `function.py` file provides a starting point for your smart home project. Feel free to ask further questions and I'll be happy to help you refine your implementation.
