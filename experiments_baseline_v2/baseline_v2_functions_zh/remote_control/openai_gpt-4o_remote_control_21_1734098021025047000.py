# Based on your functional description and the provided source code, we need to implement a Python script that orchestrates the smart home devices to perform the specified actions. Here's the plan:
# 
# 1. **Turn on the living room light and set it to medium brightness.**
# 2. **Play a stress-relieving song using the music player.**
# 3. **Turn on the coffee machine and make a cup of coffee.**
# 4. **Set the air conditioner to 22°C.**
# 5. **Close the curtain.**
# 6. **Start the cleaning robot.**
# 
# We'll create a new script, `smart_home.py`, that will leverage the classes and methods defined in your provided files to achieve these tasks.
# 
# ### `smart_home.py`
# 
# ```python
from home.home_plan import home_plan, get_room
from home.actuator import Light, MusicPlayer, CoffeeMachine, AC, Curtain, CleaningRobot

def main():
    # Initialize the home plan
    home = home_plan()

    # Get living room components
    living_room = get_room(home, "LivingRoom")

    # Task 1: Turn on the light and set brightness to medium
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("medium")

    # Task 2: Play a stress-relieving song
    for actuator in living_room.actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("stress_relief_playlist")

    # Task 3: Turn on the coffee machine and make coffee
    kitchen = get_room(home, "Kitchen")
    for actuator in kitchen.actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("espresso")

    # Task 4: Set the AC to 22°C
    for actuator in living_room.actuators:
        if isinstance(actuator, AC):
            actuator.turn_on()
            actuator.set_target_temperature(22)

    # Task 5: Close the curtain
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()

    # Task 6: Start the cleaning robot
    for actuator in living_room.actuators:
        if isinstance(actuator, CleaningRobot):
            actuator.turn_on()
            actuator.daily_routine()

if __name__ == "__main__":
    main()
# ```
# 
# ### Execution Command
# 
# To execute this script in a Linux terminal, navigate to the directory containing the `home` folder and run:
# 
# ```bash
# python smart_home.py
# ```
# 
# ### Explanation
# 
# - **Initialization**: The `home_plan()` function creates the structure of the house with all rooms and their devices.
# - **Task Implementation**: We locate the required devices in their respective rooms and invoke the appropriate methods to perform the desired actions.
# - **Logging**: The provided code already includes logging functionality, which will capture and log the actions performed by the actuators.
# 
# You can further customize the playlist name or coffee type according to your needs.