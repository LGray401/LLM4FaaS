# Based on the functional description and the provided source code, you want to create a `function.py` file that contains the main function for your smart home project. The main function should handle different plans such as "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN".
#
# Here is a basic structure of the `function.py` file:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators

def morning_plan(home):
    # Implement the morning plan here
    pass

def leave_home_plan(home):
    # Implement the leave home plan here
    pass

def movie_plan(home):
    # Implement the movie plan here
    pass

def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
#
# In the `morning_plan`, `leave_home_plan`, and `movie_plan` functions, you can use the `get_room`, `get_room_sensors`, `get_room_actuators`, `get_all_sensors`, and `get_all_actuators` functions from `home_plan.py` to control the sensors and actuators in your smart home according to your plans.
#
# Please note that this is a basic structure and you need to implement the details of each plan according to your requirements.