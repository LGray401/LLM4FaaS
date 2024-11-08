# Based on your functional description and the provided source code, I will now provide a `function.py` file that contains the main function for your smart home project. This main function will initialize the home plan, turn on all sensors, get readings, and adjust actuators based on the sensor readings.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, Heater, AC, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Turn on all sensors
    for room in home:
        for sensor in room.sensors:
            sensor.turn_on()
    
    # Main loop to get sensor readings and adjust actuators accordingly
    try:
        while True:
            # Get readings from all sensors
            for room in home:
                for sensor in room.sensors:
                    reading = sensor.get_reading()
                    
                    # Adjust actuators based on sensor readings
                    if sensor.sensor_type == "IndoorTemperature":
                        adjust_temperature_actuators(room, reading)
                    elif sensor.sensor_type == "Humidity":
                        adjust_humidity_actuators(room, reading)
                    elif sensor.sensor_type == "LightIntensive":
                        adjust_light_actuators(room, reading)
            
            # Sleep for a while before getting the next readings
            time.sleep(1)  # Adjust the sleep duration as needed
    
    except KeyboardInterrupt:
        print("Main loop interrupted. Exiting...")
    
    finally:
        # Turn off all sensors
        for room in home:
            for sensor in room.sensors:
                sensor.turn_off()

def adjust_temperature_actuators(room, current_temperature):
    heaters = get_all_actuators_in_room(room, "Heater")
    acs = get_all_actuators_in_room(room, "AC")
    
    for heater in heaters:
        if heater.target_temperature is not None:
            heater.adjust_temperature(current_temperature)
    
    for ac in acs:
        if ac.target_temperature is not None:
            ac.adjust_temperature(current_temperature)

def adjust_humidity_actuators(room, current_humidity):
    humidifiers = get_all_actuators_in_room(room, "Humidifier")
    
    for humidifier in humidifiers:
        if current_humidity < HUMIDITY_LOW:
            humidifier.increase_humidity()
        elif current_humidity > HUMIDITY_HIGH:
            humidifier.decrease_humidity()

def adjust_light_actuators(room, current_light_intensity):
    lights = get_all_actuators_in_room(room, "Light")
    
    for light in lights:
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            light.turn_on()
            light.set_brightness_level("high")
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            light.turn_off()
        # Optionally, adjust brightness level if within a certain range

def get_all_actuators_in_room(room, actuator_type):
    return [actuator for actuator in room.actuators if actuator.actuator_type == actuator_type]

if __name__ == "__main__":
    main()