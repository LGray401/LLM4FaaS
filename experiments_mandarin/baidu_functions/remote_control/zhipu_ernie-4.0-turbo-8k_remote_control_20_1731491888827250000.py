# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main functions to fulfill the requirements: 
# 
# 1. Turn on the AC ten minutes before arriving home.
# 2. Start the cleaning robot when no one is home.
# 
# Here's the `function.py` file:

import time
from datetime import datetime, timedelta
from home.home_plan import home_plan, get_all_actuators, get_room
from home.config import DAILY_ROUTINE_DURATION
from home.logger_config import logger

# Function to simulate arrival home and turn on the AC 10 minutes before
def prepare_home_before_arrival(home, arrival_time):
    # Calculate the time to turn on the AC (10 minutes before arrival)
    turn_on_ac_time = arrival_time - timedelta(minutes=10)
    
    # Wait until the right time to turn on the AC
    while datetime.now() < turn_on_ac_time:
        time.sleep(1)
    
    # Get all ACs in the home
    acs = get_all_actuators(home, "AC")
    
    # Turn on all ACs
    for ac in acs:
        if ac.status == "off":
            ac.turn_on()
            # For simplicity, assuming a target temperature of 25°C
            ac.set_target_temperature(25)
        else:
            logger.info(f"AC {ac.id} is already on.")

# Function to check if anyone is home based on sensor readings (simplified logic)
def is_anyone_home(home):
    # In a real scenario, this function would check for motion sensors, door states, etc.
    # Here, we'll assume that if any light is on, someone is home
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == "Light" and actuator.status == "on":
                return True
    return False

# Function to start the cleaning robot when no one is home
def start_cleaning_when_no_one_is_home(home):
    while True:
        if not is_anyone_home(home):
            # Get all cleaning robots in the home
            cleaning_robots = get_all_actuators(home, "CleaningRobot")
            
            # Start all cleaning robots
            for robot in cleaning_robots:
                if robot.status == "off":
                    robot.turn_on()
                    robot.daily_routine()
                else:
                    logger.info(f"Cleaning robot {robot.id} is already on or running.")
            
            # Sleep for a while before checking again
            time.sleep(DAILY_ROUTINE_DURATION + 5)  # +5 minutes buffer
        else:
            # Sleep for a short duration before checking again
            time.sleep(60)  # Check every minute

# Main function to run the smart home logic
def main():
    # Initialize the home plan
    home = home_plan()
    
    # Example arrival time (should be dynamically determined in a real scenario)
    arrival_time = datetime.now() + timedelta(hours=1)  # Assuming arrival 1 hour later
    
    # Prepare home before arrival (turn on AC 10 minutes before)
    prepare_home_before_arrival(home, arrival_time)
    
    # Start the cleaning robot when no one is home
    start_cleaning_when_no_one_is_home(home)

if __name__ == "__main__":
    main()