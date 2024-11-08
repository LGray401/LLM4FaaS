# Based on the provided functional description and source code, we can create a `function.py` file that contains the main function to orchestrate the smart home operations. This main function might initialize the rooms, turn on sensors, get readings, and adjust actuators based on those readings. Here's a simple implementation of the `function.py` file:

# function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
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
    
    # Main loop to get sensor readings and adjust actuators accordingly
    try:
        while True:
            for room in home:
                # Get temperature sensors and adjust heaters/ACs
                indoor_temps = get_all_sensors(home, "IndoorTemperature")
                outdoor_temps = get_all_sensors(home, "OutdoorTemperature")
                
                for temp_sensor in indoor_temps:
                    adjust_temperature_based_on_sensor(temp_sensor, room)
                
                # Get humidity sensors and adjust humidifiers
                humidity_sensors = get_all_sensors(home, "Humidity")
                
                for humidity_sensor in humidity_sensors:
                    adjust_humidity_based_on_sensor(humidity_sensor, room)
                
                # Get light intensity sensors and adjust lights
                light_sensors = get_all_sensors(home, "LightIntensive")
                
                for light_sensor in light_sensors:
                    adjust_light_based_on_sensor(light_sensor, room)
            
            # Sleep for a while before the next round of adjustments
            time.sleep(10)
    except KeyboardInterrupt:
        print("Main loop interrupted. Exiting...")
    finally:
        # Turn off all sensors
        for room in home:
            for sensor in room.sensors:
                sensor.turn_off()

def adjust_temperature_based_on_sensor(sensor: Sensor, room):
    if sensor.status == "on":
        reading = sensor.get_reading()
        if reading is not None:
            heaters = get_all_actuators(room.actuators, "Heater")
            acs = get_all_actuators(room.actuators, "AC")
            
            for heater in heaters:
                if reading < TEMP_LOW:
                    heater.turn_on()
                else:
                    heater.turn_off()
            
            for ac in acs:
                if reading > TEMP_HIGH:
                    ac.turn_on()
                else:
                    ac.turn_off()

def adjust_humidity_based_on_sensor(sensor: Sensor, room):
    if sensor.status == "on":
        reading = sensor.get_reading()
        if reading is not None:
            humidifiers = get_all_actuators(room.actuators, "Humidifier")
            
            for humidifier in humidifiers:
                if reading < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif reading > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()

def adjust_light_based_on_sensor(sensor: Sensor, room):
    if sensor.status == "on":
        reading = sensor.get_reading()
        if reading is not None:
            lights = get_all_actuators(room.actuators, "Light")
            
            for light in lights:
                if reading < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                    light.set_brightness_level("high")
                elif reading > LIGHT_INTENSITY_HIGH:
                    light.turn_off()
                else:
                    light.set_brightness_level("medium")

# Helper function to get actuators of a specific type from a room
def get_all_actuators(actuators, actuator_type):
    return [actuator for actuator in actuators if actuator.actuator_type == actuator_type]

if __name__ == "__main__":
    main()