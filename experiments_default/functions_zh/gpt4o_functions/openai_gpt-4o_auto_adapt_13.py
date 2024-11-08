# Based on the provided functional description and source code, here is your `function.py` file. This file will be placed in the `functions` folder and contains the main function that meets your described functionality:

import sys
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light, NotificationSender
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()
    
    # Define the desired values
    desired_temperature = 26
    desired_humidity_status = "适宜湿度。"
    desired_light_intensity_status = "光照好些"
    
    # Get the LivingRoom sensors and actuators
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Turn on all sensors
    for sensor in living_room_sensors:
        sensor.turn_on()
    
    # Get sensor readings
    temperature_reading = None
    humidity_reading = None
    light_intensity_reading = None
    
    for sensor in living_room_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature_reading = sensor.get_reading()
        elif isinstance(sensor, HumiditySensor):
            humidity_reading = sensor.get_reading()
        elif isinstance(sensor, LightIntensiveSensor):
            light_intensity_reading = sensor.get_reading()
    
    # Adjust temperature using Heater and AC
    for actuator in living_room_actuators:
        if isinstance(actuator, Heater):
            actuator.set_target_temperature(desired_temperature)
            actuator.adjust_temperature(temperature_reading)
        elif isinstance(actuator, AC):
            actuator.set_target_temperature(desired_temperature)
            actuator.adjust_temperature(temperature_reading)
    
    # Adjust humidity using Humidifier
    for actuator in living_room_actuators:
        if isinstance(actuator, Humidifier):
            if humidity_reading < HUMIDITY_LOW:
                actuator.increase_humidity()
            elif humidity_reading > HUMIDITY_HIGH:
                actuator.decrease_humidity()
    
    # Adjust light intensity using Light
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            if light_intensity_reading < LIGHT_INTENSITY_LOW:
                actuator.set_brightness_level("high")
            elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                actuator.set_brightness_level("low")
    
    # Notification
    for actuator in living_room_actuators:
        if isinstance(actuator, NotificationSender):
            actuator.turn_on()
            message = f"Temperature: {desired_temperature}度\n"
            message += f"Humidity: {desired_humidity_status}\n"
            message += f"Light Intensity: {desired_light_intensity_status}\n"
            actuator.notification_sender(message)

if __name__ == "__main__":
    main()