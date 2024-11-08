# Based on the provided functional description and the given source code files, I'll create a `function.py` file that will contain the main function to turn off the living room light. This file will be placed in the `functions` folder.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators

def main():
    # Create the home plan
    home = home_plan()

    # Get all actuators in the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Find the Light actuator and turn it off
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_off()
            print(f"The light in the Living Room has been turned off.")
            return

    print("No light actuator found in the Living Room.")

if __name__ == "__main__":
    main()