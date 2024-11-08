# Based on your functional description and the provided source code, here's a `function.py` file that contains the main functions to execute the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. I've assumed certain behaviors for these plans based on the available components and their methods.
# 
# ### function.py

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, NotificationSender
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def morning_plan(home):
    # Wake up when the alarm goes off (simulated by turning on a light or sending a notification)
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        # Turn on the light
        for actuator in bedroom.actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_on()
                break
        
        # Optionally, send a notification
        for actuator in bedroom.actuators:
            if actuator.actuator_type == "NotificationSender":
                actuator.turn_on()
                actuator.notification_sender("Good morning! Time to wake up.")
                break

def leave_home_plan(home):
    # Turn off all unnecessary devices and lock doors
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type in ["Light", "AC", "Heater", "MusicPlayer", "SmartTV"]:
                actuator.turn_off()
            elif actuator.actuator_type == "Door":
                actuator.lock()

def movie_plan(home):
    # Set up the living room for movie watching
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Turn off the lights
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
        
        # Turn on the TV
        for actuator in living_room.actuators:
            if actuator.actuator_type == "SmartTV":
                actuator.turn_on()
                actuator.play_channel("Movie Channel")  # Assuming a movie channel exists
                break
        
        # Adjust the curtains
        for actuator in living_room.actuators:
            if actuator.actuator_type == "Curtain":
                actuator.turn_off()  # Assuming turn_off means closing the curtains
                break
        
        # Optionally, turn on the AC to a comfortable temperature
        for actuator in living_room.actuators:
            if actuator.actuator_type == "AC":
                actuator.turn_on()
                actuator.set_target_temperature(22)  # Set to a comfortable temperature
                break

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Execute the morning plan
    print("Executing Morning Plan...")
    morning_plan(home)
    time.sleep(5)  # Wait for a while (simulate time passing)
    
    # Execute the leave home plan
    print("Executing Leave Home Plan...")
    leave_home_plan(home)
    time.sleep(5)  # Wait for a while (simulate time passing)
    
    # Execute the movie plan
    print("Executing Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()