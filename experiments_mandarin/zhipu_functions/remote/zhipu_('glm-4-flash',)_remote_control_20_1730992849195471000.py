# Based on the functional description and the provided source code, below is a Python script for the `function.py` file that you requested. This script will be located in the `functions` folder and will contain the main function, which will implement the described smart home functionalities:

import time
from datetime import datetime
from home_plan import home_plan
from sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from actuator import AC, CleaningRobot

def main():
    # Define the home plan
    home = home_plan()

    # Function to turn on AC 10 minutes before home owner's return
    def turn_on_ac_before_return(room_name, target_temperature):
        # Get the AC actuator from the specified room
        ac = get_room_actuators(home, room_name)[0]
        # Set the target temperature
        ac.set_target_temperature(target_temperature)
        # Turn on the AC
        ac.turn_on()
        logger.info(f"AC in {room_name} turned on with target temperature {target_temperature}°C.")

    # Function to start扫地机器人 cleaning routine when the home owner is not home
    def start_cleaning_routine(room_name):
        # Get the CleaningRobot actuator from the specified room
        cleaning_robot = get_room_actuators(home, room_name)[0]
        # Start the daily cleaning routine
        cleaning_robot.daily_routine()
        logger.info(f"Cleaning routine started for room {room_name}.")

    # Function to check if the home owner is home
    def is_home_owner_home(sensor_type):
        # Get all sensors of the specified type
        sensors = get_all_sensors(home, sensor_type)
        # Check if any sensor is active
        for sensor in sensors:
            if sensor.get_status() == "on":
                return True
        return False

    # Main loop
    while True:
        # Check if the home owner is home
        if not is_home_owner_home("IndoorTemperature"):
            # Start扫地机器人 cleaning routine
            start_cleaning_routine("LivingRoom")
            # Wait for the home owner to return
            time.sleep(600)  # Wait for 10 minutes
        # Turn on AC 10 minutes before home owner's return
        turn_on_ac_before_return("LivingRoom", 22)  # Assuming the target temperature is 22°C
        # Wait for the home owner to return
        time.sleep(600)  # Wait for 10 minutes

def get_room_actuators(home, room_name):
    for room in home:
        if room.name == room_name:
            return room.actuators
    return []

if __name__ == "__main__":
    main()