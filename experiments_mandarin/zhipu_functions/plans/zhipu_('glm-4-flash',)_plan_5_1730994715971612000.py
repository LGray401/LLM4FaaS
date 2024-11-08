# Based on your functional description and provided source code, here is a `function.py` file that contains a main function which will implement your morning, leave home, and movie plans. The function will utilize the existing sensor and actuator classes to perform the required actions.

# function.py

import time

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Curtain

# Import your room creation functions from home_plan module
from home_plan import home_plan, get_room

# Import your logger configuration from config module (if needed)
# from config import logger

def run_morning_plan():
    # Assume the living room has a coffee machine and a light
    room = get_room(home_plan(), "LivingRoom")
    if room:
        coffee_machine = next((a for a in room.actuators if isinstance(a, CoffeeMachine)), None)
        if coffee_machine:
            coffee_machine.make_coffee("Espresso")
        light = next((a for a in room.actuators if isinstance(a, Light)), None)
        if light:
            light.turn_on()

def run_leave_home_plan():
    # Assume the living room has lights
    room = get_room(home_plan(), "LivingRoom")
    if room:
        for light in (a for a in room.actuators if isinstance(a, Light)):
            light.turn_off()

def run_movie_plan():
    # Assume the living room has curtains
    room = get_room(home_plan(), "LivingRoom")
    if room:
        curtain = next((a for a in room.actuators if isinstance(a, Curtain)), None)
        if curtain:
            curtain.turn_on()

def main():
    # Run morning plan
    run_morning_plan()
    print("Morning plan executed.")

    # Wait for a bit to simulate time passing
    time.sleep(10)  # 10 seconds wait time

    # Run leave home plan
    run_leave_home_plan()
    print("Leave home plan executed.")

    # Wait for a bit to simulate time passing
    time.sleep(10)  # 10 seconds wait time

    # Run movie plan
    run_movie_plan()
    print("Movie plan executed.")

if __name__ == "__main__":
    main()