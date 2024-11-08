# Based on the functional description and the provided source code, I'll create a `function.py` file that will serve as the main entry point for your smart home project. This file will utilize the components from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 
# Here's the `function.py` file:

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import Heater, AC, CoffeeMachine, Light, CleaningRobot, NotificationSender
from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create home plan
    home = home_plan()
    
    # Print the home plan
    print_home_plan(home)

    # Retrieve sensors and actuators
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_sensors = get_room_sensors(home, "LivingRoom")
        living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Example operation: Checking temperature and controlling heater/AC
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")

    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temp = sensor.get_reading()
        for heater in heaters:
            if heater.room_name == sensor.room_name:
                heater.set_target_temperature(TEMP_LOW)
                heater.adjust_temperature(temp)
        for ac in ac_units:
            if ac.room_name == sensor.room_name:
                ac.set_target_temperature(TEMP_HIGH)
                ac.adjust_temperature(temp)

    # Example operation: Checking humidity and controlling humidifier
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity = sensor.get_reading()
        for humidifier in humidifiers:
            if humidifier.room_name == sensor.room_name:
                if humidity < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif humidity > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()
    
    # Example operation: Light control based on light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        for light in lights:
            if light.room_name == sensor.room_name:
                if light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                    light.set_brightness_level("high")
                elif light_intensity > LIGHT_INTENSITY_HIGH:
                    light.turn_off()

    # Example operation: Running daily routine for cleaning robots
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for robot in cleaning_robots:
        robot.turn_on()
        robot.daily_routine()

    # Example operation: Notification example
    notification_senders = get_all_actuators(home, "NotificationSender")
    for sender in notification_senders:
        sender.turn_on()
        sender.notification_sender("All systems are functioning normally.")

if __name__ == "__main__":
    main()