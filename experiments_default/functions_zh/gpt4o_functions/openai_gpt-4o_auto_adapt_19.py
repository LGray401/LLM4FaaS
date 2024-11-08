# Based on the functional description and the provided source code, we will create a `function.py` file located in the `functions` folder. This file will contain a main function that checks the temperature, humidity, and light intensity, and then performs actions accordingly. 
# 
# Here's the `function.py` file:

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'home'))

from home_plan import home_plan, get_room_sensors
from actuator import NotificationSender, AC, Heater, Humidifier, Light
from config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Initialize actuators
    notification_sender = next((actuator for actuator in living_room_actuators if isinstance(actuator, NotificationSender)), None)
    ac = next((actuator for actuator in living_room_actuators if isinstance(actuator, AC)), None)
    heater = next((actuator for actuator in living_room_actuators if isinstance(actuator, Heater)), None)
    humidifier = next((actuator for actuator in living_room_actuators if isinstance(actuator, Humidifier)), None)
    light = next((actuator for actuator in living_room_actuators if isinstance(actuator, Light)), None)

    # Turn on all actuators
    for actuator in [notification_sender, ac, heater, humidifier, light]:
        if actuator:
            actuator.turn_on()

    # Check sensors and take actions
    for sensor in living_room_sensors:
        reading = sensor.get_reading()
        if sensor.sensor_type == "IndoorTemperature":
            if reading > TEMP_HIGH:
                if notification_sender:
                    notification_sender.notification_sender("Temperature: 太热了")
                if ac:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(reading)
            elif reading < TEMP_LOW:
                if heater:
                    heater.set_target_temperature(TEMP_LOW)
                    heater.adjust_temperature(reading)

        elif sensor.sensor_type == "Humidity":
            if reading < HUMIDITY_LOW:
                if notification_sender:
                    notification_sender.notification_sender("Humidity: 太干了")
                if humidifier:
                    humidifier.increase_humidity()
            elif reading > HUMIDITY_HIGH:
                if humidifier:
                    humidifier.decrease_humidity()

        elif sensor.sensor_type == "LightIntensive":
            if reading > LIGHT_INTENSITY_HIGH:
                if notification_sender:
                    notification_sender.notification_sender("Light Intensity: 太亮了")
                if light:
                    light.turn_off()

if __name__ == "__main__":
    main()