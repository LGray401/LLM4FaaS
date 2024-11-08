# Based on the provided functional description and the existing code in your smart home project, we'll create the `function.py` file that will implement the required modes: Sleep mode, Wake up mode, Lights off mode, and Window closing mode.
# 
# Here's how we can structure the `function.py`:
# 
# 1. **Sleep Mode**: This mode will turn off all lights and close all windows.
# 2. **Wake Up Mode**: This mode will turn on lights in the rooms.
# 3. **Lights Off Mode**: This mode will turn off all the lights in the house.
# 4. **Window Closing Mode**: This mode will close all windows.
# 
# Below is the implementation of `function.py`:

# functions/function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
from home.actuator import Light, Window

def sleep_mode(home):
    print("Entering Sleep Mode...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
            elif isinstance(actuator, Window):
                actuator.turn_off()  # Assuming turn_off closes the window
    print("All lights turned off and windows closed.")


def wake_up_mode(home):
    print("Entering Wake Up Mode...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
    print("All lights turned on.")


def lights_off_mode(home):
    print("Turning Off All Lights...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
    print("All lights are now off.")


def window_closing_mode(home):
    print("Closing All Windows...")
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Window):
                actuator.turn_off()  # Assuming turn_off closes the window
    print("All windows are now closed.")


def main():
    home = home_plan()
    
    # Example of how to call the modes
    sleep_mode(home)
    wake_up_mode(home)
    lights_off_mode(home)
    window_closing_mode(home)

if __name__ == "__main__":
    main()