# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to control your smart home system. This function will initialize the rooms, read sensor data, and adjust actuators based on the current conditions.
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators, print_home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()
    print_home_plan(home)

    while True:
        # Iterate through each room in the home
        for room in home:
            room_name = room.name
            sensors = get_room_sensors(home, room_name)
            actuators = get_room_actuators(home, room_name)

            # Get sensor readings
            indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
            humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
            light_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)

            if indoor_temp_sensor:
                indoor_temp_sensor.turn_on()
                current_temp = indoor_temp_sensor.get_reading()
                indoor_temp_sensor.turn_off()

            if humidity_sensor:
                humidity_sensor.turn_on()
                current_humidity = humidity_sensor.get_reading()
                humidity_sensor.turn_off()

            if light_sensor:
                light_sensor.turn_on()
                current_light = light_sensor.get_reading()
                light_sensor.turn_off()

            # Adjust actuators based on sensor readings
            if current_temp is not None:
                heater = next((a for a in actuators if isinstance(a, Heater)), None)
                ac = next((a for a in actuators if isinstance(a, AC)), None)

                if current_temp < TEMP_LOW and heater:
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(current_temp)
                elif current_temp > TEMP_HIGH and ac:
                    ac.set_target_temperature(TEMP_LOW)
                    ac.adjust_temperature(current_temp)

            if current_humidity is not None:
                humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)

                if current_humidity < HUMIDITY_LOW and humidifier:
                    humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH and humidifier:
                    humidifier.decrease_humidity()

            if current_light is not None:
                light = next((a for a in actuators if isinstance(a, Light)), None)

                if current_light < LIGHT_INTENSITY_LOW and light:
                    light.turn_on()
                    light.set_brightness_level("high")
                elif current_light > LIGHT_INTENSITY_HIGH and light:
                    light.turn_off()

        # Wait for a short period before the next iteration
        time.sleep(60)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()