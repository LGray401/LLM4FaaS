# Based on your functional description and the provided source code, I will create a `function.py` file that implements the three plans: **MORNING PLAN**, **LEAVE HOME PLAN**, and **MOVIE PLAN**. This file will include a main function that executes each of these plans as specified.
# 
# Here’s the content for `function.py`:

# function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import CoffeeMachine, Curtain, Light, Door, SmartTV
from home.sensor import LightIntensiveSensor
import time

def morning_plan(home):
    room = get_room(home, "Bedroom")
    if room:
        # Open curtain
        curtain = next((actor for actor in room.actuators if isinstance(actor, Curtain)), None)
        if curtain:
            curtain.turn_on()

        # Start coffee machine
        coffee_machine = next((actor for actor in room.actuators if isinstance(actor, CoffeeMachine)), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")  # Specify the type of coffee

        # Control light based on sunlight intensity
        light_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
        if light_sensor:
            light_sensor.turn_on()
            light_intensity = light_sensor.get_reading()
            if light_intensity is not None and light_intensity < 300:  # Assuming 300 lux is the threshold for dim light
                light = next((actor for actor in room.actuators if isinstance(actor, Light)), None)
                if light:
                    light.turn_on()
                    light.set_brightness_level("medium")

def leave_home_plan(home):
    # Lock the door, turn off lights and power sockets
    room = get_room(home, "LivingRoom")
    if room:
        door = next((actor for actor in room.actuators if isinstance(actor, Door)), None)
        if door:
            door.lock()

        lights = get_room_actuators(home, "Light")
        for light in lights:
            light.turn_off()

        smart_sockets = get_room_actuators(home, "SmartSocket")
        for socket in smart_sockets:
            socket.turn_off()

def movie_plan(home):
    room = get_room(home, "LivingRoom")
    if room:
        # Close curtains
        curtain = next((actor for actor in room.actuators if isinstance(actor, Curtain)), None)
        if curtain:
            curtain.turn_off()  # Assuming turning off closes the curtains

        # Dim lights
        lights = get_room_actuators(home, "Light")
        for light in lights:
            light.turn_on()
            light.set_brightness_level("low")

        # Play movie on Smart TV
        smart_tv = next((actor for actor in room.actuators if isinstance(actor, SmartTV)), None)
        if smart_tv:
            smart_tv.turn_on()
            smart_tv.play_channel("Movie Channel")  # Replace with the actual channel name

def main():
    home = home_plan()

    # Execute the plans
    print("Executing Morning Plan...")
    morning_plan(home)
    time.sleep(2)  # Simulate delay for demonstration

    print("Executing Leave Home Plan...")
    leave_home_plan(home)
    time.sleep(2)  # Simulate delay for demonstration

    print("Executing Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()