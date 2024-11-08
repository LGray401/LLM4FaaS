# Based on the provided functional description and source code, I understand that you want to create a `function.py` file in the `functions` folder. This file should contain a main function that can be used to control and interact with the smart home system. The main function will likely involve initializing the home plan, interacting with sensors and actuators, and possibly automating some tasks based on sensor readings.
# 
# Here's a possible implementation of `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Heater, AC, CoffeeMachine, Window, Door, Curtain, CleaningRobot, NotificationSender, MusicPlayer, Light, SmartTV, SmartSocket, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION
import time

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Example: Print the home plan
    print_home_plan(home)
    
    # Example: Get a specific room and its components
    living_room = get_room(home, "LivingRoom")
    if living_room:
        print(f"LivingRoom found with {len(living_room.sensors)} sensors and {len(living_room.actuators)} actuators.")
    
    # Example: Get all temperature sensors
    all_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in all_temp_sensors:
        sensor.turn_on()
        print(sensor.get_reading())
        sensor.turn_off()
    
    # Example: Get all lights and turn them on
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_on()
        light.set_brightness_level("medium")
    
    # Example: Adjust temperature in the LivingRoom
    living_room_heater = next((act for act in living_room.actuators if isinstance(act, Heater)), None)
    living_room_ac = next((act for act in living_room.actuators if isinstance(act, AC)), None)
    
    if living_room_heater and living_room_ac:
        indoor_temp_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_on()
            current_temp = indoor_temp_sensor.get_reading()
            indoor_temp_sensor.turn_off()
            
            if current_temp < TEMP_LOW:
                living_room_heater.set_target_temperature(TEMP_HIGH)
                living_room_heater.adjust_temperature(current_temp)
            elif current_temp > TEMP_HIGH:
                living_room_ac.set_target_temperature(TEMP_LOW)
                living_room_ac.adjust_temperature(current_temp)
    
    # Example: Start the daily cleaning routine
    cleaning_robot = next((act for act in living_room.actuators if isinstance(act, CleaningRobot)), None)
    if cleaning_robot:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()
    
    # Example: Send a notification
    notification_sender = next((act for act in living_room.actuators if isinstance(act, NotificationSender)), None)
    if notification_sender:
        notification_sender.turn_on()
        notification_sender.notification_sender("Daily cleaning routine completed.")

if __name__ == "__main__":
    main()