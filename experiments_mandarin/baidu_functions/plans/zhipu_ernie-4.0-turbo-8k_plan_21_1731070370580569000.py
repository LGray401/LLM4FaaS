# Based on your functional description and the provided source code, here is the `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN:

from home.home_plan import home_plan, get_room, get_all_actuators, get_room_sensors
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, CoffeeMachine, Light, Door, SmartSocket, SmartTV
import time

def morning_plan(home):
    # Get the LivingRoom
    living_room = get_room(home, "LivingRoom")
    
    if living_room:
        # Open the curtains
        curtains = [a for a in living_room.actuators if isinstance(a, Curtain)]
        for curtain in curtains:
            curtain.turn_on()
        
        # Start the coffee machine
        coffee_machines = [a for a in living_room.actuators if isinstance(a, CoffeeMachine)]
        for coffee_machine in coffee_machines:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("regular")  # Assuming regular coffee for the example
        
        # Check light intensity and adjust lights if necessary
        light_sensors = get_room_sensors(home, "LivingRoom")
        lights = [a for a in living_room.actuators if isinstance(a, Light)]
        
        for sensor in light_sensors:
            if isinstance(sensor, LightIntensiveSensor):
                reading = sensor.get_reading()
                if reading < 300:  # Assuming 300 as the threshold for "dark"
                    for light in lights:
                        light.turn_on()
                        light.set_brightness_level("medium")
    else:
        print("LivingRoom not found.")

def leave_home_plan(home):
    # Iterate through all rooms to lock doors, turn off lights, and turn off sockets
    for room in home:
        doors = [a for a in room.actuators if isinstance(a, Door)]
        lights = [a for a in room.actuators if isinstance(a, Light)]
        sockets = [a for a in room.actuators if isinstance(a, SmartSocket)]
        
        for door in doors:
            door.lock()
        
        for light in lights:
            light.turn_off()
        
        for socket in sockets:
            socket.turn_off()

def movie_plan(home):
    # Get the LivingRoom
    living_room = get_room(home, "LivingRoom")
    
    if living_room:
        # Close the curtains
        curtains = [a for a in living_room.actuators if isinstance(a, Curtain)]
        for curtain in curtains:
            curtain.turn_off()
        
        # Dim the lights
        lights = [a for a in living_room.actuators if isinstance(a, Light)]
        for light in lights:
            light.turn_on()
            light.set_brightness_level("low")
        
        # Turn on the TV and play a movie
        tvs = [a for a in living_room.actuators if isinstance(a, SmartTV)]
        for tv in tvs:
            tv.turn_on()
            tv.play_channel("Movie Channel")  # Assuming a movie channel for the example
    else:
        print("LivingRoom not found.")

if __name__ == "__main__":
    # Create the home plan
    home = home_plan()
    
    # Execute the morning plan
    print("Executing Morning Plan...")
    morning_plan(home)

    # Simulating some delay or other activities
    time.sleep(5)

    # Execute the leave home plan
    print("Executing Leave Home Plan...")
    leave_home_plan(home)
    
    # Simulating some delay or other activities
    time.sleep(5)
    
    # Execute the movie plan
    print("Executing Movie Plan...")
    movie_plan(home)