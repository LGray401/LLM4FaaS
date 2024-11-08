# Based on your functional description and the provided source code files, I will create a `function.py` file that will include a main function to demonstrate the interaction between sensors and actuators in your smart home project. The main function will simulate the readings and control of the temperature, humidity, and light intensity based on the specified conditions.
# 
# Here is the code for `function.py`:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_HIGH
from home.logger_config import logger


def main():
    # Create home plan
    home = home_plan()

    # Iterate through each room and get the sensors and actuators
    for room in home:
        print(f"\nChecking room: {room.name}")
        
        # Check sensors
        temperature_sensor = None
        humidity_sensor = None
        light_sensor = None
        
        for sensor in room.sensors:
            if sensor.sensor_type == "IndoorTemperature":
                temperature_sensor = sensor
            elif sensor.sensor_type == "Humidity":
                humidity_sensor = sensor
            elif sensor.sensor_type == "LightIntensive":
                light_sensor = sensor
        
        # Turn on sensors and get readings
        if temperature_sensor:
            temperature_sensor.turn_on()
            temperature_reading = temperature_sensor.get_reading()
        
        if humidity_sensor:
            humidity_sensor.turn_on()
            humidity_reading = humidity_sensor.get_reading()
        
        if light_sensor:
            light_sensor.turn_on()
            light_reading = light_sensor.get_reading()

        # Check and control actuators based on sensor readings
        for actuator in room.actuators:
            if actuator.actuator_type == "Heater" and temperature_reading is not None:
                if temperature_reading < TEMP_HIGH:
                    actuator.set_target_temperature(TEMP_HIGH)
                    actuator.adjust_temperature(temperature_reading)

            elif actuator.actuator_type == "Humidifier" and humidity_reading is not None:
                if humidity_reading < HUMIDITY_HIGH:
                    actuator.increase_humidity()

            elif actuator.actuator_type == "Light":
                if light_reading is not None:
                    if light_reading < 900:  # Example threshold for light
                        actuator.turn_on()
                        actuator.set_brightness_level("medium")
                    else:
                        actuator.turn_off()

        # Turn off sensors after reading
        if temperature_sensor:
            temperature_sensor.turn_off()
        if humidity_sensor:
            humidity_sensor.turn_off()
        if light_sensor:
            light_sensor.turn_off()


if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Home Plan Creation**: The `main` function starts by creating a home plan using the `home_plan()` function which initializes the rooms and their components.
# 
# 2. **Sensor Interactions**: For each room, it identifies the temperature, humidity, and light sensors. It turns on each sensor to get readings.
# 
# 3. **Actuator Control**: Based on the readings from the sensors:
#    - The heater is turned on if the temperature is below the defined high threshold.
#    - The humidifier is activated if the humidity is below a defined high threshold.
#    - The light is turned on if the light intensity is below a certain threshold.
# 
# 4. **Sensor Shutdown**: After the readings and actions are taken, the sensors are turned off.
# 
# This structure allows for a straightforward interaction between sensors and actuators based on the functional requirements you provided. You can modify the thresholds and conditions as per your requirements.