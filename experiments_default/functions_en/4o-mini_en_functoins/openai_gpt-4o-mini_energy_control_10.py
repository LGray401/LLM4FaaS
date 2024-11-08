# Based on your functional description of turning off the air conditioner, I have created the `function.py` file for your smart home project. This file will contain the main function that initializes your home plan and turns off the air conditioner in a specified room. 
# 
# Here is the content for `function.py`:

# function.py

from home.home_plan import home_plan, get_all_actuators
from home.actuator import AC
from home.logger_config import logger

def turn_off_ac_in_room(home, room_name):
    # Get all AC actuators in the specified room
    acs = get_all_actuators(home, "AC")
    room_ac = [ac for ac in acs if ac.room_name == room_name]

    if room_ac:
        for ac in room_ac:
            ac.turn_off()
            print(f"{ac.id} has been turned off.")
            logger.info(f"{ac.id} has been turned off.")
    else:
        print(f"No AC found in {room_name}.")
        logger.warning(f"No AC found in {room_name}.")

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Specify the room name where the AC should be turned off
    room_name = "LivingRoom"  # Change this to the desired room name

    # Turn off the air conditioner in the specified room
    turn_off_ac_in_room(home, room_name)

if __name__ == "__main__":
    main()