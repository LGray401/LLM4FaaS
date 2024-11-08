# To create a smart home application based on your functional description and the provided source code, we need to implement a script that sets up the environment and uses the available sensors and actuators to reflect your specified conditions. Based on the functional description, we'll create a script that will:
# 
# 1. Set the temperature to 25°C.
# 2. Set humidity to a moderate level.
# 3. Set light intensity to a high level.
# 
# Let's create a script named `smart_home.py` that uses the provided `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.
# 
# ### smart_home.py
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH

def main():
    # Create the home environment
    home = home_plan()
    
    # Temperature
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp < TEMP_HIGH:
            acs = get_all_actuators(home, "AC")
            for ac in acs:
                ac.set_target_temperature(TEMP_HIGH)
                ac.turn_on()
        else:
            heaters = get_all_actuators(home, "Heater")
            for heater in heaters:
                heater.set_target_temperature(TEMP_HIGH)
                heater.turn_off()
    
    # Humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        humidifiers = get_all_actuators(home, "Humidifier")
        for humidifier in humidifiers:
            if current_humidity < HUMIDITY_LOW:
                humidifier.turn_on()
                humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                humidifier.decrease_humidity()
    
    # Light Intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_on()
            if current_light_intensity < LIGHT_INTENSITY_HIGH:
                light.set_brightness_level("high")
            else:
                light.set_brightness_level("medium")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation
# 
# - **Temperature**: We turn on all indoor temperature sensors and adjust the AC and heaters based on the current temperature readings. We aim for a target temperature of 25°C.
#   
# - **Humidity**: Humidity sensors are used to determine the current level. Humidifiers are adjusted to maintain moderate humidity levels.
# 
# - **Light Intensity**: Light sensors measure the current intensity, and lights are adjusted to ensure high light intensity.
# 
# ### Running the Script
# 
# To run the script in a Linux terminal, navigate to the directory containing your `home` folder and `smart_home.py`. Use the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# Make sure you have the necessary permissions to execute the script and that the Python environment is properly set up with any required dependencies.