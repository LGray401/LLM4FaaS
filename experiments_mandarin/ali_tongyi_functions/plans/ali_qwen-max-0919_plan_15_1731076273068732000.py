# Based on your provided functional description and the source code, I will create a `function.py` file that contains the main function to execute different plans (MORNING PLAN, LEAVE HOME PLAN, MOVIE PLAN). Since the detailed steps for each plan were not fully specified in your request, I will make some assumptions about what actions these plans might include. You can adjust these as per your requirements.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import Light, AC, Heater, CoffeeMachine, MusicPlayer, SmartTV, CleaningRobot, NotificationSender
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION
import time

def morning_plan(home):
    print("\n--- Starting Morning Plan ---")
    
    # Get the Bedroom
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        # Turn on the lights in the bedroom
        for actuator in get_room_actuators(home, "Bedroom"):
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("medium")
        
        # Start the coffee machine in the kitchen
        kitchen = get_room(home, "Kitchen")
        if kitchen:
            for actuator in get_room_actuators(kitchen, "CoffeeMachine"):
                if isinstance(actuator, CoffeeMachine):
                    actuator.turn_on()
                    actuator.make_coffee("Latte")
        
        # Play some music in the bedroom
        for actuator in get_room_actuators(bedroom, "MusicPlayer"):
            if isinstance(actuator, MusicPlayer):
                actuator.turn_on()
                actuator.play_music("Morning Playlist")
        
        # Adjust the temperature in the bedroom
        for sensor in get_room_sensors(bedroom, "IndoorTemperatureSensor"):
            if isinstance(sensor, IndoorTemperatureSensor):
                current_temp = sensor.get_reading()
                if current_temp < TEMP_LOW:
                    for actuator in get_room_actuators(bedroom, "Heater"):
                        if isinstance(actuator, Heater):
                            actuator.turn_on()
                            actuator.set_target_temperature(TEMP_HIGH)
                elif current_temp > TEMP_HIGH:
                    for actuator in get_room_actuators(bedroom, "AC"):
                        if isinstance(actuator, AC):
                            actuator.turn_on()
                            actuator.set_target_temperature(TEMP_LOW)

def leave_home_plan(home):
    print("\n--- Starting Leave Home Plan ---")
    
    # Turn off all lights
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
    
    # Lock all doors
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Door):
                actuator.lock()
    
    # Turn off all actuators
    for room in home:
        for actuator in room.actuators:
            if actuator.status == "on":
                actuator.turn_off()
    
    # Send a notification
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, NotificationSender):
                actuator.turn_on()
                actuator.notification_sender("Leaving home. All systems are turned off.")
                actuator.turn_off()

def movie_plan(home):
    print("\n--- Starting Movie Plan ---")
    
    # Get the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Dim the lights
        for actuator in get_room_actuators(living_room, "Light"):
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")
        
        # Turn on the Smart TV
        for actuator in get_room_actuators(living_room, "SmartTV"):
            if isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Movie Channel")
        
        # Play some background music
        for actuator in get_room_actuators(living_room, "MusicPlayer"):
            if isinstance(actuator, MusicPlayer):
                actuator.turn_on()
                actuator.play_music("Relaxing Playlist")

def main():
    # Create the home plan
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    time.sleep(DAILY_ROUTINE_DURATION)  # Simulate some time passing
    leave_home_plan(home)
    time.sleep(DAILY_ROUTINE_DURATION)  # Simulate some time passing
    movie_plan(home)

if __name__ == "__main__":
    main()