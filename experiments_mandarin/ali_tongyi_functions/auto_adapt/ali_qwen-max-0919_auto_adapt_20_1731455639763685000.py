# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control the smart home system. This function will handle the following:
# 
# 1. **Temperature Control**: If the indoor temperature exceeds 26°C, the AC will automatically turn on.
# 2. **Humidity Control**: Automatically adjust the humidity level.
# 3. **Light Intensity Control**: Automatically adjust the light intensity.
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def control_smart_home():
    # Initialize the home plan
    home = home_plan()

    while True:
        # Iterate over each room in the home
        for room in home:
            # Get sensors and actuators for the current room
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            # Find specific sensors and actuators
            indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
            humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
            light_intensity_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)

            ac = next((a for a in actuators if isinstance(a, AC)), None)
            humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
            lights = [a for a in actuators if isinstance(a, Light)]

            # Temperature Control
            if indoor_temp_sensor and ac:
                indoor_temp_sensor.turn_on()
                temp_reading = indoor_temp_sensor.get_reading()
                if temp_reading and temp_reading > TEMP_HIGH:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(temp_reading)
                else:
                    ac.turn_off()
                indoor_temp_sensor.turn_off()

            # Humidity Control
            if humidity_sensor and humidifier:
                humidity_sensor.turn_on()
                humidity_reading = humidity_sensor.get_reading()
                if humidity_reading:
                    if humidity_reading < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif humidity_reading > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()
                humidity_sensor.turn_off()

            # Light Intensity Control
            if light_intensity_sensor and lights:
                light_intensity_sensor.turn_on()
                light_reading = light_intensity_sensor.get_reading()
                if light_reading:
                    if light_reading < LIGHT_INTENSITY_LOW:
                        for light in lights:
                            light.set_brightness_level("high")
                    elif light_reading > LIGHT_INTENSITY_HIGH:
                        for light in lights:
                            light.set_brightness_level("low")
                    else:
                        for light in lights:
                            light.set_brightness_level("medium")
                light_intensity_sensor.turn_off()

        # Wait for a short period before the next iteration
        time.sleep(5)

if __name__ == "__main__":
    control_smart_home()