# Sure, I will provide you with the 'function.py' file based on the given functional description and the provided source code files.
# 
# Here is the 'function.py' file:

import sys
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, \
    get_all_sensors, get_all_actuators
from home.logger_config import logger
from home.sensor import Sensor
from home.actuator import Actuator
  
def main():
    temperature = 24
    humidity = 30
    light_intensity = 45
    
    sensors = get_all_sensors(home_plan(), "IndoorTemperature") + get_all_sensors(home_plan(), "Humidity") + get_all_sensors(home_plan(), "LightIntensive")
    actuators = get_all_actuators(home_plan(), "Light") + get_all_actuators(home_plan(), "Heater") + get_all_actuators(home_plan(), "AC")
    
    for sensor in sensors:
        reading = sensor.get_reading()
        if sensor.sensor_type == "IndoorTemperature":
            temperature = reading
        elif sensor.sensor_type == "Humidity":
            humidity = reading
        elif sensor.sensor_type == "LightIntensive":
            light_intensity = reading
            
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            if light_intensity < 300:
                actuator.turn_on()
            elif light_intensity > 900:
                actuator.turn_off()
        elif actuator.actuator_type == "Heater":
            if temperature < 15:
                actuator.turn_on()
            elif temperature > 25:
                actuator.turn_off()
        elif actuator.actuator_type == "AC":
            if temperature > 25:
                actuator.turn_on()
            elif temperature < 15:
                actuator.turn_off()

if __name__ == "__main__":
    main()