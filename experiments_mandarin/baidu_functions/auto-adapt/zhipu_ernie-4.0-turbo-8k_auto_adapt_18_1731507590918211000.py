# Based on your functional description and provided source code, I will create a `function.py` file that contains the main function to initialize the home plan, turn on the sensors, get readings, and perform some basic actions based on those readings. This `function.py` will be located in the `functions` folder.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, Heater, AC, Humidifier, Light
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home plan
    home = home_plan()

    # Turn on all sensors
    for room in home:
        for sensor in room.sensors:
            sensor.turn_on()
    
    # Wait for a while to get stable sensor readings
    time.sleep(2)
    
    # Get readings from all sensors and perform actions
    for room in home:
        print(f"\nChecking sensors in {room.name}...")
        for sensor in room.sensors:
            reading = sensor.get_reading()
            if reading is not None:
                handle_sensor_reading(sensor, reading, room)

def handle_sensor_reading(sensor, reading, room):
    if sensor.sensor_type == "IndoorTemperature":
        handle_temperature(sensor, reading, room)
    elif sensor.sensor_type == "Humidity":
        handle_humidity(sensor, reading, room)
    elif sensor.sensor_type == "LightIntensive":
        handle_light_intensity(sensor, reading, room)

def handle_temperature(sensor, reading, room):
    heaters = get_all_actuators(room.sensors + room.actuators, "Heater")
    acs = get_all_actuators(room.sensors + room.actuators, "AC")
    
    if reading < TEMP_LOW:
        for heater in heaters:
            heater.turn_on()
            heater.set_target_temperature(TEMP_LOW + 1)  # Set a slightly higher target than TEMP_LOW
    elif reading > TEMP_HIGH:
        for ac in acs:
            ac.turn_on()
            ac.set_target_temperature(TEMP_HIGH - 1)  # Set a slightly lower target than TEMP_HIGH
    else:
        for actuator in heaters + acs:
            actuator.turn_off()

def handle_humidity(sensor, reading, room):
    humidifiers = get_all_actuators(room.sensors + room.actuators, "Humidifier")
    
    if reading < HUMIDITY_LOW:
        for humidifier in humidifiers:
            humidifier.increase_humidity()
    elif reading > HUMIDITY_HIGH:
        for humidifier in humidifiers:
            humidifier.decrease_humidity()

def handle_light_intensity(sensor, reading, room):
    lights = get_all_actuators(room.sensors + room.actuators, "Light")
    
    if reading < LIGHT_INTENSITY_LOW:
        for light in lights:
            light.turn_on()
            light.set_brightness_level("high")
    elif reading > LIGHT_INTENSITY_HIGH:
        for light in lights:
            light.turn_off()
    else:
        # Set to medium brightness if within the acceptable range
        for light in lights:
            light.turn_on()
            light.set_brightness_level("medium")

# This is to ensure that the main function runs when this script is executed directly
if __name__ == "__main__":
    main()