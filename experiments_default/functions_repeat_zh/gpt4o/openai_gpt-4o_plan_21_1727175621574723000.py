# Based on your functional description and the provided source code files, I will create a `function.py` file that implements the main functions for the different plans you described: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Below is the content for `function.py`:

from home.sensor import LightIntensiveSensor
from home.actuator import CoffeeMachine, Curtain, Light, Door, SmartSocket, SmartTV
from home.home_plan import home_plan, get_room_actuators, get_all_sensors
import time

def morning_plan(home):
    # Assume the CoffeeMachine and Curtain are in the Kitchen
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    curtain = next((act for act in kitchen_actuators if isinstance(act, Curtain)), None)
    coffee_machine = next((act for act in kitchen_actuators if isinstance(act, CoffeeMachine)), None)
    light = next((act for act in living_room_actuators if isinstance(act, Light)), None)

    if curtain:
        curtain.turn_on()
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")
    
    light_sensor = next((sensor for sensor in get_all_sensors(home, "LightIntensive") if isinstance(sensor, LightIntensiveSensor)), None)

    if light_sensor:
        light_sensor.turn_on()
        light_reading = light_sensor.get_reading()
        
        if light_reading and light_reading < 900:
            if light:
                light.turn_on()
                light.set_brightness_level("medium")

def leave_home_plan(home):
    # Lock the door and turn off all lights and sockets
    door = next((act for act in get_all_actuators(home, "Door") if isinstance(act, Door)), None)
    lights = get_all_actuators(home, "Light")
    sockets = get_all_actuators(home, "SmartSocket")

    if door:
        door.lock()
    
    for light in lights:
        light.turn_off()
    
    for socket in sockets:
        socket.turn_off()

def movie_plan(home):
    # Assume the Curtains and SmartTV are in the Living Room
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    curtain = next((act for act in living_room_actuators if isinstance(act, Curtain)), None)
    light = next((act for act in living_room_actuators if isinstance(act, Light)), None)
    smart_tv = next((act for act in living_room_actuators if isinstance(act, SmartTV)), None)

    if curtain:
        curtain.turn_off()
    if light:
        light.turn_on()
        light.set_brightness_level("low")
    if smart_tv:
        smart_tv.turn_on()
        smart_tv.play_channel("movie_channel")

def main():
    home = home_plan()
    
    while True:
        print("\nChoose a plan: 1) Morning Plan 2) Leave Home Plan 3) Movie Plan 4) Exit")
        choice = input("Enter the number of the plan: ")

        if choice == "1":
            morning_plan(home)
        elif choice == "2":
            leave_home_plan(home)
        elif choice == "3":
            movie_plan(home)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter the number of the plan.")

if __name__ == "__main__":
    main()