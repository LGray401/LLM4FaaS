# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to close the lights in the living room. This file will be placed in the `functions` folder as per your requirement.
# 
# Here is the `function.py`:

# functions/function.py

from home.home_plan import get_room_actuators, home_plan

def main():
    # Create the home plan
    home = home_plan()

    # Get the actuators in the living room
    room_name = "LivingRoom"
    actuators = get_room_actuators(home, room_name)

    if actuators:
        # Find and turn off all lights in the living room
        for actuator in actuators:
            if actuator.actuator_type == "Light":
                if actuator.status == "on":
                    actuator.turn_off()
                    print(f"Turned off light: {actuator.id}")
                else:
                    print(f"Light {actuator.id} is already off.")
    else:
        print(f"No actuators found in {room_name}.")

if __name__ == "__main__":
    main()