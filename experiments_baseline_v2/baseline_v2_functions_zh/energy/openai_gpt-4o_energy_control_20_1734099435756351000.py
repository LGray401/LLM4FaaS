# To develop a smart home application that automatically adjusts indoor temperature, humidity, and light intensity, we can leverage the provided classes and modules. Here's a simple implementation of the main application that will integrate and utilize these functionalities:
# 
# ### Main Application
# 
# We'll create a new Python file named `smart_home.py` which will use the sensor and actuator classes to monitor and adjust the indoor environment based on predefined thresholds.
# 
# ```python
# smart_home.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def adjust_environment(room):
    sensors = room.sensors
    actuators = room.actuators

    # Turn on all sensors
    for sensor in sensors:
        sensor.turn_on()

    # Retrieve sensor readings
    temperature = next((s.get_reading() for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
    humidity = next((s.get_reading() for s in sensors if isinstance(s, HumiditySensor)), None)
    light_intensity = next((s.get_reading() for s in sensors if isinstance(s, LightIntensiveSensor)), None)

    # Find actuators
    heater = next((a for a in actuators if isinstance(a, Heater)), None)
    ac = next((a for a in actuators if isinstance(a, AC)), None)
    humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
    light = next((a for a in actuators if isinstance(a, Light)), None)

    # Adjust temperature
    if temperature is not None:
        if temperature < TEMP_LOW and heater:
            heater.set_target_temperature(TEMP_HIGH)
            heater.adjust_temperature(temperature)
        elif temperature > TEMP_HIGH and ac:
            ac.set_target_temperature(TEMP_LOW)
            ac.adjust_temperature(temperature)

    # Adjust humidity
    if humidity is not None:
        if humidity < HUMIDITY_LOW and humidifier:
            humidifier.turn_on()
            humidifier.increase_humidity()
        elif humidity > HUMIDITY_HIGH and humidifier:
            humidifier.turn_on()
            humidifier.decrease_humidity()

    # Adjust light intensity
    if light_intensity is not None and light:
        if light_intensity < LIGHT_INTENSITY_LOW:
            light.turn_on()
            light.set_brightness_level("high")
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            light.turn_off()

def main():
    home = home_plan()
    while True:
        for room in home:
            adjust_environment(room)
        time.sleep(60)  # Wait for 1 minute before next adjustment

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Application
# 
# 1. Make sure you have all the referenced files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`) in a directory named `home`.
# 2. Save the above code in a file named `smart_home.py`.
# 3. Open a terminal and navigate to the directory where `smart_home.py` is located.
# 4. Run the application with the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This application will continuously adjust the temperature, humidity, and light intensity of each room based on the sensor readings and the thresholds defined in the `config.py` file.