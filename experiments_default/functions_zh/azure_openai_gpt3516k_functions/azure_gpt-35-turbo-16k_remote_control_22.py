# Sure! Here is the 'function.py' file based on your given functional description and the provided source code files:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators, print_home_plan


def main():
    # Create the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Get the sensors and actuators of the desired rooms
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    bedroom_sensors = get_room_sensors(home, "Bedroom")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    bathroom_sensors = get_room_sensors(home, "Bathroom")
    bathroom_actuators = get_room_actuators(home, "Bathroom")

    # Turn on the lights in the living room, bedroom, and bathroom
    for sensor in living_room_sensors:
        if sensor.sensor_type == "LightIntensive":
            sensor.turn_on()
    for sensor in bedroom_sensors:
        if sensor.sensor_type == "LightIntensive":
            sensor.turn_on()
    for sensor in bathroom_sensors:
        if sensor.sensor_type == "LightIntensive":
            sensor.turn_on()

    # Turn on the air conditioners in the living room and bedroom
    for actuator in living_room_actuators:
        if actuator.actuator_type == "AC":
            actuator.turn_on()
    for actuator in bedroom_actuators:
        if actuator.actuator_type == "AC":
            actuator.turn_on()

    # Turn on the heater in the bathroom
    for actuator in bathroom_actuators:
        if actuator.actuator_type == "Heater":
            actuator.turn_on()

    # Turn on the TV in the living room
    for actuator in living_room_actuators:
        if actuator.actuator_type == "SmartTV":
            actuator.turn_on()

    # Print the status of the sensors and actuators in the living room, bedroom, and bathroom
    for sensor in living_room_sensors:
        sensor.get_status()
    for sensor in bedroom_sensors:
        sensor.get_status()
    for sensor in bathroom_sensors:
        sensor.get_status()
    for actuator in living_room_actuators:
        actuator.get_status()
    for actuator in bedroom_actuators:
        actuator.get_status()
    for actuator in bathroom_actuators:
        actuator.get_status()


if __name__ == "__main__":
    main()