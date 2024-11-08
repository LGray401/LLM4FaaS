# Here is the 'function.py' file based on your functional description:

from home.home_plan import home_plan, get_room_actuators

def turn_off_lights_in_living_room():
    home = home_plan()
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_off()

if __name__ == "__main__":
    turn_off_lights_in_living_room()