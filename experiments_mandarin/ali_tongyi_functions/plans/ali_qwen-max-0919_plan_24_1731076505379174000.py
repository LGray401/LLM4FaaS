# Based on your provided functional description and the source code, I will create a `function.py` file that contains the main function to execute the morning, leave home, and movie plans. The `function.py` will be placed in the `functions` folder.
# 
# Here is the `function.py`:

# functions/function.py

from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, SmartSocket, Door
from home.home_plan import home_plan, get_room_actuators, get_room_sensors

def execute_morning_plan(home):
    # Get the living room actuators and sensors
    living_room = get_room_actuators(home, "LivingRoom")
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Open the curtains
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            actuator.turn_on()

    # Check light intensity and turn on lights if it's dark
    for sensor in living_room_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading is not None and reading < LIGHT_INTENSITY_HIGH:
                for actuator in living_room:
                    if isinstance(actuator, Light):
                        actuator.turn_on()
                        actuator.set_brightness_level("medium")
            sensor.turn_off()

    # Make coffee
    for actuator in living_room:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Latte")
            actuator.turn_off()

    # Play music after coffee is ready
    for actuator in living_room:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")
            actuator.turn_off()

def execute_leave_home_plan(home):
    # Get the living room actuators and sensors
    living_room = get_room_actuators(home, "LivingRoom")
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Check light intensity and open curtains if it's bright
    for sensor in living_room_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading is not None and reading >= LIGHT_INTENSITY_HIGH:
                for actuator in living_room:
                    if isinstance(actuator, Curtain):
                        actuator.turn_on()
            sensor.turn_off()

    # Turn off all lights
    for actuator in living_room:
        if isinstance(actuator, Light):
            actuator.turn_off()

    # Turn off all smart sockets
    for actuator in living_room:
        if isinstance(actuator, SmartSocket):
            actuator.turn_off()

    # Lock the door
    for actuator in living_room:
        if isinstance(actuator, Door):
            actuator.lock()

def execute_movie_plan(home):
    # Get the living room actuators
    living_room = get_room_actuators(home, "LivingRoom")

    # Close the curtains
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            actuator.turn_off()

    # Turn off all lights
    for actuator in living_room:
        if isinstance(actuator, Light):
            actuator.turn_off()

def main():
    # Initialize the home plan
    home = home_plan()

    # Execute the morning plan
    print("\nExecuting Morning Plan...")
    execute_morning_plan(home)

    # Execute the leave home plan
    print("\nExecuting Leave Home Plan...")
    execute_leave_home_plan(home)

    # Execute the movie plan
    print("\nExecuting Movie Plan...")
    execute_movie_plan(home)

if __name__ == "__main__":
    main()