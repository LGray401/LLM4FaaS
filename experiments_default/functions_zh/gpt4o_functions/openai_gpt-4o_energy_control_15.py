# Based on the given functional description and provided source code files, I will create a `function.py` file that contains the main function for your smart home project.
# 
# The main function will initialize the home plan, turn on all sensors and actuators, and print their statuses. Here is the `function.py`:
# 
# ## function.py

from home.home_plan import home_plan, print_home_plan, get_all_sensors, get_all_actuators

def main():
    # Initialize the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Turn on all sensors
    all_sensors = []
    for room in home:
        all_sensors.extend(room.sensors)

    for sensor in all_sensors:
        sensor.turn_on()

    # Turn on all actuators
    all_actuators = []
    for room in home:
        all_actuators.extend(room.actuators)

    for actuator in all_actuators:
        actuator.turn_on()

    # Print the status of all sensors and actuators
    print("\n---Sensor Status---")
    for sensor in all_sensors:
        sensor.get_status()

    print("\n---Actuator Status---")
    for actuator in all_actuators:
        actuator.get_status()

if __name__ == "__main__":
    main()