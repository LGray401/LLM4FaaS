# Based on your functional description and the provided code, I will create the `function.py` file to monitor the temperature, humidity, and light intensity in your smart home and activate the corresponding actuators (like the heater, humidifier, or light) when the specified conditions are met. 
# 
# Here's how the `function.py` file will be structured:
# 
# 1. **Main function** to initialize the home setup.
# 2. **Monitoring conditions** for temperature, humidity, and light intensity.
# 3. **Actuating responses** based on those conditions.
# 
# Here is the `function.py` code:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, Humidifier, Light
from home.logger_config import logger

def monitor_home_conditions():
    home = home_plan()

    for room in home:
        sensors = room.sensors
        actuators = room.actuators

        # Check each sensor's reading and perform actions
        temp_sensor = next((s for s in sensors if s.sensor_type == "IndoorTemperature"), None)
        humidity_sensor = next((s for s in sensors if s.sensor_type == "Humidity"), None)
        light_sensor = next((s for s in sensors if s.sensor_type == "LightIntensive"), None)

        # Temperature condition
        if temp_sensor:
            current_temp = temp_sensor.get_reading()
            if current_temp is not None:
                if current_temp > TEMP_HIGH:
                    # Too hot, turn on the heater
                    heater = next((a for a in actuators if isinstance(a, Heater)), None)
                    if heater:
                        heater.set_target_temperature(TEMP_HIGH)
                        heater.adjust_temperature(current_temp)
                elif current_temp < TEMP_LOW:
                    # Too cold, turn on the AC
                    ac = next((a for a in actuators if isinstance(a, AC)), None)
                    if ac:
                        ac.set_target_temperature(TEMP_LOW)
                        ac.adjust_temperature(current_temp)

        # Humidity condition
        if humidity_sensor:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    # Too dry, turn on humidifier
                    humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
                    if humidifier:
                        humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    # Too humid, turn off humidifier
                    humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
                    if humidifier:
                        humidifier.decrease_humidity()

        # Light condition
        if light_sensor:
            current_light = light_sensor.get_reading()
            if current_light is not None:
                if current_light < LIGHT_INTENSITY_LOW:
                    # Too dark, turn on the lights
                    light = next((a for a in actuators if isinstance(a, Light)), None)
                    if light:
                        light.turn_on()
                elif current_light > LIGHT_INTENSITY_HIGH:
                    # Too bright, turn off the lights
                    light = next((a for a in actuators if isinstance(a, Light)), None)
                    if light:
                        light.turn_off()

def main():
    print("Starting Smart Home Monitoring...")
    monitor_home_conditions()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Home Initialization**: The `home_plan` function is called to get the current setup of rooms, sensors, and actuators.
#   
# 2. **Monitoring Loop**: The code checks the readings from the temperature, humidity, and light sensors. Based on the readings:
#    - If the temperature is too high, the heater is activated.
#    - If the temperature is too low, the AC is activated.
#    - If the humidity is too low, the humidifier is activated.
#    - If the humidity is too high, the humidifier is turned off.
#    - If the light intensity is too low, the lights are turned on.
#    - If the light intensity is too high, the lights are turned off.
# 
# 3. **Main Function**: The main function initializes the monitoring process.
# 
# Make sure to place this file in the `functions` folder and ensure that all imports and configurations are correct relative to your project structure.