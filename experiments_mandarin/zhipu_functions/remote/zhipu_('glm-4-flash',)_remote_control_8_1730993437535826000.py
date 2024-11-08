# # function.py

from home.sensor import IndoorTemperatureSensor
from home.actuator import AC, Light
from home.home_plan import home_plan
from home.logger_config import logger

def main():
    # Load the home plan
    home = home_plan()
    
    # Find the Living Room
    living_room = get_room(home, "LivingRoom")
    
    if living_room is None:
        logger.error("Failed to find the Living Room.")
        return

    # Find the AC and Light in the Living Room
    ac = get_room_actuators(living_room, "AC")
    light = get_room_actuators(living_room, "Light")

    if ac and light:
        # Turn on the AC and set temperature to 17 degrees
        ac[0].set_target_temperature(17)
        logger.info("AC in Living Room is turned on and temperature is set to 17 degrees.")

        # Turn on the light
        light[0].turn_on()
        logger.info("Light in Living Room is turned on.")
    else:
        logger.error("Failed to find AC or Light in the Living Room.")

def get_room(home, room_name):
    for room in home:
        if room.name == room_name:
            return room
    return None

def get_room_actuators(room, actuator_type):
    return [actuator for actuator in room.actuators if actuator.actuator_type == actuator_type]

if __name__ == "__main__":
    main()