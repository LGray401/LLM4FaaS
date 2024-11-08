# Based on the provided functional description and source code, I will create a `function.py` file that contains a main function to control the smart home devices as described. The main function will turn on the lights in the living room, bedroom, and bathroom; turn on the air conditioners in the living room and bedroom; turn on the heater in the bathroom; and turn on the TV in the living room.
# 
# Here is the `function.py` file:

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

    # Function to turn on specific actuators in a given room
    def turn_on_actuators(room_name, actuator_types):
        actuators = get_room_actuators(home, room_name)
        if actuators:
            for actuator in actuators:
                if isinstance(actuator, tuple([globals()[act_type] for act_type in actuator_types])):
                    actuator.turn_on()
                    print(f"Turned on {actuator.actuator_type} in {room_name}")
        else:
            print(f"No actuators found in {room_name}")

    # Turn on the specified actuators in each room
    for room_name, actuator_types in rooms_to_control.items():
        turn_on_actuators(room_name, actuator_types)

if __name__ == "__main__":
    main()