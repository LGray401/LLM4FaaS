# Based on your provided functional description and code files, I will now create a `function.py` file that contains the main function to interact with your smart home system. This main function will initialize the home plan, turn on the required sensors, get readings, and perform some basic actions based on the sensor readings.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Turn on all sensors
    for room in home:
        for sensor in room.sensors:
            sensor.turn_on()
    
    # Wait for a while to get stable sensor readings
    time.sleep(2)
    
    # Get readings from all sensors and perform actions
    for room in home:
        print(f"\nChecking sensors in {room.name}:")
        for sensor in room.sensors:
            reading = sensor.get_reading()
            if reading is not None:
                handle_sensor_reading(sensor, reading)
    
    # Example: Turn on all lights in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_on()
                actuator.set_brightness_level("medium")

def handle_sensor_reading(sensor: Sensor, reading: float):
    if sensor.sensor_type == "IndoorTemperature":
        handle_temperature_reading(sensor, reading)
    elif sensor.sensor_type == "Humidity":
        handle_humidity_reading(sensor, reading)
    elif sensor.sensor_type == "LightIntensive":
        handle_light_intensity_reading(sensor, reading)
    # Add more sensor types and their handling logic here if needed

def handle_temperature_reading(sensor: Sensor, reading: float):
    room_name = sensor.room_name
    if reading < TEMP_LOW:
        print(f"Temperature in {room_name} is too low: {reading}°C. Turning on the heater.")
        turn_on_heater(room_name)
    elif reading > TEMP_HIGH:
        print(f"Temperature in {room_name} is too high: {reading}°C. Turning on the AC.")
        turn_on_ac(room_name)
    else:
        print(f"Temperature in {room_name} is within the acceptable range: {reading}°C.")

def handle_humidity_reading(sensor: Sensor, reading: float):
    room_name = sensor.room_name
    if reading < HUMIDITY_LOW:
        print(f"Humidity in {room_name} is too low: {reading}%. Increasing humidity.")
        increase_humidity(room_name)
    elif reading > HUMIDITY_HIGH:
        print(f"Humidity in {room_name} is too high: {reading}%. Decreasing humidity.")
        decrease_humidity(room_name)
    else:
        print(f"Humidity in {room_name} is within the acceptable range: {reading}%.")

def handle_light_intensity_reading(sensor: Sensor, reading: float):
    room_name = sensor.room_name
    if reading < LIGHT_INTENSITY_LOW:
        print(f"Light intensity in {room_name} is too low: {reading} lux. Turning on the lights.")
        turn_on_lights(room_name)
    elif reading > LIGHT_INTENSITY_HIGH:
        print(f"Light intensity in {room_name} is too high: {reading} lux. Consider dimming the lights or closing curtains.")
        # Add logic to dim lights or close curtains if needed
    else:
        print(f"Light intensity in {room_name} is within the acceptable range: {reading} lux.")

def turn_on_heater(room_name: str):
    heaters = get_all_actuators(get_home_plan(), "Heater")
    for heater in heaters:
        if heater.room_name == room_name:
            heater.turn_on()
            heater.set_target_temperature(25)  # Set to a comfortable temperature

def turn_on_ac(room_name: str):
    acs = get_all_actuators(get_home_plan(), "AC")
    for ac in acs:
        if ac.room_name == room_name:
            ac.turn_on()
            ac.set_target_temperature(20)  # Set to a comfortable temperature

def increase_humidity(room_name: str):
    humidifiers = get_all_actuators(get_home_plan(), "Humidifier")
    for humidifier in humidifiers:
        if humidifier.room_name == room_name:
            humidifier.increase_humidity()

def decrease_humidity(room_name: str):
    # Assuming the same actuator can decrease humidity
    humidifiers = get_all_actuators(get_home_plan(), "Humidifier")
    for humidifier in humidifiers:
        if humidifier.room_name == room_name:
            humidifier.decrease_humidity()

def turn_on_lights(room_name: str):
    lights = get_all_actuators(get_home_plan(), "Light")
    for light in lights:
        if light.room_name == room_name:
            light.turn_on()
            light.set_brightness_level("high")

# Helper function to get the home plan (this could be refactored to use a global variable or dependency injection)
def get_home_plan():
    return home_plan()

if __name__ == "__main__":
    main()