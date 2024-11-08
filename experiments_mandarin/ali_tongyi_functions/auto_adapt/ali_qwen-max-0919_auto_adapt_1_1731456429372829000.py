# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control the temperature, humidity, and light intensity according to the specified requirements. The main function will:
# 
# 1. Set the temperature to 26°C.
# 2 .Set the humidity to 40%.
# 3. Set the light intensity to "medium".
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home plan
    home = home_plan()

    # Define the target values
    target_temperature = 26.0  # Celsius
    target_humidity = 40.0     # Percentage
    target_light_intensity = "medium"

    # Get all rooms in the home
    for room in home:
        print(f"Processing {room.name}...")

        # Get sensors and actuators for the current room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Find the relevant sensors and actuators
        indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
        humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
        light_intensive_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)

        heater = next((a for a in actuators if isinstance(a, Heater)), None)
        ac = next((a for a in actuators if isinstance(a, AC)), None)
        humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
        light = next((a for a in actuators if isinstance(a, Light)), None)

        # Turn on all relevant sensors
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_on()
        if humidity_sensor:
            humidity_sensor.turn_on()
        if light_intensive_sensor:
            light_intensive_sensor.turn_on()

        # Adjust temperature
        if indoor_temp_sensor and (heater or ac):
            current_temperature = indoor_temp_sensor.get_reading()
            if current_temperature is not None:
                if current_temperature < target_temperature:
                    if heater:
                        heater.set_target_temperature(target_temperature)
                        heater.adjust_temperature(current_temperature)
                elif current_temperature > target_temperature:
                    if ac:
                        ac.set_target_temperature(target_temperature)
                        ac.adjust_temperature(current_temperature)

        # Adjust humidity
        if humidity_sensor and humidifier:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < target_humidity:
                    humidifier.increase_humidity()
                elif current_humidity > target_humidity:
                    humidifier.decrease_humidity()

        # Adjust light intensity
        if light:
            light.set_brightness_level(target_light_intensity)

        # Turn off all relevant sensors
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_off()
        if humidity_sensor:
            humidity_sensor.turn_off()
        if light_intensive_sensor:
            light_intensive_sensor.turn_off()

if __name__ == "__main__":
    main()