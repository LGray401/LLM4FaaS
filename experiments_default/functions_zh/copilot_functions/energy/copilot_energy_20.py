# Based on the provided functional description and source code, you want to create a `function.py` file that automatically adjusts the indoor temperature, humidity, and light intensity. Here's a plan:
#
# 1. Import necessary modules and classes from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 2. Define a `main` function in `function.py`.
# 3. Inside the `main` function, create a home plan using the `home_plan` function from `home_plan.py`.
# 4. Iterate over each room in the home plan.
# 5. For each room, get the sensors and actuators.
# 6. Check the readings from the temperature, humidity, and light intensity sensors.
# 7. Based on the sensor readings, control the actuators to adjust the indoor temperature, humidity, and light intensity.
#
# Here's the Python code for `function.py`:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        for sensor in sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                temperature = sensor.get_reading()
                for actuator in actuators:
                    if isinstance(actuator, Heater):
                        if temperature < TEMP_LOW:
                            actuator.turn_on()
                        else:
                            actuator.turn_off()
                    elif isinstance(actuator, AC):
                        if temperature > TEMP_HIGH:
                            actuator.turn_on()
                        else:
                            actuator.turn_off()

            elif isinstance(sensor, HumiditySensor):
                humidity = sensor.get_reading()
                for actuator in actuators:
                    if isinstance(actuator, AC):
                        if humidity > HUMIDITY_HIGH:
                            actuator.turn_on()
                        else:
                            actuator.turn_off()

            elif isinstance(sensor, LightIntensiveSensor):
                light_intensity = sensor.get_reading()
                for actuator in actuators:
                    if isinstance(actuator, Light):
                        if light_intensity < LIGHT_INTENSITY_LOW:
                            actuator.turn_on()
                        else:
                            actuator.turn_off()

if __name__ == "__main__":
    main()
# ```
#
# This script will automatically adjust the indoor temperature, humidity, and light intensity based on the sensor readings. The `main` function should be placed in the `function.py` file in the 'functions' folder as per your project structure.