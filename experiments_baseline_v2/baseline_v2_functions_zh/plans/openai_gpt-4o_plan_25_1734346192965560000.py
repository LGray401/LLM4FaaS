# To create a smart home application based on your functional description, we will implement three main plans: "Morning Plan," "Leave Home Plan," and "Movie Plan." These plans will use the sensors and actuators defined in the provided source code files.
# 
# Here's how we can implement these plans:
# 
# 1. **Morning Plan**:
#    - Triggered when the light intensity sensor in the bedroom detects a certain threshold.
#    - Actions: Open curtains, turn off bedroom lights, turn on the music player, and start the coffee machine.
# 
# 2. **Leave Home Plan**:
#    - Triggered by a command to lock the main entrance door.
#    - Actions: Close curtains, turn off indoor lights, and switch off smart sockets.
# 
# 3. **Movie Plan**:
#    - Triggered by a command to turn on the TV.
#    - Actions: Close curtains and dim indoor lights.
# 
# Let's create a `smart_home.py` file that implements these functionalities:
# 
# ```python
import time
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, MusicPlayer, CoffeeMachine, Door, SmartSocket, SmartTV
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

# Initialize the home with all rooms and their components
home = home_plan()

def morning_plan():
    # Get bedroom sensors and actuators
    bedroom_sensors = get_room_sensors(home, "Bedroom")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    
    # Check light intensity to trigger the morning routine
    for sensor in bedroom_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            sensor.turn_on()
            light_intensity = sensor.get_reading()
            if light_intensity and light_intensity >= 900:
                for actuator in bedroom_actuators:
                    if isinstance(actuator, Curtain):
                        actuator.turn_on()  # Open curtains
                    elif isinstance(actuator, Light):
                        actuator.turn_off()  # Turn off lights
                    elif isinstance(actuator, MusicPlayer):
                        actuator.turn_on()
                        actuator.play_music("morning_playlist")
                    elif isinstance(actuator, CoffeeMachine):
                        actuator.turn_on()
                        actuator.make_coffee("espresso")
            sensor.turn_off()

def leave_home_plan():
    # Get living room actuators
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Lock the door and perform actions
    for actuator in living_room_actuators:
        if isinstance(actuator, Door):
            actuator.lock()
            for act in living_room_actuators:
                if isinstance(act, Curtain) or isinstance(act, Light) or isinstance(act, SmartSocket):
                    act.turn_off()

def movie_plan():
    # Get living room actuators
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Turn on the TV and perform actions
    for actuator in living_room_actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("favorite_movie_channel")
            for act in living_room_actuators:
                if isinstance(act, Curtain):
                    act.turn_off()  # Close curtains
                elif isinstance(act, Light):
                    act.turn_on()
                    act.set_brightness_level("low")  # Dim lights

def main():
    morning_plan()
    time.sleep(5)  # Simulate time between plans
    leave_home_plan()
    time.sleep(5)  # Simulate time between plans
    movie_plan()

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# You can run this application in a Linux terminal by executing the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This script initializes the smart home system, defines the plans according to the functional description, and executes these plans sequentially. Adjust the timings and conditions as needed to fit the specific requirements of your smart home environment.