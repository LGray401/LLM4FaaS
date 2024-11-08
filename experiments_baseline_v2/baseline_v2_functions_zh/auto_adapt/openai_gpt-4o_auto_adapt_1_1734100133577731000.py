# To create a smart home application based on your functional description and the provided source code, I will write a Python script that utilizes the existing components (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) to adjust the temperature, humidity, and light intensity as specified.
# 
# Here is the application script, `smart_home.py`, which you can run in a Linux terminal:
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan

def adjust_temperature(room, target_temperature):
    for sensor in room.sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            sensor.turn_on()
            current_temperature = sensor.get_reading()
            for actuator in room.actuators:
                if isinstance(actuator, Heater) or isinstance(actuator, AC):
                    actuator.set_target_temperature(target_temperature)
                    actuator.adjust_temperature(current_temperature)
            sensor.turn_off()

def adjust_humidity(room, target_humidity):
    for sensor in room.sensors:
        if isinstance(sensor, HumiditySensor):
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            for actuator in room.actuators:
                if isinstance(actuator, Humidifier):
                    if current_humidity < target_humidity:
                        actuator.increase_humidity()
                    else:
                        actuator.decrease_humidity()
            sensor.turn_off()

def adjust_light_intensity(room, level):
    for sensor in room.sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            sensor.get_reading()
            for actuator in room.actuators:
                if isinstance(actuator, Light):
                    actuator.turn_on()
                    actuator.set_brightness_level(level)
            sensor.turn_off()

def main():
    home = home_plan()
    
    # Adjust settings based on functional description
    target_temperature = 26
    target_humidity = 40
    light_level = "medium"

    for room in home:
        adjust_temperature(room, target_temperature)
        adjust_humidity(room, target_humidity)
        adjust_light_intensity(room, light_level)

if __name__ == "__main__":
    main()
# ```
# 
# ### Instructions to Run the Application:
# 
# 1. Save the script above as `smart_home.py` in the same directory where the `home` folder is located.
# 
# 2. Open a terminal and navigate to the directory containing `smart_home.py`.
# 
# 3. Run the script using Python:
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This script initializes the home environment, checks the current conditions using the sensors, and adjusts the actuators to achieve the desired temperature, humidity, and light intensity settings as specified in your functional description.