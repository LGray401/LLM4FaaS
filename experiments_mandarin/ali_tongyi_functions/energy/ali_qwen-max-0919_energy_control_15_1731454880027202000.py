# Based on your provided functional description and source code, I will create a `function.py` file that contains the main function to control and interact with the smart home system. The `main` function will initialize the home plan, turn on and off sensors and actuators, get readings, and perform other actions as needed.
# 
# Here is the `function.py` file:

# functions/function.py

import os
import sys
from datetime import datetime
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Heater, AC, CoffeeMachine, Window, Door, Curtain, CleaningRobot, NotificationSender, MusicPlayer, Light, SmartTV, SmartSocket, Humidifier
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def main():
    # Initialize the home plan
    home = home_plan()
    print_home_plan(home)

    # Example: Get all temperature sensors and print their readings
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        print(sensor.get_reading())
        sensor.turn_off()

    # Example: Get all lights in the LivingRoom and turn them on
    living_room_lights = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Light)]
    for light in living_room_lights:
        light.turn_on()
        light.set_brightness_level("high")

    # Example: Adjust the temperature in the Bedroom using the heater and AC
    bedroom_heater = next((actuator for actuator in get_room_actuators(home, "Bedroom") if isinstance(actuator, Heater)), None)
    bedroom_ac = next((actuator for actuator in get_room_actuators(home, "Bedroom") if isinstance(actuator, AC)), None)
    bedroom_temp_sensor = next((sensor for sensor in get_room_sensors(home, "Bedroom") if isinstance(sensor, IndoorTemperatureSensor)), None)

    if bedroom_heater and bedroom_ac and bedroom_temp_sensor:
        bedroom_heater.turn_on()
        bedroom_ac.turn_on()
        bedroom_heater.set_target_temperature(TEMP_HIGH)
        bedroom_ac.set_target_temperature(TEMP_LOW)
        current_temp = bedroom_temp_sensor.get_reading()
        if current_temp is not None:
            bedroom_heater.adjust_temperature(current_temp)
            bedroom_ac.adjust_temperature(current_temp)

    # Example: Make coffee in the Kitchen
    kitchen_coffee_machine = next((actuator for actuator in get_room_actuators(home, "Kitchen") if isinstance(actuator, CoffeeMachine)), None)
    if kitchen_coffee_machine:
        kitchen_coffee_machine.turn_on()
        kitchen_coffee_machine.make_coffee("Espresso")

    # Example: Start the daily cleaning routine in the LivingRoom
    living_room_cleaning_robot = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, CleaningRobot)), None)
    if living_room_cleaning_robot:
        living_room_cleaning_robot.turn_on()
        living_room_cleaning_robot.daily_routine()

    # Example: Send a notification from the LivingRoom
    living_room_notification_sender = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, NotificationSender)), None)
    if living_room_notification_sender:
        living_room_notification_sender.turn_on()
        living_room_notification_sender.notification_sender("Daily cleaning completed.")

    # Example: Play music in the LivingRoom
    living_room_music_player = next((actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, MusicPlayer)), None)
    if living_room_music_player:
        living_room_music_player.turn_on()
        living_room_music_player.play_music("Relaxing Jazz")

    # Example: Turn off all lights in the LivingRoom
    for light in living_room_lights:
        light.turn_off()

if __name__ == "__main__":
    main()