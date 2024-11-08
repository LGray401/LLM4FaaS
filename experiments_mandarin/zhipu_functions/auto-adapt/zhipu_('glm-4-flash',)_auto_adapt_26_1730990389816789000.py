# Based on your functional description and provided source code, I'll create a `function.py` file that will serve as the main function controlling your smart home system. This script will use the existing sensors and actuators to maintain the desired temperature and humidity, and adjust the lighting based on the activity level.
# 
# Here's the `function.py` file:

# function.py
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, Humidifier
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create sensors and actuators
    indoor_temp_sensor = IndoorTemperatureSensor("LivingRoom")
    humidity_sensor = HumiditySensor("LivingRoom")
    light_intensity_sensor = LightIntensiveSensor("LivingRoom")
    
    heater = Heater("LivingRoom")
    ac = AC("LivingRoom")
    light = Light("LivingRoom")
    humidifier = Humidifier("LivingRoom")

    # Set target temperatures and humidity
    target_temp = 26
    target_humidity = 60

    while True:
        # Read current conditions
        current_temp = indoor_temp_sensor.get_reading()
        current_humidity = humidity_sensor.get_reading()
        current_light_intensity = light_intensity_sensor.get_reading()

        # Adjust temperature
        if current_temp < TEMP_LOW:
            heater.adjust_temperature(current_temp)
        elif current_temp > TEMP_HIGH:
            ac.adjust_temperature(current_temp)

        # Adjust humidity
        if current_humidity < HUMIDITY_LOW:
            humidifier.increase_humidity()
        elif current_humidity > HUMIDITY_HIGH:
            humidifier.decrease_humidity()

        # Adjust lighting based on activity level
        # (Assuming activity level is determined by the light intensity sensor)
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            light.set_brightness_level("high")
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            light.set_brightness_level("low")
        else:
            light.set_brightness_level("medium")

        # Wait for the next cycle
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()