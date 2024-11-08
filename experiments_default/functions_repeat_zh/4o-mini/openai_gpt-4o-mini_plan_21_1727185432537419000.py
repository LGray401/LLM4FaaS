# Based on your functional description and the provided source code files, here's how the `function.py` file can be structured. This file will implement the main function that orchestrates the smart home functionalities according to the specified plans (Morning Plan, Leave Home Plan, and Movie Plan).
# 
# ### Code for `function.py`

# function.py
from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors
from home.actuator import CoffeeMachine, Light, Curtain, Door, SmartTV
from home.sensor import LightIntensiveSensor

def morning_plan(home):
    print("Executing Morning Plan...")
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")

    # Set alarm to 7 AM (this part is conceptual as it depends on your alarm implementation)
    print("Setting alarm to 7 AM...")

    # Open curtains
    curtain = next((a for a in living_room.actuators if isinstance(a, Curtain)), None)
    if curtain:
        curtain.turn_on()

    # Start coffee machine
    coffee_machine = next((a for a in kitchen.actuators if isinstance(a, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")  # Example coffee type

    # Check light intensity and adjust accordingly
    light_sensor = next((s for s in living_room.sensors if isinstance(s, LightIntensiveSensor)), None)
    if light_sensor:
        light_sensor.turn_on()
        light_reading = light_sensor.get_reading()
        if light_reading and light_reading < 500:  # Example threshold
            light = next((a for a in living_room.actuators if isinstance(a, Light)), None)
            if light:
                light.turn_on()
                light.set_brightness_level("medium")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    living_room = get_room(home, "LivingRoom")

    # Lock the door
    door = next((a for a in living_room.actuators if isinstance(a, Door)), None)
    if door:
        door.lock()

    # Turn off lights
    lights = get_room_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # Disconnect all smart sockets (assuming we have a method for this)
    smart_sockets = get_room_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room(home, "LivingRoom")

    # Close curtains
    curtain = next((a for a in living_room.actuators if isinstance(a, Curtain)), None)
    if curtain:
        curtain.turn_off()

    # Dim lights
    light = next((a for a in living_room.actuators if isinstance(a, Light)), None)
    if light:
        light.turn_on()
        light.set_brightness_level("low")

    # Turn on TV and play a movie
    smart_tv = next((a for a in living_room.actuators if isinstance(a, SmartTV)), None)
    if smart_tv:
        smart_tv.turn_on()
        smart_tv.play_channel("Movie Channel")  # Example channel

def main():
    home = home_plan()
    
    # Execute the plans based on user input or some conditions
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()