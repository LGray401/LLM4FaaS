# Based on your functional description and the provided source code, I will create a `function.py` file that integrates the sensors and actuators to automatically adjust indoor temperature, humidity, and light intensity. The main function will orchestrate the operation of these components based on their readings.
# 
# Here's what the `function.py` file will look like:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def adjust_environment(home):
    for room in home:
        print(f"\nAdjusting environment for {room.name}...")
        
        # Get sensors and actuators in the room
        temperature_sensors = get_room_sensors(home, room.name)
        humidity_sensors = get_all_sensors(home, "Humidity")
        light_sensors = get_all_sensors(home, "LightIntensive")
        heaters = get_all_actuators(home, "Heater")
        acs = get_all_actuators(home, "AC")
        humidifiers = get_all_actuators(home, "Humidifier")
        lights = get_all_actuators(home, "Light")

        # Adjust temperature
        for temp_sensor in temperature_sensors:
            current_temp = temp_sensor.get_reading()
            if current_temp is not None:
                for heater in heaters:
                    heater.adjust_temperature(current_temp)
                for ac in acs:
                    ac.adjust_temperature(current_temp)

        # Adjust humidity
        for humidity_sensor in humidity_sensors:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                for humidifier in humidifiers:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif current_humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

        # Adjust light intensity
        for light_sensor in light_sensors:
            current_light = light_sensor.get_reading()
            if current_light is not None:
                for light in lights:
                    if current_light < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    elif current_light > LIGHT_INTENSITY_HIGH:
                        light.turn_off()

        time.sleep(1)  # Brief pause before checking again

def main():
    home = home_plan()
    print_home_plan(home)
    while True:
        adjust_environment(home)

if __name__ == "__main__":
    main()