# Based on the functional description and the provided source code, here's the `function.py` file that implements the required functionality for your smart home project.

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door
from home.sensor import LightIntensiveSensor
from random import choice


def morning_plan(home):
    print("\n--- Morning Plan Activated ---")

    # Get the living room
    living_room = home[0]  # Assuming the first room is the Living Room

    # Open curtains
    curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
    if curtain:
        curtain.turn_on()

    # Check light intensity
    light_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
    if light_sensor and light_sensor.get_reading() < 500:  # Assume 500 lux is the threshold for turning on lights
        light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
        if light:
            light.turn_on()

    # Make coffee
    coffee_machine = next((actuator for actuator in living_room.actuators if isinstance(actuator, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")  # Assuming we make an Espresso

    # Play music
    music_player = next((actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)), None)
    if music_player:
        music_player.turn_on()
        music_player.play_music("Morning Playlist")


def leave_home_plan(home):
    print("\n--- Leave Home Plan Activated ---")

    # Get the living room
    living_room = home[0]

    # Open curtains if sunny
    light_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
    if light_sensor and light_sensor.get_reading() >= 500:  # Assume sunny condition
        curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
        if curtain:
            curtain.turn_on()

    # Turn off lights and sockets
    light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
    if light:
        light.turn_off()

    smart_socket = next((actuator for actuator in living_room.actuators if isinstance(actuator, SmartSocket)), None)
    if smart_socket:
        smart_socket.turn_off()

    # Lock the door
    door = next((actuator for actuator in living_room.actuators if isinstance(actuator, Door)), None)
    if door:
        door.lock()


def movie_plan(home):
    print("\n--- Movie Plan Activated ---")

    # Get the living room
    living_room = home[0]

    # Close curtains
    curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
    if curtain:
        curtain.turn_off()

    # Turn off lights
    light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
    if light:
        light.turn_off()


def main():
    home = home_plan()

    # Example usage
    current_plan = choice([morning_plan, leave_home_plan, movie_plan])
    current_plan(home)


if __name__ == "__main__":
    main()