# Based on the provided functional description and source code, I will now create the `function.py` file. This file will contain the main function that will handle the execution of the smart home plans based on the time of the day.
# 
# Here is the content of the `function.py` file:

# function.py

from datetime import datetime
from home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from sensor import IndoorTemperatureSensor
from actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, CleaningRobot, SmartTV, Humidifier

def get_current_plan():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 7:
        return "MORNING_PLAN"
    elif 7 <= current_hour < 17:
        return "LEAVE_HOME_PLAN"
    elif 17 <= current_hour < 22:
        return "MOVIE_PLAN"
    else:
        return "NIGHT_PLAN"

def execute_plan(plan):
    if plan == "MORNING_PLAN":
        wake_up()
    elif plan == "LEAVE_HOME_PLAN":
        leave_home()
    elif plan == "MOVIE_PLAN":
        watch_movie()
    else:
        print("No plan for the current time.")

def wake_up():
    print("Waking up...")
    # Turn on lights in bedroom
    bedroom = get_room(home_plan(), "Bedroom")
    light = get_room_actuators(bedroom, "Light")[0]
    light.turn_on()

def leave_home():
    print("Leaving home...")
    # Turn off all lights and heaters
    for room in home_plan():
        lights = get_room_actuators(room, "Light")
        heaters = get_room_actuators(room, "Heater")
        for light in lights:
            light.turn_off()
        for heater in heaters:
            heater.turn_off()

def watch_movie():
    print("Watching movie...")
    # Turn off lights and turn on TV in living room
    living_room = get_room(home_plan(), "LivingRoom")
    light = get_room_actuators(living_room, "Light")[0]
    tv = get_room_actuators(living_room, "SmartTV")[0]
    light.turn_off()
    tv.play_channel("HBO")

def main():
    current_plan = get_current_plan()
    execute_plan(current_plan)

if __name__ == "__main__":
    main()