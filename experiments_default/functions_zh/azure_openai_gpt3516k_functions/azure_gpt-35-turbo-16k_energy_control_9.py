# Sure! Here's the 'function.py' file for your smart home project:

from home.home_plan import home_plan, print_home_plan, get_room_actuators, get_room_sensors, get_all_actuators


def main():
    # Get the list of rooms and their components
    home = home_plan()

    # Print the home plan
    # print_home_plan(home)

    # Turn off all lights in the home
    turn_off_lights(home)

    # Close all water sources in the home
    close_water_sources(home)

def turn_off_lights(home):
    # Get all light actuators in the home
    light_actuators = get_all_actuators(home, "Light")

    # Turn off each light actuator
    for actuator in light_actuators:
        actuator.turn_off()

def close_water_sources(home):
    # Get all water source actuators in the home
    water_source_actuators = get_all_actuators(home, "WaterSource")

    # Close each water source actuator
    for actuator in water_source_actuators:
        actuator.close()

# Run the main function
if __name__ == "__main__":
    main()