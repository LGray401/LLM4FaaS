# Sure, I have created the 'function.py' file for you. You can find the file in the 'functions' folder.
# 
# # function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light

def main():
    # Create sensor objects
    indoor_temp_sensor = IndoorTemperatureSensor("LivingRoom")
    humidity_sensor = HumiditySensor("LivingRoom")
    light_intensity_sensor = LightIntensiveSensor("LivingRoom")

    # Get sensor readings
    indoor_temp = indoor_temp_sensor.get_reading()
    humidity = humidity_sensor.get_reading()
    light_intensity = light_intensity_sensor.get_reading()

    # Determine if the light needs to be turned on or off
    if indoor_temp > 25 and humidity < 40 and light_intensity < 500:
        light = Light("LivingRoom")
        light.turn_on()
    else:
        light = Light("LivingRoom")
        light.turn_off()

if __name__ == "__main__":
    main()