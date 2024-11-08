# Based on your functional description and the provided source code files, I will create a `function.py` file that implements the three plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. The main function will orchestrate these actions based on the specified conditions.
# 
# Here is the `function.py` file:

# function.py
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Door, Light, SmartTV
from home.home_plan import home_plan
from home.config import LIGHT_INTENSITY_LOW

def morning_plan(home):
    # Get the light intensity sensor from the Living Room
    light_sensor = None
    for room in home:
        if room.name == "LivingRoom":
            light_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
            break

    if light_sensor and light_sensor.get_reading() >= LIGHT_INTENSITY_LOW:
        # Open curtains
        curtain = next((actuator for actuator in room.actuators if isinstance(actuator, Curtain)), None)
        if curtain:
            curtain.turn_on()

        # Turn off bedroom lights
        bedroom = next((room for room in home if room.name == "Bedroom"), None)
        if bedroom:
            bedroom_lights = [actuator for actuator in bedroom.actuators if isinstance(actuator, Light)]
            for light in bedroom_lights:
                light.turn_off()

        # Turn on music player
        music_player = next((actuator for actuator in room.actuators if isinstance(actuator, MusicPlayer)), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("Morning Playlist")

        # Start coffee machine and make coffee
        coffee_machine = next((actuator for actuator in room.actuators if isinstance(actuator, CoffeeMachine)), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")


def leave_home_plan(home):
    # Lock the door
    door = next((actuator for room in home for actuator in room.actuators if isinstance(actuator, Door)), None)
    if door:
        door.lock()

    # Close curtains
    curtains = [actuator for room in home for actuator in room.actuators if isinstance(actuator, Curtain)]
    for curtain in curtains:
        curtain.turn_off()

    # Turn off all lights
    lights = [actuator for room in home for actuator in room.actuators if isinstance(actuator, Light)]
    for light in lights:
        light.turn_off()

    # Disconnect all smart sockets
    smart_sockets = [actuator for room in home for actuator in room.actuators if isinstance(actuator, SmartSocket)]
    for socket in smart_sockets:
        socket.turn_off()


def movie_plan(home):
    # Turn on the TV
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    tv = next((actuator for actuator in living_room.actuators if isinstance(actuator, SmartTV)), None)
    if tv:
        tv.turn_on()
        tv.play_channel("Movie Channel")

        # Draw the curtains
        curtains = [actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)]
        for curtain in curtains:
            curtain.turn_on()

        # Dim the lights
        lights = [actuator for actuator in living_room.actuators if isinstance(actuator, Light)]
        for light in lights:
            light.set_brightness_level("low")


def main():
    # Initialize home plan
    home = home_plan()

    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()