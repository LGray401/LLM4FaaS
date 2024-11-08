# Based on the provided functional description and the existing code structure, I will create the `function.py` file. This file will include a main function that will activate the energy-saving mode for all smart devices as described. The main function will interact with the existing classes in your project to perform the required actions.
# 
# Here’s how the `function.py` file will look:

# functions/function.py
from home.home_plan import home_plan
from home.actuator import Light, Curtain, SmartSocket, Humidifier, CleaningRobot, MusicPlayer, SmartTV

def activate_energy_saving_mode(home):
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.set_brightness_level("low")
                actuator.turn_on()
            elif isinstance(actuator, Curtain):
                actuator.turn_on()
            elif isinstance(actuator, SmartSocket):
                actuator.turn_off()
            elif isinstance(actuator, Humidifier):
                actuator.turn_off()
            elif isinstance(actuator, CleaningRobot):
                actuator.turn_off()
            elif isinstance(actuator, MusicPlayer):
                actuator.turn_off()
            elif isinstance(actuator, SmartTV):
                actuator.turn_off()

def main():
    home = home_plan()  # Create the home structure
    activate_energy_saving_mode(home)  # Activate energy-saving mode

if __name__ == "__main__":
    main()