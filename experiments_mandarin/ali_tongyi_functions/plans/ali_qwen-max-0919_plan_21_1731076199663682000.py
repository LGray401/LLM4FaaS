# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to implement the plans you described. This file will be located in the `functions` folder. The `main` function will handle the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN as specified.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.actuator import Light, Curtain, CoffeeMachine, Door, SmartSocket, SmartTV
from home.sensor import LightIntensiveSensor
import time

def execute_morning_plan(home):
    # Get actuators and sensors for the living room
    living_room = get_room_actuators(home, "LivingRoom")
    bedroom = get_room_actuators(home, "Bedroom")

    # Open curtains
    for actuator in living_room + bedroom:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
            print(f"Curtain {actuator.id} is now open.")

    # Start coffee machine
    for actuator in living_room:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("espresso")
            print(f"Coffee machine {actuator.id} is now making coffee.")

    # Check light intensity and turn on lights if needed
    for sensor in get_room_sensors(home, "LivingRoom"):
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading < 900:  # Assuming LIGHT_INTENSITY_HIGH is 900
                for actuator in living_room:
                    if isinstance(actuator, Light):
                        actuator.turn_on()
                        actuator.set_brightness_level("medium")
                        print(f"Light {actuator.id} is now on with medium brightness.")
            sensor.turn_off()

def execute_leave_home_plan(home):
    # Lock doors
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Door):
                actuator.lock()
                print(f"Door {actuator.id} is now locked.")

    # Turn off all lights
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
                print(f"Light {actuator.id} is now off.")

    # Turn off all smart sockets
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, SmartSocket):
                actuator.turn_off()
                print(f"Smart socket {actuator.id} is now off.")

def execute_movie_plan(home):
    # Close curtains
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_off()
                print(f"Curtain {actuator.id} is now closed.")

    # Dim lights
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")
                print(f"Light {actuator.id} is now on with low brightness.")

    # Turn on TV and play movie
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Movie Channel")
                print(f"Smart TV {actuator.id} is now playing a movie.")

def main():
    home = home_plan()
    while True:
        print("\n--- Smart Home Control ---")
        print("1. Execute Morning Plan")
        print("2. Execute Leave Home Plan")
        print("3. Execute Movie Plan")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            execute_morning_plan(home)
        elif choice == '2':
            execute_leave_home_plan(home)
        elif choice == '3':
            execute_movie_plan(home)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()