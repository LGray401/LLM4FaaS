from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Heater, AC, CoffeeMachine, Light, SmartTV, NotificationSender, MusicPlayer, CleaningRobot
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

from home.logger_config import logger


def main():
    home = home_plan()

    # Example 1: Get all indoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        print(f"Sensor ID: {sensor.id}")
        reading = sensor.get_reading()
        if reading is not None:
            print(f"Sensor Reading: {reading}°C")

    # Example 2: Get all lights and set their brightness
    lights = get_all_actuators(home, "Light")
    for light in lights:
        print(f"Light ID: {light.id}")
        light.turn_on()
        light.set_brightness_level("medium")

    # Example 3: Get all heaters and adjust temperature based on sensor readings
    heaters = get_all_actuators(home, "Heater")
    for heater in heaters:
        print(f"Heater ID: {heater.id}")
        # Get the temperature sensor in the same room
        room_sensors = get_room_sensors(home, heater.room_name)
        indoor_temp_sensor = next((sensor for sensor in room_sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        if indoor_temp_sensor is not None:
            current_temperature = indoor_temp_sensor.get_reading()
            if current_temperature is not None:
                heater.adjust_temperature(current_temperature)

    # Example 4: Send a notification
    notification_sender = get_all_actuators(home, "NotificationSender")[0]
    notification_sender.notification_sender("This is a test notification!")

    # Example 5: Play music
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        print(f"Music Player ID: {music_player.id}")
        music_player.play_music("Pop Hits")

    # Example 6: Start daily cleaning routine for cleaning robots
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for cleaning_robot in cleaning_robots:
        print(f"Cleaning Robot ID: {cleaning_robot.id}")
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

    # Example 7: Adjust AC temperature based on sensor readings
    acs = get_all_actuators(home, "AC")
    for ac in acs:
        print(f"AC ID: {ac.id}")
        # Get the temperature sensor in the same room
        room_sensors = get_room_sensors(home, ac.room_name)
        indoor_temp_sensor = next((sensor for sensor in room_sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        if indoor_temp_sensor is not None:
            current_temperature = indoor_temp_sensor.get_reading()
            if current_temperature is not None:
                ac.adjust_temperature(current_temperature)

    # Example 8: Make coffee using a coffee machine
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_machines:
        print(f"Coffee Machine ID: {coffee_machine.id}")
        coffee_machine.make_coffee("Espresso")

    # Example 9: Adjust light intensity based on sensor readings
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_intensive_sensors:
        print(f"Light Intensity Sensor ID: {sensor.id}")
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            # Get the lights in the same room
            room_actuators = get_room_actuators(home, sensor.room_name)
            lights = [actuator for actuator in room_actuators if isinstance(actuator, Light)]
            for light in lights:
                if light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                    light.set_brightness_level("high")
                elif light_intensity > LIGHT_INTENSITY_HIGH:
                    light.turn_off()
                else:
                    light.turn_on()
                    light.set_brightness_level("medium")

    # Example 10: Play a channel on a smart TV
    smart_tvs = get_all_actuators(home, "SmartTV")
    for smart_tv in smart_tvs:
        print(f"Smart TV ID: {smart_tv.id}")
        smart_tv.play_channel("News")

    # Example 11: Adjust humidity using a humidifier
    humidifiers = get_all_actuators(home, "Humidifier")
    for humidifier in humidifiers:
        print(f"Humidifier ID: {humidifier.id}")
        # Get the humidity sensor in the same room
        room_sensors = get_room_sensors(home, humidifier.room_name)
        humidity_sensor = next((sensor for sensor in room_sensors if isinstance(sensor, HumiditySensor)), None)
        if humidity_sensor is not None:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()

    # Example 12: Control heater and AC based on outdoor temperature
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    for sensor in outdoor_temp_sensors:
        print(f"Outdoor Temperature Sensor ID: {sensor.id}")
        outdoor_temperature = sensor.get_reading()
        if outdoor_temperature is not None:
            # Get all heaters and ACs in the home
            heaters = get_all_actuators(home, "Heater")
            acs = get_all_actuators(home, "AC")

            for heater in heaters:
                heater.adjust_temperature(outdoor_temperature)

            for ac in acs:
                ac.adjust_temperature(outdoor_temperature)

    logger.info("Finished executing functions.py")
    print("Finished executing functions.py")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import Necessary Modules:**
#    - `from home.home_plan import ...`: Imports functions for managing rooms and devices.
#    - `from home.sensor import ...`: Imports sensor classes.
#    - `from home.actuator import ...`: Imports actuator classes.
#    - `from home.config import ...`: Imports configuration values.
#    - `from home.logger_config import logger`: Imports the logger for logging information.

# 2. **`main` Function:**
#    - **Get Devices:**  Uses functions from `home_plan.py` to get lists of various types of sensors and actuators.
#    - **Demonstrate Functionality:** Includes various examples showing how to interact with sensors and actuators.
#       - **Get Sensor Readings:** Demonstrates getting readings from temperature, humidity, and light sensors.
#       - **Control Lights:** Turns on lights and adjusts brightness.
#       - **Control Heaters and ACs:** Adjust heater and AC temperatures based on sensor readings.
#       - **Send Notifications:** Sends a notification message.
#       - **Play Music:** Plays music on music players.
#       - **Start Cleaning Routine:** Starts a daily cleaning routine for cleaning robots.
#       - **Make Coffee:** Makes coffee using a coffee machine.
#       - **Adjust Light Intensity:** Adjusts light brightness based on light intensity readings.
#       - **Play TV Channel:** Plays a channel on a smart TV.
#       - **Control Humidifier:** Adjusts humidity levels using a humidifier.
#       - **Control Devices Based on Outdoor Temperature:** Adjusts heaters and ACs based on outdoor temperature.

# 3. **Logger:** Uses `logger` to log information about program execution and device actions.

# **Key Points:**

# - The `function.py` file demonstrates how to interact with sensors and actuators in a smart home system.
# - It provides clear examples of how to get sensor readings, control actuators, and perform various tasks based on sensor data.
# - The use of a logger helps track program execution and device actions.
# - The code is modular, allowing you to easily add or modify functionality as needed.

# **To Use:**

# 1. Make sure you have the following files in your project:
#    - `sensor.py`
#    - `actuator.py`
#    - `home_plan.py`
#    - `config.py`
#    - `logger_config.py`

# 2. Create a `functions` folder and place `function.py` inside it.

# 3. Run `function.py` to see the example code in action.
