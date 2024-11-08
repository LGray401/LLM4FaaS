# Based on your functional description to turn off the lights in the bedroom, I'll create a `function.py` file that integrates with the existing components of your smart home project. This script will include a main function that retrieves the bedroom's light actuator and turns it off. Here's how the `function.py` file would look:

# functions/function.py
from home.home_plan import home_plan, get_room, get_room_actuators

def main():
    # Create the home plan
    home = home_plan()

    # Get the bedroom
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        # Get the actuators in the bedroom
        lights = get_room_actuators(home, "Bedroom")
        if lights:
            # Turn off all lights in the bedroom
            for light in lights:
                if light.actuator_type == "Light":
                    light.turn_off()
        else:
            print("No light actuators found in the bedroom.")
    else:
        print("Bedroom not found in the home plan.")

if __name__ == "__main__":
    main()