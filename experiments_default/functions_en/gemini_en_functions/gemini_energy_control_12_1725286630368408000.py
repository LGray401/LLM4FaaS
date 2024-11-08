from home.home_plan import get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Heater
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.logger_config import logger

def energy_saving_mode(home):
    """
    Start the energy-saving mode and automatically choose whether to enable the air conditioner according to the outdoor temperature and humidity
    :param home: home object
    :return: None
    """
    logger.info("Starting energy-saving mode...")

    # Get outdoor temperature and humidity sensors
    outdoor_temp_sensor = get_all_sensors(home, "OutdoorTemperature")[0]
    outdoor_humidity_sensor = get_all_sensors(home, "Humidity")[0]

    # Get all air conditioners and heaters
    all_ac = get_all_actuators(home, "AC")
    all_heaters = get_all_actuators(home, "Heater")

    # Get outdoor temperature and humidity readings
    outdoor_temp = outdoor_temp_sensor.get_reading()
    outdoor_humidity = outdoor_humidity_sensor.get_reading()

    # Turn off all heaters
    for heater in all_heaters:
        heater.turn_off()

    # Control air conditioners based on temperature and humidity
    for ac in all_ac:
        if outdoor_temp > TEMP_HIGH or outdoor_humidity > HUMIDITY_HIGH:
            # Turn on air conditioner if outdoor temperature is high or humidity is high
            logger.info(f"Turning on AC in {ac.room_name}")
            ac.turn_on()
        else:
            # Turn off air conditioner if outdoor temperature is low and humidity is low
            logger.info(f"Turning off AC in {ac.room_name}")
            ac.turn_off()

    logger.info("Energy-saving mode active.")


if __name__ == "__main__":
    # Example usage
    home = home_plan()
    energy_saving_mode(home)

# **Explanation:**

# 1. **Import necessary modules:** Import modules for home plan, sensors, actuators, and configuration settings.
# 2. **`energy_saving_mode(home)` function:**
#    - Takes the `home` object as input.
#    - Logs a message to indicate the start of the energy-saving mode.
#    - Retrieves the outdoor temperature and humidity sensors from the `home` object.
#    - Retrieves all air conditioners and heaters from the `home` object.
#    - Gets the readings from the outdoor temperature and humidity sensors.
#    - Turns off all heaters.
#    - Iterates through all air conditioners:
#      - If the outdoor temperature is above the `TEMP_HIGH` threshold or the outdoor humidity is above the `HUMIDITY_HIGH` threshold, turn on the air conditioner.
#      - Otherwise, turn off the air conditioner.
#    - Logs a message to confirm the energy-saving mode is active.
# 3. **`if __name__ == "__main__":` block:**
#    - Creates a home plan using `home_plan()`.
#    - Calls the `energy_saving_mode()` function to activate the energy-saving mode.

# **To use this function:**

# 1. **Place the `function.py` file in the `functions` folder.**
# 2. **Call the `energy_saving_mode()` function from your main script or another function, passing the `home` object as an argument.**

# **Example:**

from home.home_plan import home_plan
from functions.function import energy_saving_mode

# ... other code ...

home = home_plan()
energy_saving_mode(home)
