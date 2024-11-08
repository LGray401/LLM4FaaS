# Based on your provided functional descriptions and the source code files, I will create a `function.py` file that covers the three main functional descriptions: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. The main function will be the entry point for executing these plans.
# 
# Here's the `function.py`:

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.home_plan import home_plan, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def morning_plan(home):
    print("Executing Morning Plan...")
    # Get Bedroom actuators
    bedroom = get_room_actuators(home, "Bedroom")
    
    # Turn on light
    for actuator in bedroom:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("high")
    
    # Open curtains
    for actuator in bedroom:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
    
    # Turn on coffee machine in Kitchen
    kitchen = get_room_actuators(home, "Kitchen")
    for actuator in kitchen:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")
    
    # Turn on music player
    for actuator in bedroom:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")


def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    # Turn off all lights and actuators
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light) or isinstance(actuator, Window) or isinstance(actuator, Curtain) or isinstance(actuator, MusicPlayer) or isinstance(actuator, CoffeeMachine):
                actuator.turn_off()
    
    # Lock all doors
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Door):
                actuator.lock()
    
    # Turn on cleaning robot in LivingRoom
    living_room = get_room_actuators(home, "LivingRoom")
    for actuator in living_room:
        if isinstance(actuator, CleaningRobot):
            actuator.turn_on()
            actuator.daily_routine()


def movie_plan(home):
    print("Executing Movie Plan...")
    # Get LivingRoom actuators
    living_room = get_room_actuators(home, "LivingRoom")
    
    # Dim lights
    for actuator in living_room:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")
    
    # Close curtains
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            actuator.turn_off()
    
    # Turn on TV
    for actuator in living_room:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Movie Channel")
    
    # Turn on AC
    for actuator in living_room:
        if isinstance(actuator, AC):
            actuator.turn_on()
            actuator.set_target_temperature(22)


def main():
    home = home_plan()
    
    # Execute plans based on user input
    while True:
        print("\nSelect a plan to execute:")
        print("1. Morning Plan")
        print("2. Leave Home Plan")
        print("3. Movie Plan")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            morning_plan(home)
        elif choice == '2':
            leave_home_plan(home)
        elif choice == '3':
            movie_plan(home)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

        time.sleep(2)  # Add delay for better readability


if __name__ == "__main__":
    main()