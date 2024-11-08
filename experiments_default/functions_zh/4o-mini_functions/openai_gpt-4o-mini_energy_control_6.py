# Based on your functional description of enabling energy-saving mode in your smart home project, we will implement a `function.py` file in the `functions` folder. This file will contain a main function that initializes the smart home environment and activates the energy-saving mode.
# 
# The energy-saving mode could involve turning off unnecessary lights and adjusting the temperature settings of HVAC systems based on sensor readings. Below is a proposed implementation for the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
from home.sensor import IndoorTemperatureSensor
from home.actuator import Light, Heater, AC
from home.logger_config import logger

def enable_energy_saving_mode(home):
    logger.info("Enabling energy-saving mode...")
    print("Enabling energy-saving mode...")
    
    for room in home:
        # Get all sensors and actuators in the room
        temperature_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        heaters = [actuator for actuator in room.actuators if isinstance(actuator, Heater)]
        acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]

        # Turn off unnecessary lights
        for light in lights:
            light.turn_off()

        # Check temperature sensors and adjust HVAC
        for sensor in temperature_sensors:
            sensor.turn_on()  # Ensure sensor is on to get reading
            current_temperature = sensor.get_reading()
            if current_temperature is not None:
                if current_temperature < TEMP_LOW and heaters:
                    # Turn on heaters if temperature is below the low threshold
                    for heater in heaters:
                        heater.set_target_temperature(TEMP_HIGH)  # Set target temperature for heater
                        heater.turn_on()
                elif current_temperature > TEMP_HIGH and acs:
                    # Turn on AC if temperature is above the high threshold
                    for ac in acs:
                        ac.set_target_temperature(TEMP_LOW)  # Set target temperature for AC
                        ac.turn_on()

def main():
    home = home_plan()  # Create the home plan
    enable_energy_saving_mode(home)  # Activate energy-saving mode

if __name__ == "__main__":
    main()