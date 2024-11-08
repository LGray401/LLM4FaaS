# Based on the functional description and provided source code, we can create a `function.py` file that contains a main function to manage the smart home system. This function will interact with the sensors and actuators to maintain the specified conditions: managing temperature, humidity, and light intensity.
# 
# Here's the `function.py` file:

# function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
import time

def main():
    home = home_plan()

    # Manage Temperature
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")
    
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp and current_temp > TEMP_HIGH:
            print(f"It's too hot in the house: {sensor.room_name}")
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.turn_on()
                    ac.set_target_temperature(TEMP_HIGH)

    # Manage Humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity and current_humidity < HUMIDITY_LOW:
            print(f"The house is a bit dry: {sensor.room_name}")
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    humidifier.turn_on()
                    humidifier.increase_humidity()

    # Manage Light Intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    
    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity and current_light_intensity < LIGHT_INTENSITY_LOW:
            print(f"The room is too dark: {sensor.room_name}")
            for light in lights:
                if light.room_name == sensor.room_name:
                    light.turn_on()
                    light.set_brightness_level("high")

if __name__ == "__main__":
    main()