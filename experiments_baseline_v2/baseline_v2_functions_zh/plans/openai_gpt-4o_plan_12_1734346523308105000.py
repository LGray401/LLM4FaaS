# Based on your functional description and the provided source code, I'll create a Python script that can execute the specified smart home plans: "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN". These plans will leverage the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` modules.
# 
# Here's the implementation of the main script, `smart_home.py`, which will be located in the same directory as the `home` folder:
# 
# ```python
import sys
from home.home_plan import home_plan, get_all_actuators

def execute_morning_plan(home):
    print("\nExecuting MORNING PLAN:")
    # 窗帘打开 音乐响起 咖啡机工作
    curtains = get_all_actuators(home, "Curtain")
    music_players = get_all_actuators(home, "MusicPlayer")
    coffee_machines = get_all_actuators(home, "CoffeeMachine")

    for curtain in curtains:
        curtain.turn_on()

    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Morning Playlist")

    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

def execute_leave_home_plan(home):
    print("\nExecuting LEAVE HOME PLAN:")
    # 入户门关闭 灯关闭
    doors = get_all_actuators(home, "Door")
    lights = get_all_actuators(home, "Light")

    for door in doors:
        door.turn_off()

    for light in lights:
        light.turn_off()

def execute_movie_plan(home):
    print("\nExecuting MOVIE PLAN:")
    # 窗帘关闭 电视打开
    curtains = get_all_actuators(home, "Curtain")
    tvs = get_all_actuators(home, "SmartTV")

    for curtain in curtains:
        curtain.turn_off()

    for tv in tvs:
        tv.turn_on()
        tv.play_channel("Movie Channel")

def main(plan_name):
    home = home_plan()

    if plan_name == "MORNING_PLAN":
        execute_morning_plan(home)
    elif plan_name == "LEAVE_HOME_PLAN":
        execute_leave_home_plan(home)
    elif plan_name == "MOVIE_PLAN":
        execute_movie_plan(home)
    else:
        print(f"Unknown plan: {plan_name}. Please use MORNING_PLAN, LEAVE_HOME_PLAN, or MOVIE_PLAN.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python smart_home.py <PLAN_NAME>")
    else:
        main(sys.argv[1])
# ```
# 
# ### Instructions to Run the Script
# 
# 1. **Save the Script**: Save the above script as `smart_home.py` in the same directory where the `home` folder is located.
# 
# 2. **Usage**: Open a terminal and navigate to the directory where `smart_home.py` is located. Use the following command to execute different plans:
# 
#    - For the Morning Plan:
#      ```bash
#      python smart_home.py MORNING_PLAN
#      ```
# 
#    - For the Leave Home Plan:
#      ```bash
#      python smart_home.py LEAVE_HOME_PLAN
#      ```
# 
#    - For the Movie Plan:
#      ```bash
#      python smart_home.py MOVIE_PLAN
#      ```
# 
# This script utilizes the provided framework to activate different plans based on your description. Adjustments can be made to the script if the actuators or sensors need additional functionality or logic specific to your environment.