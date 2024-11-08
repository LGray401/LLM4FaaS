# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to handle the smart home functionalities. The main function will monitor the temperature, humidity, and light intensity in each room and take appropriate actions using the actuators.
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW

def check_and_adjust_temperature(home):
    for room in home:
        for sensor in get_room_sensors(home, room.name):
            if isinstance(sensor, IndoorTemperatureSensor):
                sensor.turn_on()
                current_temp = sensor.get_reading()
                if current_temp is not None:
                    if current_temp < TEMP_LOW:
                        for actuator in get_room_actuators(home, room.name):
                            if isinstance(actuator, Heater):
                                actuator.set_target_temperature(TEMP_HIGH)
                                actuator.adjust_temperature(current_temp)
                                print(f"Heater in {room.name} turned on to increase temperature.")
                    elif current_temp > TEMP_HIGH:
                        for actuator in get_room_actuators(home, room.name):
                            if isinstance(actuator, AC):
                                actuator.set_target_temperature(TEMP_LOW)
                                actuator.adjust_temperature(current_temp)
                                print(f"AC in {room.name} turned on to decrease temperature.")
                sensor.turn_off()

def check_and_adjust_humidity(home):
    for room in home:
        for sensor in get_room_sensors(home, room.name):
            if isinstance(sensor, HumiditySensor):
                sensor.turn_on()
                current_humidity = sensor.get_reading()
                if current_humidity is not None:
                    if current_humidity < HUMIDITY_LOW:
                        for actuator in get_room_actuators(home, room.name):
                            if isinstance(actuator, Humidifier):
                                actuator.increase_humidity()
                                print(f"Humidifier in {room.name} turned on to increase humidity.")
                    elif current_humidity > HUMIDITY_HIGH:
                        for actuator in get_room_actuators(home, room.name):
                            if isinstance(actuator, Humidifier):
                                actuator.decrease_humidity()
                                print(f"Humidifier in {room.name} turned on to decrease humidity.")
                sensor.turn_off()

def check_and_adjust_light_intensity(home):
    for room in home:
        for sensor in get_room_sensors(home, room.name):
            if isinstance(sensor, LightIntensiveSensor):
                sensor.turn_on()
                current_light_intensity = sensor.get_reading()
                if current_light_intensity is not None:
                    if current_light_intensity < LIGHT_INTENSITY_LOW:
                        for actuator in get_room_actuators(home, room.name):
                            if isinstance(actuator, Light):
                                actuator.turn_on()
                                actuator.set_brightness_level("high")
                                print(f"Light in {room.name} turned on and set to high brightness.")
                sensor.turn_off()

def main():
    home = home_plan()
    
    while True:
        check_and_adjust_temperature(home)
        check_and_adjust_humidity(home)
        check_and_adjust_light_intensity(home)
        
        # Wait for a short duration before the next check
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()