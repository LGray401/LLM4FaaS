# Based on the provided code and functional description, the required `function.py` file should implement a function to turn off the lights in the bedroom. Here's the `function.py` file that meets your requirements:

# function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def turn_off_bedroom_lights(home):
    bedroom = get_room_actuators(home, "Bedroom")
    if bedroom:
        for actuator in bedroom:
            if isinstance(actuator, Light):
                actuator.turn_off()
                print(f"Turned off light: {actuator.id}")

def main():
    home = home_plan()
    turn_off_bedroom_lights(home)

if __name__ == "__main__":
    main()