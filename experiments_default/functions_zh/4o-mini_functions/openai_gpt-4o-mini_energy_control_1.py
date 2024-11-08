# Based on the functional description you've provided, which translates to "please turn off unnecessary switches," I will create a `function.py` file. This file will contain a main function that will utilize the existing classes from your project to turn off all actuators that are currently on.
# 
# Here's the content for `function.py`:

# functions/function.py

from home.home_plan import home_plan

def turn_off_unnecessary_switches(home):
    for room in home:
        for actuator in room.actuators:
            if actuator.get_status() == 'on':
                actuator.turn_off()

def main():
    home = home_plan()
    turn_off_unnecessary_switches(home)

if __name__ == "__main__":
    main()