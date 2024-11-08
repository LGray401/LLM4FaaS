# Based on your functional description and the provided source code, I'll create a `function.py` file that implements energy-saving modes for your smart home project. The file will include a main function that will check the current temperature readings from the sensors and activate the appropriate actuators (window and curtain) based on the defined conditions.
# 
# Here’s how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, Curtain

def energy_saving_mode(home):
    for room in home:
        indoor_temp_sensor = None
        outdoor_temp_sensor = None
        window = None
        curtain = None
        
        # Retrieve sensors and actuators from the room
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
        
        # If both sensors are present in the room
        if indoor_temp_sensor and outdoor_temp_sensor:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()
            
            # Check the energy saving conditions
            if outdoor_temp is not None and indoor_temp is not None:
                # Condition 1: If outdoor temperature is lower than indoor temperature, open the window
                if outdoor_temp < indoor_temp:
                    window.turn_on()
                else:
                    window.turn_off()
                
                # Condition 2: If indoor temperature is lower than outdoor temperature and it’s sunny (light intensity high), close the curtains
                if indoor_temp < outdoor_temp:
                    curtain.turn_on()  # Assuming curtain can be turned on to close
                else:
                    curtain.turn_off()  # Assuming curtain can be turned off to open

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()