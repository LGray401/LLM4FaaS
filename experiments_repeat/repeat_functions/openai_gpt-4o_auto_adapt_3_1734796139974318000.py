# To create a `function.py` file that fulfills your requirements, I'll design a script that sets up a basic smart home environment by initializing rooms with sensors and actuators, and then interacts with the sensors to obtain readings and control the actuators based on predefined conditions. The main function will orchestrate these operations.
# 
# Here is the `function.py` code:
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, Humidifier
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Get all indoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Get all light intensity sensors
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all heaters and ACs
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    # Get all lights
    lights = get_all_actuators(home, "Light")

    # Get all humidifiers
    humidifiers = get_all_actuators(home, "Humidifier")

    # Turn on all actuators for the demonstration
    for heater in heaters:
        heater.turn_on()

    for ac in acs:
        ac.turn_on()

    for light in lights:
        light.turn_on()

    for humidifier in humidifiers:
        humidifier.turn_on()

    # Read and adjust temperature
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temp_reading = sensor.get_reading()
        if temp_reading is not None:
            for heater in heaters:
                heater.set_target_temperature(TEMP_LOW)
                heater.adjust_temperature(temp_reading)
            for ac in acs:
                ac.set_target_temperature(TEMP_HIGH)
                ac.adjust_temperature(temp_reading)

    # Read and adjust humidity
    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity_reading = sensor.get_reading()
        if humidity_reading is not None:
            for humidifier in humidifiers:
                if humidity_reading < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif humidity_reading > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()

    # Read and adjust light intensity
    for sensor in light_sensors:
        sensor.turn_on()
        light_reading = sensor.get_reading()
        if light_reading is not None:
            for light in lights:
                if light_reading < LIGHT_INTENSITY_LOW:
                    light.set_brightness_level("high")
                elif light_reading < LIGHT_INTENSITY_HIGH:
                    light.set_brightness_level("medium")
                else:
                    light.set_brightness_level("low")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Initialization**: The script begins by importing necessary classes and functions from the `home` module. It initializes the home configuration using `home_plan()`.
# 
# 2. **Sensor and Actuator Management**: It collects all sensors and actuators of interest, such as temperature sensors, humidity sensors, light sensors, heaters, ACs, lights, and humidifiers.
# 
# 3. **Actuator Control**: All actuators are turned on for demonstration purposes. In a real-world scenario, you would control them based on sensor readings and conditions.
# 
# 4. **Temperature Adjustment**: It iterates over temperature sensors to read the current temperature and adjust heaters and ACs accordingly.
# 
# 5. **Humidity Adjustment**: It adjusts humidity using humidifiers based on readings from humidity sensors.
# 
# 6. **Light Adjustment**: It sets the brightness of lights based on readings from light intensity sensors.
# 
# This script assumes the logger and other dependencies are correctly configured in your project. The `main()` function orchestrates the operations as described in your functional requirements. You can expand this script to include more complex logic as needed for your smart home project.