# Based on the functional description you've provided and the existing code structure, here is a proposed `function.py` file that integrates the functionality of turning on the air conditioner based on the readings from the sensors. The code assumes that the main functionality will be invoked in the `main` function.
# 
# ### `function.py`

import time
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import AC

def monitor_environment(home):
    for room in home:
        # Get the sensors in the room
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]

        # Check temperature
        for sensor in temperature_sensors:
            sensor.turn_on()
            current_temp = sensor.get_reading()
            if current_temp is not None:
                if current_temp > 26:
                    ac = get_ac_in_room(room)
                    if ac:
                        ac.turn_on()
                time.sleep(1)  # Simulating time delay for next sensor reading

        # Check humidity
        for sensor in humidity_sensors:
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            if current_humidity is not None and current_temp > 10:
                ac = get_ac_in_room(room)
                if ac:
                    ac.turn_on()
            time.sleep(1)

        # Check light intensity
        for sensor in light_sensors:
            sensor.turn_on()
            current_light = sensor.get_reading()
            if current_light is not None and current_light > 20:
                ac = get_ac_in_room(room)
                if ac:
                    ac.turn_on()
            time.sleep(1)

def get_ac_in_room(room):
    for actuator in room.actuators:
        if isinstance(actuator, AC):
            return actuator
    return None

def main():
    home = home_plan()
    monitor_environment(home)

if __name__ == "__main__":
    main()