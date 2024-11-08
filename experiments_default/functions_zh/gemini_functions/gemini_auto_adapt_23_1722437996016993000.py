from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

import time


def main():
    """
    Main function for the smart home system.
    """
    home = home_plan()

    # Example usage:
    # - Get a room by name
    living_room = get_room(home, "LivingRoom")

    # - Get all sensors in a room
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # - Get all actuators in a room
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # - Get all sensors of a specific type
    all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")

    # - Get all actuators of a specific type
    all_lights = get_all_actuators(home, "Light")

    # Example interactions:
    # - Turn on the light in the living room
    for light in all_lights:
        if light.room_name == "LivingRoom":
            light.turn_on()
            light.set_brightness_level("high")

    # - Adjust the temperature in the living room
    for heater in get_all_actuators(home, "Heater"):
        if heater.room_name == "LivingRoom":
            heater.set_target_temperature(22)  # Set target temperature to 22 degrees Celsius
            break

    # Example automation:
    # - Auto-adjust temperature based on sensor readings
    while True:
        for temp_sensor in all_temperature_sensors:
            current_temp = temp_sensor.get_reading()
            if current_temp is not None:
                for heater in get_all_actuators(home, "Heater"):
                    if heater.room_name == temp_sensor.room_name:
                        heater.adjust_temperature(current_temp)
                        break

                for ac in get_all_actuators(home, "AC"):
                    if ac.room_name == temp_sensor.room_name:
                        ac.adjust_temperature(current_temp)
                        break

        for humidity_sensor in get_all_sensors(home, "Humidity"):
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                for humidifier in get_all_actuators(home, "Humidifier"):
                    if humidifier.room_name == humidity_sensor.room_name:
                        if current_humidity < HUMIDITY_LOW:
                            humidifier.increase_humidity()
                        elif current_humidity > HUMIDITY_HIGH:
                            humidifier.decrease_humidity()
                        break

        for light_sensor in get_all_sensors(home, "LightIntensive"):
            current_light_intensity = light_sensor.get_reading()
            if current_light_intensity is not None:
                for light in get_all_actuators(home, "Light"):
                    if light.room_name == light_sensor.room_name:
                        if current_light_intensity < LIGHT_INTENSITY_LOW:
                            light.turn_on()
                            light.set_brightness_level("medium")
                        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                            light.turn_off()
                        break

        # Example of a simple automation: Turn on the heater if the temperature is below 20 degrees
        # for sensor in all_temperature_sensors:
        #     current_temp = sensor.get_reading()
        #     if current_temp is not None and current_temp < 20:
        #         for heater in get_all_actuators(home, "Heater"):
        #             if heater.room_name == sensor.room_name:
        #                 heater.turn_on()
        #                 break

        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions to create the home plan, get rooms, sensors, and actuators.
#    - `home.sensor`: Contains classes for different sensor types (temperature, humidity, etc.).
#    - `home.actuator`: Contains classes for different actuator types (lights, heater, etc.).
#    - `home.config`: Contains configuration settings like temperature thresholds, sensor update intervals.
#    - `time`: Used for pausing the program to simulate real-time behavior.

# 2. **`main` function:**
#    - **Creating the home plan:** `home = home_plan()` creates the home structure with rooms, sensors, and actuators.
#    - **Accessing rooms, sensors, and actuators:** Demonstrates how to get specific rooms, sensors, and actuators based on their names and types.
#    - **Example interactions:**  Shows how to control actuators directly (e.g., turning on a light, setting brightness level, adjusting heater temperature).
#    - **Example automation:** Demonstrates a simple automation loop that reads sensor data and automatically adjusts actuators based on predefined rules (e.g., turning on a heater if the temperature is below the threshold).

# **Key Improvements:**

# - **Clearer function names:** Updated function names to be more descriptive (e.g., `get_room_sensors` instead of `get_sensors`).
# - **Better organization:** Improved the structure of the main function, separating different functionalities.
# - **Example automation:** Included a more realistic automation example that adjusts the temperature based on sensor readings.
# - **Complete example:** The code now provides a more comprehensive example with both manual interactions and automation.

# **To Run the Code:**

# 1. Make sure you have the necessary files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`) in the correct directory.
# 2. Run the `function.py` file: `python function.py`
# 3. Observe the output in the console, which will simulate sensor readings, actuator actions, and automation.
