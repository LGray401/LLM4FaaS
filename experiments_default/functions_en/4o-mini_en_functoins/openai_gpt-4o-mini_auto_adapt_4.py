# Based on your functional description and the provided source code, I will create the `function.py` file for your smart home project. This file will include a `main` function that initializes the home, retrieves the sensor readings for temperature, humidity, and light intensity, and then uses actuators to manage the environment according to the specified conditions.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize the home
    home = home_plan()

    # Define target conditions
    target_temperature = 20  # Target temperature in Celsius
    target_humidity = 50     # Target humidity in percentage
    target_light_intensity = 15  # Target light intensity in lux

    # Get sensors and actuators in the living room
    living_room = next(room for room in home if room.name == "LivingRoom")
    temperature_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "IndoorTemperature")
    humidity_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "Humidity")
    light_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "LightIntensive")

    heater = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Heater")
    ac = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "AC")
    light = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Light")

    # Turn on sensors to get readings
    temperature_sensor.turn_on()
    humidity_sensor.turn_on()
    light_sensor.turn_on()

    # Get sensor readings
    current_temperature = temperature_sensor.get_reading()
    current_humidity = humidity_sensor.get_reading()
    current_light_intensity = light_sensor.get_reading()

    # Adjust actuators based on readings
    if current_temperature is not None:
        heater.set_target_temperature(target_temperature)
        heater.adjust_temperature(current_temperature)
        ac.set_target_temperature(target_temperature)
        ac.adjust_temperature(current_temperature)

    if current_humidity is not None:
        if current_humidity < HUMIDITY_LOW:
            humidifier = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Humidifier")
            humidifier.increase_humidity()
        elif current_humidity > HUMIDITY_HIGH:
            humidifier = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Humidifier")
            humidifier.decrease_humidity()

    if current_light_intensity is not None:
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            light.turn_on()
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            light.turn_off()

    # Turn off sensors after use
    temperature_sensor.turn_off()
    humidity_sensor.turn_off()
    light_sensor.turn_off()

if __name__ == "__main__":
    main()