# Based on your provided functional description and the source code, I will create a `function.py` file that includes a main function to start the energy-saving mode. The energy-saving mode will adjust the settings of various actuators (e.g., lights, AC, heater) to save energy while maintaining a comfortable environment.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators
from home.actuator import Light, AC, Heater, SmartTV, MusicPlayer, CoffeeMachine, CleaningRobot
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def enable_energy_saving_mode():
    """
    Enables the energy-saving mode for the smart home.
    This function adjusts the settings of various actuators to save energy.
    """
    home = home_plan()
    
    # Get all actuators
    all_lights = get_all_actuators(home, "Light")
    all_acs = get_all_actuators(home, "AC")
    all_heaters = get_all_actuators(home, "Heater")
    all_smart_tvs = get_all_actuators(home, "SmartTV")
    all_music_players = get_all_actuators(home, "MusicPlayer")
    all_coffee_machines = get_all_actuators(home, "CoffeeMachine")
    all_cleaning_robots = get_all_actuators(home, "CleaningRobot")

    # Adjust light settings
    for light in all_lights:
        if light.status == "on":
            light.set_brightness_level("low")
            print(f"Set {light.id} brightness to low to save energy.")

    # Adjust AC and heater settings
    for ac in all_acs:
        if ac.status == "on":
            if ac.target_temperature < TEMP_HIGH:
                ac.set_target_temperature(TEMP_HIGH)
                print(f"Set {ac.id} target temperature to {TEMP_HIGH}°C to save energy.")
    
    for heater in all_heaters:
        if heater.status == "on":
            if heater.target_temperature > TEMP_LOW:
                heater.set_target_temperature(TEMP_LOW)
                print(f"Set {heater.id} target temperature to {TEMP_LOW}°C to save energy.")

    # Turn off non-essential devices
    for smart_tv in all_smart_tvs:
        if smart_tv.status == "on":
            smart_tv.turn_off()
            print(f"Turned off {smart_tv.id} to save energy.")

    for music_player in all_music_players:
        if music_player.status == "on":
            music_player.turn_off()
            print(f"Turned off {music_player.id} to save energy.")

    for coffee_machine in all_coffee_machines:
        if coffee_machine.status == "on":
            coffee_machine.turn_off()
            print(f"Turned off {coffee_machine.id} to save energy.")

    for cleaning_robot in all_cleaning_robots:
        if cleaning_robot.status == "on":
            cleaning_robot.turn_off()
            print(f"Turned off {cleaning_robot.id} to save energy.")

if __name__ == "__main__":
    enable_energy_saving_mode()