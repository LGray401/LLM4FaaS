# Based on the functional description you provided and the existing code files, I will create a `function.py` file that includes a main function to control the lights, air conditioning, heating, and TV in the specified rooms (Living Room, Bedroom, and Bathroom). Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light, AC, Heater, SmartTV

def main():
    # Initialize the home plan
    home = home_plan()

    # Define the rooms and their respective actuators
    rooms_to_control = {
        "LivingRoom": ["Light", "AC", "SmartTV"],
        "Bedroom": ["Light", "AC"],
        "Bathroom": ["Light", "Heater"]
    }

    # Control actuators based on the functional description
    for room_name, actuator_types in rooms_to_control.items():
        room_actuators = get_room_actuators(home, room_name)
        
        if room_actuators is not None:
            for actuator in room_actuators:
                if actuator.actuator_type in actuator_types:
                    actuator.turn_on()  # Turn on the light, AC, or heater
        else:
            print(f"No actuators found for {room_name}.")

if __name__ == "__main__":
    main()