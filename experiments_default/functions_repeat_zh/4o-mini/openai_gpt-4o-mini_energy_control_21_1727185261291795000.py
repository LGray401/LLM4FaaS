# Based on the functional description you provided, the `function.py` file will implement the energy-saving mode for your smart home project. This will involve controlling various actuators to set the desired states for each device as specified in the description. 
# 
# Here’s the implementation for `function.py`:

# function.py
from home.home_plan import home_plan
from home.actuator import Light, Curtain, SmartSocket, Humidifier, CleaningRobot, MusicPlayer, SmartTV

def energy_saving_mode(home):
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.set_brightness_level("low")  # Set light to low brightness
                actuator.turn_on()
            elif isinstance(actuator, Curtain):
                actuator.turn_on()  # Close the curtains
            elif isinstance(actuator, SmartSocket):
                actuator.turn_off()  # Turn off unused sockets
            elif isinstance(actuator, Humidifier):
                actuator.turn_off()  # Stop the humidifier
            elif isinstance(actuator, CleaningRobot):
                actuator.turn_off()  # Return the cleaning robot to its base
            elif isinstance(actuator, MusicPlayer):
                actuator.turn_off()  # Turn off the music
            elif isinstance(actuator, SmartTV):
                actuator.turn_on()  # Set TV to energy-saving mode (assumed to be 'on' but in a low-power state)

def main():
    # Create the home plan
    home = home_plan()
    
    # Activate energy saving mode
    energy_saving_mode(home)

if __name__ == "__main__":
    main()