# Based on the functional description and the provided source code files, here’s how you can implement the `function.py` file to manage the energy-saving modes for your smart home project.
# 
# The `function.py` file will contain a main function that checks the temperature readings from the indoor and outdoor sensors and controls the actuators (windows and curtains) based on the specified conditions.
# 
# Here is the `function.py` file:

# function.py

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan
from home.logger_config import logger

def energy_saving_mode(home):
    for room in home:
        indoor_temp_sensor = None
        outdoor_temp_sensor = None
        window = None
        curtain = None

        # Identify the sensors and actuators in the room
        for sensor in room.sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temp_sensor = sensor
            elif isinstance(sensor, OutdoorTemperatureSensor):
                outdoor_temp_sensor = sensor

        for actuator in room.actuators:
            if isinstance(actuator, Window):
                window = actuator
            elif isinstance(actuator, Curtain):
                curtain = actuator

        # Proceed only if we have the required sensors and actuators
        if indoor_temp_sensor and outdoor_temp_sensor and window and curtain:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            if indoor_temp is not None and outdoor_temp is not None:
                # Energy-saving mode conditions
                if outdoor_temp < indoor_temp:
                    window.turn_on()  # Open window to cool down
                    logger.info(f"Opened window in {room.name} to cool down as outdoor temp ({outdoor_temp}) < indoor temp ({indoor_temp}).")
                if indoor_temp < outdoor_temp:
                    curtain.turn_on()  # Close curtain to block sunlight
                    logger.info(f"Closed curtain in {room.name} to block sunlight as indoor temp ({indoor_temp}) < outdoor temp ({outdoor_temp}).")

def main():
    # Create home plan
    home = home_plan()
    
    # Activate energy-saving mode
    energy_saving_mode(home)

if __name__ == "__main__":
    main()