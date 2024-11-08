# Based on your functional description and the provided source code, I'll provide a Python application that simulates a smart home environment. This application will utilize the existing classes from the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files to achieve the functionalities described. Here is how the functionality will be implemented:
# 
# 1. **Temperature**: We'll assume you want to keep the indoor temperature around 26°C. We'll use AC and Heater actuators to maintain this temperature.
# 2. **Humidity**: To ensure an "适宜湿度" (suitable humidity), we'll use the Humidifier to maintain the humidity within a certain range.
# 3. **Light Intensity**: We'll control the Light actuators to ensure "光照好些" (good lighting).
# 
# ```python
# main.py
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Light, Humidifier
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH

def main():
    # Create the home plan
    home = home_plan()

    # Control temperature
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")

    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temp = sensor.get_reading()
        for ac in acs:
            ac.set_target_temperature(26)
            ac.adjust_temperature(temp)
        for heater in heaters:
            heater.set_target_temperature(26)
            heater.adjust_temperature(temp)

    # Control humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity = sensor.get_reading()
        for humidifier in humidifiers:
            if humidity < HUMIDITY_LOW:
                humidifier.turn_on()
                humidifier.increase_humidity()
            elif humidity > HUMIDITY_HIGH:
                humidifier.turn_on()
                humidifier.decrease_humidity()
            else:
                humidifier.turn_off()

    # Control light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        for light in lights:
            if light_intensity < LIGHT_INTENSITY_HIGH:
                light.turn_on()
                light.set_brightness_level("high")
            else:
                light.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# To run this application in a Linux terminal, save the above code in a file named `main.py` in the same directory as your `home` folder. Then, execute the following command:
# 
# ```bash
# python3 main.py
# ```
# 
# This script will use the sensors to read current conditions and adjust the actuators to meet the specified requirements based on your functional description. Make sure to have the `home` directory with the provided `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files available in the same directory as `main.py`.