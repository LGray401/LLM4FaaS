# Sure, I can help with that. Based on the functional description and the provided source code files, I'll create a `function.py` file to implement the main functions for the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. This file will contain functions that can be called to execute these plans.
# 
# Here is the `function.py` file:

# function.py

from home_plan import home_plan, get_all_actuators, get_all_sensors
from config import LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

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

    # Start the coffee machine
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # Check light intensity and turn on lights if it's dark
    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading < LIGHT_INTENSITY_LOW:
            for light in lights:
                light.turn_on()
                light.set_brightness_level("medium")

    print("Morning Plan Executed.")

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

    print("Leave Home Plan Executed.")

def movie_plan(home):
    print("Executing Movie Plan...")

    # Get all curtains, lights, and TVs
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")
    tvs = get_all_actuators(home, "SmartTV")

    # Close all curtains
    for curtain in curtains:
        curtain.turn_off()

    # Set lights to low brightness
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

    # Turn on TV and play a movie
    for tv in tvs:
        tv.turn_on()
        tv.play_channel("Movie Channel")

    print("Movie Plan Executed.")

def main():
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()