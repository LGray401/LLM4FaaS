# Based on the functional description and the provided source code files, I will create a `function.py` file that integrates the functionality for managing temperature, humidity, and light intensity in a smart home setting.
# 
# This script will monitor sensor readings and control actuators accordingly. Here's the implementation of `function.py`:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
from home.actuator import AC, Humidifier, Light
from home.logger_config import logger

def manage_home():
    home = home_plan()

    # Iterate through each room in the home
    for room in home:
        logger.info(f"Checking room: {room.name}")
        
        # Get sensors and actuators in the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Initialize variables to hold sensor readings
        temperature = None
        humidity = None
        light_intensity = None

        # Read values from sensors
        for sensor in sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                temperature = sensor.get_reading()
            elif isinstance(sensor, HumiditySensor):
                humidity = sensor.get_reading()
            elif isinstance(sensor, LightIntensiveSensor):
                light_intensity = sensor.get_reading()

        # Control the AC based on temperature
        if temperature is not None:
            if temperature > TEMP_HIGH:
                ac = next((a for a in actuators if isinstance(a, AC)), None)
                if ac:
                    ac.turn_on()
                    logger.info(f"AC turned on in {room.name} due to high temperature: {temperature}°C")
            else:
                ac = next((a for a in actuators if isinstance(a, AC)), None)
                if ac:
                    ac.turn_off()
                    logger.info(f"AC turned off in {room.name} due to normal temperature: {temperature}°C")
        
        # Control the humidifier based on humidity
        if humidity is not None:
            if humidity < HUMIDITY_LOW:
                humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
                if humidifier:
                    humidifier.increase_humidity()
                    logger.info(f"Humidifier turned on in {room.name} due to low humidity: {humidity}%")
            else:
                humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
                if humidifier:
                    humidifier.decrease_humidity()
                    logger.info(f"Humidifier turned off in {room.name} due to normal humidity: {humidity}%")

        # Control lighting based on light intensity
        if light_intensity is not None:
            if light_intensity < LIGHT_INTENSITY_LOW:
                light = next((a for a in actuators if isinstance(a, Light)), None)
                if light:
                    light.turn_on()
                    logger.info(f"Light turned on in {room.name} due to low light intensity: {light_intensity} lux")
            else:
                light = next((a for a in actuators if isinstance(a, Light)), None)
                if light:
                    light.turn_off()
                    logger.info(f"Light turned off in {room.name} due to normal light intensity: {light_intensity} lux")

def main():
    manage_home()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Imports**: The necessary classes and functions from the other modules are imported.
# 2. **manage_home function**: 
#    - It retrieves the home plan and iterates through each room.
#    - For each room, it gathers sensor readings for temperature, humidity, and light intensity.
#    - Based on these readings, it controls the air conditioning, humidifier, and lights according to the specified thresholds.
# 3. **main function**: This function serves as the entry point, calling `manage_home` to execute the smart home management logic.
# 
# ### Usage:
# - Place the `function.py` file in the `functions` folder of your project.
# - You can run this script to monitor and manage your smart home based on the sensor readings.