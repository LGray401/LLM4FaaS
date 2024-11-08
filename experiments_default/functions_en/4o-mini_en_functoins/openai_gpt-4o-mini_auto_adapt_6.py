# Based on your functional description and the provided source code, I will create a `function.py` file that integrates the functionalities of the sensors and actuators in your smart home project. This file will contain a `main` function that demonstrates how to use the different sensors and actuators to monitor and control the environment effectively.
# 
# Here’s the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Create the home plan
    home = home_plan()
    
    # Example: Monitor and control the environment in the Living Room
    living_room = next(room for room in home if room.name == "LivingRoom")
    
    # Get sensors and actuators in the Living Room
    temp_sensors = [sensor for sensor in living_room.sensors if sensor.sensor_type == "IndoorTemperature"]
    humidity_sensors = [sensor for sensor in living_room.sensors if sensor.sensor_type == "Humidity"]
    light_sensors = [sensor for sensor in living_room.sensors if sensor.sensor_type == "LightIntensive"]
    
    lights = [actuator for actuator in living_room.actuators if actuator.actuator_type == "Light"]
    heater = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Heater")
    ac = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "AC")

    # Turn on sensors
    for sensor in temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()

    # Get readings
    for sensor in temp_sensors:
        temperature = sensor.get_reading()
        if temperature is not None:
            logger.info(f"Current temperature in {living_room.name}: {temperature}°C")
            # Control heater or AC based on temperature
            heater.adjust_temperature(temperature)
            ac.adjust_temperature(temperature)

    for sensor in humidity_sensors:
        humidity = sensor.get_reading()
        if humidity is not None:
            logger.info(f"Current humidity in {living_room.name}: {humidity}%")
            # Control humidifier if humidity is outside the range
            if humidity < HUMIDITY_LOW:
                humidifier = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Humidifier")
                humidifier.increase_humidity()
            elif humidity > HUMIDITY_HIGH:
                humidifier = next(actuator for actuator in living_room.actuators if actuator.actuator_type == "Humidifier")
                humidifier.decrease_humidity()

    for sensor in light_sensors:
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            logger.info(f"Current light intensity in {living_room.name}: {light_intensity} lux")
            # Control lights based on light intensity
            for light in lights:
                if light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                elif light_intensity > LIGHT_INTENSITY_HIGH:
                    light.turn_off()

    # Print out the current status of actuators
    for actuator in living_room.actuators:
        actuator.get_status()

    # Turn off sensors after usage
    for sensor in temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()