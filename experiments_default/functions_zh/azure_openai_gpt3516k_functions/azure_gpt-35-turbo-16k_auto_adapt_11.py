# Here is the 'function.py' file based on the given functional description:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC

def main():
    # Create sensors
    temperature_sensor = IndoorTemperatureSensor("LivingRoom")
    humidity_sensor = HumiditySensor("LivingRoom")
    light_sensor = LightIntensiveSensor("LivingRoom")

    # Create actuators
    ac = AC("LivingRoom")

    # Get sensor readings
    temperature = temperature_sensor.get_reading()
    humidity = humidity_sensor.get_reading()
    light_intensity = light_sensor.get_reading()

    # Control the AC based on the sensor readings
    if temperature > 26:
        ac.turn_on()
    elif humidity > 10:
        ac.turn_on()
    elif light_intensity > 20:
        ac.turn_on()
    else:
        ac.turn_off()

if __name__ == "__main__":
    main()