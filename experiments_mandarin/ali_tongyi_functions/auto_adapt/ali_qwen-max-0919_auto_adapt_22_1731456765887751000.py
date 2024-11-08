# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to control the smart home system. The `main` function will handle the temperature, humidity, and light intensity conditions as described.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Humidifier, Light, Curtain
import time

def control_temperature(home):
    # Get all indoor temperature sensors
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    
    # Check if any room's temperature is above 26 degrees
    for sensor in temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp > 26:
            # Turn on all ACs and close all windows
            for room in home:
                for actuator in room.actuators:
                    if isinstance(actuator, AC):
                        actuator.set_target_temperature(26)
                        actuator.adjust_temperature(current_temp)
                    elif isinstance(actuator, Window):
                        actuator.turn_off()
            break

def control_humidity(home):
    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")
    
    # Check if any room's humidity is below 30%
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity < HUMIDITY_LOW:
            # Turn on all humidifiers
            for room in home:
                for actuator in room.actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.increase_humidity()
            break

def control_light_intensity(home):
    # Get all light intensity sensors
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    # Check if any room's light intensity is below 150 lux or above 11080 lux
    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            # Brighten all lights
            for room in home:
                for actuator in room.actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_on()
                        actuator.set_brightness_level("high")
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            # Close all curtains and turn on all lights
            for room in home:
                for actuator in room.actuators:
                    if isinstance(actuator, Curtain):
                        actuator.turn_off()
                    elif isinstance(actuator, Light):
                        actuator.turn_on()
                        actuator.set_brightness_level("medium")

def main():
    home = home_plan()
    
    while True:
        control_temperature(home)
        control_humidity(home)
        control_light_intensity(home)
        
        # Sleep for a while before the next check
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()