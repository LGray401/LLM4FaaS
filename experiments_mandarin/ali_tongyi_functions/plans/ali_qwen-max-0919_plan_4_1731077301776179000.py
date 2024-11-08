# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to handle the morning plan, leave home plan, and movie plan. This file will be placed in the `functions` folder.
# 
# ### Functional Description
# - **MORNING PLAN:**
#   - Open the curtains in all rooms.
# - **LEAVE HOME PLAN:**
#   - Turn off all lights in the house.
# - **MOVIE PLAN:**
#   - Set the brightness level of all lights to "low" in the living room.
# 
# ### `function.py`

from home.home_plan import home_plan, get_all_actuators, get_room_actuators
from home.actuator import Curtain, Light

def execute_morning_plan(home):
    """
    Executes the morning plan by opening all curtains in the house.
    """
    for curtain in get_all_actuators(home, "Curtain"):
        curtain.turn_on()
        print(f"Curtain {curtain.id} is now open.")
    print("Morning plan executed successfully.")

def execute_leave_home_plan(home):
    """
    Executes the leave home plan by turning off all lights in the house.
    """
    for light in get_all_actuators(home, "Light"):
        light.turn_off()
        print(f"Light {light.id} is now off.")
    print("Leave home plan executed successfully.")

def execute_movie_plan(home):
    """
    Executes the movie plan by setting the brightness level of all lights in the living room to 'low'.
    """
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if isinstance(light, Light):
            light.set_brightness_level("low")
            print(f"Light {light.id} brightness set to low.")
    print("Movie plan executed successfully.")

def main():
    home = home_plan()
    
    # Execute the plans
    execute_morning_plan(home)
    execute_leave_home_plan(home)
    execute_movie_plan(home)

if __name__ == "__main__":
    main()