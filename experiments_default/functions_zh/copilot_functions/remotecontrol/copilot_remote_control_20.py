# Based on the functional description and the provided source code, you want to create a `function.py` file that contains the main function for your smart home project. The main function should control the air conditioner and the cleaning robot based on certain conditions.
#
# Here is a high-level plan:
#
# 1. Import necessary modules and classes from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 2. Define a function `main` that will control the smart home system.
# 3. In the `main` function, create an instance of the home plan.
# 4. Get the air conditioner and cleaning robot actuators.
# 5. Implement the logic to control the air conditioner and cleaning robot based on the functional description.
#
# Here is the Python code for `function.py`:
#
# ```python
from home.sensor import IndoorTemperatureSensor
from home.actuator import AC, CleaningRobot
from home.home_plan import home_plan, get_all_actuators
from home.config import TEMP_HIGH

def main():
    # Create an instance of the home plan
    home = home_plan()

    # Get the air conditioner and cleaning robot actuators
    acs = get_all_actuators(home, "AC")
    cleaning_robots = get_all_actuators(home, "CleaningRobot")

    # Control the air conditioner and cleaning robot based on the functional description
    for ac in acs:
        # If the indoor temperature is higher than the high threshold, turn on the air conditioner
        indoor_temp_sensor = IndoorTemperatureSensor(ac.room_name)
        if indoor_temp_sensor.get_reading() > TEMP_HIGH:
            ac.turn_on()
        else:
            ac.turn_off()

    for cleaning_robot in cleaning_robots:
        # If there is no one at home, start the cleaning robot
        # Here we assume that we have a way to check if there is anyone at home
        # If not, we need to implement this part according to the actual situation
        if not is_anyone_at_home():
            cleaning_robot.turn_on()
        else:
            cleaning_robot.turn_off()

def is_anyone_at_home():
    # Implement the logic to check if there is anyone at home
    # This is a placeholder and needs to be replaced with the actual implementation
    pass

if __name__ == "__main__":
    main()
# ```
#
# Please replace the `is_anyone_at_home` function with the actual implementation. This function should return `True` if there is anyone at home, and `False` otherwise.