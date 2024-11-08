# Based on the functional description and the provided source code for your smart home project, I will create the `function.py` file with a main function that utilizes the sensors and actuators. This main function will simulate a scenario where the temperature, humidity, and light intensity are monitored, and the appropriate actions are taken based on predefined thresholds.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize home plan with rooms and their components
    home = home_plan()

    # Get sensors and actuators from the living room as an example
    living_room = next(room for room in home if room.name == "LivingRoom")
    temperature_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "IndoorTemperature")
    humidity_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "Humidity")
    light_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "LightIntensive")

    heater = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Heater")
    ac = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "AC")
    light_actuator = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Light")

    # Turn on sensors
    temperature_sensor.turn_on()
    humidity_sensor.turn_on()
    light_sensor.turn_on()
    heater.turn_on()
    ac.turn_on()
    light_actuator.turn_on()

    # Get readings
    temperature = temperature_sensor.get_reading()
    humidity = humidity_sensor.get_reading()
    light_intensity = light_sensor.get_reading()

    # Control logic based on readings
    if temperature is not None:
        if temperature < TEMP_LOW:
            heater.set_target_temperature(TEMP_HIGH)
            heater.adjust_temperature(temperature)
        elif temperature > TEMP_HIGH:
            ac.set_target_temperature(TEMP_LOW)
            ac.adjust_temperature(temperature)

    if humidity is not None:
        if humidity < HUMIDITY_LOW:
            print("Humidity is low, consider using a humidifier.")
        elif humidity > HUMIDITY_HIGH:
            print("Humidity is high, consider turning on a dehumidifier.")

    if light_intensity is not None:
        if light_intensity < LIGHT_INTENSITY_LOW:
            light_actuator.set_brightness_level("high")
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            light_actuator.set_brightness_level("low")

    # Turn off sensors and actuators after use
    temperature_sensor.turn_off()
    humidity_sensor.turn_off()
    light_sensor.turn_off()
    heater.turn_off()
    ac.turn_off()
    light_actuator.turn_off()

if __name__ == "__main__":
    main()