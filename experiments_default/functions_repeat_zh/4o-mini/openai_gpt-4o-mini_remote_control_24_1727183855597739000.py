# Based on your functional description to turn off the lights in the bedroom, here’s how the `function.py` file can be structured. This script will utilize the classes defined in your existing source code files to turn off the light actuator in the bedroom.
# 
# Here’s the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators

def main():
    # Create the home layout
    home = home_plan()

    # Specify the room name
    room_name = "Bedroom"

    # Get the room object
    bedroom = get_room(home, room_name)
    
    if bedroom is not None:
        # Get all actuators in the bedroom
        light_actuators = get_room_actuators(home, room_name)
        
        # Turn off all light actuators in the bedroom
        for actuator in light_actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_off()

if __name__ == "__main__":
    main()