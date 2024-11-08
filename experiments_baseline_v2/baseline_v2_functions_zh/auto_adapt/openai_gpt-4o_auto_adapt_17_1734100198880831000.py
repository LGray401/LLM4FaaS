# To create a smart home application based on the provided functional description and existing code, I'll write a new Python script that utilizes the components from the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files. The application will simulate a simple smart home environment where it monitors sensor readings and adjusts actuators accordingly.
# 
# ### Smart Home Application Script
# 
# Let's create a script named `smart_home.py` that will run in a Linux terminal. This script will perform the following:
# 
# 1. Set up the home environment using the `home_plan()` function.
# 2. Monitor the temperature, humidity, and light intensity.
# 3. Use actuators to adjust the environment based on the functional description provided (Temperature: 26°C, Humidity: 40%, Light Intensity: 80%).
# 
# Below is the implementation of `smart_home.py`:
# 
# ```python
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create the home environment
    home = home_plan()

    # Desired states from the functional description
    desired_temperature = 26
    desired_humidity = 40
    desired_light_intensity = 80

    # Get all sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    ac_units = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Turn on sensors
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()

    # Monitor and adjust environment
    for temp_sensor in temperature_sensors:
        current_temp = temp_sensor.get_reading()
        for ac in ac_units:
            ac.set_target_temperature(desired_temperature)
            ac.adjust_temperature(current_temp)

    for humidity_sensor in humidity_sensors:
        current_humidity = humidity_sensor.get_reading()
        for humidifier in humidifiers:
            if current_humidity < HUMIDITY_LOW:
                humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                humidifier.decrease_humidity()

    for light_sensor in light_sensors:
        current_light = light_sensor.get_reading()
        for light in lights:
            light.turn_on()
            if current_light < LIGHT_INTENSITY_LOW:
                light.set_brightness_level("high")
            elif LIGHT_INTENSITY_LOW <= current_light <= LIGHT_INTENSITY_HIGH:
                light.set_brightness_level("medium")
            else:
                light.set_brightness_level("low")

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# Save the above script as `smart_home.py`. To run the application from a Linux terminal, navigate to the directory where `smart_home.py` is located and run:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This command will execute the script, and it will use the existing sensor and actuator classes to simulate a smart home environment. The script will adjust the actuators based on the sensor readings to match the desired conditions specified in the functional description.