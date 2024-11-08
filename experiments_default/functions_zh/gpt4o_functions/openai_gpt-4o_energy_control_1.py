# To create the `function.py` file that follows the functional description "请关闭不必要的开关" (which translates to "Please turn off unnecessary switches"), we need to write a function that iterates through all sensors and actuators in the home, and turns off any that are currently on but not needed.
# 
# Here's how the `function.py` file would look like:

# function.py
from home.home_plan import home_plan, get_all_actuators

def turn_off_unnecessary_switches():
    home = home_plan()
    
    # Iterate through all actuators and turn off the ones that are on
    for room in home:
        for actuator in room.actuators:
            if actuator.get_status() == "on":
                actuator.turn_off()

def main():
    turn_off_unnecessary_switches()

if __name__ == "__main__":
    main()