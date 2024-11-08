# Based on the functional description and the provided source code, you need to create a `function.py` file that contains a main function. This function should start the energy-saving mode and automatically decide whether to enable the air conditioner based on the outdoor temperature and humidity.
#
# Here is a step-by-step plan:
#
# 1. Import necessary modules and classes from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 2. Define a function named `energy_saving_mode` that will be the main function in `function.py`.
# 3. In this function, create an instance of the home plan.
# 4. Get all outdoor temperature sensors and humidity sensors.
# 5. Get the readings from these sensors.
# 6. Based on the readings, decide whether to turn on the air conditioner. If the temperature is above a certain threshold (e.g., `TEMP_HIGH` from `config.py`) and the humidity is below a certain threshold (e.g., `HUMIDITY_HIGH`), turn on the air conditioner. Otherwise, turn it off.
# 7. Write this function in the `function.py` file.
#
# Here is the Python code for `function.py`:
#
# ```python
from home.sensor import OutdoorTemperatureSensor, HumiditySensor
from home.actuator import AC
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH

def energy_saving_mode():
    # Create an instance of the home plan
    home = home_plan()

    # Get all outdoor temperature sensors and humidity sensors
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Get the readings from these sensors
    outdoor_temp_readings = [sensor.get_reading() for sensor in outdoor_temp_sensors]
    humidity_readings = [sensor.get_reading() for sensor in humidity_sensors]

    # Get all air conditioners
    acs = get_all_actuators(home, "AC")

    # Based on the readings, decide whether to turn on the air conditioner
    for ac in acs:
        if any(temp > TEMP_HIGH for temp in outdoor_temp_readings) and any(humidity < HUMIDITY_HIGH for humidity in humidity_readings):
            ac.turn_on()
        else:
            ac.turn_off()

if __name__ == "__main__":
    energy_saving_mode()
# ```
#
# This code should be placed in the `function.py` file in the `functions` folder. The `energy_saving_mode` function will start the energy-saving mode and automatically decide whether to enable the air conditioner based on the outdoor temperature and humidity.