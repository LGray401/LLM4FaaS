# Based on your functional description and the provided source code files for your smart home project, I will create a `function.py` file that implements the main functionality for the morning plan, leave home plan, and movie plan.
# 
# Here's the implementation of `function.py`:

# functions/function.py

import time
from datetime import datetime
from home.home_plan import home_plan
from home.actuator import Light, CoffeeMachine, Curtain, MusicPlayer, Door, SmartSocket

def morning_plan(home):
    current_time = datetime.now().time()
    if current_time.hour == 7 and current_time.minute == 0:
        print("Executing Morning Plan...")
        
        # Turn on lights and adjust brightness based on light intensity
        living_room = get_room(home, "LivingRoom")
        light_sensor = get_all_sensors(living_room, "LightIntensive")[0]  # Assuming there's only one sensor
        light_sensor.turn_on()
        light_intensity = light_sensor.get_reading()
        
        light_actuator = get_all_actuators(living_room, "Light")[0]  # Assuming there's only one light
        if light_intensity < 300:
            light_actuator.set_brightness_level("high")
        elif light_intensity < 600:
            light_actuator.set_brightness_level("medium")
        else:
            light_actuator.set_brightness_level("low")

        # Make cappuccino
        kitchen = get_room(home, "Kitchen")
        coffee_machine = get_all_actuators(kitchen, "CoffeeMachine")[0]
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Cappuccino")

        # Open curtains
        curtain = get_all_actuators(living_room, "Curtain")[0]
        curtain.turn_on()

        # Play relaxing music
        music_player = get_all_actuators(living_room, "MusicPlayer")[0]
        music_player.turn_on()
        music_player.play_music("Relaxing Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    # Close door
    living_room = get_room(home, "LivingRoom")
    door = get_all_actuators(living_room, "Door")[0]
    door.lock()  # Assuming locking is what you mean by closing

    # Turn off all lights
    for light in get_all_actuators(home, "Light"):
        light.turn_off()

    # Turn off all smart sockets
    for socket in get_all_actuators(home, "SmartSocket"):
        socket.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room(home, "LivingRoom")
    
    # Pull down curtains
    curtain = get_all_actuators(living_room, "Curtain")[0]
    curtain.turn_on()  # Assuming turning on pulls curtains down

    # Dim lights
    for light in get_all_actuators(living_room, "Light"):
        light.set_brightness_level("low")

def main():
    home = home_plan()
    
    # Here you would typically have a loop that checks the time or events
    while True:
        morning_plan(home)
        leave_home_plan(home)
        movie_plan(home)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()