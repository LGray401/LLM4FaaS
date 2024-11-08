# Given your functional description of "节约能源" (savings energy) and the provided source code, I will create a `function.py` file in the `functions` folder that contains a `main` function that could be used to implement energy-saving strategies in your smart home system.
# 
# Here's a sample `function.py` that could be a starting point:

# functions/function.py
import logging
from home.sensor import get_all_sensors
from home.actuator import get_all_actuators
from home_plan import home_plan
from config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():
    # Get all sensors and actuators
    all_sensors = get_all_sensors(home_plan(), "IndoorTemperature")
    all_actuators = get_all_actuators(home_plan(), "Heater")

    # Example of energy-saving strategy: Turn off heaters when the temperature is above a certain threshold
    for sensor in all_sensors:
        if sensor.get_reading() > TEMP_HIGH:
            # Turn off all heaters
            for actuator in all_actuators:
                actuator.turn_off()
                logger.info(f"Energy-saving mode: Heater turned off in room {actuator.room_name}")

    # Example of energy-saving strategy: Turn off lights when the light intensity is above a certain threshold
    light_sensors = get_all_sensors(home_plan(), "LightIntensive")
    for sensor in light_sensors:
        if sensor.get_reading() > LIGHT_INTENSITY_HIGH:
            # Turn off all lights
            for actuator in all_actuators:
                if actuator.actuator_type == "Light":
                    actuator.turn_off()
                    logger.info(f"Energy-saving mode: Light turned off in room {actuator.room_name}")

    # Example of energy-saving strategy: Turn off humidifiers when the humidity is above a certain threshold
    humidifier_sensors = get_all_sensors(home_plan(), "Humidity")
    for sensor in humidifier_sensors:
        if sensor.get_reading() > HUMIDITY_HIGH:
            # Turn off all humidifiers
            for actuator in all_actuators:
                if actuator.actuator_type == "Humidifier":
                    actuator.turn_off()
                    logger.info(f"Energy-saving mode: Humidifier turned off in room {actuator.room_name}")

if __name__ == "__main__":
    main()