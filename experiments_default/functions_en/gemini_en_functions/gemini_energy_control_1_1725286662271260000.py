from home.home_plan import get_all_actuators, get_all_sensors, get_room_actuators, get_room_sensors, home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def turn_off_unnecessary_switches(home):
    """
    This function turns off unnecessary switches in the smart home based on sensor readings and pre-defined thresholds.

    Args:
        home: The smart home object containing rooms, sensors, and actuators.

    Returns:
        None
    """

    # Turn off lights in rooms with sufficient light intensity
    lights = get_all_actuators(home, "Light")
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    for light in lights:
        for sensor in light_intensive_sensors:
            if sensor.room_name == light.room_name and sensor.get_reading() > LIGHT_INTENSITY_HIGH:
                print(f"Turning off {light.id} in {light.room_name} because light intensity is high.")
                logger.info(
                    f"Turning off {light.id} in {light.room_name} because light intensity is high."
                )
                light.turn_off()

    # Turn off heaters in rooms with temperature above the threshold
    heaters = get_all_actuators(home, "Heater")
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    for heater in heaters:
        for sensor in indoor_temperature_sensors:
            if sensor.room_name == heater.room_name and sensor.get_reading() > TEMP_HIGH:
                print(f"Turning off {heater.id} in {heater.room_name} because temperature is high.")
                logger.info(
                    f"Turning off {heater.id} in {heater.room_name} because temperature is high."
                )
                heater.turn_off()

    # Turn off ACs in rooms with temperature below the threshold
    acs = get_all_actuators(home, "AC")
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    for ac in acs:
        for sensor in indoor_temperature_sensors:
            if sensor.room_name == ac.room_name and sensor.get_reading() < TEMP_LOW:
                print(f"Turning off {ac.id} in {ac.room_name} because temperature is low.")
                logger.info(
                    f"Turning off {ac.id} in {ac.room_name} because temperature is low."
                )
                ac.turn_off()

    # Turn off humidifiers in rooms with humidity above the threshold
    humidifiers = get_all_actuators(home, "Humidifier")
    humidity_sensors = get_all_sensors(home, "Humidity")
    for humidifier in humidifiers:
        for sensor in humidity_sensors:
            if sensor.room_name == humidifier.room_name and sensor.get_reading() > HUMIDITY_HIGH:
                print(
                    f"Turning off {humidifier.id} in {humidifier.room_name} because humidity is high."
                )
                logger.info(
                    f"Turning off {humidifier.id} in {humidifier.room_name} because humidity is high."
                )
                humidifier.turn_off()


def main():
    """
    The main function of the script.

    This function creates the smart home object, reads sensor data,
    and calls the `turn_off_unnecessary_switches` function to turn off
    unnecessary switches based on the sensor readings.
    """

    # Create smart home object (replace with your home plan setup)
    home = home_plan()

    # ... (Code to read sensor data and populate the home object)

    # Turn off unnecessary switches
    turn_off_unnecessary_switches(home)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `get_all_actuators`, `get_all_sensors`, `get_room_actuators`, `get_room_sensors`: Functions to retrieve actuators and sensors from the home plan.
#    - `TEMP_LOW`, `TEMP_HIGH`, `HUMIDITY_LOW`, `HUMIDITY_HIGH`, `LIGHT_INTENSITY_LOW`, `LIGHT_INTENSITY_HIGH`: Thresholds for temperature, humidity, and light intensity.
#    - `logger`: Logger for logging information and warnings.

# 2. **`turn_off_unnecessary_switches(home)` function:**
#    - Iterates through all `Light` actuators and `LightIntensive` sensors.
#    - If the sensor reading is above `LIGHT_INTENSITY_HIGH`, the corresponding light is turned off.
#    - Iterates through all `Heater` actuators and `IndoorTemperature` sensors.
#    - If the sensor reading is above `TEMP_HIGH`, the corresponding heater is turned off.
#    - Iterates through all `AC` actuators and `IndoorTemperature` sensors.
#    - If the sensor reading is below `TEMP_LOW`, the corresponding AC is turned off.
#    - Iterates through all `Humidifier` actuators and `Humidity` sensors.
#    - If the sensor reading is above `HUMIDITY_HIGH`, the corresponding humidifier is turned off.

# 3. **`main()` function:**
#    - Creates the smart home object (you'll need to replace this with your home plan setup).
#    - ... (Code to read sensor data and populate the home object).
#    - Calls `turn_off_unnecessary_switches(home)` to turn off unnecessary switches.

# 4. **`if __name__ == "__main__":` block:**
#    - Executes the `main()` function when the script is run directly.

# **To use this function:**

# 1. **Replace the placeholder in the `main()` function with your code to read sensor data and populate the home object.**
# 2. **Create a `home_plan()` function in a separate file (`home_plan.py`) to define the structure of your smart home with rooms, sensors, and actuators.**
# 3. **Run the script (`function.py`) to execute the logic and turn off unnecessary switches based on sensor readings.**
