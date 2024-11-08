# Based on your functional description of turning off the lights in the bedroom, I will create a `function.py` file that includes a main function to accomplish this task. The `function.py` will utilize the classes defined in your provided source code to interact with the light actuator in the bedroom.
# 
# Here is the `function.py` file that you can use in your `functions` folder:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators

def main():
    # Create the home plan
    home = home_plan()

    # Get the bedroom
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        # Get all light actuators in the bedroom
        light_actuators = get_room_actuators(home, "Bedroom")
        
        # Turn off all light actuators in the bedroom
        for light in light_actuators:
            if light.actuator_type == "Light":
                light.turn_off()
    else:
        print("Bedroom not found.")

if __name__ == "__main__":
    main()