# Sure, I will create the 'function.py' file for your smart home project based on the given functional description and source code.
# 
# Here is the 'function.py' file:

from home.home_plan import home_plan, get_room_actuators

def main():
    home = home_plan()
    room_name = "Bedroom"
    actuator_type = "Light"

    room_actuators = get_room_actuators(home, room_name)
    if room_actuators:
        for actuator in room_actuators:
            if actuator.actuator_type == actuator_type:
                actuator.turn_off()
    else:
        print(f"No actuators found in {room_name}.")

if __name__ == "__main__":
    main()