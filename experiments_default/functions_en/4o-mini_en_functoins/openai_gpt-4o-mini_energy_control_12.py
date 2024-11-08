# Based on the functional description and the provided code files, I will create a `function.py` file that will implement the energy-saving mode and automatically control the air conditioning based on outdoor temperature and humidity.
# 
# Here's what the `function.py` will look like:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.logger_config import logger

def check_energy_saving_mode():
    home = home_plan()

    # Assuming we are interested in the living room for the AC control
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    if living_room is None:
        logger.error("LivingRoom not found in home plan.")
        print("LivingRoom not found in home plan.")
        return

    # Get outdoor temperature and humidity sensors
    outdoor_temp_sensor = next((sensor for sensor in living_room.sensors if sensor.sensor_type == "OutdoorTemperature"), None)
    humidity_sensor = next((sensor for sensor in living_room.sensors if sensor.sensor_type == "Humidity"), None)

    # Get the AC actuator
    ac_actuator = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "AC"), None)

    if outdoor_temp_sensor is None or humidity_sensor is None or ac_actuator is None:
        logger.error("Required sensors or actuators not found in LivingRoom.")
        print("Required sensors or actuators not found in LivingRoom.")
        return

    # Read values from sensors
    outdoor_temp_sensor.turn_on()
    humidity_sensor.turn_on()

    outdoor_temp = outdoor_temp_sensor.get_reading()
    humidity = humidity_sensor.get_reading()

    outdoor_temp_sensor.turn_off()
    humidity_sensor.turn_off()

    # Validate readings
    if outdoor_temp is None or humidity is None:
        logger.error("Failed to get readings from sensors.")
        print("Failed to get readings from sensors.")
        return

    # Determine if the AC should be turned on or off
    if outdoor_temp > TEMP_HIGH and humidity > HUMIDITY_HIGH:
        ac_actuator.turn_on()
        logger.info("AC turned ON due to high outdoor temperature and humidity.")
    else:
        ac_actuator.turn_off()
        logger.info("AC turned OFF as conditions are not met.")

def main():
    print("Starting energy-saving mode...")
    check_energy_saving_mode()

if __name__ == "__main__":
    main()