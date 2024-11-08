# Based on your functional description and provided source code, here is the `function.py` file that contains the main function for your smart home project.

# function.py
import os

# Assuming that 'home' and 'functions' are sibling directories.
# If not, adjust the path accordingly.
HOME_DIR = os.path.join(os.getcwd(), 'home')
FUNCTIONS_DIR = os.path.join(os.getcwd(), 'functions')

# Add 'home' and 'functions' directories to Python's path
import sys
sys.path.append(HOME_DIR)
sys.path.append(FUNCTIONS_DIR)

from sensor import Sensor, IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, \
    LightIntensiveSensor, SmokeSensor
from actuator import Actuator, Heater, AC, CoffeeMachine, Window, Door, Curtain, CleaningRobot, \
    NotificationSender, MusicPlayer, Light, SmartTV, SmartSocket, Humidifier
from home_plan import home_plan
from config import DAILY_ROUTINE_DURATION

def main():
    # Create the home plan
    home = home_plan()

    # Define the plans
    morning_plan = {
        "Light": ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"],
        "AC": ["LivingRoom", "Bedroom"],
        "Heater": ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]
    }

    leave_home_plan = {
        "Light": ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"],
        "AC": ["LivingRoom", "Bedroom"],
        "Heater": ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]
    }

    movie_plan = {
        "Light": ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"],
        "SmartTV": ["LivingRoom"],
        "Curtain": ["LivingRoom"]
    }

    # Function to apply a plan
    def apply_plan(plan):
        for actuator_type, rooms in plan.items():
            actuators = get_all_actuators(home, actuator_type)
            for actuator in actuators:
                if actuator.room_name in rooms:
                    if actuator_type == "Light":
                        actuator.turn_on()
                    elif actuator_type == "SmartTV":
                        actuator.turn_on()
                        actuator.play_channel("Your Favorite Channel")
                    elif actuator_type == "Curtain":
                        actuator.turn_on()
                    # Add more conditions for other actuators if necessary
                    else:
                        print(f"Actuator {actuator.id} not implemented for plan.")

    # Simulate the morning plan
    print("Applying Morning Plan...")
    apply_plan(morning_plan)

    # Simulate the leave home plan
    print("Applying Leave Home Plan...")
    apply_plan(leave_home_plan)

    # Simulate the movie plan
    print("Applying Movie Plan...")
    apply_plan(movie_plan)

    # Start the daily routine for the cleaning robot
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for robot in cleaning_robots:
        robot.daily_routine()

    print("Smart Home is ready and running!")


if __name__ == "__main__":
    main()