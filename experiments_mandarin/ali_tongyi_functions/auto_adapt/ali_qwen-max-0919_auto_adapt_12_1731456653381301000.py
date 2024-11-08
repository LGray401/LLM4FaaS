# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to control the smart home system. The main function will read the sensor values, check if they meet the desired conditions (temperature 22°C, moderate humidity, and low light intensity), and then take appropriate actions using actuators.
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
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

            # Find specific sensors
            indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
            humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
            light_intensity_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)

            # Turn on sensors
            if indoor_temp_sensor:
                indoor_temp_sensor.turn_on()
            if humidity_sensor:
                humidity_sensor.turn_on()
            if light_intensity_sensor:
                light_intensity_sensor.turn_on()

            # Get readings
            temp_reading = indoor_temp_sensor.get_reading() if indoor_temp_sensor else None
            humidity_reading = humidity_sensor.get_reading() if humidity_sensor else None
            light_reading = light_intensity_sensor.get_reading() if light_intensity_sensor else None

            # Turn off sensors
            if indoor_temp_sensor:
                indoor_temp_sensor.turn_off()
            if humidity_sensor:
                humidity_sensor.turn_off()
            if light_intensity_sensor:
                light_intensity_sensor.turn_off()

            # Check and adjust temperature
            if temp_reading is not None:
                heater = next((a for a in actuators if isinstance(a, Heater)), None)
                ac = next((a for a in actuators if isinstance(a, AC)), None)

                if temp_reading < 22:
                    if heater:
                        heater.set_target_temperature(22)
                        heater.adjust_temperature(temp_reading)
                elif temp_reading > 22:
                    if ac:
                        ac.set_target_temperature(22)
                        ac.adjust_temperature(temp_reading)

            # Check and adjust humidity
            if humidity_reading is not None:
                humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)

                if humidity_reading < HUMIDITY_LOW:
                    if humidifier:
                        humidifier.increase_humidity()
                elif humidity_reading > HUMIDITY_HIGH:
                    if humidifier:
                        humidifier.decrease_humidity()

            # Check and adjust light intensity
            if light_reading is not None:
                lights = [a for a in actuators if isinstance(a, Light)]

                if light_reading < LIGHT_INTENSITY_LOW:
                    for light in lights:
                        light.turn_on()
                        light.set_brightness_level("high")
                elif light_reading > LIGHT_INTENSITY_HIGH:
                    for light in lights:
                        light.turn_off()

        # Wait for a while before the next iteration
        time.sleep(60)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()