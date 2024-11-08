# Based on the functional description you provided, I will create the `function.py` file that includes a main function to implement the different plans for your smart home. The `function.py` file will utilize the classes and methods defined in your other source files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) to fulfill the requirements specified in your plans.
# 
# Here's the `function.py` content:

# function.py
from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import SmartTV, Light, CleaningRobot, NotificationSender, Door

def morning_plan(home):
    print("Executing MORNING PLAN...")
    # Turn on the lights and start the cleaning robot
    for room in home:
        for actuator in get_room_actuators(home, room.name):
            if isinstance(actuator, Light):
                actuator.turn_on()
            elif isinstance(actuator, CleaningRobot):
                actuator.turn_on()
                actuator.daily_routine()

def leave_home_plan(home):
    print("Executing LEAVE HOME PLAN...")
    # Lock the doors and send a notification
    for room in home:
        for actuator in get_room_actuators(home, room.name):
            if isinstance(actuator, Door):
                actuator.lock()
            elif isinstance(actuator, NotificationSender):
                actuator.turn_on()
                actuator.notification_sender("The house is now secured.")

def movie_plan(home):
    print("Executing MOVIE PLAN...")
    # Turn on the TV and turn off the lights
    for room in home:
        for actuator in get_room_actuators(home, room.name):
            if isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Movie Channel")
            elif isinstance(actuator, Light):
                actuator.turn_off()

def main():
    home = home_plan()  # Initialize the home plan

    # Execute the different plans
    morning_plan(home)   # Execute morning plan
    leave_home_plan(home)  # Execute leave home plan
    movie_plan(home)      # Execute movie plan

if __name__ == "__main__":
    main()