# Sure! Here is the 'function.py' file based on your functional description and the provided source code:

from home.home_plan import home_plan, get_room_actuators

def main():
    home = home_plan()
    room_name = "LivingRoom"
    actuators = get_room_actuators(home, room_name)

    for actuator in actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_off()
            print(f"Turned off the lights in {room_name}")
            break

if __name__ == "__main__":
    main()