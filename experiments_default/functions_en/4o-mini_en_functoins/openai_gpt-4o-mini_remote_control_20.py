# Based on the functional description and the provided source code, I will create a `function.py` file that implements the main functionality of turning on the air conditioner ten minutes before arriving home and using the robot vacuum cleaner to sweep the floor when no one is at home.
# 
# Here is the `function.py` file for your smart home project:

# functions/function.py

import time
from datetime import datetime, timedelta
from home.home_plan import home_plan, get_all_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import AC, CleaningRobot
from home.logger_config import logger

def turn_on_ac_before_arrival(home):
    # Get the current time
    current_time = datetime.now()

    # Calculate the time 10 minutes from now
    arrival_time = current_time + timedelta(minutes=10)

    # Find the AC actuator in the home
    ac_actuators = get_all_actuators(home, "AC")
    
    if ac_actuators:
        for ac in ac_actuators:
            ac.turn_on()  # Turn on the AC

            # Log the action
            logger.info(f"AC {ac.id} turned on at {current_time.strftime('%H:%M:%S')} for arrival at {arrival_time.strftime('%H:%M:%S')}.")

            # Simulate waiting for 10 minutes (for demonstration purposes, we'll just sleep)
            time.sleep(10)  # In a real scenario, this would be the time until arrival
            logger.info(f"AC {ac.id} is still on for arrival at {arrival_time.strftime('%H:%M:%S')}.")

    else:
        logger.warning("No AC actuators found in the home.")

def activate_cleaning_robot(home):
    # Check if anyone is home
    # For simplicity, we will assume the home is empty
    # In a real scenario, you would have a method to check occupancy status
    home_empty = True  # Change this based on actual occupancy checking logic

    if home_empty:
        cleaning_robots = get_all_actuators(home, "CleaningRobot")
        
        if cleaning_robots:
            for robot in cleaning_robots:
                robot.turn_on()  # Turn on the cleaning robot
                robot.daily_routine()  # Start the cleaning routine
        else:
            logger.warning("No Cleaning Robots found in the home.")

def main():
    home = home_plan()  # Create the home plan with rooms and components

    # Example of triggering the actions
    turn_on_ac_before_arrival(home)
    activate_cleaning_robot(home)

if __name__ == "__main__":
    main()