# To build a smart home application based on the provided functional description and source code files, you can create a new Python script that orchestrates the different plans (MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN) using the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.
# 
# Here's a Python script named `smart_home.py` that implements the plans you described. This script will utilize the components from the provided source code:
# 
# ```python
# smart_home.py

from home.home_plan import home_plan, get_room, get_all_actuators
from home.logger_config import logger

def morning_plan(home):
    logger.info("Executing Morning Plan...")
    bedroom_lights = get_all_actuators(home, "Light")
    coffee_machine = get_all_actuators(home, "CoffeeMachine")
    
    # Turn on bedroom lights
    for light in bedroom_lights:
        if "Bedroom" in light.id:
            light.turn_on()
            light.set_brightness_level("high")
    
    # Turn on coffee machine
    if coffee_machine:
        coffee_machine[0].turn_on()
        coffee_machine[0].make_coffee("Espresso")

def leave_home_plan(home):
    logger.info("Executing Leave Home Plan...")
    all_lights = get_all_actuators(home, "Light")
    doors = get_all_actuators(home, "Door")
    
    # Turn off all lights
    for light in all_lights:
        light.turn_off()

    # Lock all doors
    for door in doors:
        door.lock()

def movie_plan(home):
    logger.info("Executing Movie Plan...")
    living_room_lights = get_all_actuators(home, "Light")
    smart_tv = get_all_actuators(home, "SmartTV")
    
    # Dim living room lights
    for light in living_room_lights:
        if "LivingRoom" in light.id:
            light.turn_on()
            light.set_brightness_level("low")
    
    # Turn on smart TV
    if smart_tv:
        smart_tv[0].turn_on()
        smart_tv[0].play_channel("Netflix")

def main():
    home = home_plan()

    # Execute each plan
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run
# 
# 1. Save the above script as `smart_home.py` in the same directory where you have the `home` folder containing the provided source code files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`).
# 
# 2. Open a terminal and navigate to the directory containing `smart_home.py`.
# 
# 3. Run the script with the following command:
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This script will simulate the three plans by interacting with the home setup defined in your `home_plan.py`. The `morning_plan` will turn on the bedroom lights and coffee machine, the `leave_home_plan` will turn off all lights and lock all doors, and the `movie_plan` will dim the living room lights and turn on the smart TV to a specific channel. Adjust the implementation as needed to fit your specific use case or expand on this functionality by adding more details to each plan.