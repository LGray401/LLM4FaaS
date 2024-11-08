# Based on your functional description and the source code provided, I will create the `function.py` file that implements the energy-saving mode for your smart home project. This will involve controlling various actuators based on the specified actions: dimming lights, closing curtains, turning off unused sockets, stopping the humidifier, returning the cleaning robot, stopping music, and putting the TV in energy-saving mode.
# 
# Here's the `function.py` file:

# function.py

from home.home_plan import home_plan
from home.actuator import Light, Curtain, SmartSocket, Humidifier, CleaningRobot, MusicPlayer, SmartTV
from home.logger_config import logger

def energy_saving_mode(home):
    for room in home:
        # Dim the lights
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")
        
        # Close curtains
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Assuming turning on closes the curtain

        # Turn off unused smart sockets
        for actuator in room.actuators:
            if isinstance(actuator, SmartSocket):
                actuator.turn_off()

        # Stop the humidifier
        for actuator in room.actuators:
            if isinstance(actuator, Humidifier):
                actuator.turn_off()  # Assuming turning off stops the humidifier

        # Return the cleaning robot to its base
        for actuator in room.actuators:
            if isinstance(actuator, CleaningRobot):
                actuator.turn_on()  # Turn on the robot
                actuator.daily_routine()  # Execute its routine to return to base

        # Stop music playback
        for actuator in room.actuators:
            if isinstance(actuator, MusicPlayer):
                actuator.turn_off()

        # Set TV to energy-saving mode
        for actuator in room.actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_off()  # Assuming turning off puts it in energy saving mode

def main():
    home = home_plan()
    energy_saving_mode(home)
    logger.info("Energy saving mode activated for all rooms.")

if __name__ == "__main__":
    main()