# Based on the given functional description and the code files provided, I'll create the `function.py` file with a main function that uses the classes and methods from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`. The main function will simulate the conditions described in the functional description.
# 
# Here is the `function.py` file:

import sys
import os

# Add the 'home' directory to the system path for imports
home_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'home'))
sys.path.append(home_dir)

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def main():
    # Initialize the home plan
    home = home_plan()

    # Simulate the functional description
    room_name = "LivingRoom"

    # Get sensors for the room
    sensors = get_room_sensors(home, room_name)

    # Turn on all sensors in the room
    for sensor in sensors:
        sensor.turn_on()

    # Get readings from sensors
    temperature_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    humidity_sensor = next((sensor for sensor in sensors if isinstance(sensor, HumiditySensor)), None)
    light_sensor = next((sensor for sensor in sensors if isinstance(sensor, LightIntensiveSensor)), None)

    # Simulate readings based on the functional description
    if temperature_sensor:
        temperature_reading = 22  # as described
        print(f"Temperature: {temperature_reading}°C")

    if humidity_sensor:
        humidity_reading = "湿度适中"  # as described
        print(f"Humidity: {humidity_reading}")

    if light_sensor:
        light_reading = "微弱"  # as described
        print(f"Light Intensity: {light_reading}")

    # Get actuators for the room
    actuators = get_room_actuators(home, room_name)

    # Turn on the light in the room and set brightness
    light_actuator = next((actuator for actuator in actuators if isinstance(actuator, Light)), None)
    if light_actuator:
        light_actuator.turn_on()
        light_actuator.set_brightness_level("low")

    # Assuming we have AC and Heater in the room, we can adjust the temperature if needed
    ac_actuator = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
    heater_actuator = next((actuator for actuator in actuators if isinstance(actuator, Heater)), None)
    if ac_actuator:
        ac_actuator.set_target_temperature(temperature_reading)
        ac_actuator.adjust_temperature(temperature_reading)
    if heater_actuator:
        heater_actuator.set_target_temperature(temperature_reading)
        heater_actuator.adjust_temperature(temperature_reading)

if __name__ == "__main__":
    main()