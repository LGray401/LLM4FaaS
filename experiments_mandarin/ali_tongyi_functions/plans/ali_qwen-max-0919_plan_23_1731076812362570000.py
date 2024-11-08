# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to execute the different plans (MORNING PLAN, LEAVE HOME PLAN, MOVIE PLAN). The `function.py` will be placed in the `functions` folder.
# 
# ### `functions/function.py`

from home.home_plan import home_plan, get_room_actuators, get_all_sensors
from home.actuator import Curtain, MusicPlayer, Light, Door
from home.sensor import LightIntensiveSensor

def execute_morning_plan(home):
    # Get the LivingRoom actuators
    living_room = get_room_actuators(home, "LivingRoom")
    
    # Open the curtains
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
    
    # Play music
    for actuator in living_room:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")

def execute_leave_home_plan(home):
    # Get the LivingRoom actuators
    living_room = get_room_actuators(home, "LivingRoom")
    
    # Close the door
    for actuator in living_room:
        if isinstance(actuator, Door):
            actuator.lock()
    
    # Open the curtains
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
    
    # Turn off the lights
    for actuator in living_room:
        if isinstance(actuator, Light):
            actuator.turn_off()

def execute_movie_plan(home):
    # Get the LivingRoom actuators
    living_room = get_room_actuators(home, "LivingRoom")
    
    # Close the curtains
    for actuator in living_room:
        if isinstance(actuator, Curtain):
            actuator.turn_off()
    
    # Dim the lights
    for actuator in living_room:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Execute the plans based on the conditions
    while True:
        # Check the light intensity sensor in the LivingRoom
        living_room_sensors = get_room_actuators(home, "LivingRoom")
        light_intensity_sensor = None
        for sensor in living_room_sensors:
            if isinstance(sensor, LightIntensiveSensor):
                light_intensity_sensor = sensor
                break
        
        if light_intensity_sensor:
            light_intensity = light_intensity_sensor.get_reading()
            if light_intensity > 900:
                print("Light intensity is high, executing MORNING PLAN...")
                execute_morning_plan(home)
            else:
                print("Light intensity is not high, no action needed.")
        
        # Simulate user input for other plans
        user_input = input("Enter 'leave' for LEAVE HOME PLAN or 'movie' for MOVIE PLAN: ")
        if user_input == "leave":
            print("Executing LEAVE HOME PLAN...")
            execute_leave_home_plan(home)
        elif user_input == "movie":
            print("Executing MOVIE PLAN...")
            execute_movie_plan(home)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()