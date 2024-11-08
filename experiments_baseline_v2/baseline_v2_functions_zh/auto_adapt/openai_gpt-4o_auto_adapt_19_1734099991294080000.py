# To create a smart home application based on your functional description and the provided source code, we'll need to implement a Python script that interacts with the sensors and actuators. This script will:
# 
# 1. Monitor the temperature, humidity, and light intensity.
# 2. Respond to conditions that are "too hot," "too dry," or "too bright" by activating the appropriate actuators.
# 
# Based on your provided thresholds and the source code, let's implement the main application logic in a new file, `smart_home.py`. This file will utilize the existing modules (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) to perform the required actions.
# 
# ### smart_home.py
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Curtain
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

def check_conditions(home):
    # Check temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading > TEMP_HIGH:
            print("太热了! Turning on AC.")
            acs = get_all_actuators(home, "AC")
            for ac in acs:
                ac.set_target_temperature(TEMP_HIGH)
                ac.adjust_temperature(reading)

    # Check humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in humidity_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading < HUMIDITY_LOW:
            print("太干了! Turning on Humidifiers.")
            humidifiers = get_all_actuators(home, "Humidifier")
            for humidifier in humidifiers:
                humidifier.increase_humidity()

    # Check light intensity sensors
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading > LIGHT_INTENSITY_HIGH:
            print("太亮了! Closing curtains.")
            curtains = get_all_actuators(home, "Curtain")
            for curtain in curtains:
                curtain.turn_on()

def main():
    home = home_plan()
    check_conditions(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, use the following command. Ensure you're in the directory where your Python files are located, or provide the full path to the script:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation
# 
# - **Sensors**: We check the readings from temperature, humidity, and light sensors.
# - **Actuators**: Depending on the readings:
#   - If it's too hot, we turn on the air conditioning.
#   - If it's too dry, we activate humidifiers.
#   - If it's too bright, we close the curtains.
# - **Logging**: The application will log actions using the logger configured in the existing code.
# 
# This script uses the `home_plan` to initialize rooms and components, checks conditions, and operates actuators accordingly. Make sure all dependencies and modules are correctly set up in your environment.