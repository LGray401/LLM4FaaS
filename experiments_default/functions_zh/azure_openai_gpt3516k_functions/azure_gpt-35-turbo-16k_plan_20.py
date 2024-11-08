# Here is the 'function.py' file based on your functional description and the provided source code:

from home.home_plan import print_home_plan, get_room, get_room_actuators, get_room_sensors, get_all_sensors, get_all_actuators

def main():
    # Print Home Plan
    home = home_plan()
    print_home_plan(home)

    # Get Room
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")

    # Get Sensors and Actuators in a Room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get All Sensors and Actuators of a Specific Type
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    light_actuators = get_all_actuators(home, "Light")

if __name__ == "__main__":
    main()