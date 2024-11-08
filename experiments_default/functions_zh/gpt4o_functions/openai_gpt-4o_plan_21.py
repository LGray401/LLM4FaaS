# Based on the provided functional descriptions and source code files, here is the `function.py` file located in the 'functions' folder. This file contains the main function, which implements the required smart home plans.

# functions/function.py

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, CoffeeMachine, Light, Door, SmartSocket, SmartTV

def morning_plan(home):
    # Get sensors and actuators
    bedroom_curtains = get_all_actuators(home, "Curtain")
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    lights = get_all_actuators(home, "Light")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Implement the morning plan
    for curtain in bedroom_curtains:
        curtain.turn_on()

    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    for light_sensor in light_sensors:
        light_sensor.turn_on()
        light_intensity = light_sensor.get_reading()
        if light_intensity < 300:  # assuming 300 is the threshold for "较暗"
            for light in lights:
                light.turn_on()
                light.set_brightness_level("medium")

def leave_home_plan(home):
    doors = get_all_actuators(home, "Door")
    lights = get_all_actuators(home, "Light")
    sockets = get_all_actuators(home, "SmartSocket")

    # Implement the leave home plan
    for door in doors:
        door.lock()

    for light in lights:
        light.turn_off()

    for socket in sockets:
        socket.turn_off()

def movie_plan(home):
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")
    tvs = get_all_actuators(home, "SmartTV")

    # Implement the movie plan
    for curtain in curtains:
        curtain.turn_off()

    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

    for tv in tvs:
        tv.turn_on()
        tv.play_channel("Movie")

def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()