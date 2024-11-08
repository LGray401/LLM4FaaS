from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
import time
from home.logger_config import logger


def main():
    home = home_plan()  # Initialize the home plan
    print_home_plan(home)

    # Example usage
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_sensors = get_room_sensors(home, "LivingRoom")
        living_room_actuators = get_room_actuators(home, "LivingRoom")

        # Access sensors
        temperature_sensor = get_all_sensors(home, "IndoorTemperature")[0]
        humidity_sensor = get_all_sensors(home, "Humidity")[0]
        light_sensor = get_all_sensors(home, "LightIntensive")[0]

        # Access actuators
        light = get_all_actuators(home, "Light")[0]
        ac = get_all_actuators(home, "AC")[0]
        heater = get_all_actuators(home, "Heater")[0]
        notification_sender = get_all_actuators(home, "NotificationSender")[0]
        cleaning_robot = get_all_actuators(home, "CleaningRobot")[0]

        # Turn on sensors
        temperature_sensor.turn_on()
        humidity_sensor.turn_on()
        light_sensor.turn_on()

        # Turn on actuators
        light.turn_on()
        notification_sender.turn_on()

        # Get sensor readings
        temperature = temperature_sensor.get_reading()
        humidity = humidity_sensor.get_reading()
        light_intensity = light_sensor.get_reading()

        # Adjust temperature
        if temperature < TEMP_LOW:
            heater.turn_on()
            notification_sender.notification_sender(
                f"The temperature in the LivingRoom is below {TEMP_LOW}°C. The heater has been turned on.")
        elif temperature > TEMP_HIGH:
            ac.turn_on()
            notification_sender.notification_sender(
                f"The temperature in the LivingRoom is above {TEMP_HIGH}°C. The AC has been turned on.")
        else:
            heater.turn_off()
            ac.turn_off()

        # Adjust lighting
        if light_intensity < LIGHT_INTENSITY_LOW:
            light.set_brightness_level("high")
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            light.set_brightness_level("low")

        # Start cleaning robot
        cleaning_robot.daily_routine()

        # Simulate changes in temperature and humidity
        while True:
            temperature = temperature_sensor.get_reading()
            humidity = humidity_sensor.get_reading()

            # Adjust temperature based on readings
            if temperature < TEMP_LOW:
                heater.turn_on()
                notification_sender.notification_sender(
                    f"The temperature in the LivingRoom is below {TEMP_LOW}°C. The heater has been turned on.")
            elif temperature > TEMP_HIGH:
                ac.turn_on()
                notification_sender.notification_sender(
                    f"The temperature in the LivingRoom is above {TEMP_HIGH}°C. The AC has been turned on.")
            else:
                heater.turn_off()
                ac.turn_off()

            # Adjust humidity based on readings
            if humidity < HUMIDITY_LOW:
                # Turn on a humidifier
                print("The humidity is low. Consider turning on a humidifier.")
            elif humidity > HUMIDITY_HIGH:
                # Turn on a dehumidifier
                print("The humidity is high. Consider turning on a dehumidifier.")

            # Simulate changes over time
            time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Simulate a 1-minute time step for temperature changes

    else:
        print("Living Room not found")

    # Turn off sensors and actuators
    temperature_sensor.turn_off()
    humidity_sensor.turn_off()
    light_sensor.turn_off()
    light.turn_off()
    ac.turn_off()
    heater.turn_off()
    notification_sender.turn_off()


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - Imports necessary modules from `home` package:
#      - `home_plan` for home structure management
#      - `sensor` for sensor classes
#      - `actuator` for actuator classes
#      - `config` for configuration values
#    - Imports `time` for delays in simulations
#    - Imports `logger` from `home.logger_config` for logging.

# 2. **`main` function:**
#    - **Initializes home plan:**
#      - `home = home_plan()` creates the home structure.
#      - `print_home_plan(home)` prints the home plan to the console.
#    - **Gets LivingRoom:**
#      - `living_room = get_room(home, "LivingRoom")` retrieves the LivingRoom object.
#      - If found:
#        - **Gets sensors and actuators:**
#          - `living_room_sensors` and `living_room_actuators` lists store room's components.
#        - **Access specific sensors:**
#          - `temperature_sensor`, `humidity_sensor`, and `light_sensor` variables are assigned the first matching sensors of their type.
#        - **Access specific actuators:**
#          - `light`, `ac`, `heater`, `notification_sender`, and `cleaning_robot` variables are assigned the first matching actuators of their type.
#        - **Turns on sensors and actuators:**
#          - Calls `.turn_on()` on the selected sensors and actuators.
#        - **Gets sensor readings:**
#          - `temperature`, `humidity`, and `light_intensity` variables store the sensor readings.
#        - **Adjusts temperature and lighting:**
#          - Uses `if` conditions to check temperature and light intensity against predefined thresholds.
#          - If necessary, turns on the heater or AC, and adjusts light brightness.
#        - **Starts cleaning robot's daily routine:**
#          - Calls `cleaning_robot.daily_routine()`.
#        - **Simulates changes in temperature and humidity:**
#          - Uses a `while True` loop to continuously simulate changes.
#          - Gets updated readings from sensors.
#          - Adjusts temperature and humidity based on readings.
#          - Uses `time.sleep(TEMP_CHANGE_DURATION_WINDOW)` to simulate a 1-minute delay between temperature changes.
#      - If LivingRoom not found:
#        - Prints "Living Room not found".
#    - **Turns off sensors and actuators:**
#      - Calls `.turn_off()` on all sensors and actuators to clean up.

# 3. **`if __name__ == "__main__":` block:**
#    - Ensures that the `main()` function is executed only when the script is run directly, not when imported as a module.

# **Key points:**

# - This code demonstrates a basic smart home functionality using the provided classes and configuration.
# - It includes sensor readings, actuator control, temperature and light adjustments, and a cleaning robot routine.
# - It uses the `home_plan` module to organize the home structure and access its components.
# - The `config` module stores configuration parameters.
# - The `logger` module is used for logging events.
# - This code can be extended to incorporate more complex logic, different actuators, and user interaction.
