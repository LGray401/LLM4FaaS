# Based on the provided functional description and source code, here is a `function.py` file that includes a `main` function that utilizes the existing classes to execute the described plans.

# function.py

import sys
import os

# Ensure the home directory is in the path
sys.path.append(os.path.join(os.getcwd(), 'home'))

from sensor import Sensor, IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, \
    LightIntensiveSensor, SmokeSensor
from actuator import Actuator, Heater, AC, Window, Curtain, MusicPlayer, CoffeeMachine, \
    SmartSocket, Door, CleaningRobot, NotificationSender, MusicPlayer, Light, SmartTV, Humidifier
from home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from config import DAILY_ROUTINE_DURATION

def morning_plan():
    # Assume the home is already set up and sensors/actuators are properly initialized
    living_room = get_room(home_plan(), "LivingRoom")
    if living_room:
        # Turn on the light in the Living Room
        light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
        if light:
            light.turn_on()
            print("Morning: Light is turned on in the Living Room.")

def leave_home_plan():
    # Assume the home is already set up and sensors/actuators are properly initialized
    living_room = get_room(home_plan(), "LivingRoom")
    if living_room:
        # Open the curtains in the Living Room
        curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
        if curtain:
            curtain.turn_on()
            print("Leave Home: Curtains are opened in the Living Room.")

def movie_plan():
    # Assume the home is already set up and sensors/actuators are properly initialized
    living_room = get_room(home_plan(), "LivingRoom")
    if living_room:
        # Turn on the TV in the Living Room
        tv = next((actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)), None)
        if tv:
            tv.turn_on()
            print("Movie Time: TV is turned on in the Living Room.")

def main():
    # Run the morning plan
    morning_plan()
    # Run the leave home plan
    leave_home_plan()
    # Run the movie plan
    movie_plan()
    # Run daily routine for cleaning robot
    cleaning_robot = next((actuator for actuator in home_plan().actuators if isinstance(actuator, CleaningRobot)), None)
    if cleaning_robot:
        cleaning_robot.daily_routine()
        print("Daily Routine: Cleaning robot is running.")

if __name__ == "__main__":
    main()