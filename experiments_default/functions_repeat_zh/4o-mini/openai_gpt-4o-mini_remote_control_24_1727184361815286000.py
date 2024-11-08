# Based on your functional description to turn off the light in the bedroom, I will create the `function.py` file that includes a main function to implement this functionality. 
# 
# Here's the `function.py` code:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators

def main():
    # Create the home plan
    home = home_plan()
    
    # Specify the room name
    room_name = "Bedroom"
    
    # Get the room object
    room = get_room(home, room_name)
    
    if room:
        # Get the actuators in the room
        actuators = get_room_actuators(home, room_name)
        
        if actuators:
            # Find the Light actuator and turn it off
            for actuator in actuators:
                if actuator.actuator_type == "Light":
                    actuator.turn_off()
                    break
        else:
            print(f"No actuators found in the {room_name}.")
    else:
        print(f"The room '{room_name}' does not exist in the home plan.")

if __name__ == "__main__":
    main()