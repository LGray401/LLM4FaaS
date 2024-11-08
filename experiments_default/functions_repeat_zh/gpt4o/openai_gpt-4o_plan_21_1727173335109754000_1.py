# Based on the provided functional description and existing source code, here is the `function.py` file that implements the main functions for the Morning Plan, Leave Home Plan, and Movie Plan. This file will be located in the `functions` folder.

from home.sensor import LightIntensiveSensor
from home.actuator import Light, CoffeeMachine, Curtain, Door, SmartSocket, SmartTV
from home.home_plan import home_plan, get_room_actuators

def morning_plan(home):
    print("Executing Morning Plan...")

    # Get all curtains and coffee machines
    curtains = get_all_actuators(home, "Curtain")
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    lights = get_all_actuators(home, "Light")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Open all curtains
    for curtain in curtains:
        curtain.turn_on()

    # Start all coffee machines
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("espresso")

    # Check light intensity and turn on lights if necessary
    for light_sensor in light_sensors:
        light_sensor.turn_on()
        reading = light_sensor.get_reading()
        if reading and reading < 600:  # Assuming 600 is the threshold for "dim" sunlight
            for light in lights:
                light.turn_on()
                light.set_brightness_level("medium")


def leave_home_plan(home):
    print("Executing Leave Home Plan...")

    # Get all doors, lights, and smart sockets
    doors = get_all_actuators(home, "Door")
    lights = get_all_actuators(home, "Light")
    smart_sockets = get_all_actuators(home, "SmartSocket")

    # Lock all doors
    for door in doors:
        door.lock()

    # Turn off all lights
    for light in lights:
        light.turn_off()

    # Turn off all smart sockets
    for socket in smart_sockets:
        socket.turn_off()


def movie_plan(home):
    print("Executing Movie Plan...")

    # Get all curtains, lights, and smart TVs
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")
    tvs = get_all_actuators(home, "SmartTV")

    # Close all curtains
    for curtain in curtains:
        curtain.turn_off()

    # Dim all lights
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

    # Turn on the TV and play a movie
    for tv in tvs:
        tv.turn_on()
        tv.play_channel("movie_channel")

def main():
    home = home_plan()

    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()