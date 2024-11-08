# Based on your functional description and the provided source code, here is the `function.py` file that you can use in your smart home project. This file contains the main function that integrates the sensors and actuators according to the specified logic.

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Get all the necessary sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    acs = get_all_actuators(home, "AC")
    windows = get_all_actuators(home, "Window")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")
    
    # Turn on all sensors
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()
    
    # Read sensor data and control actuators accordingly
    for sensor in temperature_sensors:
        reading = sensor.get_reading()
        if reading > TEMP_HIGH:
            # Turn on ACs and turn off windows
            for ac in acs:
                ac.turn_on()
            for window in windows:
                window.turn_off()
    
    for sensor in humidity_sensors:
        reading = sensor.get_reading()
        if reading < HUMIDITY_LOW:
            # Turn on humidifiers
            for humidifier in humidifiers:
                humidifier.increase_humidity()
    
    for sensor in light_sensors:
        reading = sensor.get_reading()
        if reading < LIGHT_INTENSITY_LOW:
            # Turn on lights and set to high brightness
            for light in lights:
                light.turn_on()
                light.set_brightness_level("high")
        elif reading > LIGHT_INTENSITY_HIGH:
            # Close curtains and turn on indoor lights
            for curtain in curtains:
                curtain.turn_on()  # Assuming turn_on means close for curtains
            for light in lights:
                light.turn_on()
                light.set_brightness_level("high")
    
    # Turn off sensors to save energy
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()