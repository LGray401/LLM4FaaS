from home.home_plan import get_room, get_room_actuators
from home.logger_config import logger

def main():
    """
    This function is the main function of the 'function.py' file.
    It implements the functionality described in the functional description.
    In this case, it turns off the light in the living room.
    """

    home = get_room(get_room_actuators, "LivingRoom")
    if home is not None:
        for actuator in home:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
                logger.info("Living room light turned off.")
                print("Living room light turned off.")
    else:
        logger.warning("Living room not found.")
        print("Living room not found.")

if __name__ == "__main__":
    main()

# This code file creates a `main()` function that:

# 1. **Gets the living room:** Uses the `get_room()` function from `home_plan.py` to find the living room and its actuators.
# 2. **Iterates through actuators:** Loops through the list of actuators in the living room.
# 3. **Finds the light:** Checks if each actuator is of type "Light".
# 4. **Turns off the light:** If a light is found, it calls its `turn_off()` method.

# This code assumes that there will be at least one light in the living room. You can modify it to handle situations where there might be multiple lights or no lights in the living room, based on your specific requirements. 
