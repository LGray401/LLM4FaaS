# To create a smart home application based on your functional description and the provided source code, we need to integrate these components to simulate a smart home environment. Your functional description specifies specific conditions for temperature, humidity, and light intensity. Let's implement a simple Python script to meet these requirements.
# 
# I'll create a Python script named `smart_home.py` that utilizes the provided `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`. This script will simulate the behavior of a smart home based on your functional description.
# 
# Here's the `smart_home.py` script:
# 
# ```python
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def control_environment(room_name):
    home = home_plan()
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)
    
    # Turn on all sensors
    for sensor in sensors:
        sensor.turn_on()

    # Control temperature
    temperature_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
    if temperature_sensor:
        current_temp = temperature_sensor.get_reading()
        ac = next((a for a in actuators if isinstance(a, AC)), None)
        heater = next((a for a in actuators if isinstance(a, Heater)), None)
        
        if current_temp < TEMP_LOW and heater:
            heater.set_target_temperature(TEMP_LOW)
            heater.adjust_temperature(current_temp)
        elif current_temp > TEMP_HIGH and ac:
            ac.set_target_temperature(TEMP_HIGH)
            ac.adjust_temperature(current_temp)

    # Control humidity
    humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
    if humidity_sensor:
        current_humidity = humidity_sensor.get_reading()
        humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)

        if current_humidity < HUMIDITY_LOW and humidifier:
            humidifier.turn_on()
            humidifier.increase_humidity()
        elif current_humidity > HUMIDITY_HIGH and humidifier:
            humidifier.turn_on()
            humidifier.decrease_humidity()

    # Control light intensity
    light_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)
    if light_sensor:
        current_light_intensity = light_sensor.get_reading()
        light = next((a for a in actuators if isinstance(a, Light)), None)

        if current_light_intensity < LIGHT_INTENSITY_LOW and light:
            light.turn_on()
            light.set_brightness_level("high")
        elif current_light_intensity > LIGHT_INTENSITY_HIGH and light:
            light.turn_off()

if __name__ == "__main__":
    room_name = "LivingRoom"  # Replace with the room name you want to control
    control_environment(room_name)
# ```
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, save the above script as `smart_home.py` and execute the following command:
# 
# ```bash
# python smart_home.py
# ```
# 
# ### Explanation
# 
# - The script initializes the home environment using the `home_plan` function.
# - It retrieves the sensors and actuators for the specified room.
# - It turns on all sensors to get readings.
# - Based on the readings:
#   - It adjusts the temperature using an AC or Heater.
#   - It adjusts humidity using a Humidifier.
#   - It adjusts light intensity using a Light actuator.
# 
# This script uses the logic defined in your source code files to interact with sensors and actuators, ensuring the room environment matches the specified conditions. Adjust `room_name` in the script to control different rooms.