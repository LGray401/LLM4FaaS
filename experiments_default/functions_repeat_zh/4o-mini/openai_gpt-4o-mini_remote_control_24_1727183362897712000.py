# Based on the functional description you provided ("请把卧室的灯关了"), which translates to "Please turn off the light in the bedroom," I will create a `function.py` file that contains the main function to accomplish this task. This file will interact with the classes defined in your provided source code.
# 
# Here is the content for `function.py`:

# functions/function.py
from home.home_plan import home_plan, get_room, get_room_actuators

def main():
    # Create the home plan
    home = home_plan()
    
    # Get the room you want to control
    room_name = "Bedroom"
    room = get_room(home, room_name)
    
    if room:
        # Get all actuators (lights) in the bedroom
        lights = get_room_actuators(home, room_name)
        
        if lights:
            # Turn off all lights in the bedroom
            for light in lights:
                if light.actuator_type == "Light":
                    light.turn_off()
        else:
            print(f"No lights found in {room_name}.")
    else:
        print(f"Room '{room_name}' not found.")

if __name__ == "__main__":
    main()