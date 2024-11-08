# Sure, I will create the 'function.py' file for your smart home project based on the functional description and the provided source code.
# 
# Here is the 'function.py' file:

from home_plan import get_room_sensors, get_room_actuators, print_home_plan, get_all_sensors, get_all_actuators, Room
from home.sensor import Sensor
from home.actuator import Actuator, NotificationSender


def morning_plan():
    print("------ Morning Plan ------")

    # Get the sensors and actuators for the specific room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Turn on the sensors
    for sensor in living_room_sensors:
        sensor.turn_on()

    # Turn on the music player
    music_player = next(
        (actuator for actuator in living_room_actuators if isinstance(actuator, MusicPlayer)), None)
    if music_player:
        music_player.turn_on()

    # Play the music playlist
    if music_player:
        music_player.play_music("Jay Chou Playlist")

    # Turn on the coffee machine
    coffee_machine = next(
        (actuator for actuator in living_room_actuators if isinstance(actuator, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.turn_on()

    # Make coffee
    if coffee_machine:
        coffee_machine.make_coffee("latte")

    # Print the updated home plan
    print_home_plan(home)


def leave_home_plan():
    print("------ Leave Home Plan ------")

    # Get all the light actuators in the home
    light_actuators = get_all_actuators(home, "Light")

    # Turn off the lights
    for light_actuator in light_actuators:
        light_actuator.turn_off()

    # Get the door actuator in the living room
    living_room_door = next(
        (actuator for actuator in living_room_actuators if isinstance(actuator, Door)), None)
    if living_room_door:
        # Lock the door
        living_room_door.lock()

    # Print the updated home plan
    print_home_plan(home)


def movie_plan():
    print("------ Movie Plan ------")

    # Get the sensors and actuators for the specific room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Close the curtains
    curtains = next(
        (actuator for actuator in living_room_actuators if isinstance(actuator, Curtain)), None)
    if curtains:
        curtains.turn_on()

    # Dim the lights
    lights = next(
        (actuator for actuator in living_room_actuators if isinstance(actuator, Light)), None)
    if lights:
        lights.set_brightness_level("low")

    # Print the updated home plan
    print_home_plan(home)


if __name__ == "__main__":
    # Create the home plan
    home = home_plan()

    # Execute the morning plan
    morning_plan()

    # Execute the leave home plan
    leave_home_plan()

    # Execute the movie plan
    movie_plan()