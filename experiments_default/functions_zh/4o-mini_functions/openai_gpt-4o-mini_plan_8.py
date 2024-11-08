# Based on your functional description and the provided source code, I will create a `function.py` file that includes a main function to implement the three plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. This file will utilize the classes defined in your existing modules (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`).
# 
# Here's the content for `function.py`:

# function.py
from home.home_plan import home_plan, get_all_actuators
from home.actuator import SmartTV, Light, NotificationSender, CoffeeMachine, CleaningRobot
from home.logger_config import logger

def morning_plan(home):
    print("Executing MORNING PLAN: Starting the home.")
    
    # Get relevant actuators
    coffee_machine = get_all_actuators(home, "CoffeeMachine")
    cleaning_robot = get_all_actuators(home, "CleaningRobot")
    notification_sender = get_all_actuators(home, "NotificationSender")
    
    # Turn on coffee machine and start cleaning
    for cm in coffee_machine:
        cm.turn_on()
        cm.make_coffee("Espresso")  # Example coffee type
    
    for robot in cleaning_robot:
        robot.turn_on()
        robot.daily_routine()  # Start daily cleaning routine
    
    # Send morning notification
    for ns in notification_sender:
        ns.turn_on()
        ns.notification_sender("Good morning! The home is waking up.")

def leave_home_plan(home):
    print("Executing LEAVE HOME PLAN: Securing the home.")
    
    notification_sender = get_all_actuators(home, "NotificationSender")
    door = get_all_actuators(home, "Door")
    
    # Lock all doors
    for d in door:
        d.lock()
    
    # Send notification
    for ns in notification_sender:
        ns.turn_on()
        ns.notification_sender("I have left home. All doors are locked.")

def movie_plan(home):
    print("Executing MOVIE PLAN: Setting up for a movie.")
    
    smart_tv = get_all_actuators(home, "SmartTV")
    lights = get_all_actuators(home, "Light")
    
    # Turn on the TV and dim the lights
    for tv in smart_tv:
        tv.turn_on()
        tv.play_channel("Netflix")  # Example channel name
    
    for light in lights:
        light.turn_on()
        light.set_brightness_level("low")  # Dim the lights for movie time

def main():
    home = home_plan()  # Initialize home plan
    # Example calls to the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()