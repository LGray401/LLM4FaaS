# To create a smart home application based on the provided functional description and reference code, we will build a new Python script that integrates the functionality described. This script will create instances of sensors and actuators, set the desired conditions, and interact with the components to simulate a smart home environment.
# 
# Here's how we can implement this:
# 
# ### Main Script: `smart_home.py`
# 
# ```python
import time

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Light
from home.home_plan import home_plan

# Initialize the home plan
home = home_plan()

# Define target values based on the functional description
TARGET_TEMPERATURE = 26  # Celsius
TARGET_HUMIDITY = 50     # Percentage
TARGET_LIGHT = "medium"  # Brightness level

def control_living_room():
    # Get the living room
    room = next((r for r in home if r.name == "LivingRoom"), None)

    if room is None:
        print("LivingRoom not found in the home plan.")
        return

    # Turn on sensors and actuators
    for sensor in room.sensors:
        sensor.turn_on()
    
    for actuator in room.actuators:
        actuator.turn_on()

    # Control temperature
    temperature_sensor = next((s for s in room.sensors if isinstance(s, IndoorTemperatureSensor)), None)
    ac = next((a for a in room.actuators if isinstance(a, AC)), None)

    if temperature_sensor and ac:
        current_temperature = temperature_sensor.get_reading()
        if current_temperature is not None:
            ac.set_target_temperature(TARGET_TEMPERATURE)
            ac.adjust_temperature(current_temperature)

    # Control humidity
    humidity_sensor = next((s for s in room.sensors if isinstance(s, HumiditySensor)), None)
    humidifier = next((a for a in room.actuators if isinstance(a, Humidifier)), None)

    if humidity_sensor and humidifier:
        current_humidity = humidity_sensor.get_reading()
        if current_humidity is not None:
            if current_humidity < TARGET_HUMIDITY:
                humidifier.increase_humidity()
            else:
                humidifier.decrease_humidity()

    # Control light
    light_sensor = next((s for s in room.sensors if isinstance(s, LightIntensiveSensor)), None)
    light = next((a for a in room.actuators if isinstance(a, Light)), None)

    if light_sensor and light:
        light.set_brightness_level(TARGET_LIGHT)

if __name__ == "__main__":
    control_living_room()
    time.sleep(1)  # Simulate some delay
# ```
# 
# ### Command to Run the Application
# 
# To run the `smart_home.py` script from a Linux terminal, navigate to the directory containing the script and the `home` folder, and use the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation
# 
# - **Initialization**: The script initializes the home environment using the `home_plan()` function, which creates rooms and populates them with sensors and actuators.
# - **Control Logic**:
#   - **Temperature**: The script reads the current temperature from the `IndoorTemperatureSensor` and uses the `AC` to adjust it to the target temperature.
#   - **Humidity**: Similarly, it checks the humidity and uses the `Humidifier` to adjust it to the target level.
#   - **Light**: It sets the brightness of the `Light` actuator to the desired level based on the functional description.
# 
# Make sure that all referenced classes and modules (`sensor`, `actuator`, `home_plan`, etc.) are correctly located in the `home` directory as per the original source code provided.