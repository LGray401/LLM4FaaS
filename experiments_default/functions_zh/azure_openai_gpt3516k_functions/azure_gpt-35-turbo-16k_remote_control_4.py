# Sure! Here is the 'function.py' file based on the provided functional description and the given source code:

from home.home_plan import home_plan, get_room_actuators

def main():
    # Define the room and component names
    room_name = "LivingRoom"
    actuator_type = "Light"

    # Get the actuators for the specified room and component type
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    target_actuators = [actuator for actuator in actuators if actuator.actuator_type == actuator_type]

    # Turn off the specified actuators
    for actuator in target_actuators:
        actuator.turn_off()

if __name__ == "__main__":
    main()