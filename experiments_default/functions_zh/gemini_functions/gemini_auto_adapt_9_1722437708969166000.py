from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import Light, Heater, AC, CoffeeMachine, CleaningRobot, NotificationSender, MusicPlayer, \
    SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time


def main():
    home = home_plan()

    # Example usage of functions
    # 1. Get all sensors of a specific type in the home
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    print(f"Temperature Sensors in the home: {temperature_sensors}")
    logger.info(f"Temperature Sensors in the home: {temperature_sensors}")

    # 2. Get all actuators of a specific type in the home
    lights = get_all_actuators(home, "Light")
    print(f"Lights in the home: {lights}")
    logger.info(f"Lights in the home: {lights}")

    # 3. Get sensors in a specific room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    print(f"Living Room Sensors: {living_room_sensors}")
    logger.info(f"Living Room Sensors: {living_room_sensors}")

    # 4. Get actuators in a specific room
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    print(f"Living Room Actuators: {living_room_actuators}")
    logger.info(f"Living Room Actuators: {living_room_actuators}")

    # Example usage of sensors and actuators
    # Turn on the lights in the living room
    for light in lights:
        light.turn_on()

    # Check if the living room temperature is too low
    living_room = get_room(home, "LivingRoom")
    for sensor in living_room.sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature_reading = sensor.get_reading()
            if temperature_reading is not None and temperature_reading < TEMP_LOW:
                print(f"Living room temperature is too low ({temperature_reading}°C). Turning on the heater.")
                logger.info(f"Living room temperature is too low ({temperature_reading}°C). Turning on the heater.")
                for actuator in living_room.actuators:
                    if isinstance(actuator, Heater):
                        actuator.turn_on()
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                break

    # Example usage of functions related to actuators
    # Turn on the cleaning robot in the living room
    for actuator in living_room.actuators:
        if isinstance(actuator, CleaningRobot):
            actuator.turn_on()
            actuator.daily_routine()

    # Turn on the coffee machine in the kitchen
    kitchen = get_room(home, "Kitchen")
    for actuator in kitchen.actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")

    # Turn on the TV in the living room and play a specific channel
    for actuator in living_room.actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("BBC News")

    # Send a notification to the user
    for actuator in living_room.actuators:
        if isinstance(actuator, NotificationSender):
            actuator.turn_on()
            actuator.notification_sender("Reminder: Water the plants!")

    # Play music in the living room
    for actuator in living_room.actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Pop")

    # Adjust the AC in the living room based on the temperature
    for actuator in living_room.actuators:
        if isinstance(actuator, AC):
            for sensor in living_room.sensors:
                if isinstance(sensor, IndoorTemperatureSensor):
                    temperature_reading = sensor.get_reading()
                    if temperature_reading is not None:
                        actuator.adjust_temperature(temperature_reading)

    # Adjust the humidifier in the bathroom based on the humidity
    bathroom = get_room(home, "Bathroom")
    for actuator in bathroom.actuators:
        if isinstance(actuator, Humidifier):
            for sensor in bathroom.sensors:
                if isinstance(sensor, HumiditySensor):
                    humidity_reading = sensor.get_reading()
                    if humidity_reading is not None:
                        if humidity_reading < HUMIDITY_LOW:
                            actuator.increase_humidity()
                        elif humidity_reading > HUMIDITY_HIGH:
                            actuator.decrease_humidity()

    # Adjust the lights in the living room based on the light intensity
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            for sensor in living_room.sensors:
                if isinstance(sensor, LightIntensiveSensor):
                    light_intensity_reading = sensor.get_reading()
                    if light_intensity_reading is not None:
                        if light_intensity_reading < LIGHT_INTENSITY_LOW:
                            actuator.turn_on()
                            actuator.set_brightness_level("high")
                        elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                            actuator.set_brightness_level("low")

    # Check if the smoke sensor in the kitchen is triggered
    for actuator in kitchen.actuators:
        if isinstance(actuator, NotificationSender):
            for sensor in kitchen.sensors:
                if isinstance(sensor, SmokeSensor):
                    smoke_reading = sensor.get_reading()
                    if smoke_reading is not None and smoke_reading > 0:
                        actuator.notification_sender(
                            "Smoke detected in the kitchen! Please check the kitchen immediately.")

    # Simulate a daily routine
    print(f"Simulating daily routine...")
    logger.info(f"Simulating daily routine...")
    for actuator in living_room.actuators:
        if isinstance(actuator, CleaningRobot):
            actuator.turn_on()
            actuator.daily_routine()
    time.sleep(DAILY_ROUTINE_DURATION)
    print(f"Daily routine completed.")
    logger.info(f"Daily routine completed.")

    print(f"Program finished.")
    logger.info(f"Program finished.")


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions for managing the home plan, rooms, and components.
#    - `home.sensor`: Contains sensor classes like `IndoorTemperatureSensor`, `HumiditySensor`, etc.
#    - `home.actuator`: Contains actuator classes like `Light`, `Heater`, `CoffeeMachine`, etc.
#    - `home.config`: Contains configuration settings for thresholds, durations, and other values.
#    - `home.logger_config`: Handles logging of events for debugging and monitoring.
#    - `time`: Used for simulating time delays.

# 2. **`main()` function:**
#    - **Create a home plan:** `home = home_plan()` creates the initial home structure with rooms and components.
#    - **Example usages:** Demonstrates how to use functions from `home.home_plan` to get information about sensors, actuators, and rooms.
#    - **Sensor and actuator interactions:** Shows how to interact with sensors (e.g., get readings) and actuators (e.g., turn on/off) based on conditions.
#    - **Daily routine simulation:** Simulates a daily routine by turning on the cleaning robot, making coffee, playing music, etc.

# 3. **Logic:**
#    - The code checks conditions (temperature, humidity, light intensity, smoke) and triggers appropriate actuators based on those conditions.
#    - It includes logic for:
#      - Turning on heaters and ACs based on temperature.
#      - Adjusting the humidifier based on humidity.
#      - Turning lights on/off based on light intensity.
#      - Sending notifications when smoke is detected.
#      - Simulating a cleaning robot's daily routine.

# 4. **Logging:**
#    - The code uses the `logger` object from `home.logger_config` to log various events, including sensor readings, actuator actions, and program progress. This helps in debugging and monitoring the smart home system.

# **To run the code:**

# 1. Make sure you have the `home` folder with the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.
# 2. Place the `function.py` file in the `functions` folder.
# 3. Run the `function.py` file using Python: `python functions/function.py`.

# This will execute the example code, simulating interactions with sensors and actuators based on predefined conditions. You can adapt and expand this code to implement more complex smart home functionality.
