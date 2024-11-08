# Based on your functional description of turning on the light ("开灯"), I will create a `function.py` file that includes a main function to achieve this. The main function will interact with the classes defined in your existing code to turn on the lights in a specified room.
# 
# Here is the content for the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room, get_room_actuators

def turn_on_lights(room_name):
    # Get the home layout
    home = home_plan()
    
    # Retrieve the specified room
    room = get_room(home, room_name)
    
    if room is not None:
        # Retrieve all the light actuators in the room
        lights = get_room_actuators(home, room_name)
        
        if lights:
            for light in lights:
                light.turn_on()  # Turn on each light actuator
        else:
            print(f"No lights found in {room_name}.")
    else:
        print(f"Room '{room_name}' not found.")

def main():
    # Example usage
    room_name = "LivingRoom"  # Change this to the desired room name
    turn_on_lights(room_name)

if __name__ == "__main__":
    main()