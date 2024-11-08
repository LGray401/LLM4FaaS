# Based on the functional description you provided, I will create a `function.py` file in the `functions` folder. This file will contain a main function that activates the energy-saving mode by controlling various smart devices as specified. 
# 
# Here’s the implementation of `function.py`:

# function.py
from home.home_plan import home_plan
from home.actuator import Light, Curtain, SmartSocket, Humidifier, CleaningRobot, MusicPlayer, SmartTV

def activate_energy_saving_mode(home):
    # Iterate through each room in the home
    for room in home:
        print(f"Activating energy saving mode in {room.name}...")
        
        # Turn down lights to low brightness
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")
        
        # Close curtains
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()
                print(f"{actuator.id} is now closed.")

        # Turn off unused smart sockets
        for actuator in room.actuators:
            if isinstance(actuator, SmartSocket):
                actuator.turn_off()

        # Stop humidifiers
        for actuator in room.actuators:
            if isinstance(actuator, Humidifier):
                actuator.turn_off()

        # Return cleaning robots to their charging stations
        for actuator in room.actuators:
            if isinstance(actuator, CleaningRobot):
                actuator.turn_on()
                actuator.daily_routine()

        # Turn off music players
        for actuator in room.actuators:
            if isinstance(actuator, MusicPlayer):
                actuator.turn_off()

        # Set smart TVs to energy-saving mode
        for actuator in room.actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_off()

    print("Energy saving mode activated in all rooms.")

def main():
    home = home_plan()
    activate_energy_saving_mode(home)

if __name__ == "__main__":
    main()