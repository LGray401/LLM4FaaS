# Based on your functional description and the provided source code, I will create a `function.py` file that implements the requested modes: sleep mode, wake-up mode, turn off lights mode, and close windows mode. This file will include a main function to demonstrate the functionality.
# 
# Here's the content for the `function.py` file:

# function.py
from home.home_plan import home_plan
from home.actuator import Light, Window
from home.logger_config import logger

def sleep_mode(home):
    print("\nEntering Sleep Mode...")
    for room in home:
        # Turn off lights in the room
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
                
        # Close windows in the room
        for actuator in room.actuators:
            if isinstance(actuator, Window):
                actuator.turn_off()  # Assuming turning off means closing

    logger.info("Sleep mode activated: All lights turned off and windows closed.")


def wake_up_mode(home):
    print("\nEntering Wake-Up Mode...")
    for room in home:
        # Turn on lights in the room
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                
        # Open windows in the room
        for actuator in room.actuators:
            if isinstance(actuator, Window):
                actuator.turn_on()  # Assuming turning on means opening

    logger.info("Wake-up mode activated: All lights turned on and windows opened.")


def turn_off_lights_mode(home):
    print("\nTurning Off All Lights...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()

    logger.info("All lights turned off.")


def close_windows_mode(home):
    print("\nClosing All Windows...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Window):
                actuator.turn_off()  # Assuming turning off means closing

    logger.info("All windows closed.")


def main():
    home = home_plan()  # Initialize the home plan

    # Example usage of modes
    sleep_mode(home)
    wake_up_mode(home)
    turn_off_lights_mode(home)
    close_windows_mode(home)


if __name__ == "__main__":
    main()