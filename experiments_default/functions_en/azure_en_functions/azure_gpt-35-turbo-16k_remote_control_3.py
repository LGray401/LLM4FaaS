# Sure, here is the 'function.py' file based on your functional description:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def main():
    # Get the home plan
    home = home_plan()
    
    # Get the sensors and actuators in the living room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Turn off the lights in the living room
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_off()

if __name__ == "__main__":
    main()