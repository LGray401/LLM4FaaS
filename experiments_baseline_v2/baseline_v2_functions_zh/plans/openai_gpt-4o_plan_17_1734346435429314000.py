# To create a smart home application in Python that fulfills the functional description provided, we will need to implement a new script that makes use of the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files. This script will define different plans (MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN) using the actuators specified in the functional description.
# 
# Here's how you can implement the required functionality:
# 
# ### New Script: `smart_home.py`
# 
# ```python
from home.actuator import CoffeeMachine, Light, Curtain
from home.home_plan import home_plan, get_room_actuators

def morning_plan(home):
    print("\nExecuting Morning Plan...")
    # Find the CoffeeMachine in the Kitchen and turn it on
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    for actuator in kitchen_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")
            break

def leave_home_plan(home):
    print("\nExecuting Leave Home Plan...")
    # Turn off all lights in every room
    all_lights = [actuator for room in home for actuator in room.actuators if isinstance(actuator, Light)]
    for light in all_lights:
        light.turn_off()

def movie_plan(home):
    print("\nExecuting Movie Plan...")
    # Close the curtain in the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
            break

def main():
    home = home_plan()  # Create the home plan with all rooms and devices

    # Execute different plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Script
# 
# To run this script in a Linux terminal, you would save the script as `smart_home.py` in the same directory where your `home` folder (containing `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) is located. Then, execute the script using the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation
# 
# - **Morning Plan**: This plan finds the `CoffeeMachine` in the `Kitchen` and turns it on to make coffee.
# - **Leave Home Plan**: This plan finds all `Light` actuators in the home and turns them off.
# - **Movie Plan**: This plan finds the `Curtain` actuator in the `LivingRoom` and closes it (turns it on).
# 
# ### Assumptions
# 
# - The `CoffeeMachine` and `Curtain` actuators have a simple `turn_on` method, and the `CoffeeMachine` has a `make_coffee` method to simulate making coffee.
# - The `Light` actuator has a `turn_off` method to simulate turning off the light.
# - The existing classes and methods from the provided source code are used, and additional functionality (like making coffee) is simulated by calling the appropriate methods.