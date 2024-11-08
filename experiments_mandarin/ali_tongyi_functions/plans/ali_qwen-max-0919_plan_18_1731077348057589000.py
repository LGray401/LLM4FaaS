# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to execute the plans (MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN). This script will be placed in the `functions` folder. 
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import MusicPlayer, SmartSocket, Curtain
from home.config import DAILY_ROUTINE_DURATION

def execute_morning_plan(home):
    # Get actuators for the LivingRoom
    actuators = get_room_actuators(home, "LivingRoom")
    
    # Find the MusicPlayer and turn it on to play music
    for actuator in actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")
            break

def execute_leave_home_plan(home):
    # Get actuators for all rooms
    for room in home:
        actuators = room.actuators
        
        # Find all SmartSockets and turn them off
        for actuator in actuators:
            if isinstance(actuator, SmartSocket):
                actuator.turn_off()

def execute_movie_plan(home):
    # Get actuators for the LivingRoom
    actuators = get_room_actuators(home, "LivingRoom")
    
    # Find the Curtain and open it
    for actuator in actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()  # Assuming turning on the curtain means opening it
            break

def main():
    # Create the home plan
    home = home_plan()
    
    # Execute the morning plan
    print("\nExecuting MORNING PLAN...")
    execute_morning_plan(home)
    
    # Simulate some time passing
    time.sleep(DAILY_ROUTINE_DURATION)
    
    # Execute the leave home plan
    print("\nExecuting LEAVE HOME PLAN...")
    execute_leave_home_plan(home)
    
    # Simulate some time passing
    time.sleep(DAILY_ROUTINE_DURATION)
    
    # Execute the movie plan
    print("\nExecuting MOVIE PLAN...")
    execute_movie_plan(home)

if __name__ == "__main__":
    main()