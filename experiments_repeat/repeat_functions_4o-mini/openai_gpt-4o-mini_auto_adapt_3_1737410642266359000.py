# Based on the functional description and the source code provided, I will create a `function.py` file for your smart home project. The `function.py` file will contain a main function that simulates a simple control flow in your smart home environment, particularly focusing on temperature, humidity, and light intensity as described.
# 
# Here’s the content of the `function.py` file:
# 
# ```python
# function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize home plan
    home = home_plan()
    
    # Set target conditions
    desired_temperature = 26  # in degree Celsius
    desired_humidity = 50  # in percentage
    desired_light_intensity = "medium"  # brightness level for lights

    # Iterate through rooms to manage sensors and actuators
    for room in home:
        print(f"\nManaging {room.name}...")
        
        # Check all sensors in the room
        for sensor in room.sensors:
            sensor.turn_on()  # Turn on sensors to get readings
            reading = sensor.get_reading()
            if reading is not None:
                # Check for temperature
                if sensor.sensor_type == "IndoorTemperature":
                    if reading < TEMP_LOW:
                        logger.info(f"Temperature in {room.name} is too low: {reading}°C. Turning on heater.")
                        heater = next((actuator for actuator in room.actuators if isinstance(actuator, Heater)), None)
                        if heater:
                            heater.set_target_temperature(desired_temperature)
                            heater.adjust_temperature(reading)

                    elif reading > TEMP_HIGH:
                        logger.info(f"Temperature in {room.name} is too high: {reading}°C. Turning on AC.")
                        ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
                        if ac:
                            ac.set_target_temperature(desired_temperature)
                            ac.adjust_temperature(reading)

                # Check for humidity
                elif sensor.sensor_type == "Humidity":
                    if reading < HUMIDITY_LOW:
                        logger.info(f"Humidity in {room.name} is too low: {reading}%. Turning on humidifier.")
                        humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
                        if humidifier:
                            humidifier.increase_humidity()
                    
                    elif reading > HUMIDITY_HIGH:
                        logger.info(f"Humidity in {room.name} is too high: {reading}%. Taking action.")
                        humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
                        if humidifier:
                            humidifier.decrease_humidity()

                # Check for light intensity
                elif sensor.sensor_type == "LightIntensive":
                    if reading < LIGHT_INTENSITY_LOW:
                        logger.info(f"Light intensity in {room.name} is too low: {reading} lux. Turning on lights.")
                        light = next((actuator for actuator in room.actuators if isinstance(actuator, Light)), None)
                        if light:
                            light.turn_on()
                            light.set_brightness_level(desired_light_intensity)

                    elif reading > LIGHT_INTENSITY_HIGH:
                        logger.info(f"Light intensity in {room.name} is too high: {reading} lux. Adjusting lights.")
                        light = next((actuator for actuator in room.actuators if isinstance(actuator, Light)), None)
                        if light:
                            light.turn_off()

            sensor.turn_off()  # Turn off sensors after reading

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation of `function.py`:
# 1. **Initialization**: The `main` function initializes the home plan which consists of rooms, sensors, and actuators.
# 2. **Desired Conditions**: It sets desired conditions for temperature, humidity, and light intensity based on your functional description. 
# 3. **Sensor Management**: It iterates through each room to check the readings from the sensors:
#    - For temperature, it adjusts the heater or AC based on the readings.
#    - For humidity, it increases or decreases humidity as needed.
#    - For light intensity, it turns on or off the lights based on the readings.
# 4. **Logging**: It uses the logger to record actions for monitoring and debugging purposes.
# 
# Ensure that your project structure has a folder named `functions` where this `function.py` file will be placed. You can run the `function.py` file to simulate the smart home environment according to your specifications.