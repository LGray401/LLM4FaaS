# Based on the given functional description and the source code provided, I will create a `function.py` file that will contain a `main` function for your smart home project. The `main` function will simulate the environment by turning on sensors and actuators, and will also handle the logging of sensor readings and actuator status changes.
# 
# Here is the `function.py` file:

# function.py

from home.sensor import Sensor, IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, \
    LightIntensiveSensor, SmokeSensor
from home.actuator import Actuator, Heater, AC, CoffeeMachine, Light, Window, Curtain, MusicPlayer, \
    SmartSocket, Door, CleaningRobot, SmartTV, Humidifier
from home.logger_config import logger
from home_plan import home

# Initialize all sensors and actuators
def initialize_components():
    # Initialize all sensors
    sensors = []
    for room in home:
        sensors.extend(room.sensors)

    # Initialize all actuators
    actuators = []
    for room in home:
        actuators.extend(room.actuators)

    return sensors, actuators

# Main function
def main():
    logger.info("Starting Smart Home System...")
    
    # Initialize components
    sensors, actuators = initialize_components()

    # Turn on all sensors
    for sensor in sensors:
        sensor.turn_on()

    # Simulate sensor readings
    for sensor in sensors:
        sensor.get_reading()

    # Turn on all actuators
    for actuator in actuators:
        actuator.turn_on()

    # Simulate actuator operations
    for actuator in actuators:
        if isinstance(actuator, Heater):
            actuator.adjust_temperature(20)
        elif isinstance(actuator, AC):
            actuator.adjust_temperature(26)
        elif isinstance(actuator, Light):
            actuator.set_brightness_level("medium")
        elif isinstance(actuator, CleaningRobot):
            actuator.daily_routine()
        elif isinstance(actuator, Humidifier):
            actuator.increase_humidity()

    # Turn off all sensors
    for sensor in sensors:
        sensor.turn_off()

    # Turn off all actuators
    for actuator in actuators:
        actuator.turn_off()

    logger.info("Smart Home System is shutting down...")

if __name__ == "__main__":
    main()