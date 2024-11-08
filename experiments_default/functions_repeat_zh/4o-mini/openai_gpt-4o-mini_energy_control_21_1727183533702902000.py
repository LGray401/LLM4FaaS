# Based on the provided functional description and the existing code structure, I will create a `function.py` file that implements the energy-saving mode for your smart home project. The code will interact with the sensors and actuators defined in the other files to achieve the desired functionalities.
# 
# Here is the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Light, Curtain, SmartSocket, Humidifier, CleaningRobot, MusicPlayer, SmartTV
from home.logger_config import logger

def enable_energy_saving_mode(home):
    logger.info("Enabling energy saving mode...")

    # Iterate through all rooms in the home
    for room in home:
        # For each room, find and control the relevant actuators
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.set_brightness_level("low")  # Set light to low brightness
                actuator.turn_on()
            elif isinstance(actuator, Curtain):
                actuator.turn_on()  # Close curtains
            elif isinstance(actuator, SmartSocket):
                actuator.turn_off()  # Turn off unused smart sockets
            elif isinstance(actuator, Humidifier):
                actuator.turn_off()  # Stop the humidifier
            elif isinstance(actuator, CleaningRobot):
                actuator.daily_routine()  # Return the cleaning robot to its base
            elif isinstance(actuator, MusicPlayer):
                actuator.turn_off()  # Turn off the music player
            elif isinstance(actuator, SmartTV):
                actuator.turn_off()  # Put the TV in energy-saving mode (off)

    logger.info("Energy saving mode has been enabled successfully.")

def main():
    # Create home plan
    home = home_plan()
    
    # Enable energy saving mode
    enable_energy_saving_mode(home)

if __name__ == "__main__":
    main()