# Given your functional description and the source code for the smart home project, I will create the `function.py` file to implement the main function that handles the different plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here's the `function.py` file:

# function.py
import sys
from home.home_plan import home_plan, get_all_actuators
from home.logger_config import logger

def morning_plan(home):
    # 打开窗帘 (Open Curtains)
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

def leave_home_plan(home):
    # 关闭灯光，窗户 (Turn off lights, close windows)
    lights = get_all_actuators(home, "Light")
    windows = get_all_actuators(home, "Window")
    for light in lights:
        light.turn_off()
    for window in windows:
        window.turn_off()

def movie_plan(home):
    # 打开电视 (Turn on the TV)
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        tv.turn_on()

def main(plan_name):
    # Initialize the home plan
    home = home_plan()

    # Execute the desired plan
    if plan_name == "morning":
        morning_plan(home)
    elif plan_name == "leave_home":
        leave_home_plan(home)
    elif plan_name == "movie":
        movie_plan(home)
    else:
        print(f"Unknown plan: {plan_name}")
        logger.error(f"Unknown plan: {plan_name}")
        return

    print(f"{plan_name.capitalize()} plan executed successfully.")
    logger.info(f"{plan_name.capitalize()} plan executed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python function.py <plan_name>")
        sys.exit(1)

    plan_name = sys.argv[1]
    main(plan_name)