# Based on the provided functional description and the existing code for your smart home project, I've created a `function.py` file that includes a main function to activate the energy-saving mode. This function will control various actuators (lights, curtains, smart sockets, humidifiers, cleaning robots, music players, and smart TVs) according to the specified requirements.
# 
# Here is the content of `function.py`:

# function.py
from home.home_plan import home_plan
from home.actuator import Light, Curtain, SmartSocket, Humidifier, CleaningRobot, MusicPlayer, SmartTV

def activate_energy_saving_mode(home):
    for room in home:
        # Turn off the lights and set them to a low brightness
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")

            # Close curtains
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Assuming turning on means closing the curtain

            # Turn off smart sockets
            if isinstance(actuator, SmartSocket):
                actuator.turn_off()

            # Stop the humidifier
            if isinstance(actuator, Humidifier):
                actuator.turn_off()

            # Return cleaning robot to its base
            if isinstance(actuator, CleaningRobot):
                actuator.turn_on()  # Assuming turning on starts the cleaning routine
                actuator.daily_routine()

            # Stop music player
            if isinstance(actuator, MusicPlayer):
                actuator.turn_off()

            # Set smart TV to energy saving mode
            if isinstance(actuator, SmartTV):
                actuator.turn_off()

def main():
    home = home_plan()  # Initialize home plan
    print("Activating energy-saving mode...")
    activate_energy_saving_mode(home)
    print("Energy-saving mode activated.")

if __name__ == "__main__":
    main()