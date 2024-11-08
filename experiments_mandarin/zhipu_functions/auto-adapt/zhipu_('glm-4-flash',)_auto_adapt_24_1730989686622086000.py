# Based on the functional description and the provided source code, I will create a `function.py` file for your smart home project. This file will contain the `main` function which will orchestrate the smart home system based on the temperature, humidity, and light intensity thresholds.

# function.py
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW

def main():
    # Create sensors and actuators
    indoor_temp_sensor = IndoorTemperatureSensor("LivingRoom")
    humidity_sensor = HumiditySensor("LivingRoom")
    light_intensity_sensor = LightIntensiveSensor("LivingRoom")
    
    heater = Heater("LivingRoom")
    ac = AC("LivingRoom")
    light = Light("LivingRoom")
    
    # Initial readings
    indoor_temp = indoor_temp_sensor.get_reading()
    humidity = humidity_sensor.get_reading()
    light_intensity = light_intensity_sensor.get_reading()
    
    # Loop to check and control home environment
    while True:
        # Check temperature
        if indoor_temp > TEMP_HIGH:
            ac.adjust_temperature(indoor_temp)
        else:
            heater.adjust_temperature(indoor_temp)
        
        # Check humidity
        if humidity > HUMIDITY_HIGH:
            # Add a humidifier here if you have one
            pass
        
        # Check light intensity
        if light_intensity < LIGHT_INTENSITY_LOW:
            light.turn_on()
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            light.turn_off()
        
        # Update readings
        indoor_temp = indoor_temp_sensor.get_reading()
        humidity = humidity_sensor.get_reading()
        light_intensity = light_intensity_sensor.get_reading()
        
        # Wait before next check
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()