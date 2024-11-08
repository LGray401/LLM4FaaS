from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time


def main():
    home = home_plan()
    print_home_plan(home)

    # Example usage of functions
    # Get sensors in a specific room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    print("\nSensors in LivingRoom:")
    for sensor in living_room_sensors:
        print(sensor.id)

    # Get actuators in a specific room
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    print("\nActuators in Kitchen:")
    for actuator in kitchen_actuators:
        print(actuator.id)

    # Get all sensors of a specific type
    all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    print("\nAll Indoor Temperature Sensors:")
    for sensor in all_temperature_sensors:
        print(sensor.id)

    # Get all actuators of a specific type
    all_lights = get_all_actuators(home, "Light")
    print("\nAll Lights:")
    for light in all_lights:
        print(light.id)

    # Example Smart Home Automation
    living_room = get_room(home, "LivingRoom")
    living_room_light = get_room_actuators(living_room, "Light")[0]
    living_room_temp_sensor = get_room_sensors(living_room, "IndoorTemperature")[0]
    living_room_ac = get_room_actuators(living_room, "AC")[0]

    # Check current temperature
    current_temperature = living_room_temp_sensor.get_reading()

    # Turn on the AC if temperature is high
    if current_temperature > TEMP_HIGH:
        logger.info(f"Current temperature is {current_temperature}, turning on AC.")
        living_room_ac.turn_on()
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait for a while to see the effect
        current_temperature = living_room_temp_sensor.get_reading()
        logger.info(f"Temperature now is {current_temperature}")
        if current_temperature <= TEMP_HIGH:
            logger.info(f"Temperature is now {current_temperature}, turning off AC")
            living_room_ac.turn_off()

    # Turn on the light if light intensity is low
    living_room_light_sensor = get_room_sensors(living_room, "LightIntensive")[0]
    light_intensity = living_room_light_sensor.get_reading()
    if light_intensity < LIGHT_INTENSITY_LOW:
        logger.info(f"Light intensity is low, turning on the light.")
        living_room_light.turn_on()
        living_room_light.set_brightness_level("medium")

    # Automatically activate cleaning robot
    cleaning_robot = get_room_actuators(living_room, "CleaningRobot")[0]
    cleaning_robot.turn_on()
    cleaning_robot.daily_routine()
    
    # Test Notification Sender
    notification_sender = get_room_actuators(living_room, "NotificationSender")[0]
    notification_sender.turn_on()
    notification_sender.notification_sender("test message")


if __name__ == "__main__":
    main()

# This code file `function.py` utilizes the other modules in your project:

# - **`home_plan.py`:** Provides functions to access and manipulate the home plan, including retrieving rooms, sensors, and actuators.
# - **`sensor.py`:** Defines sensor classes with methods to get readings and manage status.
# - **`actuator.py`:** Defines actuator classes with methods to control devices and manage status.
# - **`config.py`:** Contains configuration settings like temperature thresholds, humidity thresholds, and waiting durations.

# **Key improvements in this code:**

# - **`main()` function:** The main function contains a basic example of smart home automation logic, demonstrating how to use the functions provided in other modules.
# - **Example Automation:** The code demonstrates:
#     - Turning on the AC if the temperature is above the threshold.
#     - Turning on the light if the light intensity is low.
#     - Automatically activating the cleaning robot for its daily routine.
# - **Test Notification Sender:**
#     - Demonstrates how to send a notification through the `NotificationSender` class.
# - **Clearer Organization:** The code is well-organized with sections for each example, making it easier to follow.
# - **Logging:** Uses `logger.info()` to log information about the automation process for debugging and monitoring.

# **Next Steps:**

# - **Expand Automation:** Add more complex automation logic based on your specific requirements, such as:
#     - Automating curtain control based on time or light intensity.
#     - Integrating voice control or other input methods.
#     - Implementing security features like motion detection and door alarms.
# - **Error Handling:** Implement error handling for situations like sensor errors or actuator failures.
# - **User Interface:** Create a user interface (web, mobile app, etc.) to interact with your smart home system.

# This `function.py` provides a starting point for building your smart home system. Remember to customize it based on your project's specific needs and expand on the automation logic to create a truly intelligent and responsive home. 
