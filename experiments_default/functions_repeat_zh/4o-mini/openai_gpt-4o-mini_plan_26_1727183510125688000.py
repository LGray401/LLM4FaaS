# Based on your functional description and the provided source code, I will create a `function.py` file that will implement the daily routines for your smart home project. This file will include a main function that orchestrates the various actions you described for the "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN". 
# 
# Here is the `function.py` file:

# functions/function.py

from datetime import datetime
import time
from home.home_plan import home_plan
from home.actuator import Light, Curtain, CoffeeMachine, MusicPlayer, Door, SmartSocket
from home.sensor import LightIntensiveSensor

def morning_plan(home):
    print("Executing Morning Plan...")
    
    # Get the current time
    current_time = datetime.now()
    
    # Turn on lights and adjust brightness according to light intensity
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                # Simulating getting light intensity; in a real case, it would be a sensor reading
                light_sensor = LightIntensiveSensor(room.name)
                light_sensor.turn_on()
                light_intensity = light_sensor.get_reading()
                
                # Adjust brightness based on light intensity
                if light_intensity < 300:
                    actuator.set_brightness_level("high")
                elif 300 <= light_intensity <= 900:
                    actuator.set_brightness_level("medium")
                else:
                    actuator.set_brightness_level("low")
    
    # Make cappuccino
    coffee_machine = None
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, CoffeeMachine):
                coffee_machine = actuator
                break
    
    if coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Cappuccino")

    # Open curtains
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Assuming turn_on opens the curtain

    # Play relaxing music
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, MusicPlayer):
                actuator.turn_on()
                actuator.play_music("Relaxing Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    # Close door, turn off lights, and turn off sockets
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Door):
                actuator.lock()  # Assuming lock function closes the door
            elif isinstance(actuator, Light):
                actuator.turn_off()
            elif isinstance(actuator, SmartSocket):
                actuator.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    
    # Close curtains and dim lights
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Assuming turn_on closes the curtain
            elif isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")  # Dimming lights

def main():
    print("Starting Smart Home System...")
    home = home_plan()
    
    # Execute the morning plan at 7:00 AM
    while True:
        current_time = datetime.now()
        if current_time.hour == 7 and current_time.minute == 0:
            morning_plan(home)
            break
        time.sleep(60)  # Check every minute
    
    # Here you could add other time-based triggers or events as needed
    # For simulation, we can just call leave_home_plan and movie_plan directly
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()