# Based on the functional description and the provided source code, I'll create the `function.py` file that contains the main function to implement the morning plan, leave home plan, and movie plan. The file will utilize the classes from the other modules to perform the required actions. 
# 
# Here's how `function.py` might look:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors
from home.actuator import NotificationSender, MusicPlayer, Light
from home.logger_config import logger

def morning_plan():
    home = home_plan()
    bedroom = get_room(home, "Bedroom")
    
    # Turn on the lights in the bedroom
    bedroom_lights = get_room_actuators(home, "Light")
    for light in bedroom_lights:
        light.turn_on()
        light.set_brightness_level("high")

    # Send notification that it's time to wake up
    notification_sender = get_room_actuators(home, "NotificationSender")
    for sender in notification_sender:
        sender.turn_on()
        sender.notification_sender("Xiao G, it's time to get up!")

def leave_home_plan():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    
    # Turn off all lights in the living room
    living_room_lights = get_room_actuators(home, "Light")
    for light in living_room_lights:
        light.turn_off()

    # Send notification that Xiao G is leaving
    notification_sender = get_room_actuators(home, "NotificationSender")
    for sender in notification_sender:
        sender.turn_on()
        sender.notification_sender("Xiao G, I'm leaving, bye.")

def movie_plan():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    
    # Turn on the smart TV and play a happy channel
    smart_tv = get_room_actuators(home, "SmartTV")
    for tv in smart_tv:
        tv.turn_on()
        tv.play_channel("Happy Channel")

    # Send notification that the movie plan is activated
    notification_sender = get_room_actuators(home, "NotificationSender")
    for sender in notification_sender:
        sender.turn_on()
        sender.notification_sender("Xiao G, I want to be happy!")

def main():
    # Execute a plan based on the user's choice
    print("Select a plan to execute:")
    print("1. Morning Plan")
    print("2. Leave Home Plan")
    print("3. Movie Plan")
    choice = input("Enter the plan number: ")

    if choice == '1':
        morning_plan()
    elif choice == '2':
        leave_home_plan()
    elif choice == '3':
        movie_plan()
    else:
        print("Invalid choice. Please select a valid plan.")

if __name__ == "__main__":
    main()