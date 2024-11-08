# Given the functional descriptions and the provided code, we'll create a `function.py` file located in the `functions` folder. This file will contain the main function to control the smart home based on the temperature, humidity, and light intensity conditions you specified.
# 
# Here's the `function.py` file:
# 
# ### function.py

import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Get relevant sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    ac_actuators = get_all_actuators(home, "AC")
    humidifier_actuators = get_all_actuators(home, "Humidifier")
    curtain_actuators = get_all_actuators(home, "Curtain")
    
    # Turn on all sensors to get readings
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()
    
    # Monitor and control the environment
    while True:
        for sensor in temperature_sensors:
            reading = sensor.get_reading()
            if reading is not None and reading >= TEMP_HIGH:
                for ac in ac_actuators:
                    if ac.room_name == sensor.room_name:
                        ac.turn_on()
                        print(f"Temperature in {sensor.room_name} is {reading}°C. Turning on AC.")
        
        for sensor in humidity_sensors:
            reading = sensor.get_reading()
            if reading is not None and reading < HUMIDITY_LOW:
                for humidifier in humidifier_actuators:
                    if humidifier.room_name == sensor.room_name:
                        humidifier.turn_on()
                        print(f"Humidity in {sensor.room_name} is {reading}%. Turning on Humidifier.")
        
        for sensor in light_sensors:
            reading = sensor.get_reading()
            if reading is not None and reading > LIGHT_INTENSITY_HIGH:
                for curtain in curtain_actuators:
                    if curtain.room_name == sensor.room_name:
                        curtain.turn_on()
                        print(f"Light intensity in {sensor.room_name} is {reading}. Closing curtain.")
        
        time.sleep(1)  # Delay to simulate continuous monitoring

if __name__ == "__main__":
    main()