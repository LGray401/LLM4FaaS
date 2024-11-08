# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to manage the smart home environment. This function will check the sensor readings and adjust the actuators accordingly to maintain comfortable conditions in the house.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, Heater, AC, Humidifier, Light
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home plan
    home = home_plan()
    
    while True:
        # Get all the sensors and actuators
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        humidity_sensors = get_all_sensors(home, "Humidity")
        light_sensors = get_all_sensors(home, "LightIntensive")
        
        heaters = get_all_actuators(home, "Heater")
        acs = get_all_actuators(home, "AC")
        humidifiers = get_all_actuators(home, "Humidifier")
        lights = get_all_actuators(home, "Light")
        
        # Check temperature sensors and adjust heaters/ACs
        for sensor in temperature_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading is not None:
                if reading < TEMP_LOW:
                    # Turn on heaters
                    for heater in heaters:
                        if heater.room_name == sensor.room_name:
                            heater.turn_on()
                            heater.set_target_temperature(TEMP_HIGH)
                            heater.adjust_temperature(reading)
                elif reading > TEMP_HIGH:
                    # Turn on ACs
                    for ac in acs:
                        if ac.room_name == sensor.room_name:
                            ac.turn_on()
                            ac.set_target_temperature(TEMP_LOW)
                            ac.adjust_temperature(reading)
                else:
                    # Turn off heaters and ACs
                    for heater in heaters:
                        if heater.room_name == sensor.room_name:
                            heater.turn_off()
                    for ac in acs:
                        if ac.room_name == sensor.room_name:
                            ac.turn_off()
            sensor.turn_off()
        
        # Check humidity sensors and adjust humidifiers
        for sensor in humidity_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading is not None:
                if reading < HUMIDITY_LOW:
                    # Turn on humidifiers
                    for humidifier in humidifiers:
                        if humidifier.room_name == sensor.room_name:
                            humidifier.turn_on()
                            humidifier.increase_humidity()
                elif reading > HUMIDITY_HIGH:
                    # Turn off humidifiers (or decrease humidity if applicable)
                    for humidifier in humidifiers:
                        if humidifier.room_name == sensor.room_name:
                            humidifier.turn_off()
                            # Assuming decrease_humidity() is implemented for de-humidification
                            humidifier.decrease_humidity()
                else:
                    # Turn off humidifiers
                    for humidifier in humidifiers:
                        if humidifier.room_name == sensor.room_name:
                            humidifier.turn_off()
            sensor.turn_off()
        
        # Check light sensors and adjust lights
        for sensor in light_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading is not None:
                if reading < LIGHT_INTENSITY_LOW:
                    # Turn on lights
                    for light in lights:
                        if light.room_name == sensor.room_name:
                            light.turn_on()
                            light.set_brightness_level("high")
                elif reading > LIGHT_INTENSITY_HIGH:
                    # Turn off lights
                    for light in lights:
                        if light.room_name == sensor.room_name:
                            light.turn_off()
                else:
                    # Adjust lights to medium brightness
                    for light in lights:
                        if light.room_name == sensor.room_name:
                            light.turn_on()
                            light.set_brightness_level("medium")
            sensor.turn_off()
        
        # Sleep for a while before checking again
        time.sleep(60)

if __name__ == "__main__":
    main()