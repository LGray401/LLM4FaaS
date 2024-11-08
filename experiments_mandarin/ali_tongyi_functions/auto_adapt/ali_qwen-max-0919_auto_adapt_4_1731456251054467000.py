# Based on your provided functional description and source code, I will create a `function.py` file that contains the main function. This main function will initialize the home plan, set up sensors and actuators, and then control the environment based on the given temperature, humidity, and light intensity values (20°C, 50%, and 15 lux respectively).
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Define the target values
    target_temperature = 20  # Celsius
    target_humidity = 50     # Percentage
    target_light_intensity = 15  # Lux

    # Control the environment in each room
    for room in home:
        # Get the sensors and actuators for the current room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Find the relevant sensors and actuators
        indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
        humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
        light_intensity_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)

        heater = next((a for a in actuators if isinstance(a, Heater)), None)
        ac = next((a for a in actuators if isinstance(a, AC)), None)
        humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
        light = next((a for a in actuators if isinstance(a, Light)), None)

        # Turn on all sensors
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_on()
        if humidity_sensor:
            humidity_sensor.turn_on()
        if light_intensity_sensor:
            light_intensity_sensor.turn_on()

        # Control the temperature
        if indoor_temp_sensor and (heater or ac):
            current_temperature = indoor_temp_sensor.get_reading()
            if current_temperature < target_temperature:
                if heater:
                    heater.set_target_temperature(target_temperature)
                    heater.adjust_temperature(current_temperature)
            elif current_temperature > target_temperature:
                if ac:
                    ac.set_target_temperature(target_temperature)
                    ac.adjust_temperature(current_temperature)

        # Control the humidity
        if humidity_sensor and humidifier:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity < target_humidity:
                humidifier.increase_humidity()
            elif current_humidity > target_humidity:
                humidifier.decrease_humidity()

        # Control the light intensity
        if light_intensity_sensor and light:
            current_light_intensity = light_intensity_sensor.get_reading()
            if current_light_intensity < target_light_intensity:
                light.set_brightness_level("high")
            elif current_light_intensity > target_light_intensity:
                light.set_brightness_level("low")

        # Turn off all sensors
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_off()
        if humidity_sensor:
            humidity_sensor.turn_off()
        if light_intensity_sensor:
            light_intensity_sensor.turn_off()

        # Wait for a short duration to allow the changes to take effect
        time.sleep(1)

if __name__ == "__main__":
    main()