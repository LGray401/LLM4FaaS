# Based on your functional description and the provided source code, I'll create a `function.py` file that orchestrates the usage of the sensors and actuators to adjust the temperature, humidity, and light intensity as specified.
# 
# Here is the `function.py` file that you can place in the `functions` folder:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def main():
    # Create a home plan
    home = home_plan()

    # Set target values
    target_temperature = 26  # in Celsius
    target_humidity = 40      # in percentage
    target_light_intensity = "medium"  # Moderate Light

    # Get sensors and actuators
    room = home[0]  # Assuming we are working with the first room, e.g., LivingRoom

    temperature_sensor = None
    humidity_sensor = None
    light_sensor = None
    heater = None
    ac = None
    humidifier = None
    light = None

    # Find the relevant sensors and actuators
    for sensor in room.sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature_sensor = sensor
        elif isinstance(sensor, HumiditySensor):
            humidity_sensor = sensor
        elif isinstance(sensor, LightIntensiveSensor):
            light_sensor = sensor

    for actuator in room.actuators:
        if isinstance(actuator, Heater):
            heater = actuator
        elif isinstance(actuator, AC):
            ac = actuator
        elif isinstance(actuator, Humidifier):
            humidifier = actuator
        elif isinstance(actuator, Light):
            light = actuator

    # Turn on sensors
    if temperature_sensor and humidity_sensor and light_sensor:
        temperature_sensor.turn_on()
        humidity_sensor.turn_on()
        light_sensor.turn_on()

    # Adjust temperature
    if temperature_sensor:
        current_temp = temperature_sensor.get_reading()
        if current_temp is not None:
            if current_temp < target_temperature:
                heater.turn_on()
                heater.set_target_temperature(target_temperature)
            elif current_temp > target_temperature:
                ac.turn_on()
                ac.set_target_temperature(target_temperature)

    # Adjust humidity
    if humidity_sensor:
        current_humidity = humidity_sensor.get_reading()
        if current_humidity is not None:
            if current_humidity < target_humidity:
                humidifier.turn_on()
                humidifier.increase_humidity()
            elif current_humidity > target_humidity:
                humidifier.turn_on()
                humidifier.decrease_humidity()

    # Adjust light intensity
    if light:
        light.turn_on()
        light.set_brightness_level(target_light_intensity)

    # Turn off sensors after use
    if temperature_sensor:
        temperature_sensor.turn_off()
    if humidity_sensor:
        humidity_sensor.turn_off()
    if light_sensor:
        light_sensor.turn_off()

if __name__ == "__main__":
    main()