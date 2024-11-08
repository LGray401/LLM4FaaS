# Based on the provided functional description and the source code files, we need to create a `function.py` file located in the `functions` folder. This file should contain the main function to turn off the air conditioner. 
# 
# Here is the content for `function.py`:

from home.home_plan import home_plan, get_all_actuators

def turn_off_air_conditioner():
    home = home_plan()
    all_ac_units = get_all_actuators(home, "AC")
    
    for ac in all_ac_units:
        ac.turn_off()

if __name__ == "__main__":
    turn_off_air_conditioner()