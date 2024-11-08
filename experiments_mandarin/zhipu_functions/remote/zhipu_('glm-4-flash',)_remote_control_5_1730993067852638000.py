# Based on your description and provided code snippets, I will create a `function.py` file that contains a `main` function that demonstrates the basic operation of your smart home system. This will include creating a home plan, interacting with sensors and actuators, and logging actions.
# 
# Here's what the `function.py` file might look like:

# function.py

import logging
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Heater, AC
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():
    # Create home plan
    home = home_plan()

    # Get all indoor and outdoor temperature sensors
    indoor_temp_sensors = [sensor for sensor in get_all_sensors(home, "IndoorTemperature")]
    outdoor_temp_sensors = [sensor for sensor in get_all_sensors(home, "OutdoorTemperature")]

    # Set target temperature for the heater and AC
    for room in home:
        if "Heater" in [actor.actuator_type for actor in room.actuators]:
            heater = next((actor for actor in room.actuators if actor.actuator_type == "Heater"), None)
            if heater:
                heater.set_target_temperature(TEMP_LOW)
        if "AC" in [actor.actuator_type for actor in room.actuators]:
            ac = next((actor for actor in room.actuators if actor.actuator_type == "AC"), None)
            if ac:
                ac.set_target_temperature(TEMP_HIGH)

    # Simulate temperature changes and control the heater/AC
    for _ in range(5):  # Simulate 5 minutes
        for sensor in indoor_temp_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            logger.info(f"Indoor temperature reading: {reading}")

            # Check if we need to adjust the heater or AC based on the temperature reading
            for room in home:
                if "Heater" in [actor.actuator_type for actor in room.actuators]:
                    heater = next((actor for actor in room.actuators if actor.actuator_type == "Heater"), None)
                    if heater:
                        heater.adjust_temperature(reading)

                if "AC" in [actor.actuator_type for actor in room.actuators]:
                    ac = next((actor for actor in room.actuators if actor.actuator_type == "AC"), None)
                    if ac:
                        ac.adjust_temperature(reading)

        for sensor in outdoor_temp_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            logger.info(f"Outdoor temperature reading: {reading}")

        time.sleep(60)  # Wait for a minute before the next reading

if __name__ == "__main__":
    main()