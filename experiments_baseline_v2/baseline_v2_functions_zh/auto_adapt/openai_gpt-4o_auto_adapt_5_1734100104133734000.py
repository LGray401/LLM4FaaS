# To create a smart home application based on your functional description and the provided source code, we will develop a Python script that initializes the sensors and actuators, reads the sensor values, and controls the actuators based on these readings. The script will be designed to run in a Linux terminal.
# 
# ### Overview
# 
# 1. **Sensors**: We will use `IndoorTemperatureSensor`, `HumiditySensor`, and `LightIntensiveSensor` to simulate the readings for temperature, humidity, and light intensity.
# 2. **Actuators**: We will use `Heater`, `AC`, `Humidifier`, and `Light` actuators to respond to sensor readings.
# 
# ### Functional Description
# 
# - **Temperature**: 24°C
# - **Humidity**: 30%
# - **Light Intensity**: 45 lux
# 
# ### Implementation Plan
# 
# 1. Create a script that initializes the home plan and retrieves the relevant sensors and actuators.
# 2. Simulate turning on sensors and retrieving their readings.
# 3. Based on the readings, adjust the actuators accordingly.
# 4. Print the status of each actuator to the terminal.
# 
# ### Python Code
# 
# Below is a Python script that follows the implementation plan using the given source files:
# 
# ```python
# main.py
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def control_home():
    # Initialize the home plan
    home = home_plan()

    # Get the sensors and actuators for the Living Room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Turn on all sensors and get readings
    sensor_readings = {}
    for sensor in living_room_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        sensor_readings[sensor.sensor_type] = reading

    # Control actuators based on sensor readings
    for actuator in living_room_actuators:
        if isinstance(actuator, Heater) or isinstance(actuator, AC):
            if "IndoorTemperature" in sensor_readings:
                current_temp = sensor_readings["IndoorTemperature"]
                if isinstance(actuator, Heater):
                    actuator.set_target_temperature(TEMP_HIGH)
                    actuator.adjust_temperature(current_temp)
                elif isinstance(actuator, AC):
                    actuator.set_target_temperature(TEMP_LOW)
                    actuator.adjust_temperature(current_temp)
        
        elif isinstance(actuator, Humidifier):
            if "Humidity" in sensor_readings:
                current_humidity = sensor_readings["Humidity"]
                if current_humidity < HUMIDITY_LOW:
                    actuator.turn_on()
                    actuator.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    actuator.turn_on()
                    actuator.decrease_humidity()
                else:
                    actuator.turn_off()
        
        elif isinstance(actuator, Light):
            if "LightIntensive" in sensor_readings:
                current_light = sensor_readings["LightIntensive"]
                if current_light < LIGHT_INTENSITY_LOW:
                    actuator.turn_on()
                    actuator.set_brightness_level("high")
                elif current_light > LIGHT_INTENSITY_HIGH:
                    actuator.turn_off()
                else:
                    actuator.turn_on()
                    actuator.set_brightness_level("medium")

if __name__ == "__main__":
    control_home()
# ```
# 
# ### Running the Application
# 
# To execute this script in a Linux terminal, use the following command:
# 
# ```bash
# python3 main.py
# ```
# 
# ### Assumptions
# 
# - The script assumes that the `logger_config` and logger usage are correctly set up in your environment.
# - The script utilizes the existing `home_plan` and related functionalities to retrieve the sensors and actuators for the "LivingRoom".
# - The script turns on all sensors, retrieves their readings, and adjusts actuators based on predefined high and low thresholds.
# 
# This script provides a basic setup based on your description and the provided code. Adjust the thresholds and actuator logic as needed to fit your specific requirements.