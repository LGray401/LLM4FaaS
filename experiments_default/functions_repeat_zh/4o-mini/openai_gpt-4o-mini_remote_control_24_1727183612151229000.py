# Based on your functional description of turning off the lights in the bedroom, I'll create a `function.py` file that utilizes the classes defined in your existing code. This file will contain a `main` function that locates the bedroom, retrieves the light actuators, and turns them off.
# 
# Here's the content for `function.py`:

# functions/function.py
from home.home_plan import home_plan, get_room, get_room_actuators

def main():
    # Create the home plan
    home = home_plan()
    
    # Get the bedroom room object
    bedroom = get_room(home, "Bedroom")
    
    if bedroom:
        # Retrieve the light actuators in the bedroom
        light_actuators = get_room_actuators(home, "Bedroom")
        
        if light_actuators:
            # Turn off all light actuators
            for light in light_actuators:
                light.turn_off()
        else:
            print("No light actuators found in the bedroom.")
    else:
        print("Bedroom not found in the home plan.")

if __name__ == "__main__":
    main()