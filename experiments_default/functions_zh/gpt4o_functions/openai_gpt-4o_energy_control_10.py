# Based on the provided functional description and source code, the `function.py` file needs to implement the functionality to turn off the air conditioner (AC) in your smart home project. Here is the `function.py` file:

# function.py

from home.home_plan import home_plan, get_all_actuators

def main():
    # Create the home plan
    home = home_plan()

    # Get all AC actuators in the home
    ac_actuators = get_all_actuators(home, "AC")

    # Turn off all ACs
    for ac in ac_actuators:
        ac.turn_off()

if __name__ == "__main__":
    main()