# Based on the functional description and the provided source code, I will create a `function.py` file that turns off unnecessary switches. This file will locate in the `functions` folder and contain a main function that interacts with the provided components to accomplish the task.
# 
# Here's the `function.py` file:

import os
import sys

# Add the home directory to the sys.path for importing modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'home'))

from home.home_plan import home_plan, get_all_actuators

def turn_off_unnecessary_switches(home):
    all_lights = get_all_actuators(home, "Light")
    all_musics = get_all_actuators(home, "MusicPlayer")
    all_tvs = get_all_actuators(home, "SmartTV")
    all_sockets = get_all_actuators(home, "SmartSocket")
    all_heaters = get_all_actuators(home, "Heater")
    all_acs = get_all_actuators(home, "AC")
    all_coffeemachines = get_all_actuators(home, "CoffeeMachine")
    all_cleaningrobots = get_all_actuators(home, "CleaningRobot")
    all_doors = get_all_actuators(home, "Door")
    all_windows = get_all_actuators(home, "Window")
    all_curtains = get_all_actuators(home, "Curtain")
    all_notificationsenders = get_all_actuators(home, "NotificationSender")

    for actuator in (all_lights + all_musics + all_tvs + all_sockets + all_heaters + 
                     all_acs + all_coffeemachines + all_cleaningrobots + all_doors +
                     all_windows + all_curtains + all_notificationsenders):
        if actuator.get_status() == "on":
            actuator.turn_off()

def main():
    home = home_plan()
    turn_off_unnecessary_switches(home)

if __name__ == "__main__":
    main()