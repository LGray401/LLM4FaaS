# Based on the provided functional description and existing code for your smart home project, I will create the `function.py` file in the `functions` folder. This file will include a main function that initializes the sensors and actuators, retrieves their readings, and manages the actions based on the specified temperature, humidity, and light intensity.
# 
# Here is the content of `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Create the home plan
    home = home_plan()
    
    # Iterate through the rooms and manage sensors and actuators
    for room in home:
        logger.info(f"Checking sensors and actuators in {room.name}.")

        # Get sensors
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]

        # Get readings for temperature, humidity, and light intensity
        temperature = sum(sensor.get_reading() for sensor in temperature_sensors if sensor.status == "on") / len(temperature_sensors) if temperature_sensors else None
        humidity = sum(sensor.get_reading() for sensor in humidity_sensors if sensor.status == "on") / len(humidity_sensors) if humidity_sensors else None
        light_intensity = sum(sensor.get_reading() for sensor in light_sensors if sensor.status == "on") / len(light_sensors) if light_sensors else None

        # Print the readings for the room
        logger.info(f"{room.name} - Temperature: {temperature}, Humidity: {humidity}, Light Intensity: {light_intensity}")

        # Manage actuators based on readings
        for actuator in room.actuators:
            if isinstance(actuator, zHeater):
                actuator.set_target_temperature(TEMP_HIGH)
                actuator.adjust_temperature(temperature)

            elif isinstance(actuator, AC):
                actuator.set_target_temperature(TEMP_LOW)
                actuator.adjust_temperature(temperature)

            elif isinstance(actuator, Humidifier):
                if humidity is not None:
                    if humidity < HUMIDITY_LOW:
                        actuator.turn_on()
                        actuator.increase_humidity()
                    elif humidity > HUMIDITY_HIGH:
                        actuator.turn_on()
                        actuator.decrease_humidity()
                    else:
                        actuator.turn_off()

            elif isinstance(actuator, Light):
                if light_intensity is not None:
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        actuator.turn_on()
                        actuator.set_brightness_level("high")  # For example, set to high brightness
                    else:
                        actuator.turn_off()

if __name__ == "__main__":
    main()