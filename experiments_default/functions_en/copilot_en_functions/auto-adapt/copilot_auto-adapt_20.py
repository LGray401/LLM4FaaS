# Based on the content of the markdown file, you are working on a smart home project and you need a `function.py` file. This file should contain the main function and be located in the 'functions' folder.
#
# The main function should control the following functionalities based on the sensor readings:
#
# 1. The air conditioner should automatically turn on when the room temperature exceeds 26°C.
# 2. The system should automatically adjust indoor humidity.
# 3. The system should automatically adjust light intensity.
#
# The `function.py` file should interact with the four existing Python files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) in your project.
#
# Here is a basic structure of the `function.py` file:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Light
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH

def main():
    # Get the home plan
    home = home_plan()

    # Iterate over each room
    for room in home:
        # Get the sensors and actuators in the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Iterate over each sensor in the room
        for sensor in sensors:
            # Check if the sensor is an IndoorTemperatureSensor
            if isinstance(sensor, IndoorTemperatureSensor):
                # Get the reading from the sensor
                temperature = sensor.get_reading()
                # If the temperature is above the threshold, turn on the AC
                if temperature > TEMP_HIGH:
                    # Find the AC in the room's actuators
                    for actuator in actuators:
                        if isinstance(actuator, AC):
                            actuator.turn_on()

            # Add similar control logic for HumiditySensor and LightIntensiveSensor

if __name__ == "__main__":
    main()
# ```
#
# This script will iterate over each room in the home, check the readings from the sensors, and control the actuators based on these readings. You will need to add similar control logic for the `HumiditySensor` and `LightIntensiveSensor`.