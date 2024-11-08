# Based on the provided functional descriptions and the source code for the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files, we can create a `function.py` file that implements the three plans: `MORNING PLAN`, `LEAVE HOME PLAN`, and `MOVIE PLAN`.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_actuators
from home.config import LIGHT_INTENSITY_LOW
import time

def morning_plan(home):
    print("Executing Morning Plan...")

    # Get the Coffee Machine in the Kitchen
    kitchen = get_room(home, "Kitchen")
    coffee_machine = next((actuator for actuator in kitchen.actuators if actuator.actuator_type == "CoffeeMachine"), None)
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # Get all Curtains and open them
    all_curtains = get_all_actuators(home, "Curtain")
    for curtain in all_curtains:
        curtain.turn_on()  # Assuming turning on the curtain means opening it

    # Get all Light sensors and check light intensity
    all_light_sensors = get_all_actuators(home, "Light")
    light_intensity_sensors = get_all_actuators(home, "LightIntensive")
    for sensor in light_intensity_sensors:
        sensor.turn_on()
        if sensor.get_reading() < LIGHT_INTENSITY_LOW:
            for light in all_light_sensors:
                light.turn_on()
                light.set_brightness_level("medium")
        sensor.turn_off()


def leave_home_plan(home):
    print("Executing Leave Home Plan...")

    # Get all Doors and lock them
    all_doors = get_all_actuators(home, "Door")
    for door in all_doors:
        door.lock()

    # Get all Lights and turn them off
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()

    # Get all SmartSockets and turn them off
    all_sockets = get_all_actuators(home, "SmartSocket")
    for socket in all_sockets:
        socket.turn_off()


def movie_plan(home):
    print("Executing Movie Plan...")

    # Get all Curtains and close them
    all_curtains = get_all_actuators(home, "Curtain")
    for curtain in all_curtains:
        curtain.turn_off()  # Assuming turning off the curtain means closing it

    # Get all Lights and set their brightness to low
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_on()
        light.set_brightness_level("low")

    # Get the TV in the Living Room and turn it on
    living_room = get_room(home, "LivingRoom")
    tv = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "SmartTV"), None)
    if tv:
        tv.turn_on()
        tv.play_channel("Movie")


def main():
    # Initialize home plan
    home = home_plan()
    
    # Execute plans
    morning_plan(home)
    time.sleep(1)  # Adding delay to simulate time between plans
    leave_home_plan(home)
    time.sleep(1)  # Adding delay to simulate time between plans
    movie_plan(home)


if __name__ == "__main__":
    main()