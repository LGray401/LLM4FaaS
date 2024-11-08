# Sure! I will create the 'function.py' file for you based on the given functional description and the provided source code. Here is the 'function.py' file:

from home.home_plan import home_plan, get_room_actuators

def turn_on_lights(room_name):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    
    if actuators is not None:
        for actuator in actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_on()
    else:
        print(f"No actuators found in {room_name}")

if __name__ == "__main__":
    turn_on_lights("LivingRoom")