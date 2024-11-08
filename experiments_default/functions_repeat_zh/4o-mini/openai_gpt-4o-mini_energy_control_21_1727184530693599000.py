# Based on your functional description of the smart home project, I will create the `function.py` file that implements the energy-saving mode. This functionality will involve controlling the various actuators in your smart home system to achieve the desired state: dimming lights, closing curtains, turning off unused sockets, stopping the humidifier, returning the cleaning robot to its base, turning off music, and setting the TV to energy-saving mode.
# 
# Here is the proposed `function.py` file:

# function.py
from home.home_plan import home_plan
from home.actuator import Light, Curtain, SmartSocket, Humidifier, CleaningRobot, MusicPlayer, SmartTV

def energy_saving_mode(home):
    # Iterate over all rooms and their actuators
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.set_brightness_level("low")  # Set lights to dim
                actuator.turn_on()  # Ensure the light is on to adjust brightness
            elif isinstance(actuator, Curtain):
                actuator.turn_on()  # Close the curtains
            elif isinstance(actuator, SmartSocket):
                actuator.turn_off()  # Turn off the smart socket
            elif isinstance(actuator, Humidifier):
                actuator.turn_off()  # Stop the humidifier
            elif isinstance(actuator, CleaningRobot):
                actuator.turn_off()  # Return the cleaning robot to its base (assumed to turn off)
            elif isinstance(actuator, MusicPlayer):
                actuator.turn_off()  # Stop the music
            elif isinstance(actuator, SmartTV):
                actuator.turn_off()  # Set the TV to energy-saving mode (assumed to turn off)

def main():
    home = home_plan()  # Create the home plan
    energy_saving_mode(home)  # Activate energy-saving mode

if __name__ == "__main__":
    main()