# # function.py

import time
from home.sensor import get_room_sensors, get_room_actuators
from home.actuator import Actuator
from home_plan import home_plan

def main():
    home = home_plan()
    time.sleep(2)  # Simulating delay before running the plan

    # Example: Turn on the lights in the Living Room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        lights = [actuator for actuator in get_room_actuators(living_room, "Light") if actuator.status == "off"]
        for light in lights:
            light.turn_on()
            time.sleep(1)  # Simulating time taken to turn on the light

    # Example: Adjust the temperature in the Living Room
    ac = [actuator for actuator in get_room_actuators(living_room, "AC") if actuator.status == "off"]
    if ac:
        ac[0].set_target_temperature(22)  # Set target temperature to 22°C
        time.sleep(2)  # Simulating time taken to adjust the temperature

    # Example: Lock the door in the Living Room
    door = [actuator for actuator in get_room_actuators(living_room, "Door") if actuator.status == "locked"]
    if door:
        door[0].lock()
        time.sleep(1)  # Simulating time taken to lock the door

    # Example: Turn on the Cleaning Robot in the Living Room
    cleaning_robot = [actuator for actuator in get_room_actuators(living_room, "CleaningRobot") if actuator.status == "off"]
    if cleaning_robot:
        cleaning_robot[0].turn_on()
        time.sleep(5)  # Simulating time taken for the Cleaning Robot to complete its task

    # Add more functionality as needed

if __name__ == "__main__":
    main()