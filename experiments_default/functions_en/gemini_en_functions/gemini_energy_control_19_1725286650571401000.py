from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger

import time

def main():
    home = home_plan()
    print_home_plan(home)
    # home_state = {}

    # Example usage
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_sensors = get_room_sensors(home, "LivingRoom")
        living_room_actuators = get_room_actuators(home, "LivingRoom")

        # Get a specific sensor
        temp_sensor = get_all_sensors(home, "IndoorTemperature")[0]
        humidity_sensor = get_all_sensors(home, "Humidity")[0]
        light_sensor = get_all_sensors(home, "LightIntensive")[0]

        # Get a specific actuator
        light = get_all_actuators(home, "Light")[0]
        window = get_all_actuators(home, "Window")[0]
        ac = get_all_actuators(home, "AC")[0]
        heater = get_all_actuators(home, "Heater")[0]
        notification_sender = get_all_actuators(home, "NotificationSender")[0]

        # Turn on sensors
        temp_sensor.turn_on()
        humidity_sensor.turn_on()
        light_sensor.turn_on()

        # Get readings
        temperature = temp_sensor.get_reading()
        humidity = humidity_sensor.get_reading()
        light_intensity = light_sensor.get_reading()

        # Example logic:
        if temperature < TEMP_LOW:
            # Turn on heater if temperature is too low
            heater.turn_on()
            heater.set_target_temperature(TEMP_HIGH)
            notification_sender.notification_sender(
                f"It's cold in the Living Room. Heating turned on to {TEMP_HIGH}°C.")
        elif temperature > TEMP_HIGH:
            # Turn on air conditioner if temperature is too high
            ac.turn_on()
            ac.set_target_temperature(TEMP_LOW)
            notification_sender.notification_sender(
                f"It's hot in the Living Room. Cooling turned on to {TEMP_LOW}°C.")

        if humidity > HUMIDITY_HIGH:
            # Open window if humidity is too high
            window.turn_on()
            notification_sender.notification_sender(f"Opening the window to reduce humidity.")

        if light_intensity < LIGHT_INTENSITY_LOW:
            # Turn on light if light intensity is too low
            light.turn_on()
            light.set_brightness_level("high")
            notification_sender.notification_sender(f"Turning on the light in the Living Room.")

        # Simulate changing temperature and humidity
        print(f"Simulating Temperature and Humidity Changes...")
        for i in range(TEMP_CHANGE_DURATION_WINDOW):
            temperature = temp_sensor.get_reading()
            humidity = humidity_sensor.get_reading()

            # Example logic:
            if temperature < TEMP_LOW:
                heater.turn_on()
            elif temperature > TEMP_HIGH:
                ac.turn_on()

            if humidity > HUMIDITY_HIGH:
                window.turn_on()

            time.sleep(1)  # Simulate time passing

        # Turn off sensors
        temp_sensor.turn_off()
        humidity_sensor.turn_off()
        light_sensor.turn_off()

        # Turn off actuators if conditions are met
        if temperature > TEMP_LOW:
            heater.turn_off()
            notification_sender.notification_sender(f"Heating turned off.")
        if temperature < TEMP_HIGH:
            ac.turn_off()
            notification_sender.notification_sender(f"Cooling turned off.")
        if humidity < HUMIDITY_HIGH:
            window.turn_off()
            notification_sender.notification_sender(f"Window closed.")
        if light_intensity > LIGHT_INTENSITY_LOW:
            light.turn_off()
            notification_sender.notification_sender(f"Light turned off.")
    else:
        print("Error: Room not found.")

if __name__ == "__main__":
    main()

# **Explanation of the function.py file:**

# 1. **Imports:**
#    - It imports relevant modules from other files in your project:
#      - `home.home_plan`: Provides functions for creating and interacting with your home plan.
#      - `home.sensor`: Defines sensor classes.
#      - `home.actuator`: Defines actuator classes.
#      - `home.config`: Contains configuration settings.
#      - `home.logger_config`: Configures logging.
#      - `time`: Used for simulating time passing.

# 2. **`main()` function:**
#    - This is the main function that runs when you execute the script.
#    - It creates a home plan (`home = home_plan()`).
#    - Retrieves the Living Room from the home plan.
#    - Gets sensors and actuators for the Living Room.
#    - Gets specific sensors and actuators.
#    - Turns on sensors to get readings.
#    - Gets readings from sensors (temperature, humidity, light intensity).
#    - Implements basic logic based on the readings:
#      - If temperature is too low, turn on the heater.
#      - If temperature is too high, turn on the air conditioner.
#      - If humidity is too high, open the window.
#      - If light intensity is too low, turn on the light.
#    - Simulates changes in temperature and humidity over time.
#    - Turns off sensors and actuators when appropriate.

# 3. **Logic Explanation:**
#    - The `main()` function demonstrates how you can use your sensors, actuators, and configuration settings to create basic home automation logic.
#    - It includes a simple temperature and humidity control system, as well as light control.
#    - The logic is illustrative and can be expanded to include more complex scenarios.

# **Key Points:**

# - This code provides a basic structure for your smart home project. You can extend it by adding more sensors, actuators, and logic to implement various functionalities.
# - The `home_plan` module defines the rooms and components of your smart home.
# - The `sensor` and `actuator` modules define the classes for the devices.
# - The `config` module holds settings and thresholds for your system.
# - The `logger_config` module helps you log events for debugging and monitoring.

# Remember to modify and enhance the code to match your specific smart home project requirements and functionalities.
