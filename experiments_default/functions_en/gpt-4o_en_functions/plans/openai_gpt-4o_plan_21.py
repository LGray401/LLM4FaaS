# Based on the functional description and the provided code, I'll create a `function.py` file that incorporates the required functionality for the smart home project. The file will contain a `main` function that sets up and executes the morning, leave home, and movie plans.
# 
# Here's the `function.py`:

from home_plan import home_plan, get_room_actuators, get_all_actuators
from actuator import Curtain, CoffeeMachine, Light, Door, SmartTV, SmartSocket
from sensor import LightIntensiveSensor
import time

def morning_plan(home):
    print("Executing Morning Plan...")
    # Open curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # Start coffee machine
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # Turn on lights and adjust brightness if sunlight is dim
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()

    # Check if sunlight is dim
    light_sensors = get_all_actuators(home, "LightIntensiveSensor")
    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading < 300:  # Assuming 300 lux as the threshold for dim light
            for light in lights:
                light.set_brightness_level("medium")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    # Lock doors
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()

    # Turn off lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # Unplug all sockets
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    # Close curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()

    # Dim lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.set_brightness_level("low")

    # Turn on the TV and play a movie
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        tv.turn_on()
        tv.play_channel("Movie Channel")

def main():
    home = home_plan()
    
    # Execute plans
    morning_plan(home)
    time.sleep(1)  # Just to simulate some delay between plans
    leave_home_plan(home)
    time.sleep(1)
    movie_plan(home)

if __name__ == "__main__":
    main()