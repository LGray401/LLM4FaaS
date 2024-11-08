# Based on the provided functional description and source code, here's the `function.py` file that contains a `main` function to handle the smart home functionalities.

# function.py
import time

from home.sensor import LightIntensiveSensor, IndoorTemperatureSensor
from home.actuator import Curtain, Light, MusicPlayer, CoffeeMachine
from home_plan import home_plan

def morning_plan():
    # Check if the light is strong enough to turn on the curtain
    for sensor in get_all_sensors(home_plan(), "LightIntensive"):
        if sensor.get_reading() >= LIGHT_INTENSITY_HIGH:
            curtain = get_room_actuators(home_plan(), "Curtain")[0]
            curtain.turn_on()  # Open the curtain

            light = get_room_actuators(home_plan(), "Light")[0]
            light.turn_off()  # Turn off the bedroom light

            music_player = get_room_actuators(home_plan(), "MusicPlayer")[0]
            music_player.turn_on()  # Turn on the music player

            coffee_machine = get_room_actuators(home_plan(), "CoffeeMachine")[0]
            coffee_machine.turn_on()  # Turn on the coffee machine

            time.sleep(5)  # Wait for the coffee to be ready

            coffee_machine.make_coffee("black")  # Make a cup of coffee

            print("Morning Plan executed successfully.")
            break

def leave_home_plan():
    # Lock the door
    door = get_room_actuators(home_plan(), "Door")[0]
    door.lock()  # Lock the door

    # Close the curtains
    curtain = get_room_actuators(home_plan(), "Curtain")[0]
    curtain.turn_off()  # Close the curtain

    # Turn off the lights
    lights = get_room_actuators(home_plan(), "Light")
    for light in lights:
        light.turn_off()  # Turn off the lights

    # Turn off the sockets
    sockets = get_room_actuators(home_plan(), "SmartSocket")
    for socket in sockets:
        socket.turn_off()  # Turn off the sockets

    print("Leave Home Plan executed successfully.")

def movie_plan():
    # Turn off the lights
    lights = get_room_actuators(home_plan(), "Light")
    for light in lights:
        light.turn_off()  # Turn off the lights

    # Turn on the TV
    tv = get_room_actuators(home_plan(), "SmartTV")[0]
    tv.turn_on()  # Turn on the TV

    print("Movie Plan executed successfully.")

def main():
    while True:
        # Execute the morning plan when the light is strong enough
        morning_plan()

        # Execute the leave home plan when the door is locked
        leave_home_plan()

        # Execute the movie plan when the TV is turned on
        movie_plan()

        time.sleep(60)  # Wait for a minute before checking again

if __name__ == "__main__":
    main()