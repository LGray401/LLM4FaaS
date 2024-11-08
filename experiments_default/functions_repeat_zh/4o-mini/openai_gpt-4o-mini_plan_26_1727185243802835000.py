# Based on your functional description and the provided source code, I will create a `function.py` file that implements the required functionalities for your smart home project. The functions will manage the morning plan, leave home plan, and movie plan as described.
# 
# Here's the `function.py` file content:

# function.py
import time
from datetime import datetime
from home.home_plan import home_plan
from home.actuator import Light, Curtain, CoffeeMachine, MusicPlayer, Door, SmartSocket

def morning_plan(home):
    current_time = datetime.now().time()
    if current_time.hour == 7 and current_time.minute == 0:  # Check if it's 7:00 AM
        print("Executing morning plan...")

        # Turn on lights and adjust brightness based on light intensity
        light_sensors = get_all_sensors(home, "LightIntensive")
        for sensor in light_sensors:
            sensor.turn_on()
            light_intensity = sensor.get_reading()
            if light_intensity is not None:
                if light_intensity < 600:  # Assuming 600 lux is the normal level
                    adjust_lights(home, "high")
                elif light_intensity < 900:
                    adjust_lights(home, "medium")
                else:
                    adjust_lights(home, "low")

        # Make coffee
        coffee_machine = get_all_actuators(home, "CoffeeMachine")
        if coffee_machine:
            coffee_machine[0].turn_on()
            coffee_machine[0].make_coffee("Cappuccino")
            coffee_machine[0].turn_off()

        # Open curtains
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_on()

        # Play relaxing music
        music_players = get_all_actuators(home, "MusicPlayer")
        for player in music_players:
            player.turn_on()
            player.play_music("Relaxing Playlist")

def leave_home_plan(home):
    print("Executing leave home plan...")
    # Close door
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()

    # Turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # Turn off all sockets
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()

def movie_plan(home):
    print("Executing movie plan...")
    # Close curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # Dim lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.set_brightness_level("low")

def adjust_lights(home, brightness_level):
    print(f"Adjusting lights to {brightness_level.upper()} brightness.")
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.set_brightness_level(brightness_level)

def get_all_sensors(home, sensor_type):
    return [sensor for room in home for sensor in room.sensors if sensor.sensor_type == sensor_type]

def get_all_actuators(home, actuator_type):
    return [actuator for room in home for actuator in room.actuators if actuator.actuator_type == actuator_type]

def main():
    home = home_plan()
    
    # Example of executing plans
    morning_plan(home)
    time.sleep(1)  # Simulate waiting time to test other functions
    leave_home_plan(home)
    time.sleep(1)
    movie_plan(home)

if __name__ == "__main__":
    main()