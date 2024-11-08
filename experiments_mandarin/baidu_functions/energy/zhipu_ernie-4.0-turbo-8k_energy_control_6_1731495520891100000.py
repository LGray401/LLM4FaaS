# Based on your functional description and the provided source code, I will create a `function.py` file that contains a main function to start the energy-saving mode. The energy-saving mode will involve turning off lights and adjusting temperature settings based on predefined thresholds.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def start_energy_saving_mode(home):
    """
    Start energy-saving mode by adjusting settings based on predefined thresholds.
    """
    # Get all sensors and actuators
    lights = get_all_actuators(home, "Light")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")

    # Turn off all lights
    for light in lights:
        if light.status == "on":
            light.turn_off()
            logger.info(f"Energy-saving mode: Turned off {light.id}")

    # Adjust temperature settings
    for heater in heaters:
        if heater.status == "on" and (heater.target_temperature is None or heater.target_temperature > TEMP_HIGH):
            heater.set_target_temperature(TEMP_HIGH)
            logger.info(f"Energy-saving mode: Set heater {heater.id} target temperature to {TEMP_HIGH}°C")

    for ac in acs:
        if ac.status == "on" and (ac.target_temperature is None or ac.target_temperature < TEMP_LOW):
            ac.set_target_temperature(TEMP_LOW)
            logger.info(f"Energy-saving mode: Set AC {ac.id} target temperature to {TEMP_LOW}°C")

    # Monitor sensors for energy-saving opportunities
    for sensor in indoor_temp_sensors + humidity_sensors + light_intensive_sensors:
        if sensor.status == "off":
            sensor.turn_on()
            logger.info(f"Energy-saving mode: Turned on {sensor.id} to monitor conditions")

    # Example: Turn off heaters if humidity is too high (assuming high humidity means it's warm enough)
    for heater, humidity_sensor in zip(heaters, humidity_sensors):  # This assumes a 1-1 mapping, which might not be realistic
        if humidity_sensor.get_reading() > HUMIDITY_HIGH and heater.status == "on":
            heater.turn_off()
            logger.info(f"Energy-saving mode: Turned off heater {heater.id} due to high humidity")

    # Example: Turn on AC if light intensity is very high (assuming it's very sunny and warm)
    for ac, light_sensor in zip(acs, light_intensive_sensors):  # This assumes a 1-1 mapping, which might not be realistic
        if light_sensor.get_reading() > LIGHT_INTENSITY_HIGH and ac.status == "off":
            ac.turn_on()
            logger.info(f"Energy-saving mode: Turned on AC {ac.id} due to high light intensity")

    # Note: The above zip examples are simplistic and may not apply directly to your use case.
    # You might need a more sophisticated approach to determine which devices to adjust based on sensor readings.

if __name__ == "__main__":
    # Initialize home plan
    home = home_plan()

    # Start energy-saving mode
    start_energy_saving_mode(home)