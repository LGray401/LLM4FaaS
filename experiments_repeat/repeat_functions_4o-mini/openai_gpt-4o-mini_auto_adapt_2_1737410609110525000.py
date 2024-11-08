# Based on the provided functional description and the existing code files for your smart home project, I will create a `function.py` file that will implement the main function to manage the temperature, humidity, and light intensity conditions in the home. The `function.py` file will utilize the sensors and actuators already defined in the project to control the environment as specified.
# 
# Here's the suggested implementation of `function.py`:
# 
# ```python
# function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Humidifier, Light

def manage_home_environment(home):
    for room in home:
        # Get the relevant sensors and actuators
        temperature_sensor = next((s for s in room.sensors if s.sensor_type == "IndoorTemperature"), None)
        humidity_sensor = next((s for s in room.sensors if s.sensor_type == "Humidity"), None)
        light_sensor = next((s for s in room.sensors if s.sensor_type == "LightIntensive"), None)

        ac = next((a for a in room.actuators if isinstance(a, AC)), None)
        humidifier = next((a for a in room.actuators if isinstance(a, Humidifier)), None)
        light = next((a for a in room.actuators if isinstance(a, Light)), None)

        # Manage temperature
        if temperature_sensor:
            current_temp = temperature_sensor.get_reading()
            if current_temp is not None:
                if current_temp > TEMP_HIGH and ac:
                    ac.turn_on()  # Turn on AC if temperature is too high
                    window = next((a for a in room.actuators if isinstance(a, Window)), None)
                    if window:
                        window.turn_off()  # Close window if AC is on

        # Manage humidity
        if humidity_sensor:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW and humidifier:
                    humidifier.increase_humidity()  # Turn on humidifier if humidity is low

        # Manage light intensity
        if light_sensor:
            current_light = light_sensor.get_reading()
            if current_light is not None:
                if current_light < LIGHT_INTENSITY_LOW and light:
                    light.turn_on()  # Turn on light if light intensity is low
                elif current_light > LIGHT_INTENSITY_HIGH and light:
                    light.turn_off()  # Turn off light if light intensity is high

def main():
    home = home_plan()  # Get the home plan with rooms, sensors, and actuators
    manage_home_environment(home)  # Manage the home environment based on sensor readings

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation of `function.py`:
# 1. **Imports**: The necessary modules are imported, including room plans, configuration values, and relevant actuator classes.
# 
# 2. **manage_home_environment Function**: This function iterates through each room in the home and retrieves the sensors and actuators. It checks the readings from the temperature, humidity, and light intensity sensors and acts accordingly:
#    - If the indoor temperature exceeds the defined high threshold, the AC is turned on and the window is closed.
#    - If the humidity is below the defined low threshold, the humidifier is activated.
#    - If the light intensity is below or above the defined thresholds, the light is turned on or off, respectively.
# 
# 3. **main Function**: This function initializes the home plan and calls the management function to control the environment.
# 
# 4. **Entry Point**: The `if __name__ == "__main__":` block ensures that the `main()` function is called when the script is run directly.
# 
# This implementation will provide the necessary functionality to automatically manage the smart home environment based on the conditions specified in the functional description.