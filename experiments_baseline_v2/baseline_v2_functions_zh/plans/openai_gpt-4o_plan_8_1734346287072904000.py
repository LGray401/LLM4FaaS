# To create a smart home application based on your functional description, we'll implement a script that utilizes the existing `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files. This script will define the actions for the three scenarios you provided: "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN".
# 
# Below is the implementation of the script `smart_home.py` with the desired plans:
# 
# ```python
from home.home_plan import home_plan, get_room_actuators

def morning_plan(home):
    print("\nExecuting MORNING PLAN: 我睡醒了，请让我们家运转起来")
    # Turn on lights in the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light" or actuator.actuator_type == "MusicPlayer" or actuator.actuator_type == "CoffeeMachine":
            actuator.turn_on()

def leave_home_plan(home):
    print("\nExecuting LEAVE HOME PLAN: 我出门了，保护好家")
    # Lock doors and turn off all lights
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == "Door":
                actuator.turn_off()
            if actuator.actuator_type == "Light":
                actuator.turn_off()

def movie_plan(home):
    print("\nExecuting MOVIE PLAN: 打开电视，关上灯")
    # Turn on TV and turn off the lights in the LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    for actuator in living_room_actuators:
        if actuator.actuator_type == "SmartTV":
            actuator.turn_on()
        if actuator.actuator_type == "Light":
            actuator.turn_off()

def main():
    home = home_plan()

    # Execute different plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Script
# 
# Assuming you've stored this script in a file named `smart_home.py`, you can run it in a Linux terminal with the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation
# 
# - **MORNING PLAN**: In this plan, we turn on the lights, the music player, and the coffee machine in the living room to simulate the house waking up.
# - **LEAVE HOME PLAN**: This plan ensures that all lights are turned off and doors are locked when you leave the house.
# - **MOVIE PLAN**: Here, the TV is turned on, and the lights in the living room are turned off to create a suitable environment for watching a movie.
# 
# Make sure that the script and the `home` folder (containing `sensor.py`, `actuator.py`, `home_plan.py`, `config.py`) are in the same directory so that the imports work correctly. Adjust the actuators and sensors in each plan according to your setup and preferences.