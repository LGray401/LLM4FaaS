# To create a smart home application based on the provided functional description, we can leverage the existing classes and methods from the reference code files you've shared. We'll design an application that can execute the specified plans (MORNING PLAN, LEAVE HOME PLAN, MOVIE PLAN) using the available actuators and sensors within a simulated home environment.
# 
# Below is a new Python script that implements these plans. This script will interact with the classes from your existing code files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) to perform the desired actions. 
# 
# Let's create a new file called `smart_home_app.py` with the following content:
# 
# ```python
from home.home_plan import home_plan, get_all_actuators, get_room_actuators

def execute_morning_plan(home):
    print("\nExecuting MORNING PLAN:")
    # Open curtains
    for curtain in get_all_actuators(home, "Curtain"):
        curtain.turn_on()
    # Turn on lights
    for light in get_all_actuators(home, "Light"):
        light.turn_on()
    # Play soothing music
    for music_player in get_all_actuators(home, "MusicPlayer"):
        music_player.turn_on()
        music_player.play_music("Soothing Playlist")
    # Make coffee
    for coffee_machine in get_all_actuators(home, "CoffeeMachine"):
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

def execute_leave_home_plan(home):
    print("\nExecuting LEAVE HOME PLAN:")
    # Close main door
    for door in get_all_actuators(home, "Door"):
        door.lock()
    # Turn off lights
    for light in get_all_actuators(home, "Light"):
        light.turn_off()

def execute_movie_plan(home):
    print("\nExecuting MOVIE PLAN:")
    # Turn on TV
    for tv in get_all_actuators(home, "SmartTV"):
        tv.turn_on()
        tv.play_channel("Movie Channel")
    # Close curtains
    for curtain in get_all_actuators(home, "Curtain"):
        curtain.turn_off()
    # Dim lights
    for light in get_all_actuators(home, "Light"):
        light.turn_on()
        light.set_brightness_level("low")

def main():
    home = home_plan()

    # Execute the plans
    execute_morning_plan(home)
    execute_leave_home_plan(home)
    execute_movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Initialization**:
#    - The `home_plan` function is used to initialize the home setup with all rooms, sensors, and actuators.
# 
# 2. **Executing Plans**:
#    - Each plan function (`execute_morning_plan`, `execute_leave_home_plan`, `execute_movie_plan`) interacts with the actuators to perform actions like turning on/off lights, opening/closing curtains, etc.
#    - The `get_all_actuators` function from `home_plan.py` is used to retrieve all actuators of a specific type across the home.
# 
# 3. **Main Function**:
#    - The `main()` function initializes the home and executes each plan in sequence.
# 
# ### Command to Run the Application:
# 
# To run this application in a Linux terminal, ensure all necessary Python files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`, `smart_home_app.py`) are present in a folder named `home`. Then, use the following command:
# 
# ```bash
# python3 home/smart_home_app.py
# ```
# 
# This script will simulate the execution of the smart home plans using the available actuators and sensors.