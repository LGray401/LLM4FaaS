# Based on the functional description you provided for your smart home project, I will create a `function.py` file that implements the specified morning, leave home, and movie plans. The file will utilize the classes defined in the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.
# 
# Here's the implementation of `function.py`:

# function.py
import time
from datetime import datetime
from home.home_plan import home_plan
from home.actuator import Light, CoffeeMachine, Curtain, MusicPlayer, Door, SmartSocket

def morning_plan(home):
    current_time = datetime.now()
    # Check if the current time is 7:00 AM
    if current_time.hour == 7 and current_time.minute == 0:
        # Assuming the house layout and actuator types are set correctly
        living_room = next((room for room in home if room.name == "LivingRoom"), None)
        if living_room is not None:
            # Turn on the lights and adjust brightness based on light intensity sensor
            light_sensor = next((sensor for sensor in living_room.sensors if sensor.sensor_type == "LightIntensive"), None)
            light_actuator = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
            if light_sensor and light_actuator:
                light_sensor.turn_on()
                light_intensity = light_sensor.get_reading()
                if light_intensity is not None:
                    if light_intensity < 600:  # Example threshold
                        light_actuator.turn_on()
                        light_actuator.set_brightness_level('high')
                    else:
                        light_actuator.set_brightness_level('low')

            # Make a cappuccino
            coffee_machine = next((actuator for actuator in living_room.actuators if isinstance(actuator, CoffeeMachine)), None)
            if coffee_machine:
                coffee_machine.turn_on()
                coffee_machine.make_coffee("Cappuccino")

            # Open the curtains
            curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
            if curtain:
                curtain.turn_on()

            # Play relaxing music
            music_player = next((actuator for actuator in living_room.actuators if isinstance(actuator, MusicPlayer)), None)
            if music_player:
                music_player.turn_on()
                music_player.play_music("Relaxing Playlist")

def leave_home_plan(home):
    # Close the door, turn off all lights and sockets when leaving home
    for room in home:
        door = next((actuator for actuator in room.actuators if isinstance(actuator, Door)), None)
        if door:
            door.lock()
        
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
            elif isinstance(actuator, SmartSocket):
                actuator.turn_off()

def movie_plan(home):
    # When watching a movie, close curtains and dim lights
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    if living_room is not None:
        curtain = next((actuator for actuator in living_room.actuators if isinstance(actuator, Curtain)), None)
        if curtain:
            curtain.turn_on()  # Close curtains

        light_actuator = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
        if light_actuator:
            light_actuator.set_brightness_level('low')  # Dim lights

def main():
    home = home_plan()  # Initialize the home plan

    # Example of invoking the plans
    while True:
        morning_plan(home)
        time.sleep(60)  # Sleep for a minute before checking again (for demo purposes)
        leave_home_plan(home)
        time.sleep(60)  # Sleep for a minute before checking again (for demo purposes)
        movie_plan(home)
        time.sleep(60)  # Sleep for a minute before checking again (for demo purposes)

if __name__ == "__main__":
    main()