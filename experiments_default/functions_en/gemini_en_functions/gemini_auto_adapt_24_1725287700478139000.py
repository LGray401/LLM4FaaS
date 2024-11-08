from home.home_plan import get_all_sensors, get_all_actuators, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def main():
    home = home_plan()
    # ---Temperature---
    # Get all indoor temperature sensors
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all heaters
    heaters = get_all_actuators(home, "Heater")

    # Get all ACs
    acs = get_all_actuators(home, "AC")

    # Iterate through indoor temperature sensors
    for sensor in indoor_temperature_sensors:
        temperature_reading = sensor.get_reading()
        if temperature_reading is not None:
            if temperature_reading > TEMP_HIGH:
                # Turn on AC in the same room
                room = get_room(home, sensor.room_name)
                if room:
                    for ac in room.actuators:
                        if ac.actuator_type == "AC":
                            ac.turn_on()
                            print(f"Turning on AC in {sensor.room_name}")
                            logger.info(f"Turning on AC in {sensor.room_name}")
                            break
            elif temperature_reading < TEMP_LOW:
                # Turn on heater in the same room
                room = get_room(home, sensor.room_name)
                if room:
                    for heater in room.actuators:
                        if heater.actuator_type == "Heater":
                            heater.turn_on()
                            print(f"Turning on heater in {sensor.room_name}")
                            logger.info(f"Turning on heater in {sensor.room_name}")
                            break

    # ---Humidity---
    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Get all humidifiers
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        humidity_reading = sensor.get_reading()
        if humidity_reading is not None:
            if humidity_reading > HUMIDITY_HIGH:
                # Turn on humidifier in the same room
                room = get_room(home, sensor.room_name)
                if room:
                    for humidifier in room.actuators:
                        if humidifier.actuator_type == "Humidifier":
                            humidifier.decrease_humidity()
                            print(f"Decreasing humidity in {sensor.room_name}")
                            logger.info(f"Decreasing humidity in {sensor.room_name}")
                            break
            elif humidity_reading < HUMIDITY_LOW:
                # Turn on humidifier in the same room
                room = get_room(home, sensor.room_name)
                if room:
                    for humidifier in room.actuators:
                        if humidifier.actuator_type == "Humidifier":
                            humidifier.increase_humidity()
                            print(f"Increasing humidity in {sensor.room_name}")
                            logger.info(f"Increasing humidity in {sensor.room_name}")
                            break

    # ---Light Intensity---
    # Get all light intensity sensors
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")

    # Get all lights
    lights = get_all_actuators(home, "Light")

    # Get all curtains
    curtains = get_all_actuators(home, "Curtain")

    # Iterate through light intensity sensors
    for sensor in light_intensity_sensors:
        light_intensity_reading = sensor.get_reading()
        if light_intensity_reading is not None:
            if light_intensity_reading < LIGHT_INTENSITY_LOW:
                # Turn on lights in the same room
                room = get_room(home, sensor.room_name)
                if room:
                    for light in room.actuators:
                        if light.actuator_type == "Light":
                            light.turn_on()
                            print(f"Turning on lights in {sensor.room_name}")
                            logger.info(f"Turning on lights in {sensor.room_name}")
                            break
            elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                # Open curtains in the same room
                room = get_room(home, sensor.room_name)
                if room:
                    for curtain in room.actuators:
                        if curtain.actuator_type == "Curtain":
                            # Implement curtain opening logic
                            print(f"Opening curtains in {sensor.room_name}")
                            logger.info(f"Opening curtains in {sensor.room_name}")
                            break
            else:
                # If light intensity is within the desired range, do nothing
                pass


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions for managing the home structure and retrieving sensors/actuators.
#    - `home.config`: Holds configuration values for temperature, humidity, light intensity thresholds, and other constants.
#    - `home.logger_config`: Configures logging for the script.

# 2. **Define `main()` function:**
#    - Retrieves all sensors and actuators of interest using functions from `home.home_plan`.
#    - Implements the logic for each functional description:
#      - **Temperature:**
#        - Gets all indoor temperature sensors and heaters/ACs.
#        - Iterates through sensors:
#          - If temperature is above the `TEMP_HIGH` threshold:
#            - Finds the AC in the same room and turns it on.
#          - If temperature is below the `TEMP_LOW` threshold:
#            - Finds the heater in the same room and turns it on.
#      - **Humidity:**
#        - Gets all humidity sensors and humidifiers.
#        - Iterates through sensors:
#          - If humidity is above the `HUMIDITY_HIGH` threshold:
#            - Finds the humidifier in the same room and calls its `decrease_humidity` method.
#          - If humidity is below the `HUMIDITY_LOW` threshold:
#            - Finds the humidifier in the same room and calls its `increase_humidity` method.
#      - **Light Intensity:**
#        - Gets all light intensity sensors, lights, and curtains.
#        - Iterates through sensors:
#          - If light intensity is below the `LIGHT_INTENSITY_LOW` threshold:
#            - Finds the light in the same room and turns it on.
#          - If light intensity is above the `LIGHT_INTENSITY_HIGH` threshold:
#            - Finds the curtain in the same room and implements the opening logic (placeholder for now).
#          - If light intensity is within the desired range, do nothing.

# 3. **Call `main()`:**
#    - The `if __name__ == "__main__":` block ensures that the `main()` function is executed only when the script is run directly (not imported as a module).

# **Key Points:**

# - The script assumes that the `home_plan()` function from `home.home_plan` is correctly defined and returns the home structure.
# - You'll need to fill in the placeholder for opening the curtains in the light intensity logic.
# - This script provides a basic framework for your smart home project. You can expand it by adding more functionalities, sensors, actuators, and logic.
# - Consider adding error handling and more robust logic to make the script more reliable.
# - Remember to adjust the configuration values in `home.config` based on your needs.
