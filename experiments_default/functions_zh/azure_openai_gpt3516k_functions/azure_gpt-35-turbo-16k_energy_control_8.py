# Sure! I will create a `function.py` file based on the given functional description and the provided source code files.

from home.home_plan import get_room_actuators, get_room_sensors, home_plan


def main():
    # Get the actuators and sensors of the room
    room_name = "LivingRoom"
    room_actuators = get_room_actuators(home_plan(), room_name)
    room_sensors = get_room_sensors(home_plan(), room_name)
    
    # Turn on the AC and set the target temperature to 17 degrees
    for actuator in room_actuators:
        if actuator.actuator_type == "AC":
            actuator.turn_on()
            actuator.set_target_temperature(17)
    
    # Close the window
    for actuator in room_actuators:
        if actuator.actuator_type == "Window":
            actuator.turn_off()
    
    # Print the current status of the sensors
    for sensor in room_sensors:
        sensor.get_status()

if __name__ == "__main__":
    main()