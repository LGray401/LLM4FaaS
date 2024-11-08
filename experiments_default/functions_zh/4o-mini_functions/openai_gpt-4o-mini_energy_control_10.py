# Here's the `function.py` file that contains the main function to turn off the air conditioning (AC) based on the provided functional description. This implementation assumes that there is at least one AC actuator in the home setup.

# functions/function.py

from home.home_plan import home_plan
from home.actuator import AC

def turn_off_ac():
    home = home_plan()  # Create home plan with rooms and components
    all_ac_units = []

    # Collect all AC units in the home
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, AC):
                all_ac_units.append(actuator)
    
    # Turn off all AC units
    if all_ac_units:
        for ac in all_ac_units:
            ac.turn_off()
    else:
        print("No AC units found in the home.")

def main():
    print("Turning off all AC units...")
    turn_off_ac()

if __name__ == "__main__":
    main()