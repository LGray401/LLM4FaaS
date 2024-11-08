# Based on your functional description and the provided source code, here is the `function.py` file that you can use in your smart home project. This file contains the main function that checks the sensor readings and controls the actuators accordingly.

# function.py
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH

def check_and_adjust_environment(home):
    # Get all temperature sensors
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    # Get all ACs
    acs = get_all_actuators(home, "AC")
    
    # Check temperature sensors
    for sensor in temp_sensors:
        sensor.turn_on()  # Turn on the sensor to get the reading
        reading = sensor.get_reading()
        sensor.turn_off()  # Turn off the sensor after getting the reading
        
        if reading > TEMP_HIGH:
            for ac in acs:
                if ac.room_name == sensor.room_name and ac.status == "off":
                    ac.turn_on()  # Turn on the AC if temperature is high
    
    # Check humidity sensors
    for sensor in humidity_sensors:
        sensor.turn_on()  # Turn on the sensor to get the reading
        reading = sensor.get_reading()
        sensor.turn_off()  # Turn off the sensor after getting the reading
        
        if reading > HUMIDITY_HIGH:
            for ac in acs:
                if ac.room_name == sensor.room_name and ac.status == "off":
                    ac.turn_on()  # Turn on the AC if humidity is high
    
    # Check light sensors
    for sensor in light_sensors:
        sensor.turn_on()  # Turn on the sensor to get the reading
        reading = sensor.get_reading()
        sensor.turn_off()  # Turn off the sensor after getting the reading
        
        if reading > LIGHT_INTENSITY_HIGH:
            for ac in acs:
                if ac.room_name == sensor.room_name and ac.status == "off":
                    ac.turn_on()  # Turn on the AC if light intensity is high

def main():
    # Get the home plan
    home = home_plan()
    
    # Check and adjust the environment based on sensor readings
    check_and_adjust_environment(home)

if __name__ == "__main__":
    main()