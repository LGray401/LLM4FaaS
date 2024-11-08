# To create a smart home application in Python that can be run in a Linux terminal, we need to implement a script that utilizes the provided sensor and actuator classes to achieve the described functionality. The application should:
# 
# 1. Maintain indoor temperature at 26°C.
# 2. Maintain indoor humidity at 60%.
# 3. Adjust light intensity based on activity: bright for work, dim for relaxation, and off for rest.
# 
# Here's how you could implement this functionality:
# 
# ### smart_home.py
# 
# ```python
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan

TARGET_TEMPERATURE = 26  # Celsius
TARGET_HUMIDITY = 60  # Percentage

# Simulate different times of the day
def get_current_activity():
    current_hour = time.localtime().tm_hour
    if 9 <= current_hour < 17:
        return "work"
    elif 17 <= current_hour < 22:
        return "relax"
    else:
        return "rest"

def adjust_temperature(room):
    for sensor in room.sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            sensor.turn_on()
            current_temp = sensor.get_reading()
            for actuator in room.actuators:
                if isinstance(actuator, Heater):
                    actuator.set_target_temperature(TARGET_TEMPERATURE)
                    actuator.adjust_temperature(current_temp)
                elif isinstance(actuator, AC):
                    actuator.set_target_temperature(TARGET_TEMPERATURE)
                    actuator.adjust_temperature(current_temp)

def adjust_humidity(room):
    for sensor in room.sensors:
        if isinstance(sensor, HumiditySensor):
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            for actuator in room.actuators:
                if isinstance(actuator, Humidifier):
                    if current_humidity < TARGET_HUMIDITY:
                        actuator.turn_on()
                        actuator.increase_humidity()
                    else:
                        actuator.turn_off()

def adjust_lighting(room):
    activity = get_current_activity()
    for sensor in room.sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            for actuator in room.actuators:
                if isinstance(actuator, Light):
                    actuator.turn_on()
                    if activity == "work":
                        actuator.set_brightness_level("high")
                    elif activity == "relax":
                        actuator.set_brightness_level("medium")
                    elif activity == "rest":
                        actuator.turn_off()

def main():
    home = home_plan()
    for room in home:
        adjust_temperature(room)
        adjust_humidity(room)
        adjust_lighting(room)
        time.sleep(1)  # Simulate delay

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, save the above script as `smart_home.py`. You can execute it using Python:
# 
# ```bash
# python smart_home.py
# ```
# 
# ### Explanation
# 
# - **Temperature Control:** We adjust the temperature using `IndoorTemperatureSensor` for reading and `Heater`/`AC` actuators for maintaining the target temperature of 26°C.
# - **Humidity Control:** We maintain the humidity level using `HumiditySensor` and `Humidifier` actuators to achieve 60%.
# - **Lighting Control:** The `LightIntensiveSensor` is used to decide the brightness level of `Light` actuators based on the current time and assumed activity.
# 
# You can modify the `get_current_activity()` function to simulate different activities based on the current time. Adjustments are made within each room by iterating over its sensors and actuators.