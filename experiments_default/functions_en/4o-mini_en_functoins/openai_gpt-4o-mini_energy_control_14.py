# Based on the functional description and the provided source code files, I will create a `function.py` file that will include a main function to launch the Earth Environmental Protection Plan. This will involve initializing the home components and possibly conducting some basic operations as part of the plan.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_all_sensors, get_all_actuators
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH

def launch_environmental_protection_plan():
    logger.info("Launching Earth Environmental Protection Plan...")
    home = home_plan()

    print_home_plan(home)

    # Example actions for the environmental protection plan
    for room in home:
        # Get all sensors in the room
        sensors = get_all_sensors(home, room.name)

        # Get all actuators in the room
        actuators = get_all_actuators(home, room.name)
        
        # Check and log sensor readings
        for sensor in sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading is not None:
                if isinstance(sensor, (IndoorTemperatureSensor, OutdoorTemperatureSensor)):
                    if reading < TEMP_LOW:
                        logger.warning(f"Temperature in {room.name} is too low: {reading}°C")
                    elif reading > TEMP_HIGH:
                        logger.warning(f"Temperature in {room.name} is too high: {reading}°C")
                elif isinstance(sensor, HumiditySensor):
                    if reading < HUMIDITY_LOW:
                        logger.warning(f"Humidity in {room.name} is too low: {reading}%")
                    elif reading > HUMIDITY_HIGH:
                        logger.warning(f"Humidity in {room.name} is too high: {reading}%")
                # Add more conditions for other sensor types if needed

            sensor.turn_off()

    logger.info("Earth Environmental Protection Plan executed successfully.")

def main():
    launch_environmental_protection_plan()

if __name__ == "__main__":
    main()