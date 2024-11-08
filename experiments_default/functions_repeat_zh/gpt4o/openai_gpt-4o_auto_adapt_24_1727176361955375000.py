# Based on the provided functional description and the source code files, we can create the `function.py` file. This file will be located in the 'functions' folder and will include the main function to maintain the desired environmental conditions.
# 
# Here's the `function.py` file:

import time
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()
    
    while True:
        for room in home:
            print(f"Checking conditions in {room.name}...")
            
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)
            
            temperature_sensors = [sensor for sensor in sensors if sensor.sensor_type == "IndoorTemperature"]
            humidity_sensors = [sensor for sensor in sensors if sensor.sensor_type == "Humidity"]
            light_sensors = [sensor for sensor in sensors if sensor.sensor_type == "LightIntensive"]
            
            acs = [actuator for actuator in actuators if actuator.actuator_type == "AC"]
            humidifiers = [actuator for actuator in actuators if actuator.actuator_type == "Humidifier"]
            lights = [actuator for actuator in actuators if actuator.actuator_type == "Light"]
            curtains = [actuator for actuator in actuators if actuator.actuator_type == "Curtain"]
            
            # Maintain temperature
            for sensor in temperature_sensors:
                sensor.turn_on()
                current_temp = sensor.get_reading()
                if current_temp is not None and current_temp > TEMP_HIGH:
                    for ac in acs:
                        ac.turn_on()
                        ac.set_target_temperature(TEMP_HIGH)
            
            # Maintain humidity
            for sensor in humidity_sensors:
                sensor.turn_on()
                current_humidity = sensor.get_reading()
                if current_humidity is not None and current_humidity > HUMIDITY_HIGH:
                    for humidifier in humidifiers:
                        humidifier.turn_on()
                        humidifier.decrease_humidity()
            
            # Maintain light intensity
            for sensor in light_sensors:
                sensor.turn_on()
                current_light = sensor.get_reading()
                if current_light is not None:
                    if current_light < LIGHT_INTENSITY_LOW:
                        for light in lights:
                            light.turn_on()
                            light.set_brightness_level("high")
                    elif current_light > LIGHT_INTENSITY_HIGH:
                        for curtain in curtains:
                            curtain.turn_on()
        
        time.sleep(10)  # Check the conditions every 10 seconds

if __name__ == "__main__":
    main()