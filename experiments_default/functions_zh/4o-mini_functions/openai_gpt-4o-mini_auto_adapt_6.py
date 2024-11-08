# Based on the provided functional description and source code, here is the implementation for the `function.py` file. This file will serve as the main entry point for the smart home project, allowing users to check readings for temperature, humidity, and light intensity, as well as invoke actuators based on those readings.
# 
# Here's the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Create home plan
    home = home_plan()

    # Check all sensors and log readings
    for room in home:
        print(f"\n--- Checking readings in {room.name} ---")
        
        # Get temperature sensors
        temp_sensors = get_all_sensors(home, "IndoorTemperature")
        for sensor in temp_sensors:
            sensor.turn_on()
            temperature = sensor.get_reading()
            if temperature is not None:
                if temperature < TEMP_LOW:
                    print(f"Temperature in {room.name} is too low: {temperature}°C. Consider turning on the heater.")
                elif temperature > TEMP_HIGH:
                    print(f"Temperature in {room.name} is too high: {temperature}°C. Consider turning on the AC.")

        # Get humidity sensors
        humidity_sensors = get_all_sensors(home, "Humidity")
        for sensor in humidity_sensors:
            sensor.turn_on()
            humidity = sensor.get_reading()
            if humidity is not None:
                if humidity < HUMIDITY_LOW:
                    print(f"Humidity in {room.name} is too low: {humidity}%. Consider using a humidifier.")
                elif humidity > HUMIDITY_HIGH:
                    print(f"Humidity in {room.name} is too high: {humidity}%. Consider turning on the dehumidifier.")

        # Get light intensity sensors
        light_sensors = get_all_sensors(home, "LightIntensive")
        for sensor in light_sensors:
            sensor.turn_on()
            light_intensity = sensor.get_reading()
            if light_intensity is not None:
                if light_intensity < LIGHT_INTENSITY_LOW:z
                    print(f"Light intensity in {room.name} is too low: {light_intensity} lux. Consider turning on the lights.")
                elif light_intensity > LIGHT_INTENSITY_HIGH:
                    print(f"Light intensity in {room.name} is too high: {light_intensity} lux. Consider closing the curtains.")

    # Example of actuating based on a condition
    for room in home:
        print(f"\n--- Checking actuators in {room.name} ---")
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_on()
            light.set_brightness_level("medium")

if __name__ == "__main__":
    main()