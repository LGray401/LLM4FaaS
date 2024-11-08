# Certainly! Here is the 'function.py' file based on your functional description:

from home.home_plan import get_all_actuators

def main():
    # Get all actuators
    actuators = get_all_actuators()

    # Check the current plan
    current_plan = input("Enter the current plan: ")

    # Execute the corresponding actions based on the current plan
    if current_plan == "MORNING PLAN":
        open_curtains(actuators)
    elif current_plan == "LEAVE HOME PLAN":
        turn_off_lights(actuators)
        close_windows(actuators)
    elif current_plan == "MOVIE PLAN":
        turn_on_tv(actuators)
    else:
        print("Invalid plan")

def open_curtains(actuators):
    for actuator in actuators:
        if actuator.actuator_type == "Curtain":
            actuator.turn_on()

def turn_off_lights(actuators):
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_off()

def close_windows(actuators):
    for actuator in actuators:
        if actuator.actuator_type == "Window":
            actuator.turn_off()

def turn_on_tv(actuators):
    for actuator in actuators:
        if actuator.actuator_type == "SmartTV":
            actuator.turn_on()

if __name__ == "__main__":
    main()