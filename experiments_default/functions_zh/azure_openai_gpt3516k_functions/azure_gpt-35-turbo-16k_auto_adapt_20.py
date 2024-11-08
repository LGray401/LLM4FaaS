# Sure, I will create the 'function.py' file for your smart home project based on the given functional description and the provided source code.
# 
# Here is the content of the 'function.py' file:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Light

def main():
    # Create sensors
    temperature_sensor = IndoorTemperatureSensor("LivingRoom")
    humidity_sensor = HumiditySensor("LivingRoom")
    light_sensor = LightIntensiveSensor("LivingRoom")

    # Create actuators
    ac = AC("LivingRoom")
    humidifier = Humidifier("LivingRoom")
    light = Light("LivingRoom")

    # Get sensor readings
    temperature = temperature_sensor.get_reading()
    humidity = humidity_sensor.get_reading()
    light_intensity = light_sensor.get_reading()

    # Perform actions based on sensor readings
    if temperature > 26:
        ac.turn_on()
    else:
        ac.turn_off()

    if humidity < 30:
        humidifier.increase_humidity()
    elif humidity > 50:
        humidifier.decrease_humidity()

    if light_intensity < 300:
        light.set_brightness_level("low")
    elif light_intensity > 900:
        light.set_brightness_level("high")
    else:
        light.set_brightness_level("medium")

if __name__ == "__main__":
    main()