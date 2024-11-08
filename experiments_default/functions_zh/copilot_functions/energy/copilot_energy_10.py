# Based on the functional description and the provided source code, you want to create a function that turns off the air conditioner (AC) in your smart home project. Here is a Python function that you can add to your `function.py` file:
#
# ```python
from home.actuator import AC
from home.home_plan import get_all_actuators

def turn_off_ac(home):
    # Get all AC units in the home
    all_ac_units = get_all_actuators(home, "AC")

    # Turn off each AC unit
    for ac_unit in all_ac_units:
        ac_unit.turn_off()

    print("All AC units have been turned off.")
# ```
#
# This function retrieves all the AC units in your home and turns each one off. You can call this function with your `home` object as an argument to turn off all the AC units.