# Based on your functional description and the provided source code, I will create a `function.py` file that implements the desired functionality for maintaining the indoor temperature at 26°C, humidity at 60%, and adjusting light intensity based on your activities.
# 
# Here's the `function.py` file:
# 
# ### function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light
from home.logger_config import logger
import time

def maintain_environment(home):
    # Get all sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    lights = get_all_actuators(home, "Light")

    # Assuming we only have one sensor of each type for simplicity
    temperature_sensor = temperature_sensors[0] if temperature_sensors else None
    humidity_sensor = humidity_sensors[0] if humidity_sensors else None

    # Maintain temperature
    if temperature_sensor:
        current_temperature = temperature_sensor.get_reading()
        if current_temperature is not None:
            if current_temperature < 26:
                heater = get_all_actuators(home, "Heater")[0]
                heater.set_target_temperature(26)
                heater.adjust_temperature(current_temperature)
            elif current_temperature > 26:
                ac = get_all_actuators(home, "AC")[0]
                ac.set_target_temperature(26)
                ac.adjust_temperature(current_temperature)

    # Maintain humidity
    if humidity_sensor:
        current_humidity = humidity_sensor.get_reading()
        if current_humidity is not None:
            if current_humidity < 60:
                humidifier = get_all_actuators(home, "Humidifier")[0]
                humidifier.increase_humidity()
            elif current_humidity > 60:
                humidifier = get_all_actuators(home, "Humidifier")[0]
                humidifier.decrease_humidity()

    # Adjust light intensity based on activity
    for light in lights:
        # Here you can implement your logic to determine the activity
        if is_working_time():
            light.set_brightness_level("high")
        elif is_relaxing_time():
            light.set_brightness_level("low")
        elif is_rest_time():
            light.turn_off()

def is_working_time():
    # Placeholder for logic to determine if it's working time
    return True  # Replace with actual condition

def is_relaxing_time():
    # Placeholder for logic to determine if it's relaxing time
    return False  # Replace with actual condition

def is_rest_time():
    # Placeholder for logic to determine if it's rest time
    return False  # Replace with actual condition

def main():
    home = home_plan()
    while True:
        maintain_environment(home)
        time.sleep(10)  # Adjust the frequency of checks as needed

if __name__ == "__main__":
    main()