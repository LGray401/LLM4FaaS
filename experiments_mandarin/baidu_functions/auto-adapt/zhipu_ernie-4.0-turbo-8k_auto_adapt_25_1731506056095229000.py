# Based on the provided functional description and source code, here is the `function.py` file that you can use in your smart home project. This file contains the main function that implements the logic for temperature, humidity, and light intensity control.

# function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, AC, Curtain, Humidifier
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Get all relevant sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    acs = get_all_actuators(home, "AC")
    curtains = get_all_actuators(home, "Curtain")
    humidifiers = get_all_actuators(home, "Humidifier")
    
    # Turn on all sensors
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()
    
    # Check temperature and control AC
    for sensor in temperature_sensors:
        reading = sensor.get_reading()
        if reading is not None and reading >= TEMP_HIGH:
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.turn_on()  # Turn on AC to cool down
                    break
    
    # Check humidity and control humidifier
    for sensor in humidity_sensors:
        reading = sensor.get_reading()
        if reading is not None and reading <= HUMIDITY_LOW:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    humidifier.increase_humidity()  # Turn on humidifier to increase humidity
                    break
    
    # Check light intensity and control curtains
    for sensor in light_sensors:
        reading = sensor.get_reading()
        if reading is not None and reading >= LIGHT_INTENSITY_HIGH:
            for curtain in curtains:
                if curtain.room_name == sensor.room_name:
                    curtain.turn_on()  # Close curtains to reduce light intensity
                    break
    
    # Turn off sensors to save energy
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()