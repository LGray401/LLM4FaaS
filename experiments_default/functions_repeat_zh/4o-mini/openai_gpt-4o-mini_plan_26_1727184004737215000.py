# Based on your functional description and the provided source code, I will create a `function.py` file that implements the described smart home functionalities, including the Morning Plan, Leave Home Plan, and Movie Plan.
# 
# Here's the implementation for `function.py`:

# functions/function.py

from datetime import datetime
import time
from home.home_plan import home_plan
from home.actuator import Light, CoffeeMachine, Curtain, MusicPlayer, Door, SmartSocket

def morning_plan(home):
    current_time = datetime.now().time()
    # Check if the current time is 7:00
    if current_time.hour == 7 and current_time.minute == 0:
        print("Executing Morning Plan...")
        
        # Get the Living Room
        living_room = next(room for room in home if room.name == "LivingRoom")
        
        # Turn on the lights and adjust brightness based on light intensity
        light_sensor = next(sensor for sensor in living_room.sensors if sensor.sensor_type == "LightIntensive")
        light_actuator = next(actuator for actuator in living_room.actuators if isinstance(actuator, Light))
        
        light_intensity = light_sensor.get_reading()
        if light_intensity is not None:
            if light_intensity < 600:  # Assuming 600 lux is the desired brightness level
                light_actuator.turn_on()
                light_actuator.set_brightness_level("high")
            else:
                light_actuator.turn_on()
                light_actuator.set_brightness_level("low")
        
        # Make a cappuccino
        coffee_machine = next(actuator for actuator in living_room.actuators if isinstance(actuator, CoffeeMachine))
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Cappuccino")
        
        # Open the curtains
        curtain_actuator = next(actuator for actuator in living_room.actuators if isinstance(actuator, Curtain))
        curtain_actuator.turn_on()
        
        # Play relaxing music
        music_player = next(actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer))
        music_player.turn_on()
        music_player.play_music("Relaxing Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    # Get the Living Room
    living_room = next(room for room in home if room.name == "LivingRoom")
    
    # Close the door
    door_actuator = next(actuator for actuator in living_room.actuators if isinstance(actuator, Door))
    door_actuator.turn_on()
    door_actuator.lock()

    # Turn off all lights
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

    # Turn off smart sockets
    for actuator in living_room.actuators:
        if isinstance(actuator, SmartSocket):
            actuator.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    # Get the Living Room
    living_room = next(room for room in home if room.name == "LivingRoom")
    
    # Close the curtains
    curtain_actuator = next(actuator for actuator in living_room.actuators if isinstance(actuator, Curtain))
    curtain_actuator.turn_on()

    # Dim the lights
    light_actuator = next(actuator for actuator in living_room.actuators if isinstance(actuator, Light))
    light_actuator.set_brightness_level("low")

def main():
    home = home_plan()
    
    # Here you can add a loop to check time or events, for simplicity I will call each plan once
    morning_plan(home)
    time.sleep(5)  # Sleep to simulate time passing
    leave_home_plan(home)
    time.sleep(5)  # Sleep to simulate time passing
    movie_plan(home)

if __name__ == "__main__":
    main()