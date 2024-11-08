# Based on the provided functional description and the source code, we can create `function.py` to implement the energy-saving mode which autonomously decides whether to enable the air conditioner based on outdoor temperature and humidity.
# 
# Here's the content for `functions/function.py`:

from home.sensor import OutdoorTemperatureSensor, HumiditySensor
from home.actuator import AC
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW
from home.logger_config import logger

def start_energy_saving_mode(home):
    # Get all outdoor temperature sensors and humidity sensors
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Get the first outdoor temperature sensor and humidity sensor (assuming there's at least one)
    if not outdoor_temp_sensors or not humidity_sensors:
        print("No outdoor temperature or humidity sensors found.")
        logger.error("No outdoor temperature or humidity sensors found.")
        return

    outdoor_temp_sensor = outdoor_temp_sensors[0]
    humidity_sensor = humidity_sensors[0]

    outdoor_temp_sensor.turn_on()
    humidity_sensor.turn_on()

    # Get readings
    outdoor_temp = outdoor_temp_sensor.get_reading()
    humidity = humidity_sensor.get_reading()

    # Decision making based on temperature and humidity
    if outdoor_temp is None or humidity is None:
        print("Failed to get sensor readings.")
        logger.error("Failed to get sensor readings.")
        return

    ac_units = get_all_actuators(home, "AC")

    if outdoor_temp > TEMP_HIGH or humidity > HUMIDITY_HIGH:
        # Turn on all AC units if conditions meet
        for ac in ac_units:
            ac.turn_on()
            ac.set_target_temperature(TEMP_LOW)
    else:
        # Turn off all AC units if conditions do not meet
        for ac in ac_units:
            ac.turn_off()

    outdoor_temp_sensor.turn_off()
    humidity_sensor.turn_off()


if __name__ == "__main__":
    home = home_plan()
    start_energy_saving_mode(home)