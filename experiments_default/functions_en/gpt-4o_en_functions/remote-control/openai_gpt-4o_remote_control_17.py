# Given your functional description to turn off the living room lights, we'll create a `function.py` file that imports the necessary modules and includes the main function to achieve this task.
# 
# Here's the content for your `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light

def main():
    # Initialize the home plan
    home = home_plan()

    # Find the actuators in the living room
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    if living_room_actuators is not None:
        for actuator in living_room_actuators:
            # Check if the actuator is a Light and turn it off
            if isinstance(actuator, Light):
                actuator.turn_off()
                print(f"Turned off {actuator.id} in the Living Room")
    else:
        print("No actuators found in the Living Room.")

if __name__ == "__main__":
    main()