# Sure! Based on the provided `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files, and the functional description, here is the `function.py` file that includes a main function to manage and interact with the smart home system:
# 
# ### `function.py`

import os
import sys

# Ensure the home directory is on the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'home')))

from sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home_plan import home_plan, get_all_sensors
from config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Get all sensors for Indoor Temperature, Humidity, and Light Intensity
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")

    # Turn on all the sensors
    for sensor in indoor_temp_sensors + humidity_sensors + light_intensity_sensors:
        sensor.turn_on()

    # Get readings from the sensors and print them with the functional descriptions
    print("\nTemperature readings:")
    for sensor in indoor_temp_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            print(f"{sensor.room_name} - 温度: {reading}°C")

    print("\nHumidity readings:")
    for sensor in humidity_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            print(f"{sensor.room_name} - 湿度: {reading}%")

    print("\nLight Intensity readings:")
    for sensor in light_intensity_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            print(f"{sensor.room_name} - 光照: {reading} lux")

    # Turn off all the sensors
    for sensor in indoor_temp_sensors + humidity_sensors + light_intensity_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()