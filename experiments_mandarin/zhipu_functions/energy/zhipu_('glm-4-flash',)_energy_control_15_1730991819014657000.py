# # function.py

import os
from home.sensor import Sensor
from home.actuator import Actuator
from home.home_plan import home_plan
from home.logger_config import logger

# Create 'functions' directory if it does not exist
if not os.path.exists('functions'):
    os.makedirs('functions')

# Main function
def main():
    # Load the home plan
    home = home_plan()

    # Example usage
    # Access a specific room's sensors
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    print("Living Room Sensors:")
    for sensor in living_room_sensors:
        print(sensor.id)

    # Access a specific room's actuators
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    print("Bedroom Actuators:")
    for actuator in bedroom_actuators:
        print(actuator.id)

    # Perform actions on sensors and actuators
    # For example, turn on a light in the Living Room
    if living_room_sensors:
        light = next((actuator for actuator in living_room_sensors if isinstance(actuator, Actuator) and
                       actuator.actuator_type == "Light"), None)
        if light:
            light.turn_on()

    # For example, get the reading from a temperature sensor in the Living Room
    if living_room_sensors:
        temperature_sensor = next((sensor for sensor in living_room_sensors if isinstance(sensor, Sensor) and
                                   sensor.sensor_type == "IndoorTemperature"), None)
        if temperature_sensor:
            reading = temperature_sensor.get_reading()
            print(f"Indoor Temperature Reading: {reading}")

if __name__ == "__main__":
    main()