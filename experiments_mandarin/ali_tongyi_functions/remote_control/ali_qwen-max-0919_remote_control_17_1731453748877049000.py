# Based on your functional description and the provided source code, I will create a `function.py` file that contains a main function to close the living room light. The `function.py` will be placed in the `functions` folder.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import get_room_actuators
from home.actuator import Light

def main():
    # Define the name of the room where the light needs to be turned off
    room_name = "LivingRoom"

    # Get the actuators for the specified room
    actuators = get_room_actuators(home_plan(), room_name)

    if actuators:
        # Iterate through the actuators to find the Light actuator and turn it off
        for actuator in actuators:
            if isinstance(actuator, Light):
                print(f"Turning off the light in {room_name}.")
                actuator.turn_off()
                return
        print(f"No light found in {room_name}.")
    else:
        print(f"No actuators found in {room_name}.")

if __name__ == "__main__":
    from home.home_plan import home_plan  # Import home_plan function here to avoid circular import issues
    main()