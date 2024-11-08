# Based on your provided functional description and source code, I will create a `function.py` file that includes the main function to automatically regulate the indoor temperature, humidity, and light intensity. This file will be placed in the `functions` folder as per your request.
# 
# ### `function.py`

import time
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()
    
    while True:
        for room in home:
            # Get sensors and actuators for the current room
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)
            
            # Initialize variables to store sensor readings
            temp_reading = None
            humidity_reading = None
            light_reading = None
            
            # Get sensor readings
            for sensor in sensors:
                if isinstance(sensor, IndoorTemperatureSensor):
                    sensor.turn_on()
                    temp_reading = sensor.get_reading()
                    sensor.turn_off()
                elif isinstance(sensor, HumiditySensor):
                    sensor.turn_on()
                    humidity_reading = sensor.get_reading()
                    sensor.turn_off()
                elif isinstance(sensor, LightIntensiveSensor):
                    sensor.turn_on()
                    light_reading = sensor.get_reading()
                    sensor.turn_off()
            
            # Adjust temperature
            for actuator in actuators:
                if isinstance(actuator, Heater) or isinstance(actuator, AC):
                    if temp_reading is not None:
                        if temp_reading < TEMP_LOW and isinstance(actuator, Heater):
                            actuator.set_target_temperature(TEMP_HIGH)
                            actuator.adjust_temperature(temp_reading)
                        elif temp_reading > TEMP_HIGH and isinstance(actuator, AC):
                            actuator.set_target_temperature(TEMP_LOW)
                            actuator.adjust_temperature(temp_reading)
                        else:
                            actuator.turn_off()
            
            # Adjust humidity
            for actuator in actuators:
                if isinstance(actuator, Humidifier):
                    if humidity_reading is not None:
                        if humidity_reading < HUMIDITY_LOW:
                            actuator.increase_humidity()
                        elif humidity_reading > HUMIDITY_HIGH:
                            actuator.decrease_humidity()
                        else:
                            actuator.turn_off()
            
            # Adjust light intensity
            for actuator in actuators:
                if isinstance(actuator, Light):
                    if light_reading is not None:
                        if light_reading < LIGHT_INTENSITY_LOW:
                            actuator.turn_on()
                            actuator.set_brightness_level("high")
                        elif light_reading > LIGHT_INTENSITY_HIGH:
                            actuator.turn_off()
                        else:
                            actuator.set_brightness_level("medium")
        
        # Wait for a short period before the next iteration
        time.sleep(60)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()