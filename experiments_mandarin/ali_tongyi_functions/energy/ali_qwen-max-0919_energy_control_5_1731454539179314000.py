# Given your project structure and the provided source code, I will create a `function.py` file that contains the main function to control and interact with the smart home system. The `main` function will demonstrate how to use the classes and methods from the other files to manage the sensors and actuators in the smart home.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Heater, AC, CoffeeMachine, Window, Door, Curtain, CleaningRobot, NotificationSender, MusicPlayer, Light, SmartTV, SmartSocket, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION
import time

def main():
    # Create the home plan
    home = home_plan()
    
    # Print the home plan
    print_home_plan(home)
    
    # Example: Get a specific room and its components
    living_room = get_room(home, "LivingRoom")
    if living_room:
        print(f"\n--- Living Room Components ---")
        for sensor in living_room.sensors:
            print(f"Sensor: {sensor.id}")
        for actuator in living_room.actuators:
            print(f"Actuator: {actuator.id}")
    
    # Example: Get all temperature sensors
    all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    if all_temperature_sensors:
        print(f"\n--- All Indoor Temperature Sensors ---")
        for sensor in all_temperature_sensors:
            print(f"Sensor: {sensor.id}")
    
    # Example: Get all lights
    all_lights = get_all_actuators(home, "Light")
    if all_lights:
        print(f"\n--- All Lights ---")
        for light in all_lights:
            print(f"Light: {light.id}")
    
    # Example: Turn on and off a light
    if all_lights:
        light = all_lights[0]
        light.turn_on()
        light.set_brightness_level("medium")
        time.sleep(2)  # Simulate some delay
        light.turn_off()
    
    # Example: Adjust temperature using a heater
    if living_room:
        heater = next((actuator for actuator in living_room.actuators if isinstance(actuator, Heater)), None)
        if heater:
            heater.turn_on()
            heater.set_target_temperature(TEMP_HIGH)
            indoor_temp_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
            if indoor_temp_sensor:
                indoor_temp_sensor.turn_on()
                current_temp = indoor_temp_sensor.get_reading()
                if current_temp is not None:
                    heater.adjust_temperature(current_temp)
                indoor_temp_sensor.turn_off()
            heater.turn_off()
    
    # Example: Make coffee in the kitchen
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        coffee_machine = next((actuator for actuator in kitchen.actuators if isinstance(actuator, CoffeeMachine)), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")
            coffee_machine.turn_off()
    
    # Example: Run the cleaning robot
    if living_room:
        cleaning_robot = next((actuator for actuator in living_room.actuators if isinstance(actuator, CleaningRobot)), None)
        if cleaning_robot:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()
    
    # Example: Send a notification
    if living_room:
        notification_sender = next((actuator for actuator in living_room.actuators if isinstance(actuator, NotificationSender)), None)
        if notification_sender:
            notification_sender.turn_on()
            notification_sender.notification_sender("Home security system activated.")
            notification_sender.turn_off()

if __name__ == "__main__":
    main()