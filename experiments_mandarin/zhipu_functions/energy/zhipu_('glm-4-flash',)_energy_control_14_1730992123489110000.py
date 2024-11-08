# Based on your functional description and the provided source code, I will create a `function.py` file in the `functions` folder. This file will contain a `main` function that integrates the sensor and actuator components according to the `home_plan` to start the Earth环保计划.
# 
# Here is the content of `function.py`:

import logging
from home.sensor import Sensor
from home.actuator import Actuator
from home.home_plan import home_plan

# Configure logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Initialize home plan
    home = home_plan()
    
    # Example: Turn on all lights in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        lights = get_room_actuators(living_room, "Light")
        for light in lights:
            light.turn_on()
            logging.info(f"Turned on the light: {light.id}")
    
    # Example: Turn off all heaters in the home
    heaters = get_all_actuators(home, "Heater")
    for heater in heaters:
        heater.turn_off()
        logging.info(f"Turned off the heater: {heater.id}")
    
    # Example: Turn on all AC units in the home
    ac_units = get_all_actuators(home, "AC")
    for ac_unit in ac_units:
        ac_unit.turn_on()
        logging.info(f"Turned on the AC unit: {ac_unit.id}")
    
    # Example: Start the daily cleaning routine for the cleaning robot in the living room
    cleaning_robots = get_room_actuators(living_room, "CleaningRobot")
    for cleaning_robot in cleaning_robots:
        cleaning_robot.daily_routine()
        logging.info(f"Started daily cleaning routine for the cleaning robot: {cleaning_robot.id}")

def get_room(home, room_name):
    for room in home:
        if room.name == room_name:
            return room
    return None

def get_room_actuators(room, actuator_type):
    actuators = []
    for actuator in room.actuators:
        if actuator.actuator_type == actuator_type:
            actuators.append(actuator)
    return actuators

def get_all_actuators(home, actuator_type):
    all_actuators = []
    for room in home:
        room_actuators = get_room_actuators(room, actuator_type)
        all_actuators.extend(room_actuators)
    return all_actuators

if __name__ == "__main__":
    main()