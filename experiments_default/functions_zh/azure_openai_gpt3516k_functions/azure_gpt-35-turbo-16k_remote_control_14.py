# Sure! I have created the 'function.py' file in the 'functions' folder based on your provided functional description. Here is the content of the 'function.py' file:

from home.home_plan import home_plan, get_room, get_room_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Light
from home.logger_config import logger

def main():
    home = home_plan()
    room_name = "LivingRoom"
    room = get_room(home, room_name)
    
    if room:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                logger.info("The light in the living room is turned on.")
                break
        else:
            logger.warning("No light actuator found in the living room.")
    else:
        logger.warning("Living room not found in the home plan.")

if __name__ == "__main__":
    main()