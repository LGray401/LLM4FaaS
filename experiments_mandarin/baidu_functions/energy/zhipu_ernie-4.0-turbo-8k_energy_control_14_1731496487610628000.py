# Based on your functional description and the provided source code, I will create a `function.py` file that contains a main function to initiate the "Earth Eco-Friendly Plan" for your smart home. This main function will demonstrate how you can utilize the sensors and actuators defined in your other modules to achieve an eco-friendly environment.
# 
# Here's a possible implementation of the `function.py` file:

# function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators, print_home_plan
from home.sensor import Sensor
from home.actuator import Actuator, Heater, AC, Light
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def earth_eco_friendly_plan():
    # Initialize the home plan
    home = home_plan()
    print_home_plan(home)
    
    # Get all relevant sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    lights = get_all_actuators(home, "Light")
    
    # Turn on all sensors
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()
    
    # Monitor and adjust temperature
    for sensor in temperature_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            adjust_temperature_in_room(sensor.room_name, reading, heaters, acs)
    
    # Monitor and adjust humidity
    for sensor in humidity_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            adjust_humidity_in_room(sensor.room_name, reading, heaters, acs) # Assuming heaters and ACs can also affect humidity
    
    # Monitor and adjust light intensity
    for sensor in light_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            adjust_lights_in_room(sensor.room_name, reading, lights)
    
    # Turn off sensors to save energy
    for sensor in temperature_sensors + humidity_sensors + light_sensors:
        sensor.turn_off()

def adjust_temperature_in_room(room_name, temperature, heaters, acs):
    # Find the corresponding heater and AC for the room
    room_heater = next((heater for heater in heaters if heater.room_name == room_name), None)
    room_ac = next((ac for ac in acs if ac.room_name == room_name), None)
    
    if room_heater and room_ac:
        if temperature < TEMP_LOW:
            room_heater.turn_on()
            room_ac.turn_off()
        elif temperature > TEMP_HIGH:
            room_heater.turn_off()
            room_ac.turn_on()
        else:
            room_heater.turn_off()
            room_ac.turn_off()

def adjust_humidity_in_room(room_name, humidity, heaters, acs):
    # For simplicity, assume heaters increase humidity and ACs decrease it
    room_heater = next((heater for heater in heaters if heater.room_name == room_name), None)
    room_ac = next((ac for ac in acs if ac.room_name == room_name), None)
    
    if room_heater and room_ac:
        if humidity < HUMIDITY_LOW:
            room_heater.turn_on()  # Increase humidity
            room_ac.turn_off()
        elif humidity > HUMIDITY_HIGH:
            room_heater.turn_off()
            room_ac.turn_on()  # Decrease humidity
        else:
            room_heater.turn_off()
            room_ac.turn_off()

def adjust_lights_in_room(room_name, light_intensity, lights):
    room_lights = [light for light in lights if light.room_name == room_name]
    
    if room_lights:
        if light_intensity < LIGHT_INTENSITY_LOW:
            # Turn on lights if it's too dark
            for light in room_lights:
                light.turn_on()
                light.set_brightness_level("high")  # Or appropriate level based on need
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            # Turn off lights if it's too bright
            for light in room_lights:
                light.turn_off()
        else:
            # Optionally, adjust lights to a medium setting or leave as is
            for light in room_lights:
                light.set_brightness_level("medium")

if __name__ == "__main__":
    earth_eco_friendly_plan()