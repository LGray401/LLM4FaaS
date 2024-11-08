# Based on your functional description and the provided source code, I'll create the `function.py` file that implements the required functionalities. This script will handle two tasks:
# 
# 1. Turn on the air conditioning 10 minutes before arriving home.
# 2. Activate the cleaning robot to clean the house when no one is home.
# 
# Here's how the `function.py` file will look:

# functions/function.py

import time
from datetime import datetime, timedelta
from home.home_plan import home_plan
from home.actuator import AC, CleaningRobot
from home.sensor import IndoorTemperatureSensor

def main():
    # Example of the home plan
    home = home_plan()

    # Simulate arriving home in 10 minutes
    arrival_time = datetime.now() + timedelta(minutes=10)
    print(f"Scheduled arrival time: {arrival_time.strftime('%H:%M:%S')}")

    # For demonstration, we will assume the user is coming home to the LivingRoom
    living_room = next(room for room in home if room.name == "LivingRoom")
    
    # Check indoor temperature and turn on AC before arrival
    indoor_temp_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor))
    ac = next(actuator for actuator in living_room.actuators if isinstance(actuator, AC))
    
    # Simulate waiting until 10 minutes before arrival
    while datetime.now() < arrival_time:
        # Get current temperature reading
        indoor_temp_sensor.turn_on()
        current_temperature = indoor_temp_sensor.get_reading()
        
        # Set target temperature for AC
        target_temperature = 22  # Example target temperature
        ac.set_target_temperature(target_temperature)
        
        # Adjust AC based on current temperature
        ac.adjust_temperature(current_temperature)
        
        # Wait for a minute for the next reading
        time.sleep(60)

    # Now simulate cleaning when no one is home
    cleaning_robot = next(actuator for actuator in living_room.actuators if isinstance(actuator, CleaningRobot))
    
    # Assume no one is home and start cleaning
    cleaning_robot.turn_on()
    cleaning_robot.daily_routine()

if __name__ == "__main__":
    main()