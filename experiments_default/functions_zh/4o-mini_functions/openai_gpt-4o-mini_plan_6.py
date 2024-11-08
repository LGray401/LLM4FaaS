# Based on your functional description and the provided source code, I will create a `function.py` file that implements the three plans: the Morning Plan, Leave Home Plan, and Movie Plan. This file will utilize the existing classes from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 
# Here’s the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room, get_all_actuators
from home.actuator import NotificationSender, MusicPlayer, SmartTV, Light
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from time import sleep

def morning_plan():
    print("Executing Morning Plan...")
    
    # Turn on the Coffee Machine and make coffee
    coffee_machine = get_all_actuators("CoffeeMachine")
    if coffee_machine:
        coffee_machine[0].turn_on()
        coffee_machine[0].make_coffee("Morning Coffee")
    
    # Turn on the lights in the Bedroom
    bedroom = get_room(home_plan(), "Bedroom")
    if bedroom:
        for light in get_all_actuators(bedroom, "Light"):
            light.turn_on()

    # Simulate alarm sounding
    print("Alarm is ringing! Time to wake up!")
    sleep(2)

    # Notify the user that it's time to get up
    notification_sender = get_all_actuators("NotificationSender")
    if notification_sender:
        notification_sender[0].turn_on()
        notification_sender[0].notification_sender("It's time to wake up!")

def leave_home_plan():
    print("Executing Leave Home Plan...")
    
    # Lock the doors
    home = home_plan()
    for room in home:
        for actuator in get_all_actuators(room, "Door"):
            actuator.lock()
    
    # Notify the user that they're leaving
    notification_sender = get_all_actuators("NotificationSender")
    if notification_sender:
        notification_sender[0].turn_on()
        notification_sender[0].notification_sender("Leaving home now...")

def movie_plan():
    print("Executing Movie Plan...")
    
    # Turn on the Smart TV and set it to a specific channel
    living_room = get_room(home_plan(), "LivingRoom")
    if living_room:
        for tv in get_all_actuators(living_room, "SmartTV"):
            tv.turn_on()
            tv.play_channel("Favorite Movie Channel")
    
    # Dim the lights in the Living Room
    for light in get_all_actuators(living_room, "Light"):
        light.turn_on()
        light.set_brightness_level("low")
    
    # Notify the user that the movie is about to start
    notification_sender = get_all_actuators("NotificationSender")
    if notification_sender:
        notification_sender[0].turn_on()
        notification_sender[0].notification_sender("Enjoy your movie!")

def main():
    # Example execution of the plans
    morning_plan()
    leave_home_plan()
    movie_plan()

if __name__ == "__main__":
    main()