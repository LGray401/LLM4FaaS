# Given the functional description and the provided source code, I'll create a `function.py` file that will implement the main function to manage the modes: Sleep mode, Wake up mode, Lights off mode, and Window closing mode.
# 
# Here's how the `function.py` might look:

# functions/function.py
import time
from home.home_plan import home_plan, get_all_actuators, get_all_sensors
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def sleep_mode(home):
    print("Activating sleep mode...")
    # Turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
    
    # Close all windows
    windows = get_all_actuators(home, "Window")
    for window in windows:
        window.turn_off()
    
    # Stop any music
    music_players = get_all_actuators(home, "MusicPlayer")
    for player in music_players:
        player.turn_off()

def wake_up_mode(home):
    print("Activating wake up mode...")
    # Turn on lights in the bedroom
    bedroom_lights = [light for light in get_all_actuators(home, "Light") if light.room_name == "Bedroom"]
    for light in bedroom_lights:
        light.turn_on()
    
    # Turn on coffee machine in the kitchen
    coffee_machines = [cm for cm in get_all_actuators(home, "CoffeeMachine") if cm.room_name == "Kitchen"]
    for cm in coffee_machines:
        cm.turn_on()
        cm.make_coffee("Espresso")

def lights_off_mode(home):
    print("Activating lights off mode...")
    # Turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def window_closing_mode(home):
    print("Activating window closing mode...")
    # Close all windows
    windows = get_all_actuators(home, "Window")
    for window in windows:
        window.turn_off()

def main():
    home = home_plan()
    
    # Example usage of modes
    sleep_mode(home)
    time.sleep(2)  # Simulate time delay
    wake_up_mode(home)
    time.sleep(2)
    lights_off_mode(home)
    time.sleep(2)
    window_closing_mode(home)

if __name__ == "__main__":
    main()