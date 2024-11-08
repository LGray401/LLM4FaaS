# To create a smart home application in Python based on your functional description, we can define a new Python script named `smart_home.py`. This script will utilize the existing classes and methods from the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files to implement the specified plans: "MORNING PLAN," "LEAVE HOME PLAN," and "MOVIE PLAN."
# 
# Here's the implementation of the `smart_home.py` script:
# 
# ```python
# smart_home.py

from home.home_plan import home_plan, get_room_actuators

def morning_plan(home):
    print("\nExecuting MORNING PLAN...")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()  # Open curtains
        elif isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("medium")  # Light brightness medium
        elif isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")  # Start coffee machine
        elif isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Mood Booster")  # Play mood music

def leave_home_plan(home):
    print("\nExecuting LEAVE HOME PLAN...")
    rooms = ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]
    
    for room_name in rooms:
        room_actuators = get_room_actuators(home, room_name)
        for actuator in room_actuators:
            if isinstance(actuator, Light) or isinstance(actuator, SmartSocket):
                actuator.turn_off()  # Turn off lights and sockets
            elif isinstance(actuator, Curtain):
                actuator.turn_on()  # Open curtains
            elif isinstance(actuator, Door):
                actuator.lock()  # Lock the door

def movie_plan(home):
    print("\nExecuting MOVIE PLAN...")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()  # Close curtains
        elif isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")  # Dim lights
        elif isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Favorite Movie")  # Smart TV adjusts for watching

def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Application
# 
# 1. Save the above script as `smart_home.py` in the same directory where your `home` folder is located.
# 
# 2. Open a terminal in the directory containing the `smart_home.py` script.
# 
# 3. Run the script using the following command:
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This script initializes the home state using the `home_plan` function and then executes each of the predefined plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. Each function operates the actuators according to the specifications provided in the functional description.