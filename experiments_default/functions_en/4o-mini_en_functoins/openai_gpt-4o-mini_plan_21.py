# Here's the `function.py` file based on your functional description for the smart home project. This file will implement the required morning plan, leave home plan, and movie plan functionalities, utilizing the classes defined in the other files.

# functions/function.py

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.actuator import Door, Light, Curtain, CoffeeMachine, SmartTV
from home.sensor import LightIntensiveSensor
import time

def morning_plan(home):
    print("\n--- MORNING PLAN ---")
    
    # Set the alarm to 7 AM
    alarm_time = "07:00"
    print(f"Alarm set for {alarm_time}.")
    
    # Open curtains
    living_room = get_room(home, "LivingRoom")
    curtain = get_all_actuators(home, "Curtain")
    for c in curtain:
        c.turn_on()

    # Start coffee machine
    coffee_machine = get_all_actuators(home, "CoffeeMachine")
    for cm in coffee_machine:
        cm.turn_on()
        cm.make_coffee("Espresso")  # Example coffee type

    # Turn on lights and adjust brightness based on sunlight
    light_sensor = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensor:
        sensor.turn_on()
        sunlight_intensity = sensor.get_reading()

        light = get_all_actuators(home, "Light")
        for l in light:
            l.turn_on()
            if sunlight_intensity < 500:  # Assuming medium brightness is set at 500 lux
                l.set_brightness_level("medium")
            else:
                l.set_brightness_level("low")

def leave_home_plan(home):
    print("\n--- LEAVE HOME PLAN ---")
    # Lock the door
    door = get_all_actuators(home, "Door")
    for d in door:
        d.lock()

    # Turn off lights
    lights = get_all_actuators(home, "Light")
    for l in lights:
        l.turn_off()

    # Unplug sockets (not implemented, assuming we just turn off smart sockets)
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

def movie_plan(home):
    print("\n--- MOVIE PLAN ---")
    # Close curtains
    living_room = get_room(home, "LivingRoom")
    curtains = get_all_actuators(home, "Curtain")
    for c in curtains:
        c.turn_off()  # Assuming off means closed

    # Dim the lights
    lights = get_all_actuators(home, "Light")
    for l in lights:
        l.set_brightness_level("low")

    # Turn on the TV and play a movie
    smart_tv = get_all_actuators(home, "SmartTV")
    for tv in smart_tv:
        tv.turn_on()
        tv.play_channel("Movie Channel")  # Example channel for the movie

def main():
    home = home_plan()
    
    # Execute plans
    morning_plan(home)
    time.sleep(1)  # Simulate time taken for morning plan
    leave_home_plan(home)
    time.sleep(1)  # Simulate time taken for leaving home
    movie_plan(home)

if __name__ == "__main__":
    main()