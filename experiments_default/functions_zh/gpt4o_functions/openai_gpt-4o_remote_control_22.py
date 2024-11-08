# Based on the functional description and the provided source code for your smart home project, here is the contents of the `function.py` file that will be located in the `functions` folder. This file will contain the `main` function that performs the specified actions:

from home.home_plan import home_plan, get_room_actuators

def main():
    home = home_plan()

    # Actions for Living Room
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light" or actuator.actuator_type == "AC" or actuator.actuator_type == "SmartTV":
            actuator.turn_on()

    # Actions for Bedroom
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    for actuator in bedroom_actuators:
        if actuator.actuator_type == "Light" or actuator.actuator_type == "AC":
            actuator.turn_on()

    # Actions for Bathroom
    bathroom_actuators = get_room_actuators(home, "Bathroom")
    for actuator in bathroom_actuators:
        if actuator.actuator_type == "Light" or actuator.actuator_type == "Heater":
            actuator.turn_on()

if __name__ == "__main__":
    main()