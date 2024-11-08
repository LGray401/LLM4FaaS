from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def main():
    home = home_plan()

    # Temperature Control
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temperature_sensors:
        temperature = sensor.get_reading()
        if temperature is not None:
            if temperature > TEMP_HIGH:
                print(f"Temperature in {sensor.room_name} is {temperature}°C, turning on AC.")
                logger.info(f"Temperature in {sensor.room_name} is {temperature}°C, turning on AC.")
                # Turn on all ACs in the house
                acs = get_all_actuators(home, "AC")
                for ac in acs:
                    ac.turn_on()

                # Close all windows in the house
                windows = get_all_actuators(home, "Window")
                for window in windows:
                    window.turn_off()

            elif temperature < TEMP_LOW:
                print(f"Temperature in {sensor.room_name} is {temperature}°C, turning on heater.")
                logger.info(f"Temperature in {sensor.room_name} is {temperature}°C, turning on heater.")
                # Turn on all heaters in the house
                heaters = get_all_actuators(home, "Heater")
                for heater in heaters:
                    heater.turn_on()

    # Humidity Control
    humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in humidity_sensors:
        humidity = sensor.get_reading()
        if humidity is not None:
            if humidity < HUMIDITY_LOW:
                print(f"Humidity in {sensor.room_name} is {humidity}%, turning on humidifier.")
                logger.info(f"Humidity in {sensor.room_name} is {humidity}%, turning on humidifier.")
                # Turn on all humidifiers in the house
                humidifiers = get_all_actuators(home, "Humidifier")
                for humidifier in humidifiers:
                    humidifier.turn_on()

    # Light Intensity Control
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_intensive_sensors:
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            if light_intensity < LIGHT_INTENSITY_LOW:
                print(f"Light intensity in {sensor.room_name} is {light_intensity} lux, turning on lights.")
                logger.info(f"Light intensity in {sensor.room_name} is {light_intensity} lux, turning on lights.")
                # Turn on all lights in the house
                lights = get_all_actuators(home, "Light")
                for light in lights:
                    light.turn_on()
            elif light_intensity > LIGHT_INTENSITY_HIGH:
                print(f"Light intensity in {sensor.room_name} is {light_intensity} lux, closing curtains.")
                logger.info(f"Light intensity in {sensor.room_name} is {light_intensity} lux, closing curtains.")
                # Close all curtains in the house
                curtains = get_all_actuators(home, "Curtain")
                for curtain in curtains:
                    curtain.turn_off()

    # ... (Other automation logic)

    # Example: Turn on the coffee machine in the kitchen
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        coffee_machine = get_room_actuators(kitchen, "CoffeeMachine")
        if coffee_machine:
            coffee_machine[0].turn_on()
            coffee_machine[0].make_coffee("Espresso")
    else:
        logger.error("Could not find kitchen in the home plan.")

    # Example: Play music in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        music_player = get_room_actuators(living_room, "MusicPlayer")
        if music_player:
            music_player[0].turn_on()
            music_player[0].play_music("Jazz")
    else:
        logger.error("Could not find living room in the home plan.")

    # Example: Send a notification to the user
    notification_sender = get_all_actuators(home, "NotificationSender")
    if notification_sender:
        notification_sender[0].turn_on()
        notification_sender[0].notification_sender("Reminder: Don't forget to water the plants.")
    else:
        logger.error("Could not find notification sender in the home plan.")

    print(f"Home Automation System running...")
    logger.info(f"Home Automation System running...")

    # Keep the system running to handle sensor readings and act accordingly
    while True:
        # ... (Process sensor readings and trigger actions)
        time.sleep(1)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - `home.home_plan`:  Imports functions to access home structure and components.
#    - `home.config`:  Imports configuration values like temperature thresholds.
#    - `home.logger_config`:  Imports the logger to write logs.

# 2. **`main()` Function:**
#    - **Get Sensors and Actuators:**  Uses imported functions to retrieve lists of sensors and actuators based on their types.
#    - **Temperature Control:**
#      - Loops through all `IndoorTemperatureSensor`s.
#      - For each sensor:
#        - Gets the temperature reading.
#        - If the temperature is above `TEMP_HIGH`:
#          - Turns on all `AC`s.
#          - Closes all `Window`s.
#        - If the temperature is below `TEMP_LOW`:
#          - Turns on all `Heater`s.
#    - **Humidity Control:**
#      - Loops through all `HumiditySensor`s.
#      - If the humidity is below `HUMIDITY_LOW`, turns on all `Humidifier`s.
#    - **Light Intensity Control:**
#      - Loops through all `LightIntensiveSensor`s.
#      - If the light intensity is below `LIGHT_INTENSITY_LOW`, turns on all `Light`s.
#      - If the light intensity is above `LIGHT_INTENSITY_HIGH`, closes all `Curtain`s.
#    - **Example Automation:**
#      - **Coffee Machine:** Finds the coffee machine in the kitchen and makes espresso.
#      - **Music Player:** Finds the music player in the living room and plays jazz music.
#      - **Notification:** Sends a notification to the user.
#    - **Loop:** Keeps the system running to continually process sensor readings and trigger actions.

# **Key Points:**

# - **Modular Design:**  The code uses separate files (sensor.py, actuator.py, home_plan.py, config.py) to organize code logically.
# - **Home Plan:** The `home_plan.py` file defines the home structure with rooms and components, allowing you to easily adapt the automation to different home layouts.
# - **Configuration:**  `config.py` holds constants for thresholds and other settings, making them easy to adjust.
# - **Logger:**  `logger` is used to log events and messages, helping with debugging and monitoring.

# **How to Use:**

# 1. Make sure all the Python files (sensor.py, actuator.py, home_plan.py, config.py, function.py) are in their respective folders ('home' and 'functions').
# 2. Run the `function.py` file from the 'functions' folder.

# This example provides a basic foundation for home automation. You can expand this code by:

# - **Adding more sensors and actuators:**  Define new sensor and actuator classes for devices like smart locks, security cameras, etc.
# - **Implementing more complex automation logic:**  Add conditions, timers, and schedules for more sophisticated actions.
# - **Connecting to real devices:**  Replace the simulated sensor readings and actuator actions with real-world integrations.
