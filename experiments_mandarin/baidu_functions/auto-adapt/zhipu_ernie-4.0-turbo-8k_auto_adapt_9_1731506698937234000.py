# Based on your functional description and the provided source code, I will now provide a `function.py` file that contains the main function to initialize and manage your smart home system. This file will be located in the `functions` folder and will utilize the classes and methods defined in the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home plan
    home = home_plan()
    print_home_plan(home)
    
    # Example of turning on all lights in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_on()
    
    # Example of getting temperature readings from all IndoorTemperatureSensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in temperature_sensors:
        sensor.turn_on()
        temp_reading = sensor.get_reading()
        if temp_reading is not None:
            # Perform actions based on temperature readings (e.g., adjust heaters or ACs)
            adjust_hvac(home, sensor.room_name, temp_reading)
        sensor.turn_off()
    
    # Example of getting humidity readings from all HumiditySensors
    humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity_reading = sensor.get_reading()
        if humidity_reading is not None:
            # Perform actions based on humidity readings (e.g., adjust humidifiers)
            adjust_humidifier(home, sensor.room_name, humidity_reading)
        sensor.turn_off()
    
    # Example of getting light intensity readings from all LightIntensiveSensors
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        sensor.turn_on()
        light_reading = sensor.get_reading()
        if light_reading is not None:
            # Perform actions based on light intensity readings (e.g., adjust curtains or lights)
            adjust_lighting(home, sensor.room_name, light_reading)
        sensor.turn_off()

def adjust_hvac(home, room_name, temperature):
    room = get_room(home, room_name)
    if room:
        for actuator in room.actuators:
            if actuator.actuator_type == "Heater" and temperature < TEMP_LOW:
                actuator.turn_on()
            elif actuator.actuator_type == "Heater" and temperature >= TEMP_LOW:
                actuator.turn_off()
            elif actuator.actuator_type == "AC" and temperature > TEMP_HIGH:
                actuator.turn_on()
            elif actuator.actuator_type == "AC" and temperature <= TEMP_HIGH:
                actuator.turn_off()

def adjust_humidifier(home, room_name, humidity):
    room = get_room(home, room_name)
    if room:
        for actuator in room.actuators:
            if actuator.actuator_type == "Humidifier":
                if humidity < HUMIDITY_LOW:
                    actuator.increase_humidity()
                elif humidity > HUMIDITY_HIGH:
                    actuator.decrease_humidity()

def adjust_lighting(home, room_name, light_intensity):
    room = get_room(home, room_name)
    if room:
        for actuator in room.actuators:
            if actuator.actuator_type == "Light" and light_intensity < LIGHT_INTENSITY_LOW:
                actuator.turn_on()
                actuator.set_brightness_level("high")  # or appropriate level based on need
            elif actuator.actuator_type == "Light" and light_intensity > LIGHT_INTENSITY_HIGH:
                actuator.turn_off()
            elif actuator.actuator_type == "Curtain" and light_intensity > LIGHT_INTENSITY_HIGH:
                actuator.turn_on()  # Assume turning on closes the curtains
            # Add more logic for adjusting curtains based on light intensity if needed

if __name__ == "__main__":
    main()