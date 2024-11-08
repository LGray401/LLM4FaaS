# Based on your functional description and the provided source code, I will create the `function.py` file that implements the desired functionality for your smart home project. This implementation will check the status of the air conditioning units and control the windows based on the specified conditions.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window
from home.logger_config import logger
import time

def control_windows_based_on_ac_and_temperature(home):
    for room in home:
        # Check for AC and Windows in the room
        acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        
        # If there's an AC in the room
        for ac in acs:
            if ac.get_status() == "on":
                # Close windows if AC is on
                for window in windows:
                    window.turn_off()
                    logger.info(f"Closed window in {room.name} because AC is ON.")
        
        # Get indoor and outdoor temperature readings
        indoor_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((sensor for sensor in home[1:] for sensor in sensor.sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)  # Assuming outdoor sensor is in a different room
        print(outdoor_temp_sensor.id)
        if indoor_temp_sensor and outdoor_temp_sensor:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()
            
            if indoor_temp is not None and outdoor_temp is not None:
                if indoor_temp > 26 and outdoor_temp < 26:
                    # Open windows if indoor temperature is high and outdoor temperature is low
                    for window in windows:
                        window.turn_on()
                        logger.info(f"Opened window in {room.name} because indoor temperature is above 26°C and outdoor temperature is below 26°C.")

def main():
    home = home_plan()  # Create the home plan
    while True:
        control_windows_based_on_ac_and_temperature(home)
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()