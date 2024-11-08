# Based on the provided functional description and the source code of the smart home project, I will create a `function.py` file that implements the main function to enable the energy-saving mode for the smart home system. 
# 
# Here's the `function.py` file:

# function.py
from home.home_plan import home_plan, get_all_actuators

def energy_saving_mode():
    # Create the home plan
    home = home_plan()
    
    # Define the actuators to be controlled
    actuators_to_control = {
        "Light": lambda actuator: actuator.set_brightness_level("low"),
        "Curtain": lambda actuator: actuator.turn_off(),
        "SmartSocket": lambda actuator: actuator.turn_off(),
        "Humidifier": lambda actuator: actuator.turn_off(),
        "CleaningRobot": lambda actuator: actuator.turn_off(),
        "MusicPlayer": lambda actuator: actuator.turn_off(),
        "SmartTV": lambda actuator: actuator.turn_off()
    }
    
    # Iterate over each actuator type and perform the corresponding action
    for actuator_type, action in actuators_to_control.items():
        actuators = get_all_actuators(home, actuator_type)
        for actuator in actuators:
            action(actuator)
            print(f"Set {actuator.id} to energy saving mode.")
    
if __name__ == "__main__":
    energy_saving_mode()