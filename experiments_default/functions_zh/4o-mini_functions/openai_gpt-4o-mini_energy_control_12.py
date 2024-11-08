# Based on your functional description and the source code provided, I will create a `function.py` file that implements the energy-saving mode functionality. This will involve reading the outdoor temperature and humidity using the appropriate sensors, and then deciding whether to activate the air conditioning (AC) based on the readings.
# 
# Here's the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.sensor import OutdoorTemperatureSensor, HumiditySensor
from home.actuator import AC
from home.logger_config import logger

def activate_energy_saving_mode(home):
    for room in home:
        outdoor_temp_sensor = None
        humidity_sensor = None
        ac = None
        
        # Retrieve outdoor temperature and humidity sensors and AC actuator
        for sensor in room.sensors:
            if isinstance(sensor, OutdoorTemperatureSensor):
                outdoor_temp_sensor = sensor
            elif isinstance(sensor, HumiditySensor):
                humidity_sensor = sensor
        
        for actuator in room.actuators:
            if isinstance(actuator, AC):
                ac = actuator
                
        # If sensors and AC actuator are found, evaluate conditions
        if outdoor_temp_sensor and humidity_sensor and ac:
            outdoor_temp_sensor.turn_on()
            humidity_sensor.turn_on()
            
            outdoor_temp = outdoor_temp_sensor.get_reading()
            humidity = humidity_sensor.get_reading()
            
            if outdoor_temp is not None and humidity is not None:
                logger.info(f"Outdoor Temperature: {outdoor_temp}°C, Humidity: {humidity}%")
                
                # Check conditions for activating AC
                if outdoor_temp > TEMP_HIGH or humidity > HUMIDITY_HIGH:
                    ac.set_target_temperature(TEMP_HIGH)  # Set target temperature for AC
                    ac.adjust_temperature(outdoor_temp)  # Adjust AC based on current temperature
                else:
                    ac.turn_off()  # Turn off AC if conditions are not met
                    
            outdoor_temp_sensor.turn_off()
            humidity_sensor.turn_off()

def main():
    home = home_plan()  # Create home plan
    activate_energy_saving_mode(home)  # Activate energy-saving mode

if __name__ == "__main__":
    main()