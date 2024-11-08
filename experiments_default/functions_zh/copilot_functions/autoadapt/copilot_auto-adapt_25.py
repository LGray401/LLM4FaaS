# Based on the content of the markdown file, you are working on a smart home project and you need a new Python file named `function.py` that should be located in the 'functions' folder. This file should contain a main function that controls the behavior of your smart home based on the following rules:
#
# 1. When the indoor temperature reaches 26℃, the air conditioner should be turned on to cool down the room.
# 2. When the indoor humidity is below 36, the air conditioner should be turned on to increase the humidity.
# 3. When the indoor light intensity is above 80, the curtains should be pulled up.
#
# The `function.py` file should interact with the existing Python files in your project: `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`, which are located in the 'home' folder.
#
# Here is a pseudocode of what the `function.py` file could look like:
#
# 1. Import necessary modules and classes from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 2. Define a function named `main` that:
# - Creates an instance of the home plan.
# - Iterates over each room in the home plan.
# - For each room, it checks the current readings from the sensors.
# - Based on the sensor readings, it controls the actuators according to the rules described in the markdown file.
#
# Here is the Python code for `function.py`:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def main():
    home = home_plan()

    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        for sensor in sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
                if ac and sensor.get_reading() > 26:
                    ac.turn_on()
            elif isinstance(sensor, HumiditySensor):
                ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
                if ac and sensor.get_reading() < 36:
                    ac.turn_on()
            elif isinstance(sensor, LightIntensiveSensor):
                curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)
                if curtain and sensor.get_reading() > 80:
                    curtain.turn_on()

if __name__ == "__main__":
    main()
# ```
#
# This code will create a home plan, iterate over each room, and control the actuators based on the sensor readings. The `main` function is the entry point of the program.