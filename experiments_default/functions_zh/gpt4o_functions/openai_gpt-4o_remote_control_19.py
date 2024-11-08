# Sure! Below is the `function.py` file that you requested, placed in the `functions` folder. This file will contain a main function to open the living room air conditioner and set it to 26 degrees Celsius.

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.logger_config import logger

def main():
    # Create home plan
    home = home_plan()

    # Get actuators in the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Find the AC in the LivingRoom and set it to 26 degrees
    if living_room_actuators:
        for actuator in living_room_actuators:
            if actuator.actuator_type == "AC":
                actuator.turn_on()
                actuator.set_target_temperature(26)
                print(f"The {actuator.actuator_type} in {actuator.room_name} is set to {actuator.target_temperature}°C.")
                logger.info(f"The {actuator.actuator_type} in {actuator.room_name} is set to {actuator.target_temperature}°C.")
                break
        else:
            print("No AC found in the LivingRoom.")
            logger.warning("No AC found in the LivingRoom.")
    else:
        print("No actuators found in the LivingRoom.")
        logger.warning("No actuators found in the LivingRoom.")

if __name__ == "__main__":
    main()