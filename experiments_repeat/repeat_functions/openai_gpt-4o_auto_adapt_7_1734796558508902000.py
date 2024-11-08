# Based on the functional descriptions you provided for temperature, humidity, and light intensity, we can create a `function.py` file that checks the sensor readings and responds accordingly by adjusting the actuators in the smart home system. Here's how you can implement the `main` function in `function.py`:
# 
# ```python
# function.py

import time
from home_plan import home_plan, get_all_sensors, get_all_actuators
from config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def main():
    home = home_plan()  # Initialize the home plan with rooms, sensors, and actuators

    while True:
        # Check temperature
        indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        ac_units = get_all_actuators(home, "AC")

        for sensor in indoor_temperature_sensors:
            sensor.turn_on()
            temperature = sensor.get_reading()
            if temperature is not None and temperature > TEMP_HIGH:
                print("屋里太热了")
                for ac in ac_units:
                    if ac.room_name == sensor.room_name:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(temperature)

        # Check humidity
        humidity_sensors = get_all_sensors(home, "Humidity")
        humidifiers = get_all_actuators(home, "Humidifier")

        for sensor in humidity_sensors:
            sensor.turn_on()
            humidity = sensor.get_reading()
            if humidity is not None and humidity < HUMIDITY_LOW:
                print("屋里有点干")
                for humidifier in humidifiers:
                    if humidifier.room_name == sensor.room_name:
                        humidifier.turn_on()
                        humidifier.increase_humidity()

        # Check light intensity
        light_sensors = get_all_sensors(home, "LightIntensive")
        lights = get_all_actuators(home, "Light")

        for sensor in light_sensors:
            sensor.turn_on()
            light_intensity = sensor.get_reading()
            if light_intensity is not None and light_intensity < LIGHT_INTENSITY_LOW:
                print("屋里太暗了")
                for light in lights:
                    if light.room_name == sensor.room_name:
                        light.turn_on()
                        light.set_brightness_level("high")

        # Wait before checking again
        time.sleep(60)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **Temperature Control**: If any indoor temperature sensor detects a temperature above `TEMP_HIGH`, it prints "屋里太热了" and adjusts the AC in the corresponding room.
# 
# - **Humidity Control**: If any humidity sensor reads a level below `HUMIDITY_LOW`, it prints "屋里有点干" and turns on the humidifier in the corresponding room.
# 
# - **Light Intensity Control**: If any light intensity sensor detects a level below `LIGHT_INTENSITY_LOW`, it prints "屋里太暗了" and turns on the lights in the corresponding room to the highest brightness.
# 
# ### Notes:
# - The sensors are turned on before readings are taken. Actuators are adjusted based on the current readings.
# - The loop runs indefinitely, checking the conditions every 60 seconds. Adjust the sleep duration as needed for your application.
# - This script assumes that the sensors and actuators are properly initialized in `home_plan`.
# 
# Ensure that the `function.py` file is placed in the `functions` folder and the home module's structure is correctly set up so that imports work seamlessly.