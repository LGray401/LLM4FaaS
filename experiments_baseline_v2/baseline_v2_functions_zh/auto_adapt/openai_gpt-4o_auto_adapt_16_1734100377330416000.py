# To create a smart home application based on the provided functional description and source code references, let's outline and implement a Python script that runs in a Linux terminal. This script will use the provided classes to simulate a smart home environment with sensors and actuators. It will monitor the temperature, humidity, and light intensity and take necessary actions based on the given conditions.
# 
# ### Smart Home Application
# 
# We'll need to create a main script `smart_home.py` that integrates the provided functional description with the reference code files. This script will:
# 
# 1. Initialize a home plan using the `home_plan` function from `home_plan.py`.
# 2. Retrieve the sensors and actuators for each room.
# 3. Simulate sensor readings.
# 4. Control actuators based on the readings and predefined thresholds in `config.py`.
# 
# Let's implement the `smart_home.py` script:
# 
# ```python
# smart_home.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def control_temperature(room):
    for sensor in room.sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            sensor.turn_on()
            temperature = sensor.get_reading()

            for actuator in room.actuators:
                if isinstance(actuator, AC):
                    actuator.set_target_temperature(TEMP_HIGH)
                    actuator.adjust_temperature(temperature)
                elif isinstance(actuator, Heater):
                    actuator.set_target_temperature(TEMP_LOW)
                    actuator.adjust_temperature(temperature)

def control_humidity(room):
    for sensor in room.sensors:
        if isinstance(sensor, HumiditySensor):
            sensor.turn_on()
            humidity = sensor.get_reading()

            for actuator in room.actuators:
                if isinstance(actuator, Humidifier):
                    if humidity < HUMIDITY_LOW:
                        actuator.turn_on()
                        actuator.increase_humidity()
                    elif humidity > HUMIDITY_HIGH:
                        actuator.turn_off()
                        actuator.decrease_humidity()

def control_light(room):
    for sensor in room.sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            light_intensity = sensor.get_reading()

            for actuator in room.actuators:
                if isinstance(actuator, Light):
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        actuator.turn_on()
                        actuator.set_brightness_level("high")
                    else:
                        actuator.turn_off()

def main():
    home = home_plan()
    for room in home:
        control_temperature(room)
        control_humidity(room)
        control_light(room)

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Application
# 
# To run the smart home application in a Linux terminal, save the code above in a file named `smart_home.py`. Make sure it is in the same directory as the `home` folder containing the source code files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`). Then, execute the following command in the terminal:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation
# 
# - The script initializes a home plan with rooms and their associated sensors and actuators.
# - It controls the temperature by adjusting the AC or Heater based on the indoor temperature reading.
# - It manages humidity using the Humidifier to increase or decrease humidity levels.
# - It controls lights based on the light intensity sensor readings.
# - The application uses the predefined thresholds from `config.py` to decide when to turn on or off actuators.
# 
# This setup simulates a basic smart home environment where sensors and actuators interact based on environmental conditions.