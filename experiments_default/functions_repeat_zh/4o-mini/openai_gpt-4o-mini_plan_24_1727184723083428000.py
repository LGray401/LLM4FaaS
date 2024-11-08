# Based on the functional description you provided, I'll create a `function.py` file that implements the three plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. This file will utilize the classes defined in your existing source code to automate the execution of these plans.
# 
# Here’s the `function.py` file that you can place in your `functions` folder:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door, Window
from home.sensor import LightIntensiveSensor

def morning_plan(home):
    print("Executing Morning Plan...")
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    
    # Open curtains
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
            print(f"Curtains in {living_room.name} opened.")

    # Check light intensity sensor in the living room
    light_sensor = get_room_sensors(home, "LivingRoom")
    if light_sensor:
        light_reading = next((s for s in light_sensor if isinstance(s, LightIntensiveSensor)), None)
        if light_reading and light_reading.get_reading() < 500:  # Assuming 500 lux as a threshold for a cloudy day
            light_actuator = next((a for a in living_room.actuators if isinstance(a, Light)), None)
            if light_actuator:
                light_actuator.turn_on()
                print("Light turned on due to cloudy weather.")

    # Make coffee
    coffee_machine = next((a for a in get_room_actuators(home, "Kitchen") if isinstance(a, CoffeeMachine)), None)
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("espresso")
        print("Coffee is being made.")

    # Play music
    music_player = next((a for a in living_room.actuators if isinstance(a, MusicPlayer)), None)
    if music_player:
        music_player.turn_on()
        music_player.play_music("Morning Playlist")
        print("Playing morning music.")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    living_room = get_room(home, "LivingRoom")
    
    # Open curtains if sunny
    light_sensor = next((s for s in get_room_sensors(home, "LivingRoom") if isinstance(s, LightIntensiveSensor)), None)
    if light_sensor and light_sensor.get_reading() > 500:  # Assuming 500 lux as a threshold for a sunny day
        curtain = next((a for a in living_room.actuators if isinstance(a, Curtain)), None)
        if curtain:
            curtain.turn_on()
            print("Curtains opened in Living Room.")

    # Turn off lights and smart sockets
    for actuator in living_room.actuators:
        if isinstance(actuator, Light) or isinstance(actuator, SmartSocket):
            actuator.turn_off()
            print(f"{actuator.actuator_type} in {living_room.name} turned off.")

    # Lock the door
    door = next((a for a in living_room.actuators if isinstance(a, Door)), None)
    if door:
        door.lock()
        print("Door locked.")

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room(home, "LivingRoom")

    # Close curtains
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()  # Assuming turn_off closes the curtains
            print("Curtains closed in Living Room.")

    # Turn off lights
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()
            print("Lights turned off in Living Room.")

def main():
    home = home_plan()
    
    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()