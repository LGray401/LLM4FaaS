# Given your functional description and the provided source code files, here's how `function.py` should look:
# 
# `functions/function.py`

import datetime
import time

# from home.actuator import Light, Curtain, MusicPlayer, CoffeeMachine, Door, SmartSocket
# from home.home_plan import home_plan, get_room_actuators, get_room_sensors
# from home.config import LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
# from home.sensor import LightIntensiveSensor


def morning_plan(home):
    print("Executing Morning Plan...")
    # At 7 AM every day
    while True:
        now = datetime.datetime.now()
        if now.hour == 7 and now.minute == 0:
            print("Morning Plan Initiated...")
            living_room_actuators = get_room_actuators(home, 'LivingRoom')
            kitchen_actuators = get_room_actuators(home, 'Kitchen')
            bedroom_actuators = get_room_actuators(home, 'Bedroom')

            if living_room_actuators:
                for actuator in living_room_actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_on()
                        light_sensors = get_room_sensors(home, 'LivingRoom')
                        for sensor in light_sensors:
                            if isinstance(sensor, LightIntensiveSensor):
                                sensor.turn_on()
                                light_level = sensor.get_reading()
                                if light_level < LIGHT_INTENSITY_LOW:
                                    actuator.set_brightness_level("high")
                                elif light_level > LIGHT_INTENSITY_HIGH:
                                    actuator.set_brightness_level("low")
                                else:
                                    actuator.set_brightness_level("medium")
                    elif isinstance(actuator, Curtain):
                        actuator.turn_on()
                    elif isinstance(actuator, MusicPlayer):
                        actuator.turn_on()
                        actuator.play_music("Relaxing Music")

            if kitchen_actuators:
                for actuator in kitchen_actuators:
                    if isinstance(actuator, CoffeeMachine):
                        actuator.turn_on()
                        actuator.make_coffee("Cappuccino")
                    elif isinstance(actuator, Curtain):
                        actuator.turn_on()

            if bedroom_actuators:
                for actuator in bedroom_actuators:
                    if isinstance(actuator, Curtain):
                        actuator.turn_on()

            time.sleep(60)  # Wait for a minute to avoid repeated execution within the same minute

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    # When leaving home
    all_actuators = []
    for room in home:
        all_actuators.extend(room.actuators)

    for actuator in all_actuators:
        if isinstance(actuator, Door):
            actuator.lock()
        elif isinstance(actuator, Light):
            actuator.turn_off()
        elif isinstance(actuator, SmartSocket):
            actuator.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    # When watching a movie
    living_room_actuators = get_room_actuators(home, 'LivingRoom')

    if living_room_actuators:
        for actuator in living_room_actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()
            elif isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")

def main():
    home = home_plan()

    while True:
        now = datetime.datetime.now()

        # Check for specific plans based on time or other conditions
        if now.hour == 7 and now.minute == 0:
            morning_plan(home)

        # Here you can add other conditions to trigger leave_home_plan and movie_plan
        # For example, leave_home_plan can be called based on a specific event or time

        # Simulating a condition for movie plan (e.g., user triggers the plan via some input)
        # if some_condition_for_movie_plan:
        #     movie_plan(home)

        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()