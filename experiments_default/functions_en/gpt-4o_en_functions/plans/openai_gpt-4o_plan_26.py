# Sure, I'll create a `function.py` file based on your functional descriptions and the provided code. The `function.py` will implement the main functions to handle the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. Here it is:
# 
# ### functions/function.py

import time
from home.home_plan import home_plan, get_room, get_all_actuators, get_all_sensors
from home.config import LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def morning_plan(home):
    # Get all necessary actuators
    lights = get_all_actuators(home, "Light")
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    curtains = get_all_actuators(home, "Curtain")
    music_players = get_all_actuators(home, "MusicPlayer")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Turn on the lights and adjust brightness
    for light in lights:
        light.turn_on()
        # Adjust brightness based on light sensor reading
        for sensor in light_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading:
                if reading < LIGHT_INTENSITY_LOW:
                    light.set_brightness_level("high")
                elif reading > LIGHT_INTENSITY_HIGH:
                    light.set_brightness_level("low")
                else:
                    light.set_brightness_level("medium")

    # Make coffee
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("cappuccino")

    # Open curtains
    for curtain in curtains:
        curtain.turn_on()

    # Play relaxing music
    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("relaxing")

def leave_home_plan(home):
    # Get all necessary actuators
    doors = get_all_actuators(home, "Door")
    lights = get_all_actuators(home, "Light")
    sockets = get_all_actuators(home, "SmartSocket")

    # Close doors
    for door in doors:
        door.lock()

    # Turn off lights
    for light in lights:
        light.turn_off()

    # Disconnect power sockets
    for socket in sockets:
        socket.turn_off()

def movie_plan(home):
    # Get all necessary actuators
    curtains = get_all_actuators(home, "Curtain")
    lights = get_all_actuators(home, "Light")

    # Draw curtains
    for curtain in curtains:
        curtain.turn_on()

    # Dim the lights
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")

def main():
    home = home_plan()
    print("Choose a plan to execute:")
    print("1. Morning Plan")
    print("2. Leave Home Plan")
    print("3. Movie Plan")
    choice = input("Enter the number of the plan you want to execute: ")

    if choice == '1':
        morning_plan(home)
    elif choice == '2':
        leave_home_plan(home)
    elif choice == '3':
        movie_plan(home)
    else:
        print("Invalid choice. Please select a valid plan.")

if __name__ == "__main__":
    main()