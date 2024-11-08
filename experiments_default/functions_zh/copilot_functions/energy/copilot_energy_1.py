# Based on the functional description and the provided source code, it seems that you want to create a function that turns off unnecessary switches in your smart home project. The functional description is in Chinese and translates to "Please turn off unnecessary switches".
#
# Here is a plan for the function:
#
# 1. Import necessary modules and classes from the provided source code.
# 2. Define a function named `turn_off_unnecessary_switches`.
# 3. In this function, iterate over all rooms in the home.
# 4. For each room, iterate over all actuators.
# 5. If the status of an actuator is 'on', turn it off.
#
# Here is the Python code for the function:
#
# ```python
from zhome_plan import home_plan, get_all_actuators

def turn_off_unnecessary_switches():
    home = home_plan()
    all_actuators = get_all_actuators(home, "Actuator")
    for actuator in all_actuators:
        if actuator.get_status() == "on":
            actuator.turn_off()

if __name__ == "__main__":
    turn_off_unnecessary_switches()
# ```
#
# This function should be placed in a new file named `function.py` in the 'functions' folder as per your project structure. This function turns off all actuators in the home that are currently on. Please modify the function as needed to suit your specific requirements.