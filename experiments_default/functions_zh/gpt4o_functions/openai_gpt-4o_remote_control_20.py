# Certainly! Based on the provided functional description and the source code files, here is the `function.py` file:

import time
from home.home_plan import home_plan, get_room_actuators
from home.config import TEMP_HIGH

def turn_on_ac_before_arrival(home, room_name, minutes_before):
    room = get_room_actuators(home, room_name)
    if room:
        for actuator in room:
            if isinstance(actuator, AC):
                actuator.set_target_temperature(TEMP_HIGH)
                time.sleep(minutes_before * 60)
                actuator.turn_on()
                print(f"Turned on AC in {room_name} before {minutes_before} minutes.")

def start_cleaning_robot_when_no_one_home(home):
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, CleaningRobot):
                if not any(sensor.get_status() == 'on' for sensor in room.sensors):
                    actuator.turn_on()
                    actuator.daily_routine()

def main():
    home = home_plan()
    
    # Example: Turn on AC in LivingRoom 10 minutes before arrival
    turn_on_ac_before_arrival(home, 'LivingRoom', 10)
    
    # Start cleaning robot when no one is at home
    start_cleaning_robot_when_no_one_home(home)

if __name__ == "__main__":
    main()