# # function.py

import os

# Define the path for the 'home' and 'functions' folders
HOME_FOLDER = os.path.join(os.getcwd(), 'home')
FUNCTIONS_FOLDER = os.path.join(os.getcwd(), 'functions')

# Set the path for the 'function.py' file
FUNCTION_PATH = os.path.join(FUNCTIONS_FOLDER, 'function.py')

# Create the 'functions' folder if it does not exist
if not os.path.exists(FUNCTIONS_FOLDER):
    os.makedirs(FUNCTIONS_FOLDER)

# Define the main function in 'function.py'
FUNCTION_CONTENT = """
from home.sensor import Sensor
from home.actuator import Actuator
from home.home_plan import home_plan
from home.config import DAILY_ROUTINE_DURATION

def main():
    # Load the home plan
    home = home_plan()

    # Initialize actuators for daily routine
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, CleaningRobot):
                actuator.daily_routine()

    # Example: Turn on all lights in the Living Room
    living_room = get_room(home, 'LivingRoom')
    if living_room:
        for actuator in living_room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()

if __name__ == "__main__":
    main()
"""

# Write the 'function.py' content to the file
with open(FUNCTION_PATH, 'w') as function_file:
    function_file.write(FUNCTION_CONTENT)