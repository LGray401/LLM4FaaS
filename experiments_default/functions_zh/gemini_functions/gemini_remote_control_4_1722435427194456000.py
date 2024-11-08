from home.home_plan import get_room, get_room_actuators
from home.logger_config import logger


def main():
    """
    Main function to control the smart home.
    """
    # Create the home plan
    home = get_room(home, "LivingRoom")

    # Get the actuators in the living room
    actuators = get_room_actuators(home, "LivingRoom")

    # Find the Light actuator
    light = None
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            light = actuator
            break

    if light:
        # Turn off the light
        light.turn_off()
        logger.info(f"Turned off the light in the living room.")
        print(f"Turned off the light in the living room.")
    else:
        logger.warning("Could not find the light actuator in the living room.")
        print("Could not find the light actuator in the living room.")


if __name__ == "__main__":
    main()


# **Explanation:**

# 1. **Import Necessary Modules:**
#    - `from home.home_plan import get_room, get_room_actuators`: Imports functions to get specific rooms and their actuators from the `home_plan.py` file.
#    - `from home.logger_config import logger`: Imports the logger for logging events.

# 2. **`main` Function:**
#    - **Create Home Plan:** Creates the home plan using `get_room`. 
#    - **Get Living Room Actuators:** Retrieves all actuators in the living room using `get_room_actuators`.
#    - **Find the Light Actuator:** Iterates through the actuators and finds the one with the type "Light". 
#    - **Turn Off the Light:** If the light actuator is found, it turns off the light using `light.turn_off()`.
#    - **Error Handling:** If the light actuator is not found, it logs a warning message.

# **How to Use:**

# 1. **Save the Code:** Save the code as `function.py` inside your `functions` folder.
# 2. **Run the Script:** Execute the `function.py` file. This will turn off the light in the living room of your smart home simulation.

# **Remember:** This script assumes you have already implemented the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files correctly. 
