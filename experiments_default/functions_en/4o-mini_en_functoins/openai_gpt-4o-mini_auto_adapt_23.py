# Based on the functional description and the provided source code, I will create the `function.py` file for your smart home project. This file will include a main function that will utilize the sensors and actuators defined in your other modules to achieve the desired functionality.
# 
# Here's the implementation for `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Get the home plan
    home = home_plan()

    # Assuming we are focusing on the Living Room for this example
    living_room = get_room_sensors(home, "LivingRoom")
    if living_room is None:
        print("No sensors found in the Living Room.")
        return

    # Get the sensors we need to monitor
    temp_sensor = None
    humidity_sensor = None
    light_sensor = None

    for sensor in living_room:
        if sensor.sensor_type == "IndoorTemperature":
            temp_sensor = sensor
        elif sensor.sensor_type == "Humidity":
            humidity_sensor = sensor
        elif sensor.sensor_type == "LightIntensive":
            light_sensor = sensor

    # Activate sensors
    for sensor in [temp_sensor, humidity_sensor, light_sensor]:
        sensor.turn_on()

    # Read the sensors
    temperature = temp_sensor.get_reading()
    humidity = humidity_sensor.get_reading()
    light_intensity = light_sensor.get_reading()

    # Check conditions based on the specified functional description
    if temperature is not None:
        if temperature < TEMP_LOW:
            print("Temperature is too low, consider turning on the heater.")
        elif temperature > TEMP_HIGH:
            print("Temperature is too high, consider turning on the AC.")
        else:
            print("Temperature is within comfortable range.")

    if humidity is not None:
        if humidity < HUMIDITY_LOW:
            print("Humidity is low, consider using a humidifier.")
        elif humidity > HUMIDITY_HIGH:
            print("Humidity is high, consider increasing ventilation.")
        else:
            print("Humidity is within comfortable range.")

    if light_intensity is not None:
        if light_intensity < LIGHT_INTENSITY_LOW:
            print("Light intensity is too low, consider turning on the lights.")
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            print("Light intensity is too high, consider closing curtains.")
        else:
            print("Light intensity is comfortable.")

    # Turn off sensors after reading
    for sensor in [temp_sensor, humidity_sensor, light_sensor]:
        sensor.turn_off()

if __name__ == "__main__":
    main()