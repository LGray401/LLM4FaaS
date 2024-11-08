# Based on the provided functional description and source code, we can create a `function.py` file that contains the main functions for executing different home plans such as MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. Below is the implementation of the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, Heater, AC, Light
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def morning_plan(home):
    # Wake up the user by turning on the lights and adjusting the temperature
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        # Turn on the lights
        for actuator in bedroom.actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_on()
                actuator.set_brightness_level("medium")
        
        # Adjust the temperature
        for actuator in bedroom.actuators:
            if actuator.actuator_type == "Heater":
                # Assuming a comfortable morning temperature is around 20°C
                actuator.set_target_temperature(20)
                actuator.adjust_temperature(get_temperature_of_room(bedroom))
            elif actuator.actuator_type == "AC":
                # If it's too hot, turn on the AC
                actuator.set_target_temperature(20)
                actuator.adjust_temperature(get_temperature_of_room(bedroom))

def leave_home_plan(home):
    # Turn off all unnecessary devices and lock the doors
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type in ["Light", "Heater", "AC", "MusicPlayer", "SmartTV"]:
                actuator.turn_off()
            elif actuator.actuator_type == "Door":
                actuator.lock()

def movie_plan(home):
    # Set up the living room for a movie night
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Dim the lights
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_on()
                actuator.set_brightness_level("low")
        
        # Turn on the TV
        for actuator in living_room.actuators:
            if actuator.actuator_type == "SmartTV":
                actuator.turn_on()
                actuator.play_channel("Movie Channel")
        
        # Adjust the temperature
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Heater":
                # Assuming a comfortable movie temperature is around 22°C
                actuator.set_target_temperature(22)
                actuator.adjust_temperature(get_temperature_of_room(living_room))
            elif actuator.actuator_type == "AC":
                # If it's too hot, turn on the AC
                actuator.set_target_temperature(22)
                actuator.adjust_temperature(get_temperature_of_room(living_room))

def get_temperature_of_room(room):
    # Retrieve the temperature from the IndoorTemperatureSensor
    for sensor in room.sensors:
        if sensor.sensor_type == "IndoorTemperature":
            return sensor.get_reading()
    return None

def get_humidity_of_room(room):
    # Retrieve the humidity from the HumiditySensor
    for sensor in room.sensors:
        if sensor.sensor_type == "Humidity":
            return sensor.get_reading()
    return None

def get_light_intensity_of_room(room):
    # Retrieve the light intensity from the LightIntensiveSensor
    for sensor in room.sensors:
        if sensor.sensor_type == "LightIntensive":
            return sensor.get_reading()
    return None

if __name__ == "__main__":
    # Test the functions with the home plan
    home = home_plan()
    
    # Execute different plans
    morning_plan(home)
    # leave_home_plan(home)
    # movie_plan(home)