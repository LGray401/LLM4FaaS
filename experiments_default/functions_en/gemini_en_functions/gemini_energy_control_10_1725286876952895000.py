from home.home_plan import get_room_actuators, get_all_actuators
from home.logger_config import logger

def main():
    home = home_plan()
    room_name = "LivingRoom"
    actuators = get_room_actuators(home, room_name)
    # Turn off the air conditioner
    for actuator in actuators:
        if actuator.actuator_type == "AC":
            actuator.turn_off()
            logger.info(f"Turned off the air conditioner in {room_name}")
            print(f"Turned off the air conditioner in {room_name}")
            return
    logger.warning(f"No air conditioner found in {room_name}")
    print(f"No air conditioner found in {room_name}")

if __name__ == "__main__":
    main()