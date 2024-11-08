# Based on the functional description and the provided source codes, let's create a smart home application in Python. The application will read sensor data for temperature, humidity, and light intensity, and it will control actuators accordingly.
# 
# First, we'll create a new Python script called `smart_home.py`. This script will use the classes and functions provided in the reference files to simulate the smart home environment.
# 
# ### `smart_home.py`
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create the home plan
    home = home_plan()
    
    # Define a room to monitor or control, e.g., "LivingRoom"
    room_name = "LivingRoom"
    
    # Get sensors and actuators for the room
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)
    
    # Turn on all sensors in the room
    for sensor in sensors:
        sensor.turn_on()
    
    # Read sensor data
    for sensor in sensors:
        reading = sensor.get_reading()
        
        if isinstance(sensor, IndoorTemperatureSensor):
            # Control temperature using AC or Heater
            for actuator in actuators:
                if isinstance(actuator, Heater):
                    actuator.set_target_temperature(TEMP_HIGH)
                    actuator.adjust_temperature(reading)
                elif isinstance(actuator, AC):
                    actuator.set_target_temperature(TEMP_LOW)
                    actuator.adjust_temperature(reading)
                    
        elif isinstance(sensor, HumiditySensor):
            # Control humidity using Humidifier
            for actuator in actuators:
                if isinstance(actuator, Humidifier):
                    if reading < HUMIDITY_LOW:
                        actuator.turn_on()
                        actuator.increase_humidity()
                    elif reading > HUMIDITY_HIGH:
                        actuator.turn_on()
                        actuator.decrease_humidity()
                    else:
                        actuator.turn_off()
        
        elif isinstance(sensor, LightIntensiveSensor):
            # Control light intensity using Light
            for actuator in actuators:
                if isinstance(actuator, Light):
                    if reading < LIGHT_INTENSITY_LOW:
                        actuator.turn_on()
                        actuator.set_brightness_level("high")
                    elif reading > LIGHT_INTENSITY_HIGH:
                        actuator.turn_off()
                    else:
                        actuator.set_brightness_level("medium")
    
    # Turn off all sensors
    for sensor in sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# To run the application, save the above code in a file named `smart_home.py` in the same directory as your `home` folder. Open a terminal and navigate to the directory containing `smart_home.py` and the `home` folder. Then, execute the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This will simulate a smart home environment, where sensors read data and actuators adjust the environment based on predefined thresholds for temperature, humidity, and light intensity.