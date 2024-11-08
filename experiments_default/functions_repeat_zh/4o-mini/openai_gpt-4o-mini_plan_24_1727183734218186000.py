# Based on the functional description provided for your smart home project, I will create the `function.py` file that contains a main function to execute the morning plan, leave home plan, and movie plan. This will involve interacting with the sensors and actuators defined in your existing code.
# 
# Here’s the `function.py` code that meets your requirements:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door
from home.sensor import LightIntensiveSensor
from home.logger_config import logger

def morning_plan(home):
    print("Executing Morning Plan...")
    
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    if living_room:
        curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
        light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
        coffee_machine = next((actuator for actuator in living_room.actuators if isinstance(actuator, CoffeeMachine)), None)
        music_player = next((actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)), None)
        
        # Open curtains
        if curtain:
            curtain.turn_on()
        
        # Check light intensity
        light_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor)), None)
        if light_sensor and light_sensor.get_reading() < 300:  # Assuming 300 lux as the threshold for the light
            if light:
                light.turn_on()
        
        # Make coffee
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")  # Example coffee type
        
        # Play music
        if music_player:
            music_player.turn_on()
            music_player.play_music("Morning Playlist")  # Example playlist

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    if living_room:
        curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
        light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
        door = next((actuator for actuator in living_room.actuators if isinstance(actuator, Door)), None)

        # Open curtains if sunny (for simplicity, we assume it's sunny)
        if curtain:
            curtain.turn_on()

        # Turn off light and other devices
        if light:
            light.turn_off()
        
        # Lock the door
        if door:
            door.lock()

def movie_plan(home):
    print("Executing Movie Plan...")
    
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    if living_room:
        curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
        light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)

        # Close curtains
        if curtain:
            curtain.turn_off()

        # Turn off lights
        if light:
            light.turn_off()

def main():
    home = home_plan()
    
    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()