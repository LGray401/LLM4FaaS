# Based on your functional description and the provided source code, I will create a `function.py` file that implements the various plans you specified (MORNING PLAN, LEAVE HOME PLAN, MOVIE PLAN) using the sensors and actuators from your existing code. 
# 
# Here is the code for `function.py`:

# function.py
import time
from home.home_plan import home_plan
from home.actuator import Light, CoffeeMachine, Curtain, MusicPlayer, Door, SmartSocket

def morning_plan(home):
    print("Executing Morning Plan...")
    
    for room in home:
        # Control lights based on light intensity
        light_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
        light_actuator = next((actuator for actuator in room.actuators if isinstance(actuator, Light)), None)
        
        if light_sensor and light_actuator:
            light_sensor.turn_on()
            light_intensity = light_sensor.get_reading() or 500  # Default to 500 if reading fails
            if light_intensity < LIGHT_INTENSITY_LOW:
                light_actuator.set_brightness_level("high")
            elif light_intensity > LIGHT_INTENSITY_HIGH:
                light_actuator.set_brightness_level("low")
            else:
                light_actuator.set_brightness_level("medium")
        
        # Make cappuccino
        coffee_machine = next((actuator for actuator in room.actuators if isinstance(actuator, CoffeeMachine)), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("cappuccino")

        # Open curtains
        curtain = next((actuator for actuator in room.actuators if isinstance(actuator, Curtain)), None)
        if curtain:
            curtain.turn_on()  # Assuming turning on opens the curtain
        
        # Play relaxing music
        music_player = next((actuator for actuator in room.actuators if isinstance(actuator, MusicPlayer)), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("Relaxing Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    for room in home:
        door = next((actuator for actuator in room.actuators if isinstance(actuator, Door)), None)
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        smart_sockets = [actuator for actuator in room.actuators if isinstance(actuator, SmartSocket)]
        
        if door:
            door.lock()  # Lock the door
        for light in lights:
            light.turn_off()  # Turn off all lights
        for socket in smart_sockets:
            socket.turn_off()  # Turn off all smart sockets

def movie_plan(home):
    print("Executing Movie Plan...")
    
    for room in home:
        curtain = next((actuator for actuator in room.actuators if isinstance(actuator, Curtain)), None)
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        
        if curtain:
            curtain.turn_on()  # Assuming turning on closes the curtains
        for light in lights:
            light.set_brightness_level("low")  # Dim the lights

def main():
    home = home_plan()
    
    # Example calls
    current_time = time.localtime().tm_hour
    if current_time == 7:  # Assuming this function is called every hour
        morning_plan(home)
    
    # Simulate leaving home
    leave_home_plan(home)

    # Simulate watching a movie
    movie_plan(home)

if __name__ == "__main__":
    main()