# Based on your functional description of starting an "energy-saving mode," I'll create a `function.py` file that will allow you to set the energy-saving mode for various components in your smart home.
# 
# Below is the content of the `function.py` file:

# function.py
import os

# Import necessary components from the home and functions folders
home_path = os.path.join(os.getcwd(), 'home')
functions_path = os.path.join(os.getcwd(), 'functions')

# Add home and functions paths to sys.path
import sys
sys.path.append(home_path)
sys.path.append(functions_path)

from home.sensor import Sensor, IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, \
    LightIntensiveSensor, SmokeSensor
from home.actuator import Actuator, Heater, AC, Light, SmartSocket, SmartTV, MusicPlayer, CleaningRobot, \
    Curtain, Door, Window, Humidifier, SmartSocket
from home_plan import home_plan

def save_state_to_file(room_name, component_name, state):
    with open(f"{room_name}_{component_name}_state.txt", "w") as file:
        file.write(str(state))

def restore_state_from_file(room_name, component_name):
    try:
        with open(f"{room_name}_{component_name}_state.txt", "r") as file:
            return eval(file.read())
    except FileNotFoundError:
        return None

def energy_saving_mode():
    home = home_plan()
    
    # Define components to be turned off or adjusted for energy-saving mode
    components_to_adjust = {
        "Heater": "off",
        "AC": "off",
        "Light": "low",
        "SmartSocket": "off",
        "MusicPlayer": "off",
        "CleaningRobot": "off",
        "Curtain": "close",
        "Door": "locked",
        "Window": "closed",
        "Humidifier": "off"
    }
    
    # Set components to energy-saving mode
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type in components_to_adjust:
                actuator_status = components_to_adjust[actuator.actuator_type]
                if hasattr(actuator, actuator_status):
                    actuator.turn_off() if actuator_status == "off" else getattr(actuator, actuator_status)()
                    save_state_to_file(room.name, actuator.actuator_type, actuator_status)
    
    # Set lights to low brightness
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == "Light":
                actuator.set_brightness_level("low")
                save_state_to_file(room.name, actuator.actuator_type, "low")
    
    print("Energy-saving mode activated.")

# Example usage
if __name__ == "__main__":
    energy_saving_mode()