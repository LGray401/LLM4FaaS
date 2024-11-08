# Given your functional description and the provided source code files, I'll create a `function.py` file in the `functions` folder that contains a main function to illustrate the temperature, humidity, and light intensity readings for the day. 
# 
# Here's the `function.py`:

# function.py
import sys
import os

# Adding the home directory to the path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'home'))

from sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def main():
    # Create instances of sensors
    temp_sensor = IndoorTemperatureSensor("LivingRoom")
    humidity_sensor = HumiditySensor("LivingRoom")
    light_sensor = LightIntensiveSensor("LivingRoom")
    
    # Turn on the sensors
    temp_sensor.turn_on()
    humidity_sensor.turn_on()
    light_sensor.turn_on()
    
    # Get readings
    temp_reading = temp_sensor.get_reading()
    humidity_reading = humidity_sensor.get_reading()
    light_reading = light_sensor.get_reading()
    
    # Print today's readings
    print(f"Temperature: Today {temp_reading} degrees")
    print(f"Humidity: Today's humidity: {humidity_reading}")
    print(f"Light Intensity: Today's light {light_reading}")

if __name__ == "__main__":
    main()