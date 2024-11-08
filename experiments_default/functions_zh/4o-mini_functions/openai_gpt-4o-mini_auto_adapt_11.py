# Based on your functional description, I'll create a `function.py` file that contains the main function to monitor the sensors for temperature, humidity, and light intensity, and automatically turn on the AC when any of the specified conditions are met.
# 
# Here is the `function.py` file:

# functions/function.py
import time
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
from home.actuator import AC

def monitor_home_conditions():
    home = home_plan()

    while True:
        for room in home:
            # Get all the sensors in the room
            temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
            humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
            light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]

            # Check temperature sensors
            for sensor in temperature_sensors:
                sensor.turn_on()
                temperature = sensor.get_reading()
                if temperature is not None and temperature > TEMP_HIGH:
                    ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
                    if ac:
                        ac.turn_on()

            # Check humidity sensors
            for sensor in humidity_sensors:
                sensor.turn_on()
                humidity = sensor.get_reading()
                if humidity is not None and humidity > HUMIDITY_LOW:
                    ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
                    if ac:
                        ac.turn_on()

            # Check light intensity sensors
            for sensor in light_sensors:
                sensor.turn_on()
                light_intensity = sensor.get_reading()
                if light_intensity is not None and light_intensity > LIGHT_INTENSITY_LOW:
                    ac = next((actuator for actuator in room.actuators if isinstance(actuator, AC)), None)
                    if ac:
                        ac.turn_on()

            # Add some delay before the next reading to avoid rapid checks
            time.sleep(5)

if __name__ == "__main__":
    monitor_home_conditions()