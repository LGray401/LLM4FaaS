# Based on your functional description and the provided source code, I will now provide a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Light, Curtain, CoffeeMachine, MusicPlayer, Door, SmartSocket
import time
import datetime

def morning_plan(home):
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    
    if living_room:
        # Turn on the lights
        lights = [actuator for actuator in living_room.actuators if actuator.actuator_type == "Light"]
        for light in lights:
            light.turn_on()
        
        # Adjust light brightness based on indoor light intensity
        light_sensors = get_all_sensors(home, "LightIntensive")
        if light_sensors:
            for sensor in light_sensors:
                if sensor.room_name == "LivingRoom":
                    sensor.turn_on()
                    reading = sensor.get_reading()
                    # Assuming a target light intensity range for normal level
                    target_intensity = (300, 900)  # Example range
                    if reading < target_intensity[0]:
                        # Increase light brightness to medium or high
                        light.set_brightness_level("medium")  # or "high" based on preference
                    elif reading > target_intensity[1]:
                        # Decrease light brightness to low
                        light.set_brightness_level("low")
                    # Turn off the sensor after use
                    sensor.turn_off()
                    break  # Assuming only one light sensor in the living room

        # Make a cappuccino
        coffee_machines = [actuator for actuator in living_room.actuators if actuator.actuator_type == "CoffeeMachine"]
        if coffee_machines:
            coffee_machines[0].turn_on()
            coffee_machines[0].make_coffee("cappuccino")
            # Optionally turn off the coffee machine after use
            # coffee_machines[0].turn_off()

        # Open the curtains
        curtains = [actuator for actuator in living_room.actuators if actuator.actuator_type == "Curtain"]
        for curtain in curtains:
            curtain.turn_on()  # Assuming turn_on() opens the curtain, modify if needed

        # Play relaxing music
        music_players = [actuator for actuator in living_room.actuators if actuator.actuator_type == "MusicPlayer"]
        if music_players:
            music_players[0].turn_on()
            music_players[0].play_music("relaxing_music")  # Assuming a predefined playlist named "relaxing_music"
            # Optionally turn off the music player after a while
            # time.sleep(300)  # Play for 5 minutes
            # music_players[0].turn_off()

def leave_home_plan(home):
    # Iterate through all rooms to turn off lights, sockets, and close doors
    for room in home:
        # Turn off lights
        lights = [actuator for actuator in room.actuators if actuator.actuator_type == "Light"]
        for light in lights:
            light.turn_off()
        
        # Turn off sockets
        sockets = [actuator for actuator in room.actuators if actuator.actuator_type == "SmartSocket"]
        for socket in sockets:
            socket.turn_off()
        
        # Close doors
        doors = [actuator for actuator in room.actuators if actuator.actuator_type == "Door"]
        for door in doors:
            door.turn_off()  # Assuming turn_off() closes the door, modify if needed
            door.lock()  # Lock the door

def movie_plan(home):
    # Get the living room
    living_room = get_room(home, "LivingRoom")
    
    if living_room:
        # Close the curtains
        curtains = [actuator for actuator in living_room.actuators if actuator.actuator_type == "Curtain"]
        for curtain in curtains:
            curtain.turn_off()  # Assuming turn_off() closes the curtain, modify if needed

        # Dim the lights
        lights = [actuator for actuator in living_room.actuators if actuator.actuator_type == "Light"]
        for light in lights:
            light.set_brightness_level("low")

# Example usage (this would typically be called from your main program)
if __name__ == "__main__":
    # Create the home plan
    home = home_plan()

    # Schedule the morning plan to run at 7 AM
    while True:
        current_time = datetime.datetime.now().time()
        if current_time.hour == 7 and current_time.minute == 0:
            morning_plan(home)
            break
        time.sleep(60)  # Check every minute

    # Example calls for leave_home_plan and movie_plan (you would call these based on your specific triggers)
    # leave_home_plan(home)
    # movie_plan(home)