# Based on your functional description and the provided source code files, I'll create a `function.py` file that will implement the main functionality of your smart home project. This file will initialize the home with sensors and actuators, retrieve their readings, and manage the actuators based on the specified temperature, humidity, and light intensity conditions.
# 
# Here's the content for the `function.py` file to be placed in the `functions` folder:
# 
# ```python
# function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize the home with rooms, sensors, and actuators
    home = home_plan()

    # Iterate through each room to check sensor readings and control actuators
    for room in home:
        logger.info(f"Checking room: {room.name}")

        # Get sensors in the room
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]

        # Retrieve readings from the sensors
        temperature_reading = None
        humidity_reading = None
        light_reading = None

        # Check temperature
        if temperature_sensors:
            for sensor in temperature_sensors:
                sensor.turn_on()  # Ensure the sensor is on
                temperature_reading = sensor.get_reading()
                if temperature_reading is not None:
                    logger.info(f"Temperature reading in {room.name}: {temperature_reading}°C")
        
        # Check humidity
        if humidity_sensors:
            for sensor in humidity_sensors:
                sensor.turn_on()  # Ensure the sensor is on
                humidity_reading = sensor.get_reading()
                if humidity_reading is not None:
                    logger.info(f"Humidity reading in {room.name}: {humidity_reading}%")
        
        # Check light intensity
        if light_sensors:
            for sensor in light_sensors:
                sensor.turn_on()  # Ensure the sensor is on
                light_reading = sensor.get_reading()
                if light_reading is not None:
                    logger.info(f"Light intensity reading in {room.name}: {light_reading} lux")

        # Control actuators based on readings
        for actuator in room.actuators:
            if isinstance(actuator, Heater):
                if temperature_reading is not None:
                    actuator.set_target_temperature(26)  # Desired temperature
                    actuator.adjust_temperature(temperature_reading)

            elif isinstance(actuator, AC):
                if temperature_reading is not None:
                    actuator.set_target_temperature(24)  # Desired temperature
                    actuator.adjust_temperature(temperature_reading)

            elif isinstance(actuator, Humidifier):
                if humidity_reading is not None:
                    if humidity_reading < HUMIDITY_LOW:
                        actuator.increase_humidity()
                    elif humidity_reading > HUMIDITY_HIGH:
                        actuator.decrease_humidity()

            elif isinstance(actuator, Light):
                if light_reading is not None:
                    if light_reading < LIGHT_INTENSITY_LOW:
                        actuator.turn_on()
                        actuator.set_brightness_level("high")
                    elif LIGHT_INTENSITY_LOW <= light_reading <= LIGHT_INTENSITY_HIGH:
                        actuator.turn_on()
                        actuator.set_brightness_level("medium")
                    else:
                        actuator.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation of the `function.py` File
# 1. **Initialization**: The `main()` function initializes the home layout by calling `home_plan()`, which creates rooms with their respective sensors and actuators.
#   
# 2. **Sensor Readings**: The program iterates through each room, retrieves readings from the temperature, humidity, and light sensors, and logs the readings.
# 
# 3. **Actuator Control**: Based on the readings:
#    - The heater or AC will be turned on or off based on the temperature.
#    - The humidifier will adjust humidity levels if they are below or above the specified thresholds.
#    - The light will be controlled depending on the light intensity.
# 
# 4. **Execution**: The `main()` function is executed when the script is run directly.
# 
# ### Note
# Make sure to have the `logger_config.py` file properly set up since logging is utilized for tracking actions and statuses within the smart home system. Adjust the desired temperature and thresholds according to your specific requirements.