from home.actuator import AC, Light
from home.home_plan import home_plan, get_room_actuators, print_home_plan

# todo:
#   1. get the whole room plan
#   2. keyword is related to (one) specific rooms.
#   2. use the sensor readings in that room to trigger actuators in that room.
# current home plan
rooms_at_home = home_plan()  # return rooms


def morning_plan():
    # bedroom: turn on lights, open curtain
    bedroom_actuators = get_room_actuators(rooms_at_home, "Bedroom")

    lights_count = 0
    # has_curtain = False

    for actor in bedroom_actuators:
        if isinstance(actor, Light):
            lights_count += 1
            # print(f"we find {lights_count} lights now")
            actor.turn_on()

    if lights_count == 0:
        print("There is no light at home")
    else:
        print(f"There is {lights_count} lights in the Bedroom")


def morning_plan_with_id(light_id_to_turn_on=None):
    # current home plan
    # rooms_at_home = home_plan()  # return rooms
    # bedroom: turn on lights, open curtain
    bedroom_actuators = get_room_actuators(rooms_at_home, "Bedroom")

    # Track the number of lights found
    lights_count = 0

    for actor in bedroom_actuators:
        if isinstance(actor, Light):
            lights_count += 1
            if actor.id == light_id_to_turn_on:
                print(f"Turning on light with ID {light_id_to_turn_on} in the Bedroom.")
                actor.turn_on()
                return  # Exit the function after turning on the specified light

    # If no matching light is found, print a warning
    print(f"Light with ID {light_id_to_turn_on} not found in the Bedroom.")
    print(f"There are {lights_count} lights in the Bedroom.")


if __name__ == "__main__":
    morning_plan_with_id("/Actuator/Light/Bedroom/1")
    morning_plan()

    print_home_plan(rooms_at_home)
